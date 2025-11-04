from flask import Flask, request, jsonify
import tensorflow as tf
import pickle
import numpy as np

app = Flask(__name__)

# Load the model and tokenizer
model = tf.keras.models.load_model('translation_model.h5')
with open('tokenizer.pkl', 'rb') as handle:
    tokenizer = pickle.load(handle)

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    input_text = data.get('text', '')
    source_lang = data.get('source', '')
    target_lang = data.get('target', '')

    if not input_text or not source_lang or not target_lang:
        return jsonify({'error': 'Invalid input provided.'}), 400

    # Tokenize and process input text
    input_seq = tokenizer.texts_to_sequences([input_text])
    input_padded = tf.keras.preprocessing.sequence.pad_sequences(input_seq, padding='post')

    # Predict translation
    prediction = model.predict(input_padded)
    translated_text = tokenizer.sequences_to_texts([np.argmax(prediction, axis=-1)])

    return jsonify({
        'translation': translated_text[0]
    })

if __name__ == '__main__':
    app.run(debug=True)
