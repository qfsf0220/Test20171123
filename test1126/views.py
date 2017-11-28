from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def index(request):
    # return HttpResponse("这是一个test main index page.")
    return  render(request,'index.html')


def add(request,a,b):
    c=int(a)+int(b)
    return HttpResponse(str(c))

def add2(request):
    a=request.GET['a']
    b=request.GET['b']
    ia=int(a)
    ib=int(b)
    return  HttpResponse(str(ia+ib))

def info(request):
    var =95
    abc ="这是一个test string"
    listabc = ["aa","bb","cc","dd"]
    list2 = [str(x) for x in range(100)]
    info_dict= {"user":"qf","content":"web support"}
    return  render(request,'home.html',{"abcc":abc,"list":listabc,"info_dict":info_dict,"list2":list2,"var":var})
#
#     forloop.counter索引从1开始算
#     forloop.counter0索引从0开始算
#     forloop.revcounter索引从最大长度到1
#     forloop.revcounter0索引从最大长度到0
#     forloop.first当遍历的元素为第一项时为真
#     forloop.last当遍历的元素为最后一项时为真
#     forloop.parentloop用在嵌套的for 循环中，
# 获取上一层for 循环的 forloop
from .my_forms import Addform

def home2(request):
    if request.method=="POST":
        form  = Addform(request.POST)

        if form.is_valid():
            a=form.cleaned_data['a']
            b=form.cleaned_data['b']
            return HttpResponse(str(int(a)+int(b)))
    else:
        form = Addform()
    return  render(request,'index2.html',{'form':form})
