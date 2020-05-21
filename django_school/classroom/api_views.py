from rest_framework import viewsets
from rest_framework import permissions

from .models import Quiz
from .serializers import QuizSerializer


class QuizViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Quiz.objects.filter(name__startswith='w').select_related('owner')
    serializer_class = QuizSerializer
