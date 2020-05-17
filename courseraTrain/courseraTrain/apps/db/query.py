from datetime import datetime

from django.db.models import Q, Count, Avg
from pytz import UTC

from db.models import User, Blog, Topic


def create():
    u1 = User(first_name='u1', last_name='u1')
    u2 = User(first_name='u2', last_name='u2')
    u3 = User(first_name='u3', last_name='u3')
    u1.save()
    u2.save()
    u3.save()
    blog1 = Blog(title='blog1', author=u1)
    blog2 = Blog(title='blog2', author=u2)
    blog1.save()
    blog2.save()
    blog1.subscribers.add(u1)
    blog1.subscribers.add(u2)
    blog2.subscribers.add(u2)
    topic1 = Topic(title='topic1', blog=blog1, author=u1)
    topic2 = Topic(title='topic2_contetnt', blog=blog1, author=u3, created='2017-01-01')
    topic1.save()
    topic2.save()
    topic1.likes.add(u1, u2, u3)


def edit_all():
    users = User.objects.all()
    for u in users:
        u.first_name ='uu1'
        u.save()


def edit_u1_u2():
    users = User.objects.all().filter(first_name='uu1')
    for u in users:
        u.first_name = 'u1'
        u.save()


def delete_u1():
    u = User.objects.get(first_name='u1')
    u.delete()


def unsubscribe_u2_from_blogs():
    u = User.objects.get(last_name='u2')
    u.subscriptions.clear()


def get_topic_created_grated():
    topics = Topic.objects.filter(created__gt='2018-01-01')
    print(topics)


def get_topic_title_ended():
    top = Topic.objects.get(title__endswith='contetnt')
    print(top.title)


def get_user_with_limit():
    u = User.objects.all().order_by('id')[:2]
    for us in u:
        print(us.first_name)


def get_topic_count():
    blogs = Blog.objects.annotate(topic_count=Count('topic')).order_by('topic_count')
    for t in blogs:
        print(t.topic_count)


def get_avg_topic_count():
    blogs = Blog.objects.annotate(topic_count=Count('topic')).aggregate(Avg('topic_count'))
    print(blogs)


def get_blog_that_have_more_than_one_topic():
    bl = Blog.objects.annotate(topic_count=Count('topic')).filter(topic_count__gte=1)
    for b in bl:
        print(b.title, b.topic_count)


def get_topic_by_u1():
    tops = Topic.objects.all().filter(author__first_name='u1')
    print(tops)


def get_user_that_dont_have_blog():
    u = User.objects.all().filter(blog__isnull=True)
    print(u)


def get_topic_that_like_all_users():
    t = Topic.objects.annotate(likes_count=Count('likes')).filter(likes_count=User.objects.count())
    print(t)


def get_topic_that_dont_have_like():
    t = Topic.objects.annotate(likes_count=Count('likes')).filter(likes_count=0)
    print(t)
