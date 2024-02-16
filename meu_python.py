from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/a')
def a():
    return "<p>Oi plebe<p>"

if __name__ == "__main__":
    app.run(debug=True)
