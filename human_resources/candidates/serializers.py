
from rest_framework import serializers
from .models import Candidate, Industry

class CreateCandidateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Candidate
    fields = '__all__'

class UpdateCandidateSerializer(serializers.ModelSerializer):
  id = serializers.IntegerField(required = True)

  class Meta:
    model = Candidate
    fields = '__all__'