## Skin Cancer Detection Web Application

This repository contains the code for a **Skin Cancer Detection** web application developed using **FastAPI** and **TensorFlow**. The application allows users to upload skin images for analysis and determines whether the skin condition is **Benign** or **Malignant** (i.e., skin cancer) using a pre-trained deep learning model.

### Features:
- **Upload Image**: Users can upload skin images, which are then processed and analyzed using a trained deep learning model.
- **Prediction**: The system classifies the uploaded image as either "Benign" or "Malignant" with confidence percentages.
- **Blog Section**: Provides informational articles related to skin cancer prevention, detection, and treatment.
- **Responsive Design**: The website is fully responsive, with a user-friendly interface for both mobile and desktop users.
- **Image Preview**: Users can see a preview of the uploaded image before prediction.
  
### Technologies:
- **FastAPI**: For building the backend of the web application.
- **TensorFlow/Keras**: Used for the pre-trained deep learning model to classify skin conditions.
- **HTML/CSS**: For front-end design, making the page visually appealing and responsive.
- **JavaScript**: To handle dynamic user interactions and communicate with the backend API.

### How to Use:
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/skin-cancer-detection.git
   ```
2. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the FastAPI app:
   ```bash
   uvicorn app.main:app --reload
   ```
4. Visit the web application on `http://127.0.0.1:8000`.

### Folder Structure:
```
/skin-cancer-detection
    /app
        /static          # Static files like CSS, images
        /templates       # HTML templates
        /models          # Trained models
    /app.py              # FastAPI backend logic
    /requirements.txt    # List of required Python packages
    /README.md           # Project documentation (this file)
```

### Model:
The model used for detection is a **Convolutional Neural Network (CNN)**, trained to recognize benign and malignant skin lesions. The model is loaded via TensorFlow and used for predictions on the uploaded images.

### Contributing:
Feel free to fork the project, submit issues, or create pull requests if you find bugs or want to add new features. Contributions are always welcome!

### License:
This project is licensed under the Skin Cancer Detection Team License.

