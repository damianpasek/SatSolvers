import os
from subprocess import Popen, PIPE, DEVNULL

from django.core.files.storage import default_storage
from solvers.SolverInterface import SolverInterface
import solvers.utils


class MinisatSolver(SolverInterface):
    def __init__(self, path):
        super().__init__(path)

    def calculate(self, dimacs):
        filename, filepath = solvers.utils.store_in_file(dimacs.encode("utf-8"))
        pre, ext = os.path.splitext(filepath)
        outfilepath = pre + ".satout"
        p = Popen([self.binary_path, filepath, outfilepath], stdin=DEVNULL, stdout=PIPE, stderr=PIPE)
        p.communicate()

        default_storage.delete(filepath)

        outstr = ""
        for line in default_storage.open(outfilepath).read().decode("utf-8").splitlines():
            if line == "SAT":
                outstr += "s SATISFIABLE\n"
            elif line == "UNSAT":
                outstr += "s UNSATISFIABLE\n"
            else:
                outstr += "v " + line + "\n"

        default_storage.delete(outfilepath)

        return outstr
