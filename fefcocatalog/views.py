from django.views import generic
from .models import FefcoCategory


class DetailView(generic.DetailView):
    model = FefcoCategory
    template_name = 'detail.html'