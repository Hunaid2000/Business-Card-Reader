# Business-Card-Reader
Business Card Reader for Automatic Text Extraction &amp; Classification

## Introduction
The proposed project aims to design and develop a business card reader that can automatically extract necessary information from business cards and classify it into appropriate categories. The system uses morphological operations and image segmentation techniques followed by Optical Character Recognition (OCR) to extract text from images to identify and extract specific fields such as Name, Email, Phone number, and Address.

The system uses corner detection, edge detection, contour analysis, and bounding box techniques to detect and correct the alignment of the card in the image. Image pre-processing techniques such as noise removal and contrast enhancement are used to improve the accuracy of OCR recognition.

The system is developed using Python and Flask and can be deployed/used locally. The system provides a user-friendly interface for selecting and uploading an image of a business card, shows the detected card image and displays the output on the interface as well as in a text file.

## Main Features
- **Card Detection:** The system uses corner detection, edge detection, contour analysis, and bounding box techniques to detect the business card in the image.
- **Card Alignment Correction:** The system uses contours and bounding box techniques to correct the alignment of the card in the image.
- **Image Pre-processing:** The system uses noise removal and contrast enhancement techniques to improve the accuracy of OCR recognition.
- **OCR Integration:** The system integrates an OCR engine to recognize the text from the business card.
- **Field Extraction:** The system extracts necessary information from business cards such as Name, Email, Phone number, and Address.
- **Flask App Development:** The system is developed using Python and Flask to create a user-friendly web interface.
- **Output Results:** The system displays the output on the interface and write it to a text file.
- **Accurate Text Field Detection and Alignment:** The system accurately detectsthe position and alignment of text fields in the image.
- **Web Interface:** The system has a web interface to select and upload images of business cards.
- **User-Friendly UI:** The system has a user-friendly interface to display the output results in form of table.

## Software Used
The proposed system is developed using Python and Flask. Python is a popular programming language for image processing and machine learning, and Flask is a lightweight and easy-to-use web framework that enables the development of web applications.

## Inputs/Outputs
The input to the system is an image of a business card uploaded through the web interface. The output consists of the text extracted from the business card displayed on the interface and written to a text file.

## Deployment
The system is developed using Python and Flask and can be deployed locally. The system provides a user-friendly interface for selecting and uploading an image of a business card and displays the output on the interface as well as in a text file.
