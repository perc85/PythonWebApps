import json
import csv
from .models import Superhero, Article
from datetime import datetime
from django.contrib.auth.models import User

# Export as JSON
def custom_serializer(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()  # Converts datetime to ISO 8601 string
    raise TypeError(f"Type {type(obj)} not serializable")

def export_to_json():
    # Query the database
    superheroes = list(Superhero.objects.all().values())
    articles = list(Article.objects.all().values())

    # Write to JSON files
    with open('superheroes.json', 'w') as sh_file:
        json.dump(superheroes, sh_file, indent=4, default=custom_serializer)

    with open('articles.json', 'w') as art_file:
        json.dump(articles, art_file, indent=4, default=custom_serializer)

# Import from JSON
def import_from_json():
    # Import Superheroes
    with open('superheroes.json', 'r') as sh_file:
        superheroes = json.load(sh_file)
        for data in superheroes:
            Superhero.objects.update_or_create(
                id=data['id'],
                defaults={
                    'user': None if data.get('user_id') is None else User.objects.get(id=data['user_id']),
                    'name': data['name'],
                    'identity': data['identity'],
                    'description': data['description'],
                    'strength': data['strength'],
                    'weakness': data['weakness'],
                    'image': data['image'],
                    'is_default': data['is_default'],
                }
            )

    # Import Articles
    with open('articles.json', 'r') as art_file:
        articles = json.load(art_file)
        for data in articles:
            author = None
            if data.get('author_id') is not None:
                try:
                    author = User.objects.get(id=data['author_id'])
                except User.DoesNotExist:
                    print(f"User with id {data['author_id']} does not exist. Skipping article with id {data['id']}.")
                    continue  # Skip this article if the author does not exist

            Article.objects.update_or_create(
                id=data['id'],
                defaults={
                    'title': data['title'],
                    'content': data['content'],
                    'author': author,
                    'created_at': datetime.fromisoformat(data['created_at'].replace('Z', '+00:00')),
                }
            )

# Export as CSV
def export_to_csv():
    superheroes = Superhero.objects.all().values()
    articles = Article.objects.all().values()

    with open('superheroes.csv', 'w', newline='') as sh_file:
        writer = csv.DictWriter(sh_file, fieldnames=superheroes[0].keys())
        writer.writeheader()
        writer.writerows(superheroes)

    with open('articles.csv', 'w', newline='') as art_file:
        writer = csv.DictWriter(art_file, fieldnames=articles[0].keys())
        writer.writeheader()
        writer.writerows(articles)

# Import from CSV
def import_from_csv():
    with open('superheroes.csv', 'r') as sh_file:
        reader = csv.DictReader(sh_file)
        for row in reader:
            Superhero.objects.update_or_create(id=row['id'], defaults=row)

    with open('articles.csv', 'r') as art_file:
        reader = csv.DictReader(art_file)
        for row in reader:
            Article.objects.update_or_create(id=row['id'], defaults=row)
