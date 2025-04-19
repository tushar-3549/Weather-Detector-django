import requests
from django.shortcuts import render
from django.conf import settings


def index(request):
    API_KEY = settings.WEATHER_API_KEY
    data = {}
    city = ''
    
    if request.method == 'POST':
        city = request.POST.get('city')
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            json_data = response.json()
            data = {
                'country_code': json_data['sys']['country'],
                'coordinate': f"{json_data['coord']['lat']}, {json_data['coord']['lon']}",
                'temp': json_data['main']['temp'],
                'pressure': json_data['main']['pressure'],
                'humidity': json_data['main']['humidity'],
            }
        else:
            data = {
                'country_code': '',
                'coordinate': '',
                'temp': 'Not found',
                'pressure': '',
                'humidity': ''
            }

    return render(request, 'index.html', {'data': data, 'city': city})
