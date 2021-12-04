from flask import Flask, render_template, send_from_directory


app = Flask(__name__, static_folder='static') 


@app.route('/', strict_slashes=False)
def index():
    return render_template('index.html')

@app.route('/<path:filename>', strict_slashes=False)  
def send_file(filename):  
    return send_from_directory(app.static_folder, filename)

@app.route('/sw.js', strict_slashes=False)
def sw():
    return send_from_directory(app.static_folder, 'sw.js')

@app.route('/manifest.json', strict_slashes=False)
def manifest():
    return send_from_directory(app.static_folder, 'manifest.json')

@app.route('/app/static/app.js', strict_slashes=False)
def app_js():
    return send_from_directory(app.static_folder, 'app.js')


if __name__ == '__main__': app.run(debug=True)
