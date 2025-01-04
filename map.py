from app import create_app, db
from app.models import CollectionPoint  
from datetime import datetime, timedelta

app = create_app()

def init_collection_points():
    with app.app_context():
        # Clear existing points
        print("Clearing existing collection points...")
        CollectionPoint.query.delete()

        # Add multiple collection points
        print("Adding new collection points...")
        points = [
            CollectionPoint(
                nom="Point de Collecte Centre-Ville",
                adresse="123 Rue Centrale, Paris",
                horaire="08:00 - 18:00",
                latitude=48.8566,
                longitude=2.3522,
                type_dechet="recyclable",
                date_collecte=datetime.now()
            ),
            CollectionPoint(
                nom="Point de Collecte Quartier Nord",
                adresse="45 Avenue du Nord, Paris",
                horaire="09:00 - 17:00",
                latitude=48.8656,
                longitude=2.3569,
                type_dechet="organique",
                date_collecte=datetime.now() + timedelta(days=1)
            ),
            CollectionPoint(
                nom="Point de Collecte Rive Gauche",
                adresse="78 Boulevard Saint-Germain, Paris",
                horaire="08:30 - 16:30",
                latitude=48.8476,
                longitude=2.3485,
                type_dechet="autre",
                date_collecte=datetime.now() + timedelta(days=2)
            )
        ]

        try:
            # Add all points to the database
            for point in points:
                db.session.add(point)
                print(f"Added point: {point.nom}")

            # Commit the changes
            db.session.commit()
            print("\nCollection points added successfully!")
            
        except Exception as e:
            db.session.rollback()
            print(f"\nError occurred: {str(e)}")
            raise

if __name__ == "__main__":
    print("Starting initialization...")
    init_collection_points()