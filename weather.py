import requests

from settings import weather_API_KEY


def weather_by_city(city_name):
    weather_url = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
    params = {
        "key": weather_API_KEY,
        "q": city_name,
        "format": "json",
        "num_of_days": 1,
        "showlocaltime": "yes",
        "lang": "ru"
    }
    try:
        result = requests.get(weather_url, params=params)
        result.raise_for_status()
        weather = result.json()
        if "data" in weather:
            if "current_condition" in weather["data"]:
                try:
                    return  weather["data"]["current_condition"][0] 
                except (IndexError, TypeError):
                    return False
    except (requests.RequestException, ValueError):
        print('сетевая ошибка')
        return False
    return False


if __name__ == "__main__":
    w = weather_by_city("Moscow,Russia")
    print(w)

