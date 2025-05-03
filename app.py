from flask import Flask

app= Flask(__name__)
@app.route('/')
def serve_static():
    return app.send_static_file('index.html')