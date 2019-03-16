import cv2
import tensorflow as tf

CATEGORIES = ["Dog", "Cat"]
#loading model
model = tf.keras.models.load_model("64x3-CNN.model")

def prepare(filepath):
    IMG_SIZE = 50
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

def result(image):
    prediction = model.predict([prepare('cat1.jpg')])
    return CATEGORIES[int(prediction[0][0])]

print(result('cat1.jpg'))


