import os
import json
import csv
from django.test import TestCase
from django.core.management import call_command
from datetime import datetime
from .models import Superhero, Article


class ExportImportTests(TestCase):
    def setUp(self):
        """
        Set up initial test data for Superhero and Article models.
        """
        # Create initial Superhero data
        self.superhero1 = Superhero.objects.create(
            id=1,
            user_id=None,
            name="Superman",
            identity="Clark Kent",
            description="Man of Steel with superhuman powers.",
            strength="Super strength and flight",
            weakness="Kryptonite",
            image="default_superheroes/superman.jpg",
            is_default=True,
        )
        self.superhero2 = Superhero.objects.create(
            id=2,
            user_id=None,
            name="Batman",
            identity="Bruce Wayne",
            description="The Dark Knight, a genius detective and martial artist.",
            strength="Peak human abilities and intelligence",
            weakness="Human limitations",
            image="default_superheroes/batman.jpg",
            is_default=True,
        )
        self.article = Article.objects.create(
            id=1,
            title="MAC",
            content="N CHEESE",
            author_id=1,
            created_at=datetime(2024, 11, 28, 5, 9, 15, 721506),
        )

    def test_export_to_json(self):
        """
        Test exporting Superhero and Article tables to JSON files.
        """
        # Execute the export_json command
        call_command("export_json")

        # Verify JSON files are created
        self.assertTrue(os.path.exists("superheroes.json"))
        self.assertTrue(os.path.exists("articles.json"))

        # Verify content of superheroes.json
        with open("superheroes.json", "r") as sh_file:
            superheroes_data = json.load(sh_file)
        self.assertEqual(len(superheroes_data), 2)
        self.assertEqual(superheroes_data[0]["name"], "Superman")
        self.assertEqual(superheroes_data[1]["name"], "Batman")

        # Verify content of articles.json
        with open("articles.json", "r") as art_file:
            articles_data = json.load(art_file)
        self.assertEqual(len(articles_data), 1)
        self.assertEqual(articles_data[0]["title"], "MAC")
        self.assertEqual(articles_data[0]["content"], "N CHEESE")

    def test_import_from_json(self):
        """
        Test importing Superhero and Article tables from JSON files.
        """
        # First, export data to JSON to create JSON files
        call_command("export_json")

        # Clear the database
        Superhero.objects.all().delete()
        Article.objects.all().delete()
        self.assertEqual(Superhero.objects.count(), 0)
        self.assertEqual(Article.objects.count(), 0)

        # Import data from JSON files
        call_command("import_json")

        # Verify Superhero data is restored
        self.assertEqual(Superhero.objects.count(), 2)
        superman = Superhero.objects.get(name="Superman")
        self.assertEqual(superman.identity, "Clark Kent")
        self.assertEqual(superman.is_default, True)

        batman = Superhero.objects.get(name="Batman")
        self.assertEqual(batman.identity, "Bruce Wayne")

        # Verify Article data is restored
        self.assertEqual(Article.objects.count(), 1)
        article = Article.objects.get(title="MAC")
        self.assertEqual(article.content, "N CHEESE")
        self.assertEqual(article.author_id, 1)

    def test_export_to_csv(self):
        """
        Test exporting Superhero and Article tables to CSV files.
        """
        # Execute the export_csv command
        call_command("export_csv")

        # Verify CSV files are created
        self.assertTrue(os.path.exists("superheroes.csv"))
        self.assertTrue(os.path.exists("articles.csv"))

        # Verify content of superheroes.csv
        with open("superheroes.csv", "r") as sh_file:
            reader = csv.DictReader(sh_file)
            rows = list(reader)
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0]["name"], "Superman")
        self.assertEqual(rows[1]["name"], "Batman")

        # Verify content of articles.csv
        with open("articles.csv", "r") as art_file:
            reader = csv.DictReader(art_file)
            rows = list(reader)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["title"], "MAC")
        self.assertEqual(rows[0]["content"], "N CHEESE")

    def test_import_from_csv(self):
        """
        Test importing Superhero and Article tables from CSV files.
        """
        # First, export data to CSV to create CSV files
        call_command("export_csv")

        # Clear the database
        Superhero.objects.all().delete()
        Article.objects.all().delete()
        self.assertEqual(Superhero.objects.count(), 0)
        self.assertEqual(Article.objects.count(), 0)

        # Import data from CSV files
        call_command("import_csv")

        # Verify Superhero data is restored
        self.assertEqual(Superhero.objects.count(), 2)
        superman = Superhero.objects.get(name="Superman")
        self.assertEqual(superman.identity, "Clark Kent")
        self.assertEqual(superman.is_default, True)

        batman = Superhero.objects.get(name="Batman")
        self.assertEqual(batman.identity, "Bruce Wayne")

        # Verify Article data is restored
        self.assertEqual(Article.objects.count(), 1)
        article = Article.objects.get(title="MAC")
        self.assertEqual(article.content, "N CHEESE")
        self.assertEqual(article.author_id, 1)
