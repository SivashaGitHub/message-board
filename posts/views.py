from django.views.generic import ListView,DetailView
from .models import post

# Create your views here.

class HomeView(ListView):
    model = post

    template_name = "home.html"
    context_object_name = "all_posts"

class PostDetailView(DetailView):
    model = post
    template_name ="post_detail.html"

class AboutView(ListView):
    template_name ="about.html"

