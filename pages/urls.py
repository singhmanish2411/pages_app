from django.urls import path
from .views import HomePageView , AboutPageView

urlpatterns = [
    path('', HomePageView.as_view(),name = 'home'), #for the home page
    path('about/' , AboutPageView.as_view(), name= 'about'), #for the about page
]