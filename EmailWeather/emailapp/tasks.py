from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from .models import EmailSub
import requests
from rest_framework.response import Response
from rest_framework import status

@shared_task
def send_mail_task(*args):
    print("Mail sending.......")
    KEY = 'a5df6a8757bf4216b21134024232504'
    b_p = '\u2022'

    for subscriber in EmailSub.objects.all():
        message = f'Dear {subscriber.name },\n\n'

        locations = [city.location for city in subscriber.location.all()]
        email = subscriber.email

        if locations:
            for location in locations:
                url = f'https://api.weatherapi.com/v1/current.json?key={KEY}&q={location}'
                response = requests.get(url)

                if response.status_code != 200:
                    return Response({'error': 'Failed to retrieve weather information.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                
                data = response.json()

                city = data['location']['name']
                country = data['location']['country']
                local_time = data['location']['localtime'],
                temp_in_c = data['current']['temp_c'],
                temp_in_f = data['current']['temp_f'],
                condition = data['current']['condition']['text']
                wind_speed_in_kph = data['current']['wind_kph']
                
                message += f'Current Weather Report for {city}:\n{b_p} Country: {country}\n{b_p} Local Time: {local_time}\n{b_p} Temperature in Celsius: {temp_in_c}\n{b_p} Temperature in Fahrenheit: {temp_in_f}\n{b_p} Weather Conditions: {condition}\n{b_p} Wind Speed(in kph): {wind_speed_in_kph}\n\n'

            
        subject = 'MAESTRO WEATHER: YOUR DAILY WEATHER REPORT'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email,]
        send_mail( subject, message, email_from, recipient_list)
        print(f"Sent to {email}")

    return f"Mail has been sent........"