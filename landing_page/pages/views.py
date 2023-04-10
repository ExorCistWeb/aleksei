from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Image,Individual,Family,Subscription5,Subscription10,Subscription15

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    """
    Функция-контроллер главной страницы.
    :param request: Объект запроса.
    :return: Объект ответа с главной страницей.
    """
    images=Image.objects.all()
    individuals = Individual.objects.all()
    familys = Family.objects.all()
    subscription5s = Subscription5.objects.all()
    subscription10s = Subscription10.objects.all()
    subscription15s = Subscription15.objects.all()
    context = {
        'images':images,
        'individuals': individuals,
        'familys':familys,
        'subscription5s':subscription5s,
        'subscription10s':subscription10s,
        'subscription15s':subscription15s,
        }
    return render(request=request,
                  template_name='base.html',
                  context=context)