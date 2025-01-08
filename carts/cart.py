from django.conf import settings

from service.models import Service

class cart(object):
    def __init__(self, request) :
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session.get[settings.CART_SESSION_ID] ={}

        self.cart =cart

        def __iter__(self):
            for p in self.cart.keys():
                self.cart[str(p)]['service'] =Service.objects.get(pk=p)

        def __len__(self): 
            return sum(item['quantity'] for item in self.cart.values )       