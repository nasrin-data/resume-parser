import re
import pdfplumber
from docx import Document


# Read text from a PDF or Word resume
def read_resume(file_path):
    text = ""

    if file_path.lower().endswith(".pdf"):
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""

    elif file_path.lower().endswith(".docx"):
        document = Document(file_path)

        for paragraph in document.paragraphs:
            text += paragraph.text + "\n"

    else:
        print("Please upload a PDF or DOCX resume.")
        return ""

    return text


# Find basic candidate details
def extract_details(text):
    email = re.findall(
        r'[\w.-]+@[\w.-]+\.\w+', text
    )

    phone = re.findall(
        r'\+?\d[\d\s()-]{8,}\d', text
    )

    skills_list = [
        "Python", "SQL", "Excel", "Power BI",
        "Java", "HTML", "CSS", "JavaScript",
        "Communication", "Data Analysis",
        "Machine Learning", "Pandas", "NumPy",
        "Selenium", "JMeter", "LoadRunner",
        "AWS", "Azure", "GitHub"
    ]

    skills = []

    for skill in skills_list:
        if skill.lower() in text.lower():
            skills.append(skill)

    lines = [line.strip() for line in text.splitlines()
             if line.strip()]

    name = lines[0] if lines else "Not found"

    return {
        "Name": name,
        "Email": email[0] if email else "Not found",
        "Phone": phone[0] if phone else "Not found",
        "Skills": skills
    }


# Compare resume skills with job requirements
def calculate_score(candidate_skills, required_skills):
    if not required_skills:
        return 0

    matched = []

    for skill in required_skills:
        if any(skill.lower() == item.lower()
               for item in candidate_skills):
            matched.append(skill)

    score = (len(matched) / len(required_skills)) * 100

    return round(score, 2)


# Test the resume parser
if _name_ == "_main_":
    print("Resume Parser is ready!")
