# Email Spam Detector

## Project Overview

The Email Spam Detector is a basic machine learning application that classifies text messages as Spam or Not Spam. It uses Natural Language Processing (NLP) techniques and a Naive Bayes classifier to identify patterns in messages.

The application provides a simple web interface built using Streamlit, allowing users to enter a message and view its predicted category.

**Note:** The current implementation is trained on the SMS Spam Collection dataset. It demonstrates the fundamentals of spam classification but has not been specifically trained on email messages.

## Technologies Used

* Python
* Pandas
* Scikit-learn
* TF-IDF Vectorization
* Multinomial Naive Bayes
* Streamlit
* Joblib

## Features

* Text message classification
* Spam and Not Spam predictions
* Machine learning model trained on labelled messages
* Interactive web interface
* Model evaluation using accuracy, precision, recall, and F1-score

## Model Performance

The model achieved 96.05% accuracy on the held-out test set.

The spam recall was approximately 70%, indicating that some spam messages were missed during testing.

Performance may vary on new messages and datasets.

## Dataset

The project uses the SMS Spam Collection dataset from the UCI Machine Learning Repository.

Dataset: https://archive.ics.uci.edu/dataset/228/sms+spam+collection

## Project Structure

```text
Email-Spam-Detector/
├── SMSSpamCollection
├── train_model.py
├── app.py
├── spam_model.pkl
├── tfidf_vectorizer.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

The `venv` directory is created locally and should not be uploaded to GitHub.

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate into the project directory:

```bash
cd Email-Spam-Detector
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Train the model

```bash
python train_model.py
```

This generates the trained model and TF-IDF vectorizer files.

### 5. Run the application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal to use the application.

## Learning Outcomes

* Understanding supervised machine learning
* Text preprocessing and TF-IDF feature extraction
* Training and evaluating a Naive Bayes classifier
* Building a simple machine learning web application
* Saving and reusing trained models

## Future Improvements

* Train the model on an actual email dataset.
* Improve spam recall and reduce false negatives.
* Compare different classification algorithms.
* Add email-header and phishing detection features.

## Author

Add your name and GitHub profile here.
