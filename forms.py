from flask_wtf import  FlaskForm
from wtforms import StringField, SubmitField, FloatField, PasswordField, BooleanField, SubmitField, ValidationError, Label
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo

def exchanges_query():
    return Exchange.query

def symbols_query():
    return Symbol.query

class LoginForm(FlaskForm):
    name = StringField("Usuário", validators=[DataRequired(), Length(1, 80)])
    password = PasswordField("Senha", validators=[DataRequired()])
    submit   = SubmitField("Acessar")

class CreateUser(FlaskForm):
    name        = StringField("Nome completo", validators=[DataRequired(), Length(1, 80)])
    email       = StringField("Email", validators=[DataRequired(), Length(6, 80), Email()])
    password    = PasswordField("Nova senha", validators=[DataRequired(), EqualTo("password2", message="A senha e a confirmação devem ser iguais."), Length(6, 80)])
    password2   = PasswordField("Confirme a senha", validators=[DataRequired()])
    phonenumber = PhonenumberField("Escreva seu número de telefone", validator=[DataRequired-Regexp("^[0-9]{2}-([0-9]{8}|[0-9]{9})", 0, "Digite um número de telefone válido")]])
    address     = Address("Escreva seu endereço", validator=[DataRequired])
    submit      = SubmitField("Salvar")
    def validate_username(self, field):
        if User.query.filter_by(name=field.data).first():
            raise ValidationError("Nome de usuário já está em uso.")

class CreateEmployee(FlaskForm):
    name        = StringField("Nome completo", validators=[DataRequired(), Length(1, 80)])
    email       = StringField("Email", validators=[DataRequired(), Length(6, 80), Email()])
    password    = PasswordField("Nova senha", validators=[DataRequired(), EqualTo("password2", message="A senha e a confirmação devem ser iguais."), Length(6, 80)])
    password2   = PasswordField("Confirme a senha", validators=[DataRequired()])
    phonenumber = PhonenumberField("Escreva seu número de telefone", validator=[DataRequired-Regexp("^[0-9]{2}-([0-9]{8}|[0-9]{9})", 0, "Digite um número de telefone válido")]])
    address     = Address("Escreva seu endereço", validator=[DataRequired])
    funtion     = Function("Função", validators=[DataRequired()])
    submit      = SubmitField("Salvar")

class CreateProduct(FlaskForm):
    name        = StringField("Nome completo", validators=[DataRequired(), Length(1, 80)])
    price       = PriceField("preço do produto", validators=[DataRequired])
    size        = SizeField("tamanho", validators=[DataRequired()])
    Color       = ColorField("Cor", validators=[DataRequired()])
    submit      = SubmitField("Salvar")

class ChangePassword(FlaskForm):
    old_password = PasswordField("Senha atual", validators=[DataRequired()])
    password     = PasswordField("Nova senha", validators=[DataRequired(), EqualTo("password2", message="A senha e a confirmação devem ser iguais."),Length(6, 80)])
    password2    = PasswordField("Confirme a nova senha", validators=[DataRequired()])
    submit       = SubmitField("Salvar")

class ChangeAddress(FlaskForm):
    old_address = AddressField("endereço atual", validators=[DataRequired()])
    address     = AddressPasswordField("Novo endereço", validators=[DataRequired()])
    submit      = SubmitField("Salvar")

class ChangePrice(FlaskForm):
    old_price = PriceField("Preço atual", validators=[DataRequired()])
    price     = PriceField("Novo Preço", validators=[DataRequired()])
    submit    = SubmitField("Salvar")

class ExcludeAccount(FlaskForm):
    password  = PasswordField("senha", validators[DataRequired()])
    submit    = SubmitField("Excluir")

class Payment(FlaskForm):
    price     = PriceField("preço", validators=[DataRequired()])
    discount  = DiscountField("Descontos")
    CreditCard= CreditCardField("cartão", validators=[DataRequired()])
    CVV       = CVVField("CVV", validators=[DataRequired()], Length(3))
    Password  = PasswordField("Senha", validators=[DataRequired()])
    submit    = SubmitField("Excluir")

def validate_f1(self,field):
    if not field.data.isnumeric():
        raise Exception("")