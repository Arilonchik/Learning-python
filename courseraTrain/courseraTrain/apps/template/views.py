from django.shortcuts import render

# Create your views here.


def echo(request):
    context = {'get': request.GET, 'post': request.POST, 'meta': request.META}
    print(context)
    return render(request, 'echo.html', context, status=200)


def tag_check(request):
    context = {'a': request.GET['a'], 'b': request.GET['b']}
    return render(request, 'filters.html', context, status=200)


def extends(request):
    context = {'a': request.GET['a'], 'b': request.GET['b']}
    return render(request, 'extend.html', context, status=200)

