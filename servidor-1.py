from flask import Flask, render_template
from flask_bootstrap import Bootstrap
app=Flask(__name__)
Bootstrap(app)

@app.route("/")
def home():
    return render_template("new 6.html") 

@app.route("/contact")
def contact():
    return render_template("contact.html") 

@app.route("/AboutUs")
def AboutUs():
    return render_template("AboutUs.html") 

@app.route("/OurValues")
def OurValues():
    return render_template("OurValues.html") 

@app.route("/Login")
def Login():
    return render_template("Login.html") 

@app.route("/Client")
def Client():
    return render_template("Client.html") 

app.run(debug=True)