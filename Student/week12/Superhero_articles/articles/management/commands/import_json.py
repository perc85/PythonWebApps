from django.core.management.base import BaseCommand
from articles.export_import_utils import import_from_json

class Command(BaseCommand):
    help = 'Import Superhero and Article tables from JSON files'

    def handle(self, *args, **kwargs):
        import_from_json()
        self.stdout.write(self.style.SUCCESS('Data imported from JSON successfully!'))
