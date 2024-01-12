import fitz  # PyMuPDF is required, use this command in your PC's terminal ---->>> pip install PyMuPDF
import os

##CHANGE THIS TO THE LOCATION OF THE LECTURE YOU ARE TRYING TO SCRAPE FROM PDF

# Path to the PDF file
pdf_path = r"C:\Users\mecha\Downloads\GAME1001_W01_Notes.pdf"

##CHANGE THIS TO YOUR OWN PC'S DIRECTORY SELECT THE FOLDER YOU WANT

# Output directory for images
output_folder = r"C:\Users\mecha\Downloads\Images"

# Ensure the output directory exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def convert_pdf_to_images(pdf_path, output_folder):
    # Open the PDF file
    pdf = fitz.open(pdf_path)
    
    # Iterate over each page in the PDF
    for page_num in range(len(pdf)):
        # Get the page
        page = pdf[page_num]

        # Render page to an image (pix) object
        zoom = 2  # 2x zoom to increase the resolution of the image
        mat = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat)

        # Generate the image file path
        image_path = os.path.join(output_folder, f"slide_{page_num + 1}.png")

        # Save the pix object as an image file
        pix.save(image_path)

        # Print out a status message
        print(f"Converted page {page_num + 1} to image: {image_path}")

    # Close the PDF after conversion
    pdf.close()

# Convert PDF pages to images
convert_pdf_to_images(pdf_path, output_folder)