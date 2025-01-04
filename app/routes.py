from flask import Blueprint, render_template, url_for, flash, redirect, request, jsonify
from flask_login import login_user, current_user, logout_user, login_required
from app import db, bcrypt
from app.models import User, CollectionPoint, Article, EnvironmentalData, EnvironmentalNews
from app.forms import LoginForm, RegistrationForm

auth_bp = Blueprint('auth', __name__)
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    return redirect(url_for('auth.auth'))

@auth_bp.route('/auth', methods=['GET', 'POST'])
def auth():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
        
    login_form = LoginForm()
    register_form = RegistrationForm()

    # Handle login form submission
    if 'login' in request.form and login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, login_form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            flash('Connexion réussie!', 'success')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Email ou mot de passe incorrect.', 'danger')

    # Handle registration form submission
    if 'register' in request.form and register_form.validate_on_submit():
        try:
            hashed_password = bcrypt.generate_password_hash(register_form.password.data).decode('utf-8')
            user = User(
                prenom=register_form.prenom.data,
                nom=register_form.nom.data,
                email=register_form.email.data,
                telephone=register_form.telephone.data,
                password=hashed_password,
                points=0,
                organic_waste=0,
                inorganic_waste=0
            )
            db.session.add(user)
            db.session.commit()
            flash('Votre compte a été créé avec succès! Vous pouvez maintenant vous connecter.', 'success')
            return redirect(url_for('auth.auth'))
        except Exception as e:
            db.session.rollback()
            flash('Une erreur est survenue lors de l\'inscription. Veuillez réessayer.', 'danger')
            print(f"Registration error: {str(e)}")

    return render_template('authentification.html', login_form=login_form, register_form=register_form)

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Vous avez été déconnecté.', 'info')
    return redirect(url_for('auth.auth'))

@main_bp.route('/home')
def home():
    articles = Article.query.order_by(Article.date_publication.desc()).limit(3).all()
    return render_template('home.html', articles=articles)

@main_bp.route('/dashboard')
@login_required
def dashboard():
    user = current_user
    collection_points = CollectionPoint.query.all()
    
    # Get latest environmental data
    latest_env_data = EnvironmentalData.query.order_by(
        EnvironmentalData.date.desc()
    ).first()
    
    # Get latest news
    latest_news = EnvironmentalNews.query.order_by(
        EnvironmentalNews.published_at.desc()
    ).limit(3).all()
    
    return render_template('dashboard.html',
                         user=user,
                         collection_points=collection_points,
                         organic_waste=user.organic_waste,
                         inorganic_waste=user.inorganic_waste,
                         map_center={'lat': 48.8566, 'lng': 2.3522},
                         environmental_data=latest_env_data,
                         news=latest_news)

@main_bp.route('/blog')
def blog():
    articles = Article.query.order_by(Article.date_publication.desc()).all()
    return render_template('blog.html', articles=articles)

@main_bp.route('/article/<int:article_id>')
def article(article_id):
    article = Article.query.get_or_404(article_id)
    return render_template('article.html', article=article)


@main_bp.route('/get_collection_points')
@login_required
def get_collection_points():
    collection_points = CollectionPoint.query.all()
    points = [{
        'id': point.id,
        'name': point.nom,
        'address': point.adresse,
        'schedule': point.horaire,
        'lat': point.latitude,
        'lng': point.longitude,
        'type': point.type_dechet,
        'date': point.date_collecte.strftime('%d/%m/%Y %H:%M') if point.date_collecte else None
    } for point in collection_points]
    return jsonify(points)