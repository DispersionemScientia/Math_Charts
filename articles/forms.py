from django import forms
from .models import Topic, Article

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['name']
        labels = {'name': 'Название новой темы'}
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'text', 'topic']
        labels = {'name': 'Название статьй', 'text': 'Содержимое статьй', 'topic': 'Подтвердите тему'}