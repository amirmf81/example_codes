from events import Event
from myapp.models.location_model import Location


class SpeedEvent(Event):
    def __init__(self, location: Location):
        print(location)
        self.location = location
        pass
    pass
