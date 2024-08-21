#  OOP-Driven Multi-Feature NLP Application with Comprehensive GUI & API Integration


## Overview

This project is a comprehensive Natural Language Processing (NLP) application developed using Object-Oriented Programming (OOP) principles. It features a sophisticated graphical user interface (GUI) for various NLP tasks including Sentiment Analysis, Language Detection, Emotion Prediction, and English-to-Hindi Translation. The application integrates with the Hugging Face API for real-time NLP model inference and utilizes a JSON-based database for user management.

## Features

- **Login GUI**: Allows users to log in to their accounts.
- **Registration GUI**: Facilitates new user registration and account creation.
- **Home GUI**: Serves as the main dashboard with navigation to different NLP tasks.
- **Sentiment Analysis GUI**: Analyzes the sentiment of the provided text.
- **Language Detection GUI**: Detects the language of the provided text.
- **Emotion Prediction GUI**: Predicts the emotion expressed in the provided text.
- **English-to-Hindi Translation GUI**: Translates text from English to Hindi.

## Technologies Used

- **Python**: Programming language for development.
- **Tkinter**: GUI toolkit for creating the user interface.
- **Hugging Face API**: For accessing pre-trained NLP models including sentiment analysis, emotion prediction, language detection, and translation.
- **JSON**: For storing user data in a simple and lightweight format.
- **OOP (Object-Oriented Programming)**: Used for structuring the application and enhancing maintainability.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/nlp-app.git
   cd nlp-app
   ```

2. **Install dependencies**:
   ```bash
   pip install transformers requests huggingface_hub
   ```

3. **Run the application**:
   ```bash
   python gui.py
   ```

## Usage

1. **Launch the Application**: Run the `gui.py` script to start the application.

2. **Login/Registration**: Use the Login GUI to access your account or the Registration GUI to create a new account.

3. **Navigate**: Use the Home GUI to navigate to different NLP tasks.

4. **Perform NLP Tasks**: Enter text into the relevant GUI (Sentiment Analysis, Language Detection, Emotion Prediction, Translation) to get results.

## Demo

Watch the demo video to see the application in action: [Demo Video](https://drive.google.com/file/d/1uI6U6uyRu1LIewIzSgYP-MfvieSuOKXm/view?usp=sharing)

## API Integration

- **Sentiment Analysis**: Uses the Hugging Face API (`finiteautomata/bertweet-base-sentiment-analysis`) to analyze text sentiments.
- **Language Detection**: Uses the Hugging Face API (`papluca/xlm-roberta-base-language-detection`) for language detection.
- **Emotion Prediction**: Uses the Hugging Face API (`bhadresh-savani/bert-base-uncased-emotion`) to predict emotions in text.
- **Translation**: Uses the Hugging Face API (`Helsinki-NLP/opus-mt-en-hi`) for translating text from English to Hindi.

## Code Structure

- **`gui.py`**: Entry point of the application, containing the main logic and Tkinter-based GUI setup.
- **`database.py`**: Contains methods for user data management and storage.
- **`api.py`**: Contains methods for interacting with the Hugging Face API for various NLP tasks.

