from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():

    file = request.files['file']

    if file:
        filepath = os.path.join("static", file.filename)
        file.save(filepath)

        # For now just show uploaded image
        return f"Image uploaded successfully: {file.filename}"

    return "No file uploaded"


if __name__ == '__main__':
    app.run(debug=True)