# from flask import Flask, jsonify
# import time
# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return jsonify({"Time of Call": time.time()})

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', debug=True)
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    return f"Hello, {name}! Welcome to Flask."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)