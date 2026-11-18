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

* Création du fichier docker-compose.yml pour configurer mes deux conteneurs en même temps.
* Lancement des commandes :
    - docker compose up -d (KO)
        Error response from daemon: failed to set up container networking: driver failed programming external connectivity on endpoint tp-docker-vandewalle-lucas-mongo-1 (57d9b0d9f07c13a8eab4704b4cdc86cd03838412922fc96abe1281f924a22f7a): Bind for 0.0.0.0:27017 failed: port is already allocated
    - J'avais installé l'image mongo en localhost et le conteneur utilisé toujours le port. (docker rm -f mongo)

    - docker compose up -d (OK)

    - Vérification de l'éxécution de mon app (NOK)
    web-1  | Traceback (most recent call last):                           
    web-1  |   File "/app/app.py", line 2, in module                   
    web-1  |     from pymongo import MongoClient
    web-1  | ModuleNotFoundError: No module named 'pymongo'
    -  Correction dans le dockerfile avec l'ajout de "RUN pip install pymongo" 

    -  Correction dans le dockerfile avec l'ajout de "RUN pip install pymongo" + test (NOK), même message d'erreur
    - docker compose down + docker compose build --no-cache + docker compose up -d + test en http://localhost:8080 : SUCCESS (PS C:\Users\lucas\Documents\Master MIAGE\M2 UTC\Intégration et déploiement continus\TP\tp-docker-vandewalle-lucas> docker compose logs web  
    web-1  |  * Serving Flask app 'app'
    web-1  |  * Debug mode: off
    web-1  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
    web-1  |  * Running on all addresses (0.0.0.0)
    web-1  |  * Running on http://127.0.0.1:80
    web-1  |  * Running on http://172.19.0.3:80
    web-1  | Press CTRL+C to quit
    web-1  | 172.19.0.1 - - [18/Nov/2026 20:15:43]  "GET / HTTP/1.1" 200 -)
