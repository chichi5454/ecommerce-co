
from django.urls import path
from .views import index,get_card_details

urlpatterns = [
    path('', index,name='index'),
    path('view-card',get_card_details,name='view-card')
]
