# resume-parser
Python-based resume parser for the Cloudriq internship project
# CloudRiq Resume Screening Web App

This is my complete internship project for the CloudRiq Resume Screening Web Application, covering all tasks from Week 1 to Week 7.

## What this project does:
1. *Uploads Resumes:* HR managers can upload a real candidate resume in PDF format.
2. *Cleans & Extracts Text:* The app automatically reads the PDF text and uses standard Python libraries (like spaCy and pdfplumber) to filter out single words and tokens.
3. *Calculates a Match Score (Out of 100%):* It automatically checks the text for required skills, preferred skills, candidate experience years, and education background to calculate an overall percentage score.
4. *Ranked Leaderboard Table:* It saves all candidates into a live table (built with Pandas) that automatically ranks them from highest score to lowest score, starting from number 1.
5. *HR Action Tools:* Includes an administrative panel to change application status, an input bar to search candidate names, and a single-click button to download the entire candidate report list as a CSV Excel file.

## Libraries Used:
- *Streamlit* (To build the web application page and buttons)
- *spaCy & pdfplumber* (To read PDFs and clean text tokens)
- *Pandas* (To create and sort the leaderboard table)
- *Pyngrok* (To securely connect the local app to a public link using environment keys)

All code is fully operational and tested inside the attached .ipynb notebook file.
