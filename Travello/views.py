from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):

    dests = Destination.objects.all()

    '''
    dest1 = Destination()
    dest1.name = 'Dar-es Salaam'
    dest1.desc = 'The city of waters'
    dest1.img = 'destination_1.jpg'
    dest1.price = '700'
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Mumbai'
    dest2.desc = 'The city that never sleeps'
    dest2.img = 'destination_2.jpg'
    dest2.price = '650'
    dest2.offer = True

    dest3 = Destination()
    dest3.name = 'Indonesia'
    dest3.desc = 'The city of lorem'
    dest3.img = 'destination_3.jpg'
    dest3.price = '750'
    dest3.offer = False

    dest4 = Destination()
    dest4.name = 'San Franscisco'
    dest4.desc = 'The city of Technology'
    dest4.img = 'destination_4.jpg'
    dest4.price = '600'
    dest4.offer = False


    dest5 = Destination()
    dest5.name = 'Cape Town'
    dest5.desc = 'The cape of Africa'
    dest5.img = 'destination_5.jpg'
    dest5.price = '720'
    dest5.offer = False

    dest6 = Destination()
    dest6.name = 'NewYork'
    dest6.desc = 'The city of heights'
    dest6.img = 'destination_6.jpg'
    dest6.price = '560'
    dest6.offer = False


    dests = [dest1, dest2, dest3, dest4, dest5, dest6]
    '''

    return render(request, 'index.html', {'dests': dests})
