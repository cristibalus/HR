from django.db import models

class Industry(models.Model):
  class Meta:
    verbose_name = 'industry'
    verbose_name_plural = 'industries'

  name = models.CharField('name', max_length=30)

class Candidate(models.Model):
  class Meta:
    verbose_name = 'candidate'
    verbose_name_plural = 'candidates'

  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  date_of_birth = models.DateField()
  industry = models.ForeignKey(Industry, on_delete=models.RESTRICT)
  annual_income = models.PositiveIntegerField()
  years_of_experience = models.PositiveIntegerField()
