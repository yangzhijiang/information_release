# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,RequestContext

from models import Information,InformationPic,AuditHistory,User

# Create your views here.

def list(request):

    informations = Information.objects.all()

    template = loader.get_template('information/list.html')
    context = RequestContext(request,{
        'latest_question_list':informations
    })
    # for information in informations:
    #     print information.title
    print "这是消息列表处理视图"
    return  HttpResponse(template.render(context))


def detail(request,information_id):
    return HttpResponse("消息详情")

def audit(request):
    return HttpResponse("消息审核")

def add(request):
    return HttpResponse("添加消息")


