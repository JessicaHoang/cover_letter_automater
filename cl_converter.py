""" The objective of this code is to create a cover letter template that can be
inherited to easily deploy a tailored cover letter to apply to various job
applications. 
1. create and export the cover letter as a document.
2. Uses inheritance concept to utilize it as a tempalce that can be tailored.

Youtube Video Tutorial source: https://www.youtube.com/watch?v=bSEKyt_O5Ic
Githubg Repo Source: https://github.com/hetshah25/Automated-CoverLetter-Python
"""

from docxtpl import DocxTemplate
import datetime

position_name = input("Enter the name of the position you're appling for : ")
company_name = input("Enter the name of the company : ")
job_listing = input("Enter the job listing site you found the position from : ")
company_values = input("Enter the company's values : (your commitment to..) ")
company_project = input("Enter the company's current project of interested : (I am particularly drawn to..) ")
relevant_skills = input("Enter your relevant skills to the position : (my proficiency in..) ")

todays_date = datetime.datetime.today().strftime("%B %d, %Y")

context = {
    "position_name" : position_name,
    "company_name" : company_name,
    "job_listing" : job_listing,
    "company_values" : company_values,
    "company_project" : company_project,
    "relevant_skills" : relevant_skills,
    "todays_date" : todays_date,
}

# Opening our template:
doc = DocxTemplate("2024 Cover Letter Template copy.docx")

# Load this doc
doc.render(context)
doc.save("cover_letters/2024 Cover Letter "+position_name+" at "+company_name+'.docx')

