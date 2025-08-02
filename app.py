from flask import Flask

app = Flask(__name__)

@app.route('/')
def health():
    # just for test
    return "Hello Rishav, the server is up!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050)