import os
import re
import fitz #PyMuPDF

def extract_text_from_pdf(pdf_path):
    with fitz.open(pdf_path) as doc:
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    
def extract_text(file_path):
    """
    Extracts raw text from a .pdf or .docx resume file
    Returns the extracted text as a string
    """
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        return extract_text_from_pdf(file_path)
    else:
        raise ValueError("Unsupported file format: only .pdf files are supported.")

def smart_proper_case(line):
    words = line.strip().split()
    formatted = []
    for word in words:
        if len(word) <= 2 and word.isalpha():
            formatted.append(word.upper())  # keep initials like SP
        else:
            formatted.append(word.capitalize())
    return ' '.join(formatted)

def extract_name(text):
    # Step 1: Try to find "Name: <name>" and stop before "Email" or newline
    name_line = re.search(r"Name\s*[:\-]\s*([A-Za-z\s\.]+?)(?=\s+Email|\n|$)", text, re.IGNORECASE)
    if name_line:
        return smart_proper_case(name_line.group(1))

    # Step 2: Fallback to top lines (as before)
    lines = text.strip().splitlines()
    for line in lines[:5]:  # Check top 5 lines
        line_clean = line.strip()
        if not line_clean or any(k in line_clean.lower() for k in ["email", "phone", "skills"]):
            continue
        words = line_clean.split()
        if 1 < len(words) <= 3 and all(re.fullmatch(r"[A-Za-z.]+", w) for w in words):
            return smart_proper_case(line_clean)

    return None

def extract_skills(text):
    skills = []

    # 1. Try one-line format: "Skills: Python, Flask, ..."
    one_line_match = re.search(r"Skills\s*[:\-]?\s*(.+)", text, re.IGNORECASE)
    if one_line_match:
        skill_line = one_line_match.group(1)
        skills += [skill.strip() for skill in skill_line.split(",") if skill.strip()]
    else:
        # 2. Multi-section format: scan lines under "SKILLS" heading
        lines = text.splitlines()
        capture = False
        for line in lines:
            if re.search(r"^skills\b", line.strip(), re.IGNORECASE):
                capture = True
                continue
            if capture:
                if re.match(r"^[A-Z\s]+$", line.strip()):  # New heading encountered
                    break
                # Extract skills from that line
                parts = re.split(r":", line)
                if len(parts) > 1:
                    skill_items = parts[1].split(",")
                    skills += [skill.lower().strip() for skill in skill_items if skill.strip()]
                else:
                    # fallback: maybe comma-separated even without colon
                    skills += [skill.lower().strip() for skill in line.split(",") if skill.strip()]

    return list(set(skills))  # remove duplicates

# def extract_experience(text):
#     lines = text.splitlines()
#     capture = False
#     temp_block = []

#     for line in lines:
#         line_clean = line.strip()

#         # Start capture after exact "EXPERIENCE"
#         if not capture and re.fullmatch(r"EXPERIENCE", line_clean, re.IGNORECASE):
#             capture = True
#             continue

#         if capture:
#             # Stop at next uppercase heading
#             if re.fullmatch(r"[A-Z\s]{4,}", line_clean) and len(line_clean.split()) <= 4:
#                 break
#             if line_clean:
#                 temp_block.append(line_clean)

#     # Now process the captured lines
#     experiences = []
#     current = ""

#     for line in temp_block:
#         if any(k in line.lower() for k in ["intern", "engineer", "developer", "assistant", "trainee", "project"]):
#             if current:
#                 experiences.append(current.strip())
#             current = line
#         else:
#             current += " " + line

#     if current:
#         experiences.append(current.strip())

#     return experiences


def extract_experience(text):
    lines = text.splitlines()
    experience_text = ""

    for i, line in enumerate(lines):
        if line.lower().startswith("experience:"):
            # Get content from this line
            experience_text = line[len("experience:"):].strip()
            # Append the next line if it's not empty or a section header
            if i + 1 < len(lines):
                next_line = lines[i + 1].strip()
                if next_line and not re.match(r"^[A-Z\s]{4,}$", next_line):
                    experience_text += " " + next_line
            break

    # Smart split by closing parentheses only when followed by a comma
    raw_experiences = re.split(r"\)\s*,?\s*", experience_text)
    
    # Add the ")" back and clean entries
    experiences = []
    for item in raw_experiences:
        item = item.strip()
        if item:
            if not item.endswith(")"):
                item += ")"
            experiences.append(item)

    return experiences

