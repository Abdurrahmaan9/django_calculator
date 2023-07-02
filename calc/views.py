from django.shortcuts import render
from django.http import request, HttpResponse
# Create your views here.


def index(request):
    return render(request,'index.html')

def submitquery(request):
    question = request.GET['query']
    try:
        answer = eval(question)
        mydict = {
            'question': question,
            'answer': answer,
            'result': True,
            'error': False
        }
        return render(request, 'index.html',context=mydict)
    except:
        mydict = {
            'error': True
        }
        error_message='Invalid Input'
        return render(request, 'index.html', context=mydict)