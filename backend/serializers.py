from rest_framework.serializers import ModelSerializer

from .models import Solver


class SolverSerializer(ModelSerializer):
    class Meta:
        model = Solver
        fields = ('id', 'title')
