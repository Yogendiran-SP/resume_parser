import re
import spacy
from .extracter import extract_text, extract_name, extract_skills, extract_experience

#Load spaCy English NLP model
nlp = spacy.load("en_core_web_sm")

def parse_resume(text,expected_skills):
    parsed_data = {
        "name":None,
        "email":None,
        "phone":None,
        "skills":[],
        "education":None,
        "experience":None,
        "projects":None,
        "missing skills":None
    }

    #Process text with sapCy
    doc = nlp(text)


    # # Old name extraction (too rigid)
    # # name_match = re.search(r"Name\s*:\s(.+)", text, re.IGNORECASE)
    # # if name_match:
    # #     parsed_data["name"] = name_match.group(1).strip()



    # #Name extraction (using regex)
    # lines = text.strip().splitlines()
    # for line in lines[:5]:
    #     if re.search(r"\b([a-z][A-Z]+(?:\s[a-z][A-Z]+){1,2})\b",line.strip()):
    #         words = line.strip().split()
    #         if 1 < len(words) <= 3:  # Between 2 to 3 words
    #             return line.strip().title()
    
    # # name_match = re.search(r"\b([a-z][A-Z]+(?:\s[a-z][A-Z]+){1,2})\b",top_text)
    # # if name_match:
    # #     parsed_data["name"] = name_match.group(1).strip()


    #Name Extraction
    parsed_data["name"] = extract_name(text)
    

    #Email extraction (using regex)
    email_match = re.search(r"[a-zA-z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-,]+",text)
    if email_match:
        parsed_data["email"] = email_match.group().strip()
    
    #Phone number extraction (using regex)
    phone_match = re.search(r"\+?\d[\d\s-]{8,15}",text)
    if phone_match:
        parsed_data["phone"] = phone_match.group(0).strip()
    
    #Skill set matching from a predefined list
    candidate_skills = extract_skills(text)
    candidate_skills = [skill.lower() for skill in candidate_skills]
    parsed_data['skills'] = candidate_skills
    
    print("Candidate skills: ",candidate_skills)
    print("Expected skills: ",expected_skills)

    #Finding the matching skills
    found_skills = []
    missing_skills = []
    for skill in expected_skills:
        if skill in candidate_skills:
            found_skills.append(skill)
        else:
            missing_skills.append(skill)

    print("Found Skills: ",found_skills,"\n")
    parsed_data["matched skills"] = found_skills
    parsed_data["missing skills"] = missing_skills

    #Education Extraction
    education_match = re.search(r"Education\s*:\s(.+)",text)
    if education_match:
        parsed_data["education"] = education_match.group(1).strip()

    # #Experience Extraction
    # lines1 = text.splitlines()
    # experience_lines = []
    # capture_exp = False

    # for line in lines1:
    #     if re.search(r"Experience\s*:",line,re.IGNORECASE):
    #         capture_exp = True
    #         experience_lines.append(line.split(":",1)[1].strip())
    #     elif capture_exp:
    #         if re.search(r"^(Education|Projects|Skills|Name|Email|Phone)\s*:",line,re.IGNORECASE):
    #             break
    #         experience_lines.append(line.strip())

    # #Join the captured experience lines
    # if experience_lines:
    #     experience_string = " ".join(experience_lines)
    #     l1 = [i.strip() for i in experience_string.split(',')]
    #     parsed_data["experience"] = l1


    # Experience Extraction
    parsed_data["experience"] = extract_experience(text)


    #Projects Extraction
    lines2 = text.splitlines()
    projects_lines = []
    capture_pro = False

    for line in lines2:
        if re.search(r"Projects\s*:",line,re.IGNORECASE):
            capture_pro = True
            projects_lines.append(line.split(":",1)[1].strip())
        elif capture_pro:
            if re.search(r"^(Education|Experience|Skills|Name|Email|Phone)\s*:",line,re.IGNORECASE):
                break
            projects_lines.append(line.strip())

    #Join the captured experience lines
    if projects_lines:
        projects_string = " ".join(projects_lines)
        l2 = [i.strip() for i in projects_string.split(',')]
        parsed_data["projects"] = l2

    return parsed_data

    