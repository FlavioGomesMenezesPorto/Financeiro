from django.urls import path
from . import views
from .views import minha_view

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('signup/', views.signup, name='signup'),
    path('add_account/', views.add_account, name='add_account'),
    path('add_category/', views.add_category, name='add_category'),
    path('add_transaction/', views.add_transaction, name='add_transaction'),
    path('add_saving_goal/', views.add_saving_goal, name='add_saving_goal'),
    path('minha-view/', minha_view, name='minha_view'),
]
