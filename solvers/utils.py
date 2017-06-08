from pyeda.boolalg.expr import expr, expr2dimacscnf

from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from backend.models import Solver
from solvers.classes.GlucoseSolver import GlucoseSolver
from solvers.classes.LimmatSolver import LimmatSolver
from solvers.classes.LingelingSolver import LingelingSolver
from solvers.classes.RissSolver import RissSolver
from solvers.classes.JerusatSolver import JerusatSolver
from solvers.classes.RsatSolver import RsatSolver

import uuid


def cnf_to_dimacs(cnf_input):
    clause = expr(cnf_input, False)
    cnf = clause.to_cnf()
    map, dimacs = expr2dimacscnf(cnf)
    return dimacs, map


def remap_vals(dimacs_in, remap):

    if dimacs_in == "":
        return "UNSATISFIABLE"
    ret = ""
    for line in dimacs_in.splitlines():

        if line.startswith('s'):
            ret += line[2:]+"\n"

        elif line.startswith('v'):
            vals = line.split(' ')
            for v in vals[1:]:
                if v == '':
                    continue

                vint = int(v)
                if vint == 0:
                    break

                if remap:
                    if vint>0:
                        ret += remap[vint].name + "\n"
                    else:
                        ret += "~" + remap[-vint].name + "\n"
                else:
                    if vint > 0:
                        ret += v + "\n"
                    else:
                        ret += "~" + v[1:] + "\n"
        else:
            ret += line
    return ret


def store_in_file(input):
    filename = str(uuid.uuid4())
    filepath = settings.BASE_DIR+"/files/tmp/"+filename+".satin"
    default_storage.save(filepath, ContentFile(input))
    return filename, filepath


def get_solver_wrapper_by_id(id):
    solver = Solver.objects.get(pk=id)
    slug = solver.slug
    binary_path = solver.solver_binary.path

    if slug == 'glucose':
        return GlucoseSolver(binary_path)
    elif slug == 'lingeling':
        return LingelingSolver(binary_path)
    elif slug == 'limmat':
        return LimmatSolver(binary_path)
    elif slug == 'riss':
        return RissSolver(binary_path)
    elif slug == 'jerusat':
        return JerusatSolver(binary_path)
    elif slug == 'rsat':
        return RsatSolver(binary_path)
    else:
        return None
