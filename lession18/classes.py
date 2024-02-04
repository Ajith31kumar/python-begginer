class vehicle:
    def __init__(self,make,model):
        self.make = make
        self.model = model 


    def moves(self):
        print('moves along..')

    def get_make_model(self):
        print(f"i am a {self.make},{self.model}")    

my_car = vehicle('tesla','model 3')
my_car . get_make_model()
# print(my_car.make)
# print(my_car.model)
my_car .moves()      

your_car = vehicle('cadillac','escalade')
your_car.get_make_model
your_car.moves()


class Airplane(vehicle):
    def __init__(self,make,model,faa_id):
        super().__init__(make,model)
        self.faa_id = faa_id

    def moves(self):
        print('flies along..')


class Truck(vehicle):
    def moves(self):
        print('Rumbles along ..')

class Golfcart(vehicle):
    pass

cessna = Airplane('cessna','skyhawk','n-12345')
mack = Truck('mack','pinnacle')
Golfwagon = Golfcart('yamaha','gt100') 

cessna.get_make_model()
cessna.moves()

mack.get_make_model()
mack.moves()

Golfwagon.get_make_model()
Golfwagon.moves()

print('\n\n')

for v in (my_car,your_car,cessna,mack,Golfwagon):
    v.get_make_model()
    v.moves()
    
