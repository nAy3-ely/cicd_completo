from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return """
    <html>
        <head>
            <title>Hola Nayhely</title>
            <style>
                body {
                    margin: 0;
                    font-family: Helvetica, Arial, sans-serif;
                    background: #f5f5f5;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    color: #333;
                }
                .card {
                    background: white;
                    padding: 40px 50px;
                    border-radius: 12px;
                    text-align: center;
                    border: 1px solid #e0e0e0;
                }
                h1 {
                    margin: 0 0 10px;
                    font-size: 26px;
                    font-weight: 600;
                }
                p {
                    margin: 6px 0;
                    font-size: 16px;
                }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>Hola Nayhely</h1>
                <p>Status: OK</p>
                <p>Autor: Tu aplicación</p>
            </div>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
