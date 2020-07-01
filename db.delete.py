from model import db, Product, Accounts

def deleteUser(rowid)
    user = db.session.query(User).filter(User.id == user_id).first()
        if user:
            db.session.query(User).filter(User.id==user_id).delete()
            db.session().commit()

def deleteProduct(rowid):
    user = db.session.query(User).filter(User.id == user_id).first()
        if user:
            db.session.query(User).filter(User.id==user_id).delete()
            db.session().commit()