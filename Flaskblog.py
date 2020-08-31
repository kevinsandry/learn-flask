from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Hello Page</h1>"

@app.route("/about")
def about():
    return "<h1>Flask Blog v1.0</h1>"

if __name__ == '__main__':
    app.run(debug=True)