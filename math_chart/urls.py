from django.urls import path
from . import views

app_name = 'math_chart'
urlpatterns = [
    path('', views.home, name='home'),
    path('my_chart_10/', views.my_chart_10, name='my_chart_10'),
    path('my_chart_20/', views.my_chart_20, name='my_chart_20'),
    path('b6_b6', views.b6_b6, name='b6_b6'),
    path('my_square', views.my_square, name='my_square'),
    path('my_sin', views.my_sin, name='my_sin'),
    path('my_cos', views.my_cos, name='my_cos'),
    path('my_tan', views.my_tan, name='my_tan'),
    path('trigonometry', views.trigonometry, name='trigonometry'),
]
