import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hola Mundo con Heroku (PD)"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # usa $PORT si existe, si no, usa 5000
    app.run(host='0.0.0.0', port=port)
