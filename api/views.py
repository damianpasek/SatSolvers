import json
import time

from rest_framework.response import Response
from rest_framework.views import APIView

from backend.models import Solver
from backend.serializers import SolverSerializer


class IndexView(APIView):
    def post(self, request):
        body = json.loads(request.body)

        # get solver object
        solver = Solver.objects.get(pk=body['solver'])
        print(solver.solver_binary.path)

        # simulate calculations
        time.sleep(5)
        response = {
            'data': 'Some response data'
        }
        return Response(response)


class SolversList(APIView):
    def get(self, request):
        solvers = Solver.objects.all()
        serializer = SolverSerializer(solvers, many=True)
        return Response(serializer.data)
