import json

from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.models import Solver
from backend.serializers import SolverSerializer
from solvers.utils import cnf_to_dimacs, get_solver_wrapper_by_id, remap_vals


class IndexView(APIView):
    def post(self, request):
        body = json.loads(request.body.decode("utf-8"))

        if body['is_cnf']:
            dimacs, remap = cnf_to_dimacs(body['input'])
        else:
            dimacs = body['input']
            remap = None

        solver_wrapper = get_solver_wrapper_by_id(body['solver'])

        if solver_wrapper is None:
            raise Http404
        else:
            result = remap_vals(solver_wrapper.calculate(dimacs.__str__()), remap)
            response = {'data': result}
            return Response(response)


class SolversList(APIView):
    def get(self, request):
        solvers = Solver.objects.all()
        serializer = SolverSerializer(solvers, many=True)
        return Response(serializer.data)
