import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


def preprocess_input(input_data):
    # Tokenize the input string
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts([input_data])
    input_sequence = tokenizer.texts_to_sequences([input_data])

    # Pad the input sequence to match model input shape
    max_sequence_length = 100  # Example: max length of input sequence
    padded_input = pad_sequences(input_sequence, maxlen=max_sequence_length)

    return padded_input


def load_and_run_model(ckpt_path, input_data):
    # Preprocess the input data
    processed_input = preprocess_input(input_data)

    # Define your model architecture
    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(input_dim=10000, output_dim=64, input_length=100),
        tf.keras.layers.GlobalAveragePooling1D(),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    # Load weights from the checkpoint file
    model.load_weights(ckpt_path)

    # Perform inference on input data
    predictions = model.predict(processed_input)

    return predictions


# Example usage
ckpt_path = 'sd-v1-4.ckpt'
input_data = "sugar and salt"
predictions = load_and_run_model(ckpt_path, input_data)
print(predictions)
