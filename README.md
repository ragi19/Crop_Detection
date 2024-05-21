
# 🌾 Crop Detection with HarvestHelper Hub 🌾

## Overview

**Crop Detection** is a sophisticated machine learning project designed to identify and classify various types of crops using state-of-the-art image recognition techniques. This repository contains the complete code and resources required to train and deploy an efficient crop detection model. 

**Check out the complementary [HarvestHelper Hub Notebook](https://www.kaggle.com/code/ragishehab/harvesthelper-hub) on Kaggle** for detailed insights and additional resources.

## Features

- 🧠 **Advanced Image Classification**: Utilizes a powerful machine learning model to accurately classify crop images.
- 🌐 **Interactive Web Interface**: Built with Flask for easy image upload and prediction.
- 📊 **Comprehensive Data Analysis**: Detailed exploration and visualization of the dataset in the accompanying Kaggle notebook.
- 🗂️ **Pre-trained Model Included**: Ready-to-use SVM model for immediate deployment.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/ragi19/Crop_Detection.git
   ```
2. **Navigate to the Project Directory:**
   ```bash
   cd Crop_Detection
   ```
3. **Set Up a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
4. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Start the Flask Application:**
   ```bash
   flask --debug run
   ```
2. **Open the Web Interface:**
   - Navigate to `http://127.0.0.1:5000` in your browser.
3. **Upload and Predict:**
   - Upload an image of a crop to receive a classification result.

## File Structure

- `app.py`: Main Flask application.
- `requirements.txt`: List of dependencies.
- `svm_model.pkl`: Pre-trained SVM model.
- `static/`: Static assets (CSS, images, etc.).
- `templates/`: HTML templates.
- `.devcontainer/`: VS Code Dev Container configuration files.

## Model Training

To retrain the model with your own dataset:

1. **Prepare Your Dataset**: Ensure it is formatted correctly for image classification.
2. **Modify the Training Script**: Adapt the script to utilize your dataset.
3. **Train and Save the Model**:
   ```python
   # Example code snippet for training
   from sklearn import svm
   model = svm.SVC()
   # Add your training logic here
   model.fit(X_train, y_train)
   joblib.dump(model, 'svm_model.pkl')
   ```

## Contributing

We welcome contributions! Please fork this repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For support or inquiries, please open an issue on GitHub or reach out via the Kaggle notebook's discussion section.
