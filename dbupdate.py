from model import db, Product, Accounts

def NewPrice(idProduto, price):
    prod = Product.query.filter_by(id=idProduto).first()
    if prod:
        prod.price = price
        db.session().commit()

def update_user_password(rowid, old_password, new_password)
user = Accounts.query.filter_by(rowid=rowid).first()
if user:
    if user.update_password(old_password, new_password):
        db.session.commit






