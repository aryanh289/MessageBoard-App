from django.shortcuts import render
from django.views.generic import ListView
from .models import Posts

# Create your views here.
class HomePage(ListView):
    model = Posts
    template_name = "home.html"
    context_object_name = 'all_post_list'
