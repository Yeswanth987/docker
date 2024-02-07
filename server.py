from flask import Flask, render_template_string

PORT = 80

app = Flask(__name__)

@app.route("/")
def index():
    message = "Hello, world! This is Flask app (v-2.0.11)."
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Flask App</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background: linear-gradient(to right, #00b09b, #96c93d);
                    color: white;
                    text-align: center;
                    height: 100vh;
                    margin: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                }
                h1 {
                    font-size: 3rem;
                    animation: colorchange 10s infinite;
                }
                @keyframes colorchange {
                    0% {
                        color: #ff5f6d;
                    }
                    25% {
                        color: #ff7f50;
                    }
                    50% {
                        color: #ffd700;
                    }
                    75% {
                        color: #40e0d0;
                    }
                    100% {
                        color: #30dd8a;
                    }
                }
            </style>
        </head>
        <body>
            <h1>{{ message }}</h1>
            <script>
                setInterval(function() {
                    document.body.style.background = 'linear-gradient(to right, #'+Math.random().toString(16).substr(-6)+', #'+Math.random().toString(16).substr(-6)+')';
                }, 2000);
            </script>
        </body>
        </html>
    ''', message=message)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
