from django.core.management.base import BaseCommand
from articles.export_import_utils import export_to_json

class Command(BaseCommand):
    help = 'Export Superhero and Article tables to JSON'

    def handle(self, *args, **kwargs):
        export_to_json()
        self.stdout.write(self.style.SUCCESS('Data exported to JSON successfully!'))
