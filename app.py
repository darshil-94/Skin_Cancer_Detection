from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

# Initialize FastAPI app
app = FastAPI()

# CORS middleware for cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the Keras model
model = tf.keras.models.load_model("/home/petpooja-920/Projects/Skin_Cancer_Detection-master/models/My_model.h5")
CLASS_NAMES = ["Benign", "Malignant"]  # Example classes

# Set up static files and templates
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def serve_homepage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/skin-cancer", response_class=HTMLResponse)
async def serve_skin_cancer_page(request: Request):
    return templates.TemplateResponse("skin_cancer.html", {"request": request})

@app.get("/blog", response_class=HTMLResponse)
async def serve_blog_page(request: Request):
    return templates.TemplateResponse("blog.html", {"request": request})

def read_image(file) -> np.ndarray:
    image = np.array(Image.open(BytesIO(file)))
    image = tf.image.resize(image, (256, 256))  # Resize to model input size
    image = image / 255.0  # Normalize
    return image

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Load the uploaded image
    image = Image.open(file.file)
    
    # Check if the image has 4 channels (RGBA)
    if image.mode == 'RGBA':
        # Convert to RGB by removing the alpha channel
        image = image.convert('RGB')

    # Resize and preprocess the image to match model input shape
    image = image.resize((256, 256))
    image_array = np.array(image) / 255.0
    image_batch = np.expand_dims(image_array, axis=0)  # Add batch dimension

    # Make prediction
    predictions = model.predict(image_batch)
    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])
    
    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
