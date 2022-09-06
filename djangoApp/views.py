from django.shortcuts import render
import datetime

# Create your views here.
def hello(request):
    context = {'var' : datetime.datetime.now(), 'var1' : 'open'}
    return render(request, 'helo.html', context)

def main(request):
    return render(request, 'main.html')