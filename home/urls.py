from django.urls import path
from.import views

## These are the Urls we are Mapping

urlpatterns = [
    path('',views.index,name='homepage'),
    path('about/',views.about,name='aboutpage'),
    path('gallery/',views.gallery,name='gallerypage'),
    path('contact/',views.contact,name='contactpage'),
]