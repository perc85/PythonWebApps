from django.core.management.base import BaseCommand
from articles.export_import_utils import export_to_csv

class Command(BaseCommand):
    help = 'Export Superhero and Article tables to CSV'

    def handle(self, *args, **kwargs):
        export_to_csv()
        self.stdout.write(self.style.SUCCESS('Data exported to CSV successfully!'))
