from flask import Flask,render_template,request,redirect,url_for
from dbhelper import *

#create an instance of the Flask framework
app = Flask(__name__)

@app.route("/validateuser",methods=['POST'])
def validateuser()->None:
    username:str = request.form['username']
    password:str = request.form['password']
    
    if len(validate_user(username,password))>0:
        return redirect(url_for('userlist'))
    else:
        return render_template("login.html", pagetitle="USER LOGIN")
        
@app.route("/userlist")
def userlist()->None:
    users:list = getall_users()
    return render_template("userlist.html",ulist=users,pagetitle="USER LIST")
    
#create the first route
@app.route("/")
def index()->None:
    return render_template("login.html", pagetitle="USER LOGIN")
    
#create the application launcher
if __name__=="__main__":
     app.run(debug=True)
 