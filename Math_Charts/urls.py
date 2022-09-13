from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('math_chart.urls')),
    path('art/', include('articles.urls')),
    path('users/', include('users.urls')),

]
