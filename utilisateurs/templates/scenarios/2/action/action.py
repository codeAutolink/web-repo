import paramiko
from pykeepass import PyKeePass
import io
import time
import tkinter as tk
from tkinter import simpledialog
import os


def get_password(prompt):
    root = tk.Tk()
    root.withdraw()  # Masquer la fenêtre principale
    password = simpledialog.askstring("Password Input", prompt, show='*')
    return password

# Chemin vers votre base de données KeePass
DATABASE_PATH = 'C:\\keepass\\databases\\tcs.kdbx'
# Demander le mot de passe KeePass à l'utilisateur via une boîte de dialogue
KEEPASS_PASSWORD = get_password('Veuillez entrer le mot de passe de votre base de données KeePass:')
# Nom de l'entrée dans KeePass
ENTRY_TITLE = 'ssh key master'

# Charger la base de données KeePass
kp = PyKeePass(DATABASE_PATH, password=KEEPASS_PASSWORD)

# Récupérer l'entrée par son titre
entry = kp.find_entries(title=ENTRY_TITLE, first=True)
if not entry:
    raise ValueError(f'Entrée "{ENTRY_TITLE}" non trouvée dans la base de données.')

# Récupérer le nom d'utilisateur et la clé SSH depuis l'entrée
username = entry.username
ssh_key = entry.password

# Utiliser Paramiko pour établir la connexion SSH
key = paramiko.RSAKey(file_obj=io.StringIO(ssh_key))

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('35.180.131.184', username=username, pkey=key)

# Exécuter la commande
stdin, stdout, stderr = client.exec_command('cowsay I Love python')
output = stdout.read().decode()


# Chercher le fichier "new.txt" pour écrire les logs
new_log_file_path = os.path.join("C:\\work\\autolink\\utilisateurs\\templates\\scenarios\\2\\logs", "new.txt")

with open(new_log_file_path, 'w') as log_file:
    log_file.write(output)
client.close()
 