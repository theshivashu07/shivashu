from django.shortcuts import render

# Create your views here.



def index(request):
        ReturningData = dict()
        return render(request,"APIs/index.html",ReturningData); 


def documentations(request):
        ReturningData = dict()
        return render(request,"APIs/documentations.html",ReturningData); 


