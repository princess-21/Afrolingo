import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split

# Load and preprocess the dataset
df = pd.read_csv('C:/Users/Ejiro/Documents/african lang ai gen/project/dataset.csv', encoding='ISO-8859-1')
df.columns = ['Text', 'Language', 'English']
df['Text'] = df['Text'].apply(lambda x: x.encode('ISO-8859-1').decode('utf-8'))
df['Language'] = df['Language'].apply(lambda x: x.encode('ISO-8859-1').decode('utf-8'))
df['English'] = df['English'].apply(lambda x: x.encode('ISO-8859-1').decode('utf-8'))

# Prepare input and output data
X = df['Text']
y = df['English']

tokenizer = tf.keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(X)
X_seq = tokenizer.texts_to_sequences(X)
y_seq = tokenizer.texts_to_sequences(y)

X_padded = tf.keras.preprocessing.sequence.pad_sequences(X_seq, padding='post')
y_padded = tf.keras.preprocessing.sequence.pad_sequences(y_seq, padding='post')

X_train, X_val, y_train, y_val = train_test_split(X_padded, y_padded, test_size=0.2, random_state=42)

# Build and train the model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=len(tokenizer.word_index) + 1, output_dim=128),
    tf.keras.layers.LSTM(256, return_sequences=True),
    tf.keras.layers.LSTM(256),
    tf.keras.layers.Dense(len(tokenizer.word_index) + 1, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=10, batch_size=64)

# Save the model and tokenizer
model.save('translation_model.h5')
# Save the tokenizer for future use
import pickle
with open('tokenizer.pkl', 'wb') as handle:
    pickle.dump(tokenizer, handle)
