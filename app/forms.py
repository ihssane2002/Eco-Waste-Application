from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from app.models import User

class LoginForm(FlaskForm):
    email = StringField('Email', 
                       validators=[DataRequired(message='Email requis'), 
                                 Email(message='Adresse email invalide')],
                       render_kw={"placeholder": "Votre email", 
                                "class": "form-style",
                                "autocomplete": "off"})
    
    password = PasswordField('Mot de passe',
                           validators=[DataRequired(message='Mot de passe requis')],
                           render_kw={"placeholder": "Votre mot de passe", 
                                    "class": "form-style",
                                    "autocomplete": "off"})
    
    submit = SubmitField('Se connecter',
                        render_kw={"class": "btn mt-4"})

class RegistrationForm(FlaskForm):
    prenom = StringField('Prénom',
                        validators=[DataRequired(message='Prénom requis'), 
                                  Length(min=2, max=50, message='Le prénom doit contenir entre 2 et 50 caractères')],
                        render_kw={"placeholder": "Votre prénom", 
                                 "class": "form-style",
                                 "autocomplete": "off"})
    
    nom = StringField('Nom',
                     validators=[DataRequired(message='Nom requis'), 
                               Length(min=2, max=50, message='Le nom doit contenir entre 2 et 50 caractères')],
                     render_kw={"placeholder": "Votre nom", 
                              "class": "form-style",
                              "autocomplete": "off"})
    
    email = StringField('Email',
                       validators=[DataRequired(message='Email requis'), 
                                 Email(message='Adresse email invalide')],
                       render_kw={"placeholder": "Votre email", 
                                "class": "form-style",
                                "autocomplete": "off"})
    
    telephone = StringField('Téléphone',
                          validators=[Length(max=20, message='Le numéro de téléphone est trop long')],
                          render_kw={"placeholder": "Votre téléphone", 
                                   "class": "form-style",
                                   "autocomplete": "off"})
    
    password = PasswordField('Mot de passe',
                           validators=[DataRequired(message='Mot de passe requis'),
                                     Length(min=6, message='Le mot de passe doit contenir au moins 6 caractères')],
                           render_kw={"placeholder": "Votre mot de passe", 
                                    "class": "form-style",
                                    "autocomplete": "off"})
    
    confirm_password = PasswordField('Confirmer le mot de passe',
                                   validators=[DataRequired(message='Confirmation du mot de passe requise'),
                                             EqualTo('password', message='Les mots de passe ne correspondent pas')],
                                   render_kw={"placeholder": "Confirmez votre mot de passe", 
                                            "class": "form-style",
                                            "autocomplete": "off"})
    
    submit = SubmitField('S\'inscrire',
                        render_kw={"class": "btn mt-4"})

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Cette adresse email est déjà utilisée.')