from pyeda.boolalg.expr import expr, expr2dimacscnf


def cnf_to_dimacs(cnf_input):
    clause = expr(cnf_input)
    cnf = clause.to_cnf()
    mapa, dimacs = expr2dimacscnf(cnf)
    return dimacs
