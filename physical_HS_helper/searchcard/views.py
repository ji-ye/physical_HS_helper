from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Cards

def index(request):
    return render(request, 'searchcard/index.html')


def card_id(request, card_id):
    '''
    Display card name by typing a card's db_index after "searchcard/"
    '''
    collectibles = Cards.objects.all().filter(collectible = 1)
    try:
        card = collectibles[int(card_id)]
        # card = collectibles[card_id]
    except Cards.DoesNotExist:
        raise Http404("Card does not exist.")
    return render(request, 'searchcard/card_id.html', {'card': card})
