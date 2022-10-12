from flask import Flask, render_template, request

#create a server instance
 
app=Flask(__Name__)
@app.route("/", methods=["GET","POST"])
def index():
    errors = {}
    if request.method=="POST":
        uName=request.form["uName"]
        print("User=",uName)
        print("Phone=",request.form["uPhone"])
        print("Email=",request.form["uEmail"])
        if not uName[0].isalpha():
            errors["uName"]=["Username should start with alphabet"]
    return render_template("home.html",errors=errors)
app.run(host="0.0.0.0",port=50100,debug=True)