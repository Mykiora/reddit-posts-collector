[English](#english)
[French](#french)

# English

## Used skills
Virtual Environments, APIs, Object Oriented Programming, Splitting the project into multiple modules, Artificial Intelligence, Langchain, Documentation, English

## Description
This is a project meant to show my skills to employers. This script uses Reddit's API to collect a number of posts (along with their information) set by the user either on the homepage or on a specific subreddit. These posts are then saved in a text file on which Retrieval Augmented Generation is applied with a model from OpenAI in order to recommend 3 - 5 best current posts for the user.

![Example of execution (English)](assets/app_screenshot_en.png?raw=true "Optional Title")

## Requirements
The script assumes that:
- You have your own reddit app ([video tutorial here](https://youtu.be/KmFKO1dp_vQ?si=yIzYlWqkx8KAmurQ)) really easy, fast, and free. Use "http://localhost:8080" as the redirect uri.
- You have an OpenAI API key. ([video tutorial here](https://youtu.be/gBSh9JI28UQ?si=BAWFhPr3-s-0ZaH-)). Warning: NOT FREE.
- You have a Reddit account.

## Installation
In Windows CMD:

```console
git clone https://github.com/Mykiora/reddit-posts-collector.git
cd reddit-posts_collector
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

If it is the first time you launch the program, you will be asked to enter your reddit credentials, your OpenAI API key, as well as the client ID and secret (which you cand both find where you created the Reddit app at [this url](https://reddit.com/prefs/apps)). So, make sure to have these.

## Usage
All you have to do is run the "main.py" file and follow the instrutions. Everything will be done automatically in a matter of seconds. At the top of the file, there are parameters that you can modify. They are:

- subreddit: If you want to fetch the posts of a specific subreddit.
- filter: Reddit filters that you want to apply to your posts. Choose from: best, hot, new, rising, top, controversial.
- post_limit: The number of posts that you want to fetch (may cause problems if you set this parameter to a number higher than the number of posts available on the subreddit)
- rag: Performs the RAG on the collected posts' data if set to 1 (costs money). Skips the RAG alltogether if set to 0. (You then only have possess the raw data in data/post_data.txt)

 It is also possible to modify the prompt in the "rag.py" file if you want to tweak the model's behavior.

# French

## Compétences mises en pratique
Environnements virtuels, APIs, Programmation Orientée Objet, séparation du projet en de multiples modules, intelligence artificielle, Langchain, documentation, anglais

## Description
Ceci est un projet destiné à montrer une partie de mon éventail de capacités à des employeurs. Ce script fait appel à l'API de Reddit pour collecter un certain nombre de posts (ainsi que des informations sur ces derniers) fixé par l'utilisateur, ou sur la page d'accueil, ou sur un subreddit bien spécifique. Ces posts sont ensuite temporairement sauvegardés dans un fichier texte sur lequel un RAG (Retrival Augmented Generation) sera appliqué, un modèle d'OpenAI recommandant les 3 - 5 posts les plus susceptibles de plaire à l'utilisateur.

![Example of execution (French)](assets/app_screenshot_fr.png?raw=true "Optional Title")

## Pré-requis
Ce script considère que:
- Vous possédez votre propre application Reddit. ([tutoriel vidéo ici (anglais)](https://youtu.be/KmFKO1dp_vQ?si=yIzYlWqkx8KAmurQ)). Facile, rapide et gratuit. Utilisez "https://localhost:8080" comme "redirect uri".
- Vous disposez d'une clé d'API OpenAI. ([tutoriel vidéo ici (anglais)](https://youtu.be/gBSh9JI28UQ?si=BAWFhPr3-s-0ZaH-)) Attention: PAYANT.
- Vous avez un compte Reddit.

## Installation
Dans le CMD de Windows:

```console
git clone https://github.com/Mykiora/reddit-posts-collector.git
cd reddit-posts_collector
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

Si c'est la première fois que vous installez le programme, il vous sera demandé d'entrer vos identifiants Reddit, votre clé d'API OpenAI, ainsi que le client ID et le client secret (que vous pouvez trouver là où vous avez créé votre app Reddit à [cette url](https://reddit.com/prefs/apps)). Alors, assurez-vous d'avoir préparé ces informations.

## Utilisation
Tout ce que vous avez à faire est d'exécuter le fichier "main.py" et suivre les instructions. Tout se fera automatiquement en l'espace de quelques secondes. Tout en haut de ce fichier, il y a des paramètres que vous pouvez modifier. Ils sont:

- subreddit: Si vous souhaitez récupérer les posts d'un subreddit spécifique.
- filter: des filtres Reddit que vous pouvez appliquer aux posts recherchés. Choisissez parmi: best, hot, new, rising, top, controversial.
- post_limit: Le nombre de posts que vous voulez récupérer (peut causer des problèmes si ce paramètre est fixé à un nombre plus grand que le nombre de posts disponnibles sur un subreddit donné)
- rag: Procède au RAG sur les données des posts collectés si ce paramètre est fixé à 1 (coûte de l'argent). Saute complètement ce processus si fixé à 0. (Vous ne disposerez alors que données brutes dans data/post_data.txt)

## Credits
RAG code reference: https://github.com/pixegami/langchain-rag-tutorial