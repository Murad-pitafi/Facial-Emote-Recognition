# from flask import Flask, request, render_template, jsonify
# from werkzeug.utils import secure_filename
# import tensorflow as tf
# import numpy as np
# from PIL import Image

# # Load your trained model
# model_path = 'my_model.keras'  # Specify your model path
# model = tf.keras.models.load_model(model_path)

# # Define a Flask application
# app = Flask(__name__)

# # Define allowed file extensions
# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# def allowed_file(filename):
#     # Check if the file has an allowed extension
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/', methods=['GET', 'POST'])
# def upload_file():
#     # Render the HTML page with the file upload form
#     if request.method == 'GET':
#         return render_template('upload.html')
    
#     # Handle file upload
#     if request.method == 'POST':
#         file = request.files.get('file')
        
#         if file and allowed_file(file.filename):
#             # Secure the filename
#             filename = secure_filename(file.filename)
            
#             # Load the image and preprocess it
#             try:
#                 image = Image.open(file)
#                 image = image.resize((48, 48))  # Resize to model input size
#                 image = np.array(image.convert('L'))  # Convert to grayscale
#                 image = image.astype(np.float32) / 255.0  # Normalize
                
#                 # Add a batch dimension
#                 image = np.expand_dims(image, axis=0)
                
#                 # Perform inference
#                 predictions = model.predict(image)
#                 predicted_class = tf.argmax(predictions, axis=1).numpy()[0]
                
#                 # Map the predicted class index to the expression label
#                 expression_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
#                 predicted_expression = expression_labels[predicted_class]
                
#                 # Return the predicted expression as JSON
#                 return jsonify({'prediction': predicted_expression})
#             except Exception as e:
#                 # Handle any exceptions that might occur during processing
#                 return jsonify({'error': str(e)})
#         else:
#             return jsonify({'error': 'Invalid file type.'})
        
#     # Default case: handle unexpected requests
#     return jsonify({'error': 'Invalid request method.'})

# # Run the Flask application
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle file upload and prediction (as provided earlier)
        pass
    else:
        # Render the upload.html template
        return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
