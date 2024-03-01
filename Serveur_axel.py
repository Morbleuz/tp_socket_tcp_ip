'''
Laude Axel
URL photo personalité : https://img.nrj.fr/En1WlIq4eYlTcq4KgbV3lK36qNM=/800x450/smart/medias%2F2020%2F10%2Faxel-bauer-bio_5f99ebe959e72.jpg
'''
from datetime import datetime
import socket

# Si l'URL est '' alors localhost sera utilisé
URL = ''
# J'ai 20 ans donc 5000 + 20
PORT = 5020

# Initialisation du socket serveur
socket_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Première boucle pour que le serveur s'ouvre dans tous les cas, si le port 5020 est utilisé alors on incrémente de 100 à chaque itération
while True: 
        try:
            # On utilise la fonction bind pour lancer le serveur
            socket_serveur.bind((URL, PORT))
            break
        except Exception as e:
               print("Port déjà occupé, incrémentation de 100")
               PORT += 100
print("Lancement du serveur !")

# Boucle pour le serveur tourne en continue
while True:
        socket_serveur.listen(5)
        # On récupère les informations du client
        client, address = socket_serveur.accept()

        print(f"Nouveau client connecte : {address}")

        # La fonction recv nous permet de recevoir des données des clients
        response = client.recv(255)
        if response != "":
                # Si le client envoie 'Serveur es-tu la, tu vas bien, je m\'appelle Axel ?' alors on lui renvoie 'Je suis la !'
                if str(response) == 'b"Serveur es-tu la, tu vas bien, je m\'appelle Axel ?"':
                    client.send("\n Je suis la !".encode())
                # Si le client envoie l'option 3 alors on renvoie la date actuelle
                if str(response) == "b'3'":
                    client.send(f"{datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}".encode())
                # Si le client envoie l'option 4 alors on éteint le serveur
                if str(response) == "b'4'":
                      break
                       
# Fermeture du client et du serveur
client.close()
socket_serveur.close()
