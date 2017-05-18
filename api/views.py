import json
import time

from subprocess import Popen, PIPE

from rest_framework.response import Response
from rest_framework.views import APIView

from backend.models import Solver
from backend.serializers import SolverSerializer
from solvers.utils import cnf_to_dimacs


class IndexView(APIView):
    def post(self, request):
        body = json.loads(request.body)
        dimacs = cnf_to_dimacs(body['input'])

        solver = Solver.objects.get(pk=body['solver'])
        p = Popen([solver.solver_binary.path, "-model"], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = p.communicate(dimacs.__str__().encode('utf-8'))

        response = {'data': output.decode("utf-8")}
        return Response(response)


class SolversList(APIView):
    def get(self, request):
        solvers = Solver.objects.all()
        serializer = SolverSerializer(solvers, many=True)
        return Response(serializer.data)
