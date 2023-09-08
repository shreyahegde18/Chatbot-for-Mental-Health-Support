from flask import Flask, render_template, request, jsonify
from chat import get_response, bot_name

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat")
def chat():
    return render_template("chat.html")


@app.route("/test")
def test():
    return render_template("index1.html")

@app.route("/get_response", methods=["POST"])
def get_bot_response():
    user_message = request.form["user_message"]
    bot_response = get_response(user_message)
    return jsonify({"bot_response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
