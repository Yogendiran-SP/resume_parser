import os
from .parser import parse_resume
from .db_handler import insert_resume
from .extracter import extract_text

def process_single_resume(file_path, expected_skills):
    resume_text = extract_text(file_path)
    parsed_data = parse_resume(resume_text,expected_skills)
    stored_resume = []

    # Printing parsed data
    for key, value in parsed_data.items():
        print(f"{key.capitalize()}: {value}")

    if len(parsed_data["matched skills"]) >= 2:
        print(insert_resume(parsed_data))
        for item in parsed_data.items():
            stored_resume.append(item)
    else:
        print("❌ Has not enough skills")

    return stored_resume


def process_all_resume(folder_path,skills_list):
    abs_path = os.path.abspath(folder_path)
    stored_resumes=[]
    for file in os.listdir(folder_path):
        file_path = os.path.join(abs_path,file)
        print(f"\n📄 Processing: {file}")
        single_resume = process_single_resume(file_path, skills_list)
        if single_resume:
            stored_resumes.append(single_resume)
            
    return stored_resumes

def clear_upload_folder(upload_folder):
    files_deleted = 0

    for f in os.listdir(upload_folder):
        file_path = os.path.join(upload_folder, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
            files_deleted += 1

    if files_deleted:
        return f"✅ {files_deleted} file(s) removed successfully."
    else:
        return "📁 No files to remove."
