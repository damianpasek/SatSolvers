import time
from rest_framework.response import Response
from rest_framework.views import APIView


class IndexView(APIView):
    def post(self, request):
        data = {'test': 5}
        time.sleep(5)
        return Response(data)
