from django.shortcuts import render


def main_page(request):
    return render(request, 'page/main.html')


def logreg(request):
    return render(request, 'page/logreg.html')


def userdetail(request, id):
    return render(request, 'page/user_details.html')


def tag_news(request, tag):
    return render(request, 'page/tag_list.html')

