from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.views import APIView
from django.core.paginator import Paginator

from .models import Candidate
from .serializers import CreateCandidateSerializer, UpdateCandidateSerializer

@api_view(['GET'])
def get_all_candidates(request):
  """
  Get all candidates
  """
  filter_by = request.query_params.getlist('filter-by', [])
  values = request.query_params.getlist('values', [])
  sort_by = request.query_params.getlist('sort-by', [])

  if len(filter_by) != len(values):
    return Response(status=status.HTTP_400_BAD_REQUEST)

  filters = {}

  for i in range(len(filter_by)):
    filters[filter_by[i]] = values[i]
  
  all_candidates = Candidate.objects.filter(**filters).order_by(*sort_by)
  paginator = Paginator(all_candidates, request.query_params.get('count', 10))

  return Response(serializers.serialize('json', paginator.page(request.query_params.get('page', 1))))

class CandidateCrudView(APIView):
  def get(self, *args, **kwargs):
    return Response(serializers.serialize('json', Candidate.objects.filter(id=kwargs['candidate_id'])))
  
  def post(self, request):
    """
    Create a candidate
    """
    serializer = CreateCandidateSerializer(data=request.data)

    if serializer.is_valid():
      serializer.save()

      return Response(serializer.data, status=status.HTTP_200_OK)

  def put(self, request):
    """
    Update candidate
    """
    candidate_to_update = Candidate.objects.filter(id=request.data["id"]).first()

    if candidate_to_update is None:
      return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UpdateCandidateSerializer(candidate_to_update, data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()

    return Response(serializer.data, status=status.HTTP_200_OK)

  def delete(self, *args, **kwargs):
    candidate_to_delete = Candidate.objects.filter(id=kwargs["candidate_id"])

    if candidate_to_delete is None:
      return Response(status=status.HTTP_404_NOT_FOUND)

    candidate_to_delete.delete()

    return Response(status=status.HTTP_200_OK)
