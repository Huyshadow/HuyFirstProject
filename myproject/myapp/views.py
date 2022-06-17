from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'name': "Huy",
        "age": 18,
        "nationality": "VietNam"
    }
    return render(request,'index.html', context) # Truyen parameter de no dinamic
    # chi truyen duoc voi dictionary
# Create your views here.

def counter(request):
    text = request.POST['text']
    nums_of_word = len(text.split())
    return render(request,'counter.html',{'nums_of_word': nums_of_word}) 
