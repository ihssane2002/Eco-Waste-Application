# We run this Script alone to add articles to the database and more specifically to the Article table.
from app import create_app, db
from app.models import Article

app = create_app()
with app.app_context():
    # Delete existing articles in case we want to add new ones
    Article.query.delete()
    
    articles = [
        {
            'titre': "Comment gérer les déchets biodégradables dans un restaurant",
            'contenu': """La gestion des déchets biodégradables en restauration est un enjeu majeur pour l'environnement.

Les restaurants produisent quotidiennement une quantité importante de déchets organiques : épluchures, restes de préparation, retours d'assiettes... Une gestion efficace de ces biodéchets permet de réduire l'impact environnemental et de valoriser ces matières.

Solutions pratiques :
- Installation de bacs dédiés pour le tri
- Formation du personnel aux bonnes pratiques
- Compostage sur place quand c'est possible
- Partenariat avec des collecteurs spécialisés
- Optimisation des portions pour réduire le gaspillage
- Suivi et mesure des quantités produites""",
            'image_url': 'image/blog/blog1.jpg',
            'source': 'planete-durable.com'
        },
        {
            'titre': "Comment gérer la gestion des biodéchets en entreprise",
            'contenu': """La gestion des biodéchets représente un défi et une opportunité pour les entreprises.

Le tri et la valorisation des déchets organiques permettent de :
- Réduire l'empreinte environnementale
- Se conformer à la réglementation
- Réaliser des économies
- Améliorer l'image de l'entreprise""",
            'image_url': 'image/blog/blog2.jpg',
            'source': 'planete-durable.com'
        },
        {
            'titre': "Meilleures façons d'aider l'environnement",
            'contenu': """Voici des actions concrètes pour protéger l'environnement au quotidien.

- Réduire sa consommation d'énergie
- Privilégier les transports durables
- Limiter le gaspillage alimentaire
- Trier ses déchets correctement""",
            'image_url': 'image/blog/blog3.jpg',
            'source': 'canada.ca'
        }
    ]

    for article in articles:
        new_article = Article(**article)
        db.session.add(new_article)
    
    db.session.commit()