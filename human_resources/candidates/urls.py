
from django.urls.conf import path
from . import views
from . import metrics_views

app_name = 'candidates'

urlpatterns = [
  path('all', views.get_all_candidates),
  path('<candidate_id>', views.CandidateCrudView.as_view()),
  path('', views.CandidateCrudView.as_view()),
  path('metrics/average-age-by-industry/', metrics_views.get_average_age_by_industry),
  path('metrics/average-salary-by-industry/', metrics_views.get_average_salary_by_industry),
  path('metrics/average-salary-by-experience/', metrics_views.get_average_salary_by_experience),
]