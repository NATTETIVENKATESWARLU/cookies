from django.shortcuts import render

from django.http import HttpResponse

from app.forms import *
# # Create your views here.

# def web_page(request):
#     count=int(request.COOKIES.get("count",0))
#     count+=1
#     respones=render(request,"index.html",{"count":count})
#     respones.set_cookie("count",count)
#     return respones


# def home(request):
#     form=register()
#     return render(request,"home.html",{"form":form})


# def second_name(request):
#     name=request.GET['name']
#     respons=render(request,"second.html",{"name":name})
#     respons.set_cookie("name",name)
#     return respons

# import datetime

# def result_a(request):
#     name=request.COOKIES.get("name")
#     date=datetime.datetime.now()
#     return render(request,"result.html",{"name":name,"date":date})



def first_1(request):
    form=register_1()
    return render(request,"cookie/first_1.html",{"form":form})


def second_1(request):
    name=request.GET["name"]
    respones=render(request,"cookie/second_1.html",{"name":name})
    respones.set_cookie("name",name)
    return respones

def gf_name(request):
    name=request.COOKIES["name"]
    age=request.GET["age"]
    resopn=render(request,"cookie/gf_name.html",{"name":name})
    resopn.set_cookie("age",age)
    return resopn


def final_information(request):
    name=request.COOKIES["name"]
    age=request.COOKIES["age"]
    gf=request.GET["gf"]
    return render(request,"cookie/final.html",{"name":name,"age":age,"gf":gf})







