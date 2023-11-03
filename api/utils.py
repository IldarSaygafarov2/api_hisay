from django.conf import settings
from geopy import GoogleV3


def get_address_by_coordinates(coordinates: str):
    locator = GoogleV3(api_key=settings.MAPS_API_KEY, domain="maps.google.ru")
    result = locator.reverse(coordinates)
    return result.address
