import os
import sys
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.run import process_all_resume,clear_upload_folder

upload_folder = './uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = upload_folder

@app.route('/')
def home():
    folder_path = os.path.abspath(app.config['UPLOAD_FOLDER'])
    clear_upload_folder(folder_path)
    return render_template('index.html')

@app.route('/upload',methods=['POST'])
def upload_resume():
    files = request.files.getlist('resumes[]')
    skill_input = request.form.get('expected_skills','')
    expected_skills = [skill.strip().lower() for skill in skill_input.split(', ') if skill.strip()]

    folder_path = os.path.abspath(app.config['UPLOAD_FOLDER'])
    print("folder_path:",folder_path)
    os.makedirs(folder_path,exist_ok=True)

    for file in files:
        if file.filename == '':
            continue
        filename = secure_filename(file.filename)
        file_path = os.path.join(folder_path,filename)
        file.save(file_path)

    stored_resumes = process_all_resume(folder_path,expected_skills)
    print("🥇 stored_resumes:",stored_resumes)
    converted_resumes = [dict(resume) for resume in stored_resumes]
    print("🥈 converted_resumes:",converted_resumes)
    # clear_upload_folder(folder_path)

    return render_template('result.html',resumes=converted_resumes,input_skills=expected_skills)
        
if __name__ == "__main__":
    app.run(debug=True)