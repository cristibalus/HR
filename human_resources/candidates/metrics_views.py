
from datetime import date
from rest_framework.decorators import api_view

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers
from rest_framework import status

from .models import Candidate
import pandas as pd

@api_view(['GET'])
def get_average_age_by_industry(*args, **kwargs):
  candidates = Candidate.objects.all()
  data = []

  for candidate in candidates:
    today = date.today()
    dob = candidate.date_of_birth
    data.append({
      "age": today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day)),
      "industry": candidate.industry.name,
    })

  df = pd.DataFrame(data=data)
  average_age_by_industry = df.groupby(['industry']).mean().to_json()

  return Response(average_age_by_industry, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_average_salary_by_industry(*args, **kwargs):
  candidates = Candidate.objects.all().values('industry', 'annual_income')
  df = pd.DataFrame(data=candidates, columns=['industry', 'annual_income'])
  average_salary_by_industry = df.groupby(['industry']).mean().to_json()

  return Response(average_salary_by_industry, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_average_salary_by_experience(*args, **kwargs):
  candidates = Candidate.objects.all().values('years_of_experience', 'annual_income')
  df = pd.DataFrame(data=candidates, columns=['years_of_experience', 'annual_income'])
  average_salary_by_experience = df.groupby(['years_of_experience']).mean().to_json()

  return Response(average_salary_by_experience, status=status.HTTP_200_OK)