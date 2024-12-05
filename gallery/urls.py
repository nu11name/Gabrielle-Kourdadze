from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('paintings/', views.paintings, name='paintings'),
    path('works-on-paper/', views.works_on_paper, name='works_on_paper'),
    path('exhibitions/', views.exhibitions_view, name='exhibitions_view'),
    path('texts-publications-en/', views.texts_publications_en, name='texts_publications_en'),
    path('texts-publications-fr/', views.texts_publications_fr, name='texts_publications_fr'),
    path('video/', views.video, name='video'),
    path('bio/', views.bio, name='bio'),
    path('coming_soon/', views.coming_soon, name='coming_soon'),
    path('contact/', views.contact, name='contact'),
]