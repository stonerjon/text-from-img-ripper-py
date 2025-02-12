import pytesseract
from PIL import Image

# List of uploaded files
file_paths = [
    "/mnt/data/6.jpg",
    "/mnt/data/5.jpg",
    "/mnt/data/3.jpg",
    "/mnt/data/2.jpg",
    "/mnt/data/index.jpg"
]

# Extract text from each image
extracted_texts = {}
for file_path in file_paths:
    image = Image.open(file_path)
    text = pytesseract.image_to_string(image)
    extracted_texts[file_path] = text

extracted_texts
