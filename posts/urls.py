#import sys     
#print(sys.path)

from django.urls import path

from .views import HomeView, AboutView, PostDetailView

urlpatterns =[
    path('',HomeView.as_view(),name ="home"),
    path('<int:pk>/',PostDetailView.as_view(), name ="post_detail"),
    path('posts/',AboutView.as_view(),name="about"),
    ]