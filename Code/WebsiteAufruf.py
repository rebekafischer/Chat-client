import requests

url = input("Gebe die Url ein: ")

response = requests.get(url)
if response.status_code == 200:
    print("die website wurde erfolgreich aufgerufen")
else:
    print("Fehler. Website nicht erreichbar")