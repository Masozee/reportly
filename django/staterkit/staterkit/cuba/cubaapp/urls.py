from django.urls import path
from . import views


urlpatterns = [
    path('', views.indexPage,name='indexPage'),
    path('index2', views.index2,name='index2'),
    # path('raise_support', views.raise_support,name='raise_support'),
    # path('Documentation', views.Documentation,name='Documentation'),

]