# OCR (Optical Character Recognition) Web Application

## Overview
The OCR Web Application is a user-friendly and efficient tool designed to extract text from images. It provides a simple interface for users to either upload an image or provide a URL to an image. After processing, the application returns the extracted text from the image.

## Key Features

1. **Upload an Image:** Users can upload an image directly from their device. The application accepts various image formats.

2. **OCR from URL:** Users can provide a URL to an image hosted online, and the application will retrieve and process the image.

3. **Dark/Light Theme Toggle:** The application offers a convenient dark/light theme toggle, allowing users to choose their preferred theme for the user interface.

## Usage

1. **Upload an Image:**
   - Click the "Upload an Image" button.
   - Select the desired image file from your device.
   - Click the "Upload and OCR" button to process the image.

2. **OCR from URL:**
   - Enter the URL of an image in the provided input field.
   - Click the "OCR from URL" button to process the image from the URL.

## Results
Upon processing an image, the application displays the following results on the results page:

- **Extracted Text:** The text extracted from the processed image is displayed, making it easy for users to access the extracted information.

- **Uploaded Image:** If an image was uploaded, it is displayed on the results page, providing users with a visual representation of the processed image.

## Themes
The application offers a choice between a light and dark theme. Users can switch between these themes using the theme toggle switch located on the main page. The theme toggle provides a customized and visually pleasing experience for users.

## Use Case
The OCR Web Application is a versatile tool for various use cases, including:

- Digitizing printed documents: Users can convert printed documents into digital text for easy editing and storage.
- Extracting information from images: Users can capture and extract text from images, such as scanned documents or photos.
- Language support: The application supports multiple languages for OCR, making it suitable for a global audience.

## Technologies
- **Flask**: The web application framework used for the backend.
- **HTML and Jinja2 Templates**: Used for creating the web pages and rendering dynamic content.
- **Bootstrap**: Provides a responsive and visually appealing design.
- **SweetAlert2**: Used for displaying user-friendly notifications.
- **JavaScript**: Used for client-side interactivity, including the dark/light theme toggle.

## Customization
The application can be further customized and extended to meet specific requirements, including additional features, languages, and UI improvements.

## Deployment
The application can be deployed to a web server for public access, making it a valuable tool for users who need to extract text from images quickly and easily.
