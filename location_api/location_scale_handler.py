from api.location_api.get_company import get_company_func
from api.scale_api.get_company_scale import get_company_scale_func
from myapp.models.location_model import Location
from api.location_api.check_location_scale_pack.check_location_scale_handler import check_location_scale_handler_func


def location_scale_handler_func(location: Location):
    #try and exept
    company_id = get_company_func(car_id=location.car_id)
    scales = get_company_scale_func(company_id=company_id)
    check_location_scale_handler_func(location=location, scales=scales)
