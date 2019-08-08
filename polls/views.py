from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from .models import Question
import logging


logger = logging.getLogger('')




def index(request):
    context = {}
    if request.method == 'POST':
        return  HttpResponse('11')
    return HttpResponse('11')

    # quest = Question.objects.all()
    # context['quest'] = quest
    #
    # return  render(request,'index1.html',context)

def index1(request):
        context = {}
        return render(request, 'index1.html', context)


def Api(request):
    if request.method == 'POST':
        path = request.POST.get('url')
        methon = request.POST.get('method')
        result =1
        Question.objects.create(path=path,methon=methon,result=result)
        return HttpResponse('插入成功')

def index2(request):
        logger.info("1111")
        context = {}
        return render(request, 'login2.html', context)













