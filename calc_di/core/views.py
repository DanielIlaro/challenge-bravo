from django.shortcuts import render

from .forms import ListNumbers, Calculator


# function choice numbers
def choiceNumber(text_number, number):
    list = text_number.split(',')
    list_reformated = []
    if len(list) != number:
        plus = int(number) - len(list)
        for i in range(plus):
            list.append('0')

    for i in range(int(number)):
       list_reformated.append(list[i])

    bigger_number = 0
    smaller_number = int(list_reformated[0])

    for number in list_reformated:
        if int(number) > bigger_number:
            bigger_number = int(number)
        elif int(number) < smaller_number:
            smaller_number = int(number)
    return [bigger_number, smaller_number, list_reformated]

# Views
def index(request):
    # text alert
    text_alert = """Como funciona: Escolha quantidade de números que vão conter na lista, em seguida digite os números
                    da lista, separando eles por ','(vírgula) e se for acrescentado mais números do que a quantidade que 
                    foi definida no outro campo os números da lista que estiverem além do limite serão desconciderados.
                    Se for colocado uma quantidade de números menor na lista do que foi previsto pelo usuario, essas lacunas
                    serão preenchidas com 0.
                    No final do calculo aparecerá a informação de qual o maior e o menor número da lista. 
                    """

    form = ListNumbers()

    number_numbers = request.POST.get('number_numbers')
    list_numbers = request.POST.get('list_numbers')

    if number_numbers is not None and list_numbers is not None:
        list_return = choiceNumber(list_numbers, number_numbers)
        bigger_number = list_return[0]
        smaller_number = list_return[1]
        list_numbers = list_return[2]
        dictionari = {'form': form, 'text_alert': text_alert, 'number_numbers': number_numbers, 'list_numbers': list_numbers,
                      'bigger_number': bigger_number, 'smaller_number': smaller_number}
    else:
        dictionari = {'form': form, 'text_alert': text_alert, 'number_numbers': number_numbers, 'list_numbers': list_numbers}

    return render(request, 'index.html', dictionari)

# view Calculadora
def calculate(request):
    form = Calculator()
    return render(request, 'calculate.html', {'form': form})
