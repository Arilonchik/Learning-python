from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from db import query
from db.models import User, Blog, Topic


def check(request):
    query.get_topic_that_dont_have_like()
    for us in User.objects.all():
        print(us.first_name)
        print(us.last_name)
    for us in Blog.objects.all():
        print(us.title, us.author.first_name, us.created)
        print(*map(lambda x: x.first_name, us.subscribers.all()))
    for us in Topic.objects.all():
        print(us.title, us.author.first_name, us.created, us.blog.title)
        print(*map(lambda x: x.first_name, us.likes.all()))

    return HttpResponse('d')
