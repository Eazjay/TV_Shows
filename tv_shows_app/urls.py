from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.tv_shows),
    path('shows/new', views.create_shows),
    path('shows/create', views.process_shows),
    path('shows/<int:id>', views.display_shows),
    path('shows/<int:id>/edit', views.edit_shows),
    path('shows/<int:id>/update', views.update_shows),
    path('shows/<int:id>/destroy', views.delete_shows),
]