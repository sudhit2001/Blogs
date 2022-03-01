from django.shortcuts import render,redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def article_list(request):
    article=Article.objects.all().order_by('date')
    return render(request,'articles/article.html',{"articles":article})

def article_detail(request,slug):
    # return HttpResponse(slug)
    article=Article.objects.get(slug=slug)
    return render(request,'articles/article-detail.html',{"article":article})

@login_required(login_url='accounts:login')
def article_create(request):
    if request.method=='POST':
        form=forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.author=request.user
            instance.save()
            return redirect('articles:list')
    else:
        form=forms.CreateArticle
    return render(request,'articles/create.html',{"form":form})
