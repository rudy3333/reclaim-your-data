from flask import Flask

app= Flask(__name__)

#serve static css
@app.route('/styles.css')
def serve_css():
    return app.send_static_file('styles.css')

@app.route('/')
def serve_static():
    return app.send_static_file('index.html')

