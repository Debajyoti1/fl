from flask import Flask, render_template, url_for, request, session, redirect, g

app = Flask(__name__)
app.secret_key='Hellothere'
@app.route('/')

def index():
    return render_template('index.html')
@app.route('/login',methods=['GET','POST'])
def login():
    session.pop('uu',None)
    if request.method == 'POST':
        u= request.form['un']
        p=request.form['up']
        if u=='1' and p=='2':
            session['uu']='hi'
            return redirect(url_for('profile'))
    return render_template('login.html')
@app.route('/profile')
def profile():
    if session.get('uu') is None:
        return redirect(url_for('login'))
    return render_template('profile.html')
if __name__ == '__main__':
    app.run(debug=True)
