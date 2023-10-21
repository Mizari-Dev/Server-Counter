# Server-Counter
Compte sur combien de serveurs Discord vous êtes
# Setup du projet
- RDV sur https://discord.com/developers/applications
- Créer une app
- Aller dans l'onglet "OAuth2"
- Ajouter un lien de redirection vers `http://localhost:8000/cgi-bin/connection.py`
  ![image](https://github.com/Mizari-W/Server-Counter/assets/39090431/7ab321a6-4154-4e31-82ae-a6fa9eaa3582)
- Copier le client ID et le client secret pour les mettre dans le fichier `connection.py`
  ![image](https://github.com/Mizari-W/Server-Counter/assets/39090431/362fb41e-ec33-41d1-81f6-6bfd5034adfa)
- Ouvrir un terminal à la racine du projet et lancer la commande `python3 -m http.server --cgi`
- Se rendre à l'addresse `http://localhost:8000`
- May the </> be with you!
  ![image](https://github.com/Mizari-W/Server-Counter/assets/39090431/4cc916a1-b359-4ebe-8538-4f175d5cf4a6)


Pour apprendre la programmation ou demander de l'aide : [L'Ordre Des Devs](http://discord.gg/neWSxF6)
