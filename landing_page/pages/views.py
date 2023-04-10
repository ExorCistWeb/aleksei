from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    """
    Функция-контроллер главной страницы.
    :param request: Объект запроса.
    :return: Объект ответа с главной страницей.
    """
    context = {}
    return render(request=request,
                  template_name='base.html',
                  context=context)