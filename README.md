# light-intensity-service

L'arduino envoie une valeur comprise entre 0 et 1023 toutes les secondes. Plus une valeur est proche de 0, plus le bruit détecté est élevé. À l'inverse, une valeur proche de 1023 correspond à du silence.

Pour lancer le script python, vous devez installer les paquets suivants :

```bash
sudo apt install python3-serial
pip install aiohttp
```
Si vous n'êtes pas sous linux, il faudra probablement changer le port de l'arduino (COM3 par exemple sous windows).

L'application va récupérer les valeurs envoyées et si la valeur est inférieure à 100 (valeur choisie pour la démo), va faire une requête pour diminuer le score luminosité de l'utilisateur. Pour la démonstration, l'utilisateur qui est pénalisé est par défaut l'utilisateur n°1 : "Roche Etienne". 
