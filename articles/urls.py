from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('topics/', views.topics, name='topics'),
    path('topic/<int:topic_id>/', views.topic, name='topic'),
    path('article/<int:article_id>/', views.article, name='article'),
    path('add_article/', views.add_article, name='add_article'),
    path('add_topic/', views.add_topic, name='add_topic'),
    path('edit_article/<int:article_id>/', views.edit_article, name='edit_article'),
]
