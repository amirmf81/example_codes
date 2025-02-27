import threading
from myapp.models.car_model import Car


class CreateCarHandler(threading.Thread):
    def __init__(self, owner_id):
        super().__init__()
        self.owner_id = owner_id

    def run(self):
        Car.create(owner_id=self.owner_id)
