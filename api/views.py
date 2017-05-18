import json

from django.http import Http404
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.models import Solver
from backend.serializers import SolverSerializer
from solvers.utils import cnf_to_dimacs, get_solver_wrapper_by_id


class IndexView(APIView):

    def remap_vals(self, dimacs_in, remap):
        if(dimacs_in == ""):
            return "UNSATISFIABLE"
        ret = ""
        print (remap)
        for line in dimacs_in.splitlines():

            if line.startswith('s'):
                ret+=line[2:]+"\n"

            elif line.startswith('v'):
                vals = line.split(' ')
                for v in vals[1:]:
                    if v=='':
                        continue

                    vint = int(v)
                    if vint==0:
                        break

                    if vint>0:
                        ret += remap[vint].name + "\n"
                    else:
                        ret += "~" + remap[-vint].name + "\n"

            else:
                ret += line
        return ret

    def post(self, request):
        body = json.loads(request.body.decode("utf-8"))
        dimacs, remap = cnf_to_dimacs(body['input'])

        solver_wrapper = get_solver_wrapper_by_id(body['solver'])

        if solver_wrapper is None:
            raise Http404
        else:
            result = self.remap_vals(solver_wrapper.calculate(dimacs.__str__()), remap)
            response = {'data': result}
            return Response(response)


class SolversList(APIView):
    def get(self, request):
        solvers = Solver.objects.all()
        serializer = SolverSerializer(solvers, many=True)
        return Response(serializer.data)
