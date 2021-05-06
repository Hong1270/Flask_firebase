from flask import Flask, redirect,render_template,url_for,request,session, flash
from DB_handler import DBModule

DB = DBModule()
app = Flask(__name__)

@app.route('/',methods=["GET", "POST"])
def main():
    return render_template('main.html')

@app.route('/register', methods=['GET', 'POSt'])
def register():
    if request.method == 'POST':
        id = request.form['regi_id']
        pw = request.form['regi_pw']
        DB.register(id,pw)
        return render_template('main.html')
    return render_template('register.html')

if __name__ =='__main__':
    app.run(debug=True)