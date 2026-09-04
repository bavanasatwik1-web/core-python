class user:
    def order(self):
        print("Ordered pasta")
class restuarent(user):
    def order(self):
        super().order()
        print("Order recieved")
class swiggy(restuarent):
    def order(self):
        super().order()
        print("delivery partner alinged")
s1=swiggy()
s1.                       