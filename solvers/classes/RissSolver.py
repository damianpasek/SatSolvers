from solvers.SolverInterface import SolverInterface
from subprocess import Popen, PIPE


class RissSolver(SolverInterface):
    def __init__(self, path):
        super().__init__(path)

    def calculate(self, dimacs):
        p = Popen([self.binary_path], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, err = p.communicate(dimacs.encode('utf-8'))

        outstr = ""
        for line in output.decode('utf-8').splitlines():
            if not line.startswith('c'):
                outstr += line+"\n"

        return outstr
