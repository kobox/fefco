from django.views import generic
from fefcocatalog.models import FefcoCategory

class HomePage(generic.ListView):
    template_name = "home.html"
    context_object_name = 'fefco_list'

    def get_queryset(self):
        return FefcoCategory.objects.filter(parent_category=None).order_by('fefcocode')[:10]

class AboutPage(generic.TemplateView):
    template_name = "about.html"
