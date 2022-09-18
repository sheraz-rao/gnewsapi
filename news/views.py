import json
import requests

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
from rest_framework.response import Response

from GNewsAPI.settings import CACHE_TTL, GNEWS_API_KEY


class TopNewsHeadlinesView(APIView):
    '''
        API to get top (maximum 20) news from gnews API
    '''
    @method_decorator(cache_page(CACHE_TTL))
    def get(self, request):
        max_limit = int(request.query_params.get("max", 20))
        lang = request.query_params.get("lang", 'en')
        
        if not lang.isalpha():
            return Response({'articles': []}, status=400)
        
        if len(lang) != 2:
            return Response({'articles': []}, status=400)
        
        if max_limit > 20 or max_limit < 1:
            return Response({'articles': []}, status=400)

        api_response = requests.get(
            url=f"https://gnews.io/api/v4/top-headlines?max={max_limit}&lang={lang}&token={GNEWS_API_KEY}", timeout=60)
        
        if api_response.status_code == 200:
            news_articles = json.loads(api_response.content)["articles"]
            return Response({'articles': news_articles})
        
        return Response({'articles': []}, status=400)


class SearchArticlesView(APIView):
    '''
        API to search news articles based on keywords
    '''
    @method_decorator(cache_page(CACHE_TTL))
    def get(self, request):
        to_find = request.query_params.get("q", None)
        max_limit = int(request.query_params.get("max", 20))
        lang = request.query_params.get("lang", 'en')

        if not lang.isalpha():
            return Response({'articles': []}, status=400)

        if len(lang) != 2:
            return Response({'articles': []}, status=400)

        if max_limit > 20 or max_limit < 1:
            return Response({'articles': []}, status=400)
        
        api_response = requests.get(
            url=f"https://gnews.io/api/v4/search?q={to_find}&max={max_limit}&lang={lang}&in=title,description,content&token={GNEWS_API_KEY}", timeout=60)

        if api_response.status_code == 200:
            news_articles = json.loads(api_response.content)["articles"]
            return Response({'articles': news_articles})

        return Response({'articles': []}, status=400)
