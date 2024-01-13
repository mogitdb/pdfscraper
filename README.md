# PDF to Obsidian Slides Converter README

This script is designed to convert each page of a PDF file into individual image files and automatically generate a Markdown document that references these images. This is particularly useful for importing visual content into Obsidian notes.

# Requirements

- Python 3.x
- PyMuPDF (`fitz`)

You can install PyMuPDF using pip:
```bash
pip install PyMuPDF
```

# Usage Instructions
Set Up Your Paths: Modify the pdf_path and output_folder variables in the script to point to your PDF file and the desired output directory for the images, respectively.

pdf_path = r"path_to_your_pdf_file.pdf"
output_folder = r"path_to_your_output_folder"


# Run the Script: 
Execute the script in your Python environment. The script will create images from the PDF and generate a Markdown file named slides.md in the output_folder.

Check Your Images and Markdown File: The images will be stored in the output_folder, and slides.md will contain links to these images in the correct format for Obsidian.

# What the Script Does
- Reads the specified PDF file.
- Converts each page of the PDF into a PNG image with a filename pattern slide_x.png, where x is the page number.
- Creates a Markdown file named slides.md with Obsidian-compatible links to each image.
- Prints the progress in the terminal as it processes each page.


# Output Format
The Markdown file will contain links in the following format:

# Slides

![[slide_1.png]]

![[slide_2.png]]


# Troubleshooting
If the script is not executing properly:

- Ensure you have Python 3.x installed and added to your system's PATH.
- Check if PyMuPDF is installed correctly by running pip show PyMuPDF in your terminal.
- Verify that the paths for the PDF file and output folder are correct and accessible.

# License
This script is provided "as is", without warranty of any kind. You are free to modify and distribute it as you see fit.