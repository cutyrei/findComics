
from django.urls import path
from . import views

app_name = 'findComics'

urlpatterns = [
    path('', views.main, name='main'),
    path('list/', views.index, name='index'),
    # path('<int:comic_id>/', views.details, name='details'),
]