from django.shortcuts import render
from .models import Scenario, SSHKey
from django.contrib.auth.decorators import login_required
import os
from datetime import datetime

import paramiko # 2 
from pykeepass import PyKeePass
import io
import time
import tkinter as tk
from tkinter import simpledialog







# Vue pour la page d'accueil
def home(request):
    return render(request, 'home.html')

# Vue pour la page Token
def tokens(request):
    return render(request, 'pages/Token.html')

@login_required
def scenarios(request):
    scenarios_list = Scenario.objects.all()
    ssh_keys = SSHKey.objects.all()  # Récupérez toutes les clés SSH ici
    return render(request, 'pages/Scenario.html', {'scenarios': scenarios_list, 'ssh_keys': ssh_keys})





def execute_scenario(request, scenario_id):
    # Récupérer le scénario correspondant
    scenario = Scenario.objects.get(pk=scenario_id)
    
    # Construire le chemin vers le fichier action.py pour ce scénario
    action_file_path = os.path.join("C:\\work\\autolink\\utilisateurs\\templates\\scenarios", str(scenario_id), "action", "action.py")
    log_dir = os.path.join("C:\\work\\autolink\\utilisateurs\\templates\\scenarios", str(scenario_id), "logs")

    # Créer le fichier "new.txt"
    new_log_file_path = os.path.join(log_dir, "new.txt")
    with open(new_log_file_path, 'w') as new_file:
        new_file.write('')

    # Exécuter le fichier action.py
    try:
        with open(action_file_path, 'r') as file:
            exec(file.read())
        
        # Renommer le fichier new.txt avec heure_date.txt
        timestamp = datetime.now().strftime("%H_%M_%Y_%m_%d")
        renamed_log_file_path = os.path.join(log_dir, f"{scenario_id}_{timestamp}.txt")
        os.rename(new_log_file_path, renamed_log_file_path)

        # Récupérer les logs pour les afficher
        with open(renamed_log_file_path, 'r') as log_file:
            logs = log_file.read()

    except Exception as e:
        logs = f"Erreur lors de l'exécution du scénario: {e}"
    
    return render(request, 'logs.html', {'logs': logs})


