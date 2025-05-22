from flask import Flask, render_template, request, session, flash, jsonify
import sqlite3 as sql
import os
import pandas as pd
import subprocess

app = Flask(__name__)


@app.route('/')
def user_login():
   return render_template("login.html")


@app.route('/gohome')
def homepage():
    return render_template('index.html')


@app.route('/enternew')
def new_user():
   return render_template('signup.html')


@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form['Name']
            phonno = request.form['MobileNumber']
            email = request.form['email']
            unm = request.form['Username']
            passwd = request.form['password']
            with sql.connect("agricultureuser.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO agriuser(name,phono,email,username,password)VALUES(?, ?, ?, ?,?)", (nm, phonno, email, unm, passwd))
                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("login.html", msg=msg)


@app.route('/logindetails',methods = ['POST', 'GET'])
def logindetails():
    if request.method == 'POST':
            usrname = request.form['username']
            passwd = request.form['password']

            with sql.connect("agricultureuser.db") as con:
                cur = con.cursor()
                cur.execute("SELECT username,password FROM agriuser where username=? ", (usrname,))
                account = cur.fetchall()

                for row in account:
                    database_user = row[0]
                    database_password = row[1]
                    if database_user == usrname and database_password == passwd:
                        session['logged_in'] = True
                        return render_template('home.html')
                    else:
                        flash("Invalid user credentials")
                        return render_template('login.html')


@app.route('/currency')
def video():
    try:
        # Full path to testing.py
        script_path = r"C:\Users\DELL\Desktop\TOXImush\mashroom_final\testing.py"

        # Run Streamlit without blocking Flask
        subprocess.Popen(["streamlit", "run", script_path], start_new_session=True)
    
    except Exception as e:
        print(f"Error while calling subprocess: {e}")

    return render_template('home.html')


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return render_template('login.html')


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)
