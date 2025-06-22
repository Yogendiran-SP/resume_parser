from fpdf import FPDF
import random
import os

# Folder to save resumes
output_dir = "./data"

# Sample data pools
names = ["Aarav Mehta", "Diya Sharma", "Rohan Patel", "Ananya Iyer", "Karan Verma",
         "Sneha Reddy", "Nikhil Singh", "Ishita Bose", "Rajeev Nair", "Pooja Desai"]

emails = ["aaravm@email.com", "diyasharma@email.com", "rohanp@email.com", "ananyai@email.com",
          "karanv@email.com", "snehar@email.com", "nikhils@email.com", "ishitab@email.com",
          "rajeevn@email.com", "poojad@email.com"]

phones = ["+919812345678", "+918976543210", "+917845621239", "+918823456781", "+919889776655",
          "+919994455221", "+918865432178", "+917845697812", "+918812345672", "+919834567821"]

skills_pool = [
    ["Python", "Flask", "Machine Learning", "Data Analysis"],
    ["Java", "Spring Boot", "SQL", "Git"],
    ["JavaScript", "React", "Node.js", "MongoDB"],
    ["C++", "Data Structures", "Algorithms", "Problem Solving"],
    ["Python", "TensorFlow", "Deep Learning", "Pandas"],
    ["HTML", "CSS", "JavaScript", "Bootstrap"],
    ["R", "Statistics", "Data Cleaning", "Exploratory Analysis"],
    ["Python", "FastAPI", "PostgreSQL", "Docker"],
    ["Scala", "Spark", "Hadoop", "Kafka"],
    ["Go", "Kubernetes", "Microservices", "REST APIs"]
]

educations = [
    "B.Tech in Computer Science and Engineering",
    "B.Sc in Data Science",
    "B.Tech in Artificial Intelligence and Machine Learning",
    "M.Tech in Computer Science",
    "B.E. in Information Technology",
    "B.Tech in Electronics and Communication Engineering",
    "BCA in Cloud Computing",
    "M.Sc in Applied Data Science",
    "B.Tech in Cybersecurity",
    "B.Sc in Statistics"
]

experiences = [
    "Data Science Internship at DataCorp (Jan 2023 - Mar 2023), Machine Learning Intern at AI Labs (May 2023 - July 2023)",
    "Software Developer Intern at DevSoft (Feb 2022 - May 2022), Backend Developer at CodeBase (Aug 2022 - Oct 2022)",
    "Web Development Internship at WebGen (Mar 2023 - May 2023), UI Developer at Designify (June 2023 - Aug 2023)",
    "AI Intern at BrainTech (Jan 2024 - Apr 2024), Research Assistant at Vision AI Lab (May 2024 - Jul 2024)",
    "Full Stack Developer Intern at Innovatech (Feb 2023 - Apr 2023), Database Analyst at DataWise (Jul 2023 - Sep 2023)",
    "Data Analyst Intern at InsightX (Jan 2024 - Mar 2024), Python Developer at PyWorks (Apr 2024 - Jun 2024)",
    "Cloud Intern at SkyNet (Jun 2023 - Aug 2023), DevOps Intern at BuildOps (Sep 2023 - Nov 2023)",
    "AI Research Intern at NeuralNext (Feb 2024 - Apr 2024), Computer Vision Intern at VisionEdge (May 2024 - Jul 2024)",
    "ML Engineer Intern at PredictAI (Jan 2024 - Mar 2024), Data Engineering Intern at FlowData (Apr 2024 - Jun 2024)",
    "Intern at CodeX (Jan 2024 - Feb 2024), Backend Intern at AppVerse (Mar 2024 - May 2024)"
]

projects_pool = [
    ["Stock Price Prediction App", "Resume Parser using Python"],
    ["E-commerce Platform using MERN", "Portfolio Website"],
    ["Chat Application with Socket.io", "To-do App using React"],
    ["Image Classifier using CNN", "Real-Time Object Detection"],
    ["College Admission Predictor", "Data Visualization Dashboard"],
    ["IoT Home Automation", "Flask-based API Service"],
    ["Movie Recommendation System", "Customer Segmentation Tool"],
    ["Face Recognition App", "OCR Tool using Tesseract"],
    ["News Summarizer with NLP", "Sentiment Analyzer"],
    ["Online Voting System", "Event Management Portal"]
]

# Create 10 resumes
for i in range(10):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt="Resume", ln=True, align='C')
    pdf.ln(5)

    pdf.cell(200, 10, txt=f"Name: {names[i]}", ln=True)
    pdf.cell(200, 10, txt=f"Email: {emails[i]}", ln=True)
    pdf.cell(200, 10, txt=f"Phone: {phones[i]}", ln=True)
    pdf.multi_cell(200, 10, txt=f"Skills: {', '.join(skills_pool[i])}", align="L")
    pdf.cell(200, 10, txt=f"Education: {educations[i]}", ln=True)
    pdf.multi_cell(200, 10, txt=f"Experience: {experiences[i]}", align='L')
    pdf.multi_cell(200, 10, txt=f"Projects: {', '.join(projects_pool[i])}", align='L')
    
    file_path = os.path.join(output_dir, f"resume_{i+1}.pdf")
    pdf.output(file_path)
