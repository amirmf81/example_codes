from api.cars_api.create_car_pack.create_car_handler import CreateCarHandler


class CreateCar:
    def __init__(self, cars_number, owner_id):
        self.cars_number = cars_number
        self.owner_id = owner_id

    def start(self):
        for i in range(0, self.cars_number):
            CreateCarHandler(self.owner_id).start()
