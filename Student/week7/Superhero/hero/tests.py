from django.test import TestCase
from .models import Superhero

# Create your tests here.

class SuperheroModelTest(TestCase):
    def test_superhero_creation(self):
        hero = Superhero.objects.create(
            name='Test Hero',
            identity='Test Identity',
            description='Test Description',
            strength='Test Strength',
            weakness='Test Weakness',
            image='images/test_hero.jpg'
        )
        self.assertEqual(hero.name, 'Test Hero')