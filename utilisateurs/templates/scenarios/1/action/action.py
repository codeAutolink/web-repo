import requests
import json
import time
import os

server_name = "Chadi"
JENKINS_URL = "https://tcs.myddns.me"
TOKEN = "monTokenJiraJenkinscred52"
JENKINS_JOB_NAME = "GetServer"
USERNAME = "macxtn"
API_TOKEN = "11e2b660c9ab9b91d7bcc502ce38e97a43"

data = {"nomserveur": server_name}
params = {"token": TOKEN}

response = requests.post(
    f"{JENKINS_URL}/generic-webhook-trigger/invoke",
    params=params,
    data=json.dumps(data),
    headers={'Content-Type': 'application/json'}
)

logs = "Début des logs.\n"

if response.status_code == 200:
    logs += "Pipeline déclenché avec succès.\n"

    build_status_url = f"{JENKINS_URL}/job/{JENKINS_JOB_NAME}/lastBuild/api/json"
    build_finished = False
    max_attempts = 10  # nombre maximum de tentatives pour vérifier
    attempts = 0

    while not build_finished and attempts < max_attempts:
        build_status_response = requests.get(build_status_url, auth=(USERNAME, API_TOKEN))
        build_status_json = build_status_response.json()

        if "result" in build_status_json and build_status_json["result"] is not None:
            build_finished = True
        else:
            attempts += 1
            time.sleep(5)  # attendez 5 secondes avant de réessayer

    logs_url = f"{JENKINS_URL}/job/{JENKINS_JOB_NAME}/lastBuild/consoleText"
    logs_response = requests.get(logs_url, auth=(USERNAME, API_TOKEN))

    if logs_response.status_code == 200:
        logs += "Récupération des logs de Jenkins...\n"
        logs += logs_response.text
    else:
        logs += f"Erreur lors de la récupération des logs de Jenkins: {logs_response.status_code} - {logs_response.text}\n"
else:
    logs += f"Erreur lors du déclenchement du pipeline: {response.status_code} - {response.text}\n"

# Chercher le fichier "new.txt" pour écrire les logs
new_log_file_path = os.path.join("C:\\work\\autolink\\utilisateurs\\templates\\scenarios\\1\\logs", "new.txt")

with open(new_log_file_path, 'w') as log_file:
    log_file.write(logs)
