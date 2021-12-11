from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Article
from .forms import CreateArticle
# Create your views here.

def home_view(request) :
    obj = Article.objects.all()
    context = {"object":obj}
    return render(request, "home.html", context)

@login_required
def create_article(request) :
    form = CreateArticle(request.POST or None, request.FILES or None)
    if form.is_valid() :
        user = form.save(commit=False)
        user.auther = request.user
        user.save()
        return redirect("/")
    context = {"form":form}
    return render(request, "create-update.html", context)

def update_view(request, id) :
    obj = get_object_or_404(Article, id=id)
    form = CreateArticle(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("/")
    context = {"form":form}
    return render(request, "create-update.html", context)

def delete_view(request, id) :
    obj = get_object_or_404(Article, id=id)
    if request.method == "POST" :
        obj.delete()
        return redirect("/")
    context = {}
    return render(request, "delete.html", context)

def search_view(request) :
    query = request.GET.get("q")
    qs = Article.objects.all()
    if query is not None :
        lookups = Q(name__icontains=query)
        qs = Article.objects.filter(lookups)
    context={"object_list":qs}
    return render(request, "search.html", context)


def detail_view(request, id) :
    obj = get_object_or_404(Article, id=id)
    context={"object":obj}
    return render(request, "detail.html", context)