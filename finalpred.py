import cv2
import tensorflow as tf


#passed



# Open and preprocess the image
image_path = "Y1.jpg"
pred_img = cv2.imread(image_path)
pred_img = cv2.resize(pred_img, (224, 224))
pred_img = pred_img.reshape(1, 224, 224, 3)
pred_img = pred_img.astype("float32") / 255.0

# Load the model
loaded_model = tf.keras.models.load_model('BrainTumor.h5')
loaded_model.summary()

# Perform prediction
output = loaded_model.predict(pred_img)

if output[0][0] >= 0.5:
    print('Brain Tumors Detected')
else:
    print("Brain Tumors can't be Detected")

print(output)
