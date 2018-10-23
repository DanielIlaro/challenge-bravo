from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ListNumbers

#function choice numbers
def choiceNumber(text_number):
    list = text_number.split(',')
    bigger_number = 0
    smaller_number = int(list[0])

    for number in list:
        if int(number) > bigger_number:
            bigger_number = int(number)
        elif int(number) < smaller_number:
            smaller_number = int(number)
    return [bigger_number, smaller_number]

#Views
def index(request):
    form = ListNumbers()
    
    number_numbers = request.POST.get('number_numbers')
    list_numbers = request.POST.get('list_numbers')
    if number_numbers != None and list_numbers != None:
        bigger_number = choiceNumber(list_numbers)[0]
        smaller_number = choiceNumber(list_numbers)[1]
        dictionari = {'form':form, 'number_numbers':number_numbers, 'list_numbers':list_numbers,
                 'bigger_number':bigger_number, 'smaller_number':smaller_number}
    else:
        dictionari= {'form':form, 'number_numbers':number_numbers, 'list_numbers':list_numbers}
    
    return render(request, 'index.html', dictionari)

def calculate(request):
    return render(request, 'calculate.html')