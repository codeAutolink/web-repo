from django.urls import path
from . import views  # Assurez-vous d'importer vos vues ici

urlpatterns = [
    path('', views.home, name='home'),
    path('pages/Scenario', views.scenarios, name='scenarios'),
    path('pages/Token', views.tokens, name='tokens'),   
    path('execute_scenario/<int:scenario_id>/', views.execute_scenario, name='execute_scenario'),


]
