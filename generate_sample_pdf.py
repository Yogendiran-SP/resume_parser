from fpdf import FPDF

#Create a pdf class
class PDF(FPDF):
    def header(self):
        self.set_font("Arial","B",12)
        self.cell(0,10,"Resume",ln=True,align="C")

#Create an instance and add a page
pdf = PDF()
pdf.add_page()

#Add sample resume content
pdf.set_font("Arial","",12)
lines = ["Name: Yogendiran SP",
         "Email: jyogendiran@gmail.com",
         "Phone: +916369241082",
         "Skills: Python, Git, Flask, Machine Learning, Data Analysis",
         "Education: B.Tech in Artficial Intelligence and Machine Learning",
         "Experience: Full Stack Developer Internship at AICTE-EY NextGen (Jan 2024 - Feb 2024), Artificial Intelligence Internship at Pinnacle Labs (June 2025 - July 2025)",
         "Projects: E-commerce Web App using MERN Stack, Resume Parser App using Python"]

#Use multi cell for text wrapping
for line in lines:
    pdf.multi_cell(0,10,line)

#Save the pdf
pdf.output("data/test_resume.pdf")
print("✅ Successfully test_resume.pdf file created")