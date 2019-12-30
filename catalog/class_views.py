from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Customer


class AboutView(TemplateView):
    template_name = "about.html"


class CustomersList(ListView):
    model = Customer
