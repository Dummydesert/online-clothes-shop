from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from dbinsert import create_new_account
from forms import CreateUser
app=Flask(__name__)
Bootstrap(app)


@app.route("/")
def home():
    return render_template("new 6.html") 

@app.route('/new_account', methods=['GET', 'POST'])
def new_account():
    form = CreateUser()
    if form.validate_on_submit():
        create_new_account(form.name.data, form.password.data) 
    return render_template('createUser.html', form=form)

@app.route("/contact")
def contact():
    return render_template("contact.html") 

@app.route("/AboutUs")
def AboutUs():
    return render_template("AboutUs.html") 

@app.route("/OurValues")
def OurValues():
    return render_template("OurValues.html") 

@app.route("/Client")
def Client():
    return render_template("Client.html") 

@app.route('/Login', methods=['GET', 'POST'])
def Login():
    form = CreateUser()  # importado do arquivo de forms
    if form.validate_on_submit():
        create_new_user(form.username.data, form.password.data) # create_new_user importado do arquivo de cadastro / inserts
    return render_template('Login.html', form=form)

@app.route("/Payment")
def Client():
    return render_template("Payment.html") 

@app.route("/ExcludeAccount")
def Client():
    return render_template("ExcludeAccount.html") 

@app.route('/ChangePrice', methods=['GET', 'POST'])
def ChangePrice():
    form = ChangePrice()  # importado do arquivo de forms
    if form.validate_on_submit():
        NewPrice(form.oldPrice.data, form.price.data) # create_new_user importado do arquivo de cadastro / inserts
    return render_template('ChangePrice.html', form=form)

@app.route("/ChangeAddress")
def Client():
    return render_template("ChangeAddress.html") 

@app.route("/ChangePassword")
def Client():
    return render_template("ChangePassword.html") 

@app.route("/CreateProduct")
def Client():
    return render_template("CreateProduct.html") 

@app.route("/CreateEmployee")
def Client():
    return render_template("CreateEmployee.html") 

@app.route("/CreateUser")
def Client():
    return render_template("CreateUser.html") 

app.run(debug=True)

