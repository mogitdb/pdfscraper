import fitz  # PyMuPDF
import os

# Change these paths to match your own setup
pdf_path = r"C:\Users\mecha\Downloads\GAME1005_W01_Notes.pdf"
output_folder = r"C:\Users\mecha\Downloads\Images"

# Ensure the output directory exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def convert_pdf_to_images(pdf_path, output_folder):
    # Open the PDF file
    pdf = fitz.open(pdf_path)
    image_paths = []

    # Iterate over each page in the PDF
    for page_num in range(len(pdf)):
        # Get the page
        page = pdf[page_num]

        # Render page to an image (pix) object
        zoom = 2  # 2x zoom to increase the resolution of the image
        mat = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat)

        # Generate the image file path
        image_filename = f"slide_{page_num + 1}.png"
        image_path = os.path.join(output_folder, image_filename)

        # Save the pix object as an image file
        pix.save(image_path)

        # Add path to list
        image_paths.append(image_filename)

        # Print out a status message
        print(f"Converted page {page_num + 1} to image: {image_path}")

    # Close the PDF after conversion
    pdf.close()

    # Return list of image paths
    return image_paths

def create_markdown_file(image_paths, output_folder):
    # Name of the markdown file
    md_filename = "slides.md"
    md_filepath = os.path.join(output_folder, md_filename)

    # Write image links to markdown file
    with open(md_filepath, 'w') as md_file:
        md_file.write('# Slides\n\n')
        for image_path in image_paths:
            md_file.write(f"![[{image_path}]]\n\n")

    print(f"Markdown file created: {md_filepath}")

# Convert PDF pages to images and get paths
image_paths = convert_pdf_to_images(pdf_path, output_folder)

# Create markdown file with links to all images
create_markdown_file(image_paths, output_folder)