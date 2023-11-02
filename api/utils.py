from geopy.geocoders import Nominatim


def get_address_by_coordinates(coordinates: str):
    geocoder = Nominatim(user_agent="hisay")
    result = geocoder.reverse(coordinates)
    return result.address
