import requests
import json

URL = 'http://127.0.0.1:5000/predict'

samples = [
    "Breaking news today about elections and policy changes.",
    "Scientists discovered a cure for all diseases, miracle drug!",
    "Local sports team wins championship after dramatic comeback.",
    "Aliens have landed in the city center, eyewitnesses report.",
    "New study shows link between coffee and better productivity."
]

def main():
    headers = {'Content-Type': 'application/json'}
    results = []
    for text in samples:
        payload = {"text": text}
        try:
            r = requests.post(URL, json=payload, headers=headers, timeout=10)
            try:
                data = r.json()
            except Exception:
                data = r.text
            results.append({'text': text, 'status': r.status_code, 'response': data})
        except Exception as e:
            results.append({'text': text, 'error': str(e)})

    print(json.dumps(results, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    main()
