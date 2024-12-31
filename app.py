from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello_geek():
    return "Hello from Flask & Docker"

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 8080, debug = True)