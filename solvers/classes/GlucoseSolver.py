from solvers.SolverInterface import SolverInterface
from subprocess import Popen, PIPE

class GlucoseSolver(SolverInterface):
    def __init__(self, path):
        super().__init__(path)

    def calculate(self, dimacs):
        p = Popen([self.binary_path, "-model"], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = p.communicate(dimacs.encode('utf-8'))
        return output.decode('utf-8')
