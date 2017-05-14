import time
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.models import Solver
from backend.serializers import SolverSerializer


class IndexView(APIView):
    def post(self, request):
        data = {'test': 5}
        time.sleep(5)
        return Response(data)


class SolversList(APIView):
    def get(self, request):
        solvers = Solver.objects.all()
        serializer = SolverSerializer(solvers, many=True)
        return Response(serializer.data)
