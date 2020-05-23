from flask import Flask
app = Flask(__name__)

@app.route('/')
a=[x for x in range(50)]
def index():
    return str(a)

if __name__ == '__main__':
    app.run(debug=True)