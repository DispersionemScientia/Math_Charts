from django.shortcuts import render, redirect
from .forms import TopicForm, ArticleForm
from .models import Topic, Article
from django.contrib.auth.decorators import login_required

def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'articles/topics.html', context)

def article(request, article_id):
    article = Article.objects.get(id=article_id)
    topic = article.topic
    context = {'article': article, 'topic_id': topic.id}
    return render(request, 'articles/article.html', context)

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    articles = topic.article_set.order_by('date_added')
    context = {'topic': topic, 'articles': articles}
    return render(request, 'articles/topic.html', context)

@login_required
def add_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:topics')
    context = {'form': form}
    return render(request, 'articles/add_topic.html', context)

@login_required
def add_article(request):
    if request.method != 'POST':
        form = ArticleForm()
    else:
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:topics')
    context = {'form': form}
    return render(request, 'articles/add_article.html', context)

@login_required
def edit_article(request, article_id):
    article = Article.objects.get(id=article_id)
    topic = article.topic
    if request.method != 'POST':
        form = ArticleForm(instance=article)
    else:
        form = ArticleForm(instance=article, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:topic', topic_id=topic.id)
    context = {'article': article, 'topic': topic, 'form': form}
    return render(request, 'articles/edit_article.html', context)

