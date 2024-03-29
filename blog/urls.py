from django.urls import path
from .views import blogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, SignUpView


urlpatterns = [
    path("accounts/signup/", SignUpView.as_view(), name = "signup"),
    path("post/<int:pk>/delete/", BlogDeleteView.as_view(), name= "post_delete"),
    path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name= "post_edit"),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name= 'post_detail'),
    path("", blogListView.as_view(), name="home"),
]