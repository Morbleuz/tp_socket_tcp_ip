'''
Laude Axel
URL photo personalé : https://img.nrj.fr/En1WlIq4eYlTcq4KgbV3lK36qNM=/800x450/smart/medias%2F2020%2F10%2Faxel-bauer-bio_5f99ebe959e72.jpg
'''
import socket


# Si l'URL est '' alors localhost sera utilisé
URL = ""
# J'ai 20 ans donc 5000 + 20
PORT = 5020

# Initialisation du socket client
socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# On utilise la fonction connect pour se connecter au serveur
socket_client.connect((URL, PORT))


print(f"Connection au serveur : {socket_client.getsockname()}")

while True:
    # Première étape, on demande ce que l'utilisateur souhaite faire sur le serveur
    print("\nChoisir une option :")
    print("1 - Envoyer la phrase magique")
    print("2 - Vérifier la connexion avec le serveur")
    print("3 - Recevoir la date du serveur")
    print("4 - Fermerture du serveur et du client")
    response = input()
    match response : 
            # Premier cas, on envoie la phrase magique et on éteint le serveur client
            case "1":
                socket_client.send("je sui a laeropor bisouuuu je manvol".encode())
                break
            # Deuxième cas, on envoie une phrase au serveur et on attends un réponse
            case "2":
                socket_client.send("Serveur es-tu la, tu vas bien, je m'appelle Axel ?".encode())
                data = socket_client.recv(1024)
                if data != "":
                    print(data)
            # Troisième cas, on envoie 3 pour recevoir la date du serveur
            case "3":
                socket_client.send("3".encode())
                data = socket_client.recv(1024)
                if data != "":
                    print(data)
                break
            # Quatrième cas, on envoie 4 pour éteindre le serveur
            case "4":
                socket_client.send("4".encode())
                break
            # Cas si la valeur n'est pas correcte
            case _:
                print("Saisir une valeur correcte")

# Fermeture du client 
print("Fermeture du client")
socket_client.close()