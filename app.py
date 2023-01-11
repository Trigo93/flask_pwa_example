from flask import Flask, render_template, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sw.js')
def sw():
    return app.send_static_file('sw.js')

@app.route('/manifest.json')
def manifest():
    response = make_response(json.dumps(manifest))
    response.headers['Content-Type'] = 'application/manifest+json'
    return response

if __name__ == '__main__':
    app.run()
