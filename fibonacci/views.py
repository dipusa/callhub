from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from .models import Sequence
from .serializers import SequenceSerializer
from rest_framework.response import Response
from .helpers import fib

# Create your views here.


class FibonacciView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'generate_fibonacci_sequence.html'

    def post(self, request, format=None):
        number_of_term = int(request.data.get("term", 0))
        sequences = fib(number_of_term)
        Sequence.objects.create(series=sequences)
        sequences = Sequence.objects.all()
        serializer = SequenceSerializer(sequences, many=True)
        return Response({"data": serializer.data})

    def get(self, request):
        sequences = Sequence.objects.all()
        serializer = SequenceSerializer(sequences, many=True)
        return Response({"data": serializer.data})
