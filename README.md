# Fake News Detector (LSTM) — simple deployment

This folder contains a minimal Flask app to serve an LSTM-based fake news detector.

Files at project root (required):

- `app.py` — Flask application exposing `/predict` (POST JSON: {"text":"..."}).
- `fake_news_model.h5` — trained Keras model file.
- `tokenizer.pkl` — tokenizer object used when training.
- `requirements.txt` — Python dependencies to install.

Quick start (Windows PowerShell)

1. Activate your venv (if you created one):

```powershell
cd C:\Users\LENOVO\Fake_news_detector_using_LSTM
.\venv\Scripts\Activate.ps1    # or Activate.bat for cmd
```

2. Install dependencies:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

3. Run the app locally:

```powershell
python app.py
```

4. Smoke test the `/predict` endpoint (PowerShell):

```powershell
Invoke-RestMethod -Uri http://127.0.0.1:5000/predict -Method Post -ContentType 'application/json' -Body (@{text='This is a test'} | ConvertTo-Json)
```

Notes
- If `tensorflow` is heavy for your environment, you can try a lighter inference path or run the service on a machine with GPU/CPU support suited for TensorFlow.
- The `app.py` contains a safe placeholder response when model/tokenizer aren't loaded; replace `maxlen` in padding to match your training pipeline if needed.

If you'd like, I can install the dependencies into the venv and run the smoke test for you (I will detect whether installing is allowed and only proceed with your confirmation).
