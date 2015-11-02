from django.shortcuts import render
from django.shortcuts import redirect
from models import Post
# Create your views here.


def index(request):
    posts = Post.objects.all()

    return render(request, "index.html", {"posts": posts})


def post(request):
    if request.GET.get("id") is not None:
        post = Post.objects.get(id=request.GET.get("id"))
        return render(request, "post.html", {"post":post})
    return redirect("home")


def create(request):
    if request.method == "POST":
        post = Post()
        post.title = request.POST.get("title")
        post.body = request.POST.get("body")
        post.save()
        return redirect("home")
    return render(request, "create.html")