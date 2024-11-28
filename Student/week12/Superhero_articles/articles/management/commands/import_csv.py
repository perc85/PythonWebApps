from django.core.management.base import BaseCommand
from articles.export_import_utils import import_from_csv

class Command(BaseCommand):
    help = 'Import Superhero and Article tables from CSV files'

    def handle(self, *args, **kwargs):
        import_from_csv()
        self.stdout.write(self.style.SUCCESS('Data imported from CSV successfully!'))
