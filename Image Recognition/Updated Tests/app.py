import tensorflow as tf
from fastapi import FastAPI, UploadFile, File, HTTPException
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img, ImageDataGenerator
import numpy as np
import uvicorn
import os
import shutil
from zipfile import ZipFile


app = FastAPI()

MODEL_PATH = "/Users/nieves/Downloads/Created_Dense_Best_20241108-053135.keras"
class_list_path = "/Users/nieves/Downloads/ifood-2019-fgvc6_2/class_list.txt"
model = tf.keras.models.load_model(MODEL_PATH)

target_size = (224, 224)
batch_size = 32

def preprocess_image(image_path):
    image = load_img(image_path, target_size=target_size)   
    image = img_to_array(image)                                         
    image = image / 255.0                                  
    image = np.expand_dims(image, axis=0)                                
    return image

def class_map(class_number):
    with open(class_list_path, "r") as file:
        for line in file:
            number, food_name = line.strip().split(maxsplit=1)
            if int(number) == class_number:
                return food_name
    return "Unknown class"


@app.get("/")
async def status():
    return {"Model is ready to make predictions"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    temp_image_path = f"/tmp/{file.filename}"
    with open(temp_image_path, "wb") as buffer:
        buffer.write(await file.read())
    
    preprocessed_image = preprocess_image(temp_image_path)

    predictions = model.predict(preprocessed_image)
    predicted_class = np.argmax(predictions, axis=1)[0]    
    confidence_score = float(np.max(predictions))              

    status_message = 'Prediction successful'

    return {
        "predicted_class": class_map(int(predicted_class)),
        "confidence_score": confidence_score,
        "status": status_message
    }

@app.post("/evaluate")
async def evaluate(test_data: UploadFile = File(...)):
    
    test_data_dir = "/tmp/test_data"
    os.makedirs(test_data_dir, exist_ok=True)
    
    new_dir = os.path.join(test_data_dir, "test")

    zip_path = os.path.join(test_data_dir, "test_data.zip")
    with open(zip_path, "wb") as buffer:
        buffer.write(await test_data.read())

    with ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(new_dir)

    extracted_dirs = os.listdir(new_dir)
    target_dir = os.path.join(new_dir, extracted_dirs[1])

    print(f"Using directory: {target_dir}")

    valid_extensions = {'.jpg', '.jpeg', '.png'}

    for root, _, files in os.walk(target_dir):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            _, ext = os.path.splitext(file_name)
            if ext.lower() not in valid_extensions:
                print(f"Removing non-image file: {file_path}")
                os.remove(file_path)

    test_datagen = ImageDataGenerator(rescale=1. / 255)
    test_generator = test_datagen.flow_from_directory(
        target_dir, 
        target_size=target_size,
        batch_size=batch_size,
        class_mode='categorical',
        shuffle=False
    )

    result = model.evaluate(test_generator)
    status_message = 'Evaluation completed'
    return {"Loss": result[0], 
    "Accuracy": result[1], 
    "Precision": result[2], 
    "Recall": result[3],
    "Status": status_message
}

# Running the app (in local development)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
