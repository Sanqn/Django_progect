from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')
register_converter(converters.MydateConverter, 'my_date')

urlpatterns = [
    # path('<my_date:sigen_zodiac>/', views.get_date),  # dynamic URLS
    # path('<yyyy:sigen_zodiac>/', views.get_four_digits),  # dynamic URLS
    path('', views.index, name= 'url_index'),  # dynamic URLS
    path('type/', views.type),
    path('type/<type_sign>/', views.get_type_sign, name='url_type'),
    path('<int:month>/<int:day>/', views.check_day),
    path('<int:sigen_zodiac>/', views.get_more_sigen_zodiac_by_number),  # dynamic URLS
    path('<str:sigen_zodiac>/', views.get_more_sigen_zodiac, name='url_revers'), # dynamic URLS
    # path('leo', views.leo),
    # path('scorpio', views.scorpio),
    # path('aries', views.aries),
    # path('taurus', views.taurus),
    # path('gemini', views.gemini),

]