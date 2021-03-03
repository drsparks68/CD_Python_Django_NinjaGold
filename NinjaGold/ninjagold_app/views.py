from django.shortcuts import render, redirect
import random
from datetime import datetime

def index(request):
    request.session['total_gold'] = 0
    request.session['ledger'] = []
    return render(request, 'index.html')

def process(request):
    if request.method == "POST":
        if request.POST['place'] == 'farm':
            gold = random.randint(10, 21)
            request.session['ledger'].append('You won ' + str(gold) + ' gold pieces from the ' + request.POST['place'] + '! (' + str(datetime.now()) + ')')
        
        elif request.POST['place'] == 'cave':
            gold = random.randint(5, 10)
            request.session['ledger'].append('You won ' + str(gold) + ' gold pieces from the ' + request.POST['place'] + '! (' + str(datetime.now()) + ')')

        elif request.POST['place'] == 'house':
            gold = random.randint(2, 5)
            request.session['ledger'].append('You won ' + str(gold) + ' gold pieces from the ' + request.POST['place'] + '! (' + str(datetime.now()) + ')')

        if request.POST['place'] == 'casino':
            gold = random.randint(-50, 51)
            if gold >= 0:
                request.session['ledger'].append('You won ' + str(gold) + ' gold pieces from the ' + request.POST['place'] + '! (' + str(datetime.now()) + ')')
            else:
                request.session['ledger'].append('OUCH! You lost ' + str(gold) + ' gold pieces from the ' + request.POST['place'] + '! (' + str(datetime.now()) + ')')
    
        request.session['total_gold'] += gold
    return redirect('/')    
