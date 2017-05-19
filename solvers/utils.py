from pyeda.boolalg.expr import expr, expr2dimacscnf

from backend.models import Solver
from solvers.classes.GlucoseSolver import GlucoseSolver
from solvers.classes.LingelingSolver import LingelingSolver


def cnf_to_dimacs(cnf_input):
    clause = expr(cnf_input)
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

                if vint>0:
                    ret += remap[vint].name + "\n"
                else:
                    ret += "~" + remap[-vint].name + "\n"

        else:
            ret += line
    return ret


def get_solver_wrapper_by_id(id):
    solver = Solver.objects.get(pk=id)
    slug = solver.slug
    binary_path = solver.solver_binary.path

    if slug == 'glucose':
        return GlucoseSolver(binary_path)
    elif slug == 'lingeling':
        return LingelingSolver(binary_path)
    else:
        return None
