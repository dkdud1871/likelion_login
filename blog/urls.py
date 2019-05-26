from django.urls import path
from .import views

urlpatterns=[
    path('home/', views.home, name='home'),
    path('idea/<int:idea_id>/', views.detail, name='detail'),
    path('idea/new/', views.idea_new, name='new'),
    path('idea/<int:idea_id>/edit', views.idea_edit, name='edit'),
    path('idea/<int:idea_id>/delete', views.idea_delete, name='delete'),
   
]