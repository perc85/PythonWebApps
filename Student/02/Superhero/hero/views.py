from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'heroes.html'

class HulkView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Hulk',
            'body': 'Thats my secret, Captain. Im always angry.',
            'image': '/static/images/hulk.jpg'
        }

class CaptainView(TemplateView):
    template_name = 'hero.html'
    
    def get_context_data(self, **kwargs):
        return {
            'title': 'Captain America',
            'body': 'I can do this all day.',
            'image': '/static/images/captain_america.jpg'
        }
    
class WonderView(TemplateView):
    template_name = 'hero.html'
    
    def get_context_data(self, **kwargs):
        return {
            'title': 'Wonder Woman',
            'body': 'Its not about what you deserve; its about what you believe. And I believe in love.',
            'image': '/static/images/wonder_woman.jpg'
        }
    
class PantherView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Black Panther',
            'body': 'In times of crisis, the wise build bridges while the foolish build barriers.',
            'image': '/static/images/black_panther.jpg'
        }