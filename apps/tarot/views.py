from django.shortcuts import render, HttpResponse, redirect
from apps.tarot.models import *
import random

def index(request):
    return render(request, 'tarot/index.html')

def major_arcana(request):
    context = {
        "major_arcana": Tarot.objects.filter(category="major"),
    }
    return render(request, 'tarot/major-arcana.html', context)

def tarot_meaning(request, id):
    context = {
        "one_major": Tarot.objects.get(id=id)
    }
    return render(request, 'tarot/tarot-meaning.html', context)

def minor_arcana(request):
    context = {
        "minor_arcana": Tarot.objects.filter(category="minor"),
    }
    return render(request, 'tarot/minor-arcana.html', context)

def readings(request):
    return render(request, 'tarot/readings.html')

def random_card(num_of_cards):
    tarot_length = len(Tarot.objects.all())
    rand_card = random.sample(range(1, tarot_length), num_of_cards)
    return rand_card

def three_card(request):
    rand_card = random_card(3)
    past_id = rand_card[0]
    present_id = rand_card[1]
    future_id = rand_card[2]
    context = {
        "past_card": Tarot.objects.get(id=past_id),
        "present_card": Tarot.objects.get(id=present_id),
        "future_card": Tarot.objects.get(id=future_id)
    }
    request.session['past_id'] = past_id
    request.session['present_id'] = present_id
    request.session['future_id'] = future_id
    return render(request, 'tarot/three-card.html', context)

def save_three_card(request):
    current_user = User.objects.get(id=request.session['id'])
    print(request.session['past_id'])
    three_card_reading = ThreeCardReading.objects.create(
        past=Tarot.objects.get(id=request.session['past_id']), 
        present=Tarot.objects.get(id=request.session['present_id']),
        future=Tarot.objects.get(id=request.session['future_id']), 
        user=current_user)
    return redirect('/user_account/' + str(request.session['id']))

def four_card(request):
    rand_card = random_card(4)
    you_id = rand_card[0]
    unknown_id = rand_card[1]
    known_id = rand_card[2]
    action_id = rand_card[3]
    context = {
        "you_card": Tarot.objects.get(id=you_id),
        "unknown_card": Tarot.objects.get(id=unknown_id),
        "known_card": Tarot.objects.get(id=known_id),
        "action_card": Tarot.objects.get(id=action_id)
    }
    return render(request, 'tarot/four-card.html', context)