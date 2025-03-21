from django.urls import path
from . import views

app_name = 'posts'      #This says that the urlpatterns below are inside the posts app

urlpatterns = [
    path('', views.posts_list, name = "list"),
    path('<slug:slug>', views.post_page, name = "page"),
]