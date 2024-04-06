from django.urls import path
from . import views  # Импортируем views из текущего приложения

app_name = 'pages'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('rules/', views.rules, name='rules'),
]
