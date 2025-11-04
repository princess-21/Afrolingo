# Afrolingo – AI Language Platform Prototype

Afrolingo is an AI-powered translation project designed to help users translate and learn African languages using deep learning.  
It uses a TensorFlow sequence model trained on paired text data to translate between African languages and English.

## 🧠 Overview
The project explores how artificial intelligence can preserve and promote African languages through intelligent translation models.  
It uses a **Flask API** for handling translation requests and a **TensorFlow LSTM model** for language generation.

Although the current version does not include a frontend interface, the backend logic is fully functional and demonstrates the AI workflow.

## ⚙️ Tech Stack
- **Python**
- **Flask**
- **TensorFlow / Keras**
- **scikit-learn**
- **NumPy & Pandas**


## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/princess-21/Afrolingo.git
   cd Afrolingo

📝Install dependencies:
pip install flask tensorflow scikit-learn pandas numpy

Run the Flask app:
python app.py

Test the translation endpoint:
Send a POST request to http://localhost:5000/translate with JSON data:

{
  "text": "Ndewo",
  "source": "Igbo",
  "target": "English"
}

📚 How It Works

The train_model.py script loads a dataset of paired African and English sentences.

Text data is tokenized and converted into padded sequences.

A TensorFlow LSTM model is trained to predict the English translation.

The Flask app loads the trained model and tokenizer, accepts user text, and returns AI-generated translations.

🌍 Future Plans

Add a user interface for text input and translation display.

Expand the dataset to cover more African languages.

Integrate a multilingual transformer model (e.g., mBART or MarianMT).

Deploy the API to the cloud (Render, Hugging Face, or AWS).

👩‍💻 Author
Chidera Okeke Ejiroghene
GitHub: @princess-21
Medium: @wrlegacy21
