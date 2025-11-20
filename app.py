from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({
        "mensaje": "✨ Hola Nayhely desde Python! ✨",
        "status": "OK",
        "autor": "Tu aplicación"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
