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

# below are tutorial test
from .forms import NameForm
def byname(request):
    form_class = NameForm
    context = {
        'form': form_class,
    }

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            card_name = request.POST.get('card_name', '')
            collectibles = Cards.objects.all().filter(collectible = 1)
            result = collectibles.filter(name__contains=card_name)
            return HttpResponse(result)

    return render(request, 'searchcard/byname.html', context)
