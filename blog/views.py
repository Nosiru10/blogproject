# blog/views.py

from django.views.generic import ListView

from .models import post


class BlogListView(ListView):

    model = post

    template_name = 'home.html'





# Create your views here.
