from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello_client')
def hello_client():
    return "Hello Cllient!"

if __name__ == "__main__":
    app.run(debug=True)