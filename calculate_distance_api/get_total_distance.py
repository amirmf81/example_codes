from myapp.models.location_model import Location
from api.calculate_distance_api.calculate_geography_distance import calculate_geography_distance_func


def get_total_distance_func(car_id, day):
    total_distance = 0.0
    locations = Location.get_all_locations(car_id=car_id)
    for location_place in range(0, len(locations)):
        if locations[location_place].date.date() == day and location_place + 1 < len(locations):
            first_location = locations[location_place]
            second_location = locations[location_place + 1]
            total_distance += calculate_geography_distance_func(
                lat1=first_location.latitude,
                lon1=first_location.longitude,
                lat2=second_location.latitude,
                lon2=second_location.longitude,
            )
    return total_distance
