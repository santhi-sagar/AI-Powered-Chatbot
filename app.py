from flask import Flask, render_template, request
from chatbot_model import get_bot_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chat():
    user_msg = request.form["msg"]
    bot_reply = get_bot_response(user_msg)
    return bot_reply

if __name__ == "__main__":
    app.run(debug=True)
