from flask import Flask, jsonify, request
import pickle
import os

# Optional: import TensorFlow if available
try:
    from tensorflow.keras.models import load_model
    from tensorflow.keras.preprocessing.sequence import pad_sequences
except Exception:
    load_model = None
    pad_sequences = None

app = Flask(__name__)

# Paths to your model and tokenizer
BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, 'fake_news_model.h5')
TOKENIZER_PATH = os.path.join(BASE_DIR, 'tokenizer.pkl')

model = None
tokenizer = None

# Load model
if os.path.exists(MODEL_PATH) and load_model is not None:
    try:
        model = load_model(MODEL_PATH)
        print("Model loaded successfully")
    except Exception as e:
        print("Could not load model:", e)

# Load tokenizer
if os.path.exists(TOKENIZER_PATH):
    try:
        with open(TOKENIZER_PATH, 'rb') as f:
            tokenizer = pickle.load(f)
        print("Tokenizer loaded successfully")
    except Exception as e:
        print("Could not load tokenizer:", e)

# Root endpoint: returns your exact JSON
@app.route("/", methods=["GET"])
def home():
    return {
        "message": "Welcome to Fake News Detector API",
        "version": "1.0",
        "endpoints": {
            "POST /predict": "Submit text for fake news prediction. Send JSON: {\"text\": \"your text here\"}"
        },
        "example_request": "curl -X POST http://localhost:5000/predict -H \"Content-Type: application/json\" -d '{\"text\":\"Breaking news...\"}'"
    }

# Predict endpoint
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True, silent=True)
    if not data or "text" not in data:
        return jsonify({"error": "No text provided"}), 400

    text = data["text"]

    if model is None or tokenizer is None:
        return jsonify({"prediction": None, "note": "model or tokenizer not loaded on server"}), 200

    try:
        seq = tokenizer.texts_to_sequences([text])
        seq = pad_sequences(seq, maxlen=100)
        pred = model.predict(seq)
        result = float(pred[0][0]) if pred.shape[-1] == 1 else pred.tolist()
        return jsonify({"prediction": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
from flask import Flask, jsonify, request
import pickle
import os

# Optional: import TensorFlow if available
try:
    from tensorflow.keras.models import load_model
    from tensorflow.keras.preprocessing.sequence import pad_sequences
except Exception:
    load_model = None
    pad_sequences = None

app = Flask(__name__)

# Paths to your model and tokenizer
BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, 'fake_news_model.h5')
TOKENIZER_PATH = os.path.join(BASE_DIR, 'tokenizer.pkl')

model = None
tokenizer = None

# Load model
if os.path.exists(MODEL_PATH) and load_model is not None:
    try:
        model = load_model(MODEL_PATH)
        print("Model loaded successfully")
    except Exception as e:
        print("Could not load model:", e)

# Load tokenizer
if os.path.exists(TOKENIZER_PATH):
    try:
        with open(TOKENIZER_PATH, 'rb') as f:
            tokenizer = pickle.load(f)
        print("Tokenizer loaded successfully")
    except Exception as e:
        print("Could not load tokenizer:", e)

# Root endpoint: returns your exact JSON
@app.route("/", methods=["GET"])
def home():
    return {
        "message": "Welcome to Fake News Detector API",
        "version": "1.0",
        "endpoints": {
            "POST /predict": "Submit text for fake news prediction. Send JSON: {\"text\": \"your text here\"}"
        },
        "example_request": "curl -X POST http://localhost:5000/predict -H \"Content-Type: application/json\" -d '{\"text\":\"Breaking news...\"}'"
    }

# Predict endpoint
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True, silent=True)
    if not data or "text" not in data:
        return jsonify({"error": "No text provided"}), 400

    text = data["text"]

    if model is None or tokenizer is None:
        return jsonify({"prediction": None, "note": "model or tokenizer not loaded on server"}), 200

    try:
        seq = tokenizer.texts_to_sequences([text])
        seq = pad_sequences(seq, maxlen=100)
        pred = model.predict(seq)
        result = float(pred[0][0]) if pred.shape[-1] == 1 else pred.tolist()
        return jsonify({"prediction": result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
