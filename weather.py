import urllib.request, json

def make_link_and_data(city):

    url= f'https://api.openweathermap.org/data/2.5/weather?q={city}&APPID=225a89990cad37c63353ff33daccd85b'
    with urllib.request.urlopen(url) as url:
        data = json.load(url)
        print(data)
        return data


def extract_data(dictw):

    temperature = int(dictw['main']['temp'])-273
    temperature_min = int(dictw['main']['temp_min']) - 273
    temperature_max = int(dictw['main']['temp_max']) - 273
    temperature_feel = int(dictw['main']['feels_like'])-273
    humidity = str(dictw['main']['humidity']) + '%'
    description = dictw['weather'][0]['description']
    wind=dictw['wind']['speed']
    city=dictw['name']
    return [temperature, temperature_feel, temperature_min, temperature_max, humidity, description,wind,city]


print(extract_data(make_link_and_data('Stockholm')))

