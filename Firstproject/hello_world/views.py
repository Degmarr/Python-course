from django.shortcuts import render

# Create your views here.
def Mainpage(request):
    context = {}
    return render(request,"hello_world/index.html",context)
