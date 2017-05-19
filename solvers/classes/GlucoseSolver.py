from solvers.SolverInterface import SolverInterface
from subprocess import Popen, PIPE

class GlucoseSolver(SolverInterface):
    def __init__(self, path):
        super().__init__(path)

    def calculate(self, dimacs):
        p = Popen([self.binary_path, "-model", "-verb=0"], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = p.communicate(dimacs.encode('utf-8'))

        outstr = ""
        for line in output.decode('utf-8').splitlines():
            if not line.startswith('c') and line != "":
                outstr += line + "\n"

        return outstr
