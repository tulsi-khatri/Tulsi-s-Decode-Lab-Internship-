# Optical Character Recognition (OCR) System using Python

A Python-based Optical Character Recognition (OCR) project that extracts text from images using Tesseract OCR and OpenCV. The system detects text with high confidence, displays the extracted text in tabular form, and highlights detected text regions on the image.

## Features

* Reads text from images using Tesseract OCR
* Image preprocessing using grayscale conversion and Gaussian blur
* Applies Otsu thresholding for better text detection
* Filters text based on confidence score
* Displays extracted text with confidence values
* Draws bounding boxes around detected text
* Shows the processed image with annotations
* Stores results in a Pandas DataFrame

## Technologies Used

* Python 3
* OpenCV
* Pytesseract
* Pandas

## Project Structure

```text
OCR-Text-Detection-System/
│
├── ocr_system.py
└── README.md
```

## Installation

Install the required libraries:

```bash
pip install opencv-python pytesseract pandas
```

## Tesseract OCR Installation

Download and install Tesseract OCR from:

https://github.com/UB-Mannheim/tesseract/wiki

After installation, update the Tesseract path in the code:

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

## Run the Program

```bash
python ocr_system.py
```

## How It Works

1. Loads an image provided by the user.
2. Converts the image to grayscale.
3. Applies Gaussian blur and thresholding.
4. Extracts text using Tesseract OCR.
5. Filters text with confidence greater than or equal to 80%.
6. Stores detected text and confidence values.
7. Draws rectangles around detected text.
8. Displays the extracted text and annotated image.

## Sample Input

```text
Enter image path:
C:\Users\User\Desktop\sample.jpg
```

## Sample Output

```text
Detected Text:

Text        Confidence
HELLO          96.21
WORLD          94.87
PYTHON         92.15
```

## Libraries Used

* OpenCV
* Pytesseract
* Pandas

## Future Improvements

* Support PDF text extraction
* Save extracted text to CSV or Excel files
* Detect handwritten text
* Build a GUI using Tkinter
* Create a web application using Flask or Streamlit
* Add support for multiple languages

## Applications

* Document Digitization
* Invoice Processing
* License Plate Recognition
* Receipt Scanning
* Text Extraction from Images
* Data Entry Automation

## Author

Tulsi Khatri

## License

This project is created for educational and internship purposes.
