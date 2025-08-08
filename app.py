
from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)
IMAGE_DIR = os.path.join(os.path.dirname(__file__), 'images')

@app.route('/')
def index():
    return '<h1>Hello World</h1>'

@app.route('/images')
def list_images():
    files = os.listdir(IMAGE_DIR)
    return '<br>'.join(files)

@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory(IMAGE_DIR, filename)

@app.route('/admin')
def admin():
    return '<h2>Admin panel placeholder</h2>'

@app.route('/view')
def view():
    page = request.args.get('page', '')
    try:
        return send_from_directory('pages', f'{page}.html')
    except:
        return "Page not found", 404

@app.route('/api/secret')
def secret():
    if request.headers.get("X-API-KEY") == "letmein":
        return "Access Granted"
    else:
        return "Forbidden", 403

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
