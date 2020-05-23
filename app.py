from flask import Flask
app = Flask(__name__)
a=[x for x in range(20)]
@app.route('/')
def index():
    return '<h1>Hello There How</h1>'

if __name__ == '__main__':
    app.run(debug=True)