from django.db import models


class Solver(models.Model):
    title = models.TextField(max_length=100)
    slug = models.TextField(max_length=20)
    solver_binary = models.FileField(upload_to='solvers/')

    def __str__(self):
        return self.title
