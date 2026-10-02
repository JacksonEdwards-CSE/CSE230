from django.shortcuts import render
from .models import Post


def home(request):
    topic = ""
    error = ""

    if request.method == "POST":
        topic = request.POST.get("topic", "").strip()
        if not topic:
            error = "Please enter a discussion topic."
        elif len(topic) < 3:
            error = "Your topic must be at least 3 characters long."
        elif len(topic) > 80:
            error = "Your topic must be 80 characters or fewer."
        else:
            Post.objects.create(topic=topic)

    posts = Post.objects.order_by("-created_at")

    return render(request, "main/home.html", {
        "topic": topic,
        "error": error,
        "posts": posts,
    })
