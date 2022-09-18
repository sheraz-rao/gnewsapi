import json
import requests

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
from rest_framework.response import Response

from GNewsAPI.settings import GNEWS_API_KEY


class TopNewsHeadlinesView(APIView):
    @method_decorator(cache_page(60*60*2))
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

        news_articles = json.loads(api_response.content)["articles"]

        return Response({'articles': news_articles})
