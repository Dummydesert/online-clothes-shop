from flask_wtf import  FlaskForm
from wtforms import StringField, SubmitField, FloatField, PasswordField, BooleanField, SubmitField, ValidationError, Label
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from flask_login import LoginManager, login_user, login_required, logout_user
from db_select import check_email_already_registered, check_username_already_registered
from dbModel import User, Exchange, Symbol
from WhiteList import check_white_list

def exchanges_query():
    return Exchange.query

def symbols_query():
    return Symbol.query

class LoginForm(FlaskForm):
    username = StringField("Usuário", validators=[DataRequired(), Length(1, 64)])
    password = PasswordField("Senha", validators=[DataRequired()])
    submit   = SubmitField("Acessar")

    def validate_username(self, field):
        if User.query.filter_by(name=field.data).first():
            raise ValidationError("Nome de usuário já está em uso.")

class ConfirmUser(FlaskForm):
    full_name = StringField("Nome completo", validators=[DataRequired(), Length(1, 64)])
    email     = StringField("Email", validators=[DataRequired(), Length(1, 64), Email()])
    password  = PasswordField("Nova senha", validators=[DataRequired(), EqualTo("password2", message="A senha e a confirmação devem ser iguais.")])
    password2 = PasswordField("Confirme a senha", validators=[DataRequired()])
    submit    = SubmitField("Salvar")

class CreateUser(FlaskForm):
    username = StringField("Usuário", validators=[DataRequired(), Length(1, 64)])
    is_admin = BooleanField("Admin")
    submit   = SubmitField("Salvar")    

class ChangePassword(FlaskForm):
    old_password = PasswordField("Senha atual", validators=[DataRequired()])
    password     = PasswordField("Nova senha", validators=[DataRequired(), EqualTo("password2", message="A senha e a confirmação devem ser iguais.")])
    password2    = PasswordField("Confirme a nova senha", validators=[DataRequired()])
    submit       = SubmitField("Salvar")