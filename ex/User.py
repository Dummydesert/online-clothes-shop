from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    id            = db.Column(db.Integer, nullable=False, primary_key=True)
    confirmed     = db.Column(db.Boolean, default=False)
    name          = db.Column(db.String(80), nullable=False)
    full_name     = db.Column(db.String(80), nullable=True)
    email         = db.Column(db.String(64), unique=True, nullable=True)
    admin         = db.Column(db.Boolean, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    status        = db.Column(db.Boolean, nullable=False)
    created       = db.Column(db.DateTime, nullable=False)
    updated       = db.Column(db.DateTime, nullable=False)

    @property
    def password(self):
        raise AttributeError("password is not a readable attribute.")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
