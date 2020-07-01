from model import db, Accounts

def create_new_account(username, password):
    user = Accounts(name = username, password  = password)
    db.session.add(user)
    db.session.commit()

