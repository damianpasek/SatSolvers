import json
import time

from subprocess import Popen, PIPE

from pyeda.boolalg.expr import expr, expr2dimacscnf
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.models import Solver
from backend.serializers import SolverSerializer


class IndexView(APIView):
    def post(self, request):
        body = json.loads(request.body)

        clause = expr(body['input'])
        cnf = clause.to_cnf();
        mapa, dimacs = expr2dimacscnf(cnf);

        solver = Solver.objects.get(pk=body['solver'])
        p = Popen([solver.solver_binary.path, "-model"], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        # output, err = p.communicate(body['input'].encode('utf-8'))
        output, err = p.communicate(dimacs.__str__().encode('utf-8'))
        # print(output.decode("utf-8"))

        response = {
            'data': output.decode("utf-8")
        }
        return Response(response)


class SolversList(APIView):
    def get(self, request):
        solvers = Solver.objects.all()
        serializer = SolverSerializer(solvers, many=True)
        return Response(serializer.data)
