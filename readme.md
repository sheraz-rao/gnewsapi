GNews is an application based on Django framework.
I have utilized 2 GNews APIS to get and search for news articles for this project.

Take clone of this repository
Install requirements mentioned in requirements.txt (I have used Python 3.9 and Django 4.1)

Make sure you have redis installed and running on your system. I have used redis for cache purpose. If you dont have redis installed just comment out cache settings in settings.py

Get your API key for GNews after sign up on GNews. Add your api key in "GNEWS_API_KEY" in settings.py

After you have done above mentioned steps. Run the django server

python manage.py runserver

I have created 2 endpoints in "news" application's views.py

1- <base_url>/api/top-headlines/ to get top headlines
    params are "lang" and "max"

    this endpoint will make use of the GNews top headlines endpoint (https://gnews.io/api/v4/top-headlines?max=&lang=&token={GNEWS_API_KEY}) and will return top headlines in articles array as json

2- <base_url>/api/search/ to search articles by given keywords
    params are "q" is the keyword to search, "lang" and "max"

    this endpoint will make use of the GNews search articles endpoint (https://gnews.io/api/v4/search?q=&max=&lang=&in=&token={GNEWS_API_KEY}) and will return top headlines in articles array as json

redis will cache the response of both endpoints to save extra api calls to gnews apis.