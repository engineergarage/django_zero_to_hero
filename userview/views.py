from django.shortcuts import render


def indexview(request):
    return render(request,"index.html")



def loginview(request):
    return render(request, "login.html")