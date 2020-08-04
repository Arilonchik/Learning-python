import json

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from django.forms.models import model_to_dict
import base64
from django.contrib.auth import authenticate

from .models import Item, Review
from .forms import ItemForm, ReviewForm

from django.contrib.auth.mixins import LoginRequiredMixin


@method_decorator(csrf_exempt, name='dispatch')
class AddItemView(View):
    """View для создания товара."""

    def get(self, request):
        return render(request, 'tryform.html', {'req': request})

    def post(self, request):
        if 'HTTP_AUTHORIZATION' in request.META:

            auth = request.META['HTTP_AUTHORIZATION'].split()
            if len(auth) == 2:
                if auth[0].lower() == "basic":
                    uname, passwd = base64.b64decode(auth[1].encode("utf-8")).decode('utf-8').split(':')
                    print(uname, passwd)
                    user = authenticate(username=uname, password=passwd)
                    if user is None:
                        return JsonResponse({}, status=401)
                else:
                    return JsonResponse({}, status=401)
            else:
                return JsonResponse({}, status=401)
        else:
            return JsonResponse({}, status=401)
        print(user.is_staff)
        if user.is_staff:
            formset = ItemForm(request.POST)
            if formset.is_valid():
                good = Item(**formset.cleaned_data)
                good.save()
                id = good.pk
                data = {'id': id}
                return JsonResponse(data, status=201)
            else:
                return JsonResponse({}, status=400)
        else:
            return JsonResponse({}, status=403)


@method_decorator(csrf_exempt, name='dispatch')
class PostReviewView(View):
    """View для создания отзыва о товаре."""


    def post(self, request, item_id):

        formset = ItemForm(request.POST)
        if formset.is_valid():
            try:
                good = Item.objects.get(pk=item_id)
                rev = Review(item=good, **formset.cleaned_data)
                rev.save()
                data = {'id': rev.pk}
                return JsonResponse(data, status=201)
            except ObjectDoesNotExist:
                return JsonResponse({}, status=404)
        else:
            return JsonResponse({}, status=400)



@method_decorator(csrf_exempt, name='dispatch')
class GetItemView(View):
    """View для получения информации о товаре.

    Помимо основной информации выдает последние отзывы о товаре, не более 5
    штук.
    """

    def get(self, request, item_id):
        try:
            good = Item.objects.get(pk=item_id)
            reviews = good.review_set.objects.all()[:5]
            data = model_to_dict(good, fields=['title', 'description', 'price'])
            data['id'] = good.pk
            data['reviews'] = []
            for rew in reviews:
                data['reviews'].append(model_to_dict(rew, fields=['text', 'grade']))
                data['reviews'][-1]['id'] = rew.pk
            return JsonResponse(data, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({}, status=404)
