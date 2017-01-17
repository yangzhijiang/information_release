from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def list(request):
    return  HttpResponse("这是消息列表处理视图")

def detail(request):
    return HttpResponse("消息详情")

def audit(request):
    return HttpResponse("消息审核")

def add(request):
    return HttpResponse("添加消息")


