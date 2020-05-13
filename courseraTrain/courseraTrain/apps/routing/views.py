from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@require_GET
def simple_route(request):
    return HttpResponse('', status=200)


def slug_route(request, slug):
    if len(slug) > 16:
        return HttpResponse(status=404)
    return HttpResponse(slug, status=200)


def sum_route(request, first, second):
    return check_int(first, second, 404)


@require_GET
def sum_get_method(request):
    return check_int(request.GET['a'], request.GET['b'], code=400)


@csrf_exempt
@require_POST
def sum_post_method(request):
    return check_int(request.POST['a'], request.POST['b'], code=400)


def check_int(a, b, code):
    try:
        first = int(a)
        second = int(b)
    except ValueError:
        return HttpResponse(status=code)
    return HttpResponse(first+second, status=200)
