from django.urls import path
from .views import *

urlpatterns = [
    path('/contact-create', ContactCreateView.as_view()),
    path('/contact', ContactListView.as_view()),
]