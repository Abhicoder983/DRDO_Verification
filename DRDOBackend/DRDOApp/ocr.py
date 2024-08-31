from PIL import Image
import pytesseract

def extract_text_from_image(image):
    # Open the image file
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    img = Image.open(image)

    # Use pytesseract to do OCR on the image
    text = pytesseract.image_to_string(img)

    return text
