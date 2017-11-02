from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import StepsSerializer
from .models import Steps

@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_step(request, pk):
    try:
        step = Steps.objects.get(pk=pk)
    except Steps.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StepsSerializer(step)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        step.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = StepsSerializer(step, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_post_steps(request):
    print(request.user)
    # GET all steps
    if request.method == 'GET':
        steps = Steps.objects.filter(owner=request.user)
        serializer = StepsSerializer(steps, many=True)
        return Response(serializer.data)
    # Insert new step record
    if request.method == 'POST':
        data = {
            'date_start': request.data.get('date_start'),
            'date_end': request.data.get('date_end'),
            'steps': request.data.get('steps'),
            'owner': request.user,
        }
        serializer = StepsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
# class StepsCreateView(generics.ListCreateAPIView):
#     """Create step behavior"""
#     queryset = Steps.objects.all()
#     serializer_class = StepsSerializer
#
#     def perform_create(self, serializer):
#         """Save the data when sending in steps"""
#         serializer.save(owner=self.request.user)
#
# class StepsDetailsView(generics.RetrieveUpdateDestroyAPIView):
#     """Handles GET, PUT, DELETE"""
#     queryset = Steps.objects.all()
#     serializer_class = StepsSerializer
