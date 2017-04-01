from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Cards
from .forms import NameForm

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

# below are tutorial test, works more or less at 2:27am April 1, 2017
def byname(request):
    form_class = NameForm
    context = {
        'form': form_class,
        'img_link': 'http://media.services.zam.com/v1/media/byName/hs/cards/enus/____.png'
    }

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            card_name = request.POST.get('card_name', '')
            collectibles = Cards.objects.all().filter(collectible = 1)
            result = collectibles.filter(name__contains=card_name)
            card_lst = []
            img_lst = []
            for card in result:
                card_lst.append(card)
            # img_link = 'http://media.services.zam.com/v1/media/byName/hs/cards/enus/CS2_029.png'
                img_link = context['img_link'].replace('____', card.id)
                img_lst.append(img_link)
            return render(request, 'searchcard/bynameresult.html', {'form': card_lst, 'img_lst':img_lst})

    return render(request, 'searchcard/byname.html', context)
