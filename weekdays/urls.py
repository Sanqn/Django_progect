from django.urls import path
from . import views

urlpatterns = [
    path('<int:new_day>/', views.create_day_number),
    path('<str:new_day>/', views.create_day, name='revers_url_day'),
    # path('monday', views.monday),
    # path('tuesday', views.tuesday),
]