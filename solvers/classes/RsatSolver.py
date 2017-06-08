from django.core.files.storage import default_storage
from solvers.SolverInterface import SolverInterface
from subprocess import Popen, PIPE, DEVNULL
import solvers.utils


class RsatSolver(SolverInterface):
    def __init__(self, path):
        super().__init__(path)

    def calculate(self, dimacs):
        filename, filepath = solvers.utils.store_in_file(dimacs.encode("utf-8"))
        p = Popen([self.binary_path, filepath, "-s"], stdin=DEVNULL, stdout=PIPE, stderr=PIPE)
        output, err = p.communicate()

        default_storage.delete(filepath)

        outstr = ""
        sat = ""
        for line in output.decode('utf-8').splitlines():
            if line.startswith('s'):
                sat = line
            elif not line.startswith('c'):
                outstr += line+"\n"

        return sat + "\n" + outstr
