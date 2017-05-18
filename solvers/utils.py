from pyeda.boolalg.expr import expr, expr2dimacscnf

from backend.models import Solver
from solvers.classes.GlucoseSolver import GlucoseSolver
from solvers.classes.LingelingSolver import LingelingSolver


def cnf_to_dimacs(cnf_input):
    clause = expr(cnf_input)
    cnf = clause.to_cnf()
    mapa, dimacs = expr2dimacscnf(cnf)
    return dimacs, mapa


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
