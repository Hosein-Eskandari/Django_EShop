CART_SESSION_ID = 'cart'

class Cart:
    def __init__(self, request):
        self.session = request.session

        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}

        self.cart = cart

    def __getitem__(self, item):
        return self.cart[item]

    def __iter__(self):
        for item in self.cart.values():
            yield item


    @property
    def product_ids(self):
        return self.cart.keys()

    def add_to_cart(self, product_id, product_price, quantity, is_update):

        if product_id not in self.cart:
            self.cart[product_id] = {
                "quantity": 0,
                "price": product_price
            }

        if is_update:
            self.cart[product_id]["quantity"] = quantity
        else:
            self.cart[product_id]["quantity"] += quantity

        self.__save_session()


    def remove_from_cart(self, product_id):
        if product_id in self.cart:
            del self.cart[product_id]
            self.__save_session()



    def __save_session(self):
        self.session[CART_SESSION_ID] = self.cart
        self.session.modified = True

