#!usr/bin/python3
# pip install PyPDF2
# pip install pdf2image
# Developer: DOMO NOSTA
# Organisation: Cyberguards

import os 
from PyPDF2 import PdfFileReader
from pdf2image import  convert_from_path

def pdf_to_images(pdf_file, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    pdf_reader = PdfFileReader(pdf_file)

    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        image = convert_from_path(pdf_file, first_page=page_num + 1, last_page=page_num + 1)[0]

        # Saving the image
        image_path = os.path.join(output_folder, f"page_{page_num + 1}.png")
        image.save(image_path, "PNG")

    print("PDF pages converted to images  successfully!")

pdf_file = input("Enter PDF path: ")
output_folder = input("Output folder")
pdf_to_images(pdf_file, output_folder)
