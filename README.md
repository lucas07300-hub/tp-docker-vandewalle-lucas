# TP1 Docker

===============================================
## Exercice 1 : 
* Installation de Docker Desktop pour Windows :
    - Installation de wls + sous systeme Linux

===============================================

## Exercice 3 : 

* Téléchargement de l'image avec `docker pull hello-world`
* Nettoyage de l'environnement par suppression du conteneur.
    - "Error response from daemon....." lors de la tentative de suppression de l'image.
    - Solution : L'image ne s'est pas supprimé pcq qu'un conteneur était en cours d'exec avec cette image. J'ai donc supprimé le conteneur en cours avec  'docker rm XX' puis faire la supprission de l'image 'docker rmi XX'.

===============================================

## Exercice 4

* Récupération de l'image nginx.
* Lancement d'un conteneur nginx sur 8080:80
* Vérif du conteneur et validation de l'affichage via "http://localhost:8080" sur navigateur.

===============================================

## Exercice 5 :

* Installation de flask sur ma machine avec pip install flask
* Création du fichier app.py en faisant une fonction pour l'affichage du hello World et du lancement de l'application sur le port 80.
* Test sur mon navigateur ok

* Ecriture du Dockerfile et exposition sur le port 80. 
* Création de l'image flask depuis mon dockerfile :
    - docker build -t flask-app .
    - docker run -d -p 8080:80 --name flask flask-app NOK
    - Mon DockerFile provoque l'erreur python: can't open file '/app/app.py': [Errno 2] No such file or directory". En ajoutant la ligne "COPY . ." , cela a pu copier mon app depuis le bon répertoire. En réalisant la modification, le conteneur a pu se lancer correctement.
* Test OK sur mon navigateur en localhost:8080.

===============================================

## Exercice 6 :
