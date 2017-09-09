.. Seiya documentation master file, created by

Seiya
=======

-------------
Description
~~~~~~
Seiya est une application de collaboration de tableau blanc dont l'objectif est de permettre / faciliter le partage en temps réel d'idées sous la forme de composants (par exemple: text, images, code, etc) qui peut être reconstitué et édité par plusieurs personnes lors d'une session en direct, et exporté à tout moment.

En ce moment (*v0.1.0*), Le seul composant disponible est le texte, avec le chat de la barre latérale (qui est disponible pour tous).

Le plan consiste à ajouter des composants et des fonctionnalités (comme exporter le tableau en tant que texte au lieu d'image), progressivement, jusqu'à ce que le projet atteigne son but initial(indiqué ci-dessus).

Ce projet faisait partie de la deuxième édition de `Learn IT, Girl`_,et n'aurait pas été possible sans le mentorat continu, le soutien et la tolérance de 'newbie' questions avec gracieuseté de `@daniel-j-h`_. 

Rules
~~~~~~
- Les utilisateurs inscrits peuvent créer un tableau, auquel ils peuvent donner accès à un nombre quelconque d'autres utilisateurs.
- Chaque conseil peut avoir accès à 3 types d'utilisateurs:
	- **Owner**
		Peut faire tout ce qui peut être plus: éditer le titre du forum, terminer le conseil tôt, inviter d'autres et contrôler leurs autorisations, et supprimer le tableau.
	- **Editor**
		Peut faire tout ce que les téléspectateurs peuvent plus: éditer les composants de la carte.
	- **Viewer**
		Peut afficher le tableau, exporter son contenu à tout moment et participer au chat de la barre latérale.
- **Editors** et **Viewers** peut accéder au conseil soit en vous connectant au site Web en utilisant le courrier électronique auquel ils ont été invités ou en y accédant par le biais de leur lien d'invitation unique.
- Tout utilisateur connecté a accès à un certain conseil qui n'est pas non plus **Owner** peuvent se retirer à tout moment.
- Pour éviter l'édition de conflits, une seule personne peut modifier la carte à la fois.

.. note:: Afin de simplifier l'interaction avec le serveur, la plupart des "heavy lifting" est fait cote client. Le serveur enregistre et fournit simplement des données sur le tableau au besoin, et le client le regroupe dans le DOM. La logique du tableau côté client peut être trouvée `on Github`_.

Installation
~~~~~~~~~~~~
1. Clone the repo. 
::
	$ git clone https://github.com/blaringsilence/pegasus.git
	$ cd pegasus
2. Install `virtualenv`_ and activate it.
::
	$ pip install virtualenv
	$ virtualenv venv
	$ . venv/bin/activate
	$ pip install -r requirements.txt
3. Initialize the database.
::
	$ chmod a+x init_db.py
	$ ./init_db.py
4. Run the app.
::
	$ chmod a+x run_pegasus.py
	$ ./run_pegasus.py
.. note:: Default IP:port is 127.0.0.1:5000. You can change that by specifying the port and/or IP like this:
	``$ ./run_pegasus.py -ip IP_ADDRESS -port PORT_NUMBER``


Docs
-----
.. automodule:: pegasus
	:members:
	:exclude-members: Flask, pegasus, views, errorhandlers, DATABASE, DEBUG, SECRET_KEY, app

.. automodule:: pegasus.views
	:members:

.. automodule:: pegasus.errorhandlers
	:members:

.. automodule:: test_pegasus
	:members:

