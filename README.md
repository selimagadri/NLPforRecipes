# NLPforRecipes


**Description du projet :**

**Objectif :** Collecter un large ensemble de données de recettes à partir de différents sites web de cuisine pour construire un corpus de recettes.

**Cas d'utilisation :** Recommandation de recettes : Utiliser le corpus pour créer un système de recommandation qui suggère des recettes en fonction des préférences culinaires de l'utilisateur, des restrictions alimentaires ou des ingrédients disponibles.

**Sources de données :** les sites web ou les plateformes de cuisine qui fournissent un large éventail de recettes. Parmi les sources les plus populaires, citons : Marmiton, Cuisine AZ.

**Étapes de la création du corpus de recettes et de modélisation :**

1. **Sélection des Sources de Données :** Choisir les sites web ou les plateformes culinaires pour extraire les recettes, en respectant les conditions d'utilisation (Marmiton, Cuisine AZ).
1. **Extraction de Données Web :** Utiliser des outils de scraping web (BeautifulSoup, Scrapy …) pour collecter les détails des recettes, tels que les noms, les ingrédients, les étapes de préparation, les temps de cuisson, les restrictions alimentaires. Recueillir aussi des données sur les interactions des utilisateurs avec les recettes, telles que les vues, les goûts et les sauvegardes, afin de personnaliser les recommandations.
1. **Nettoyage des Données :** S’assurer que les données sont cohérentes en normalisant les noms d'ingrédients, en supprimant les balises HTML, et en corrigeant les variations de format. Il est également possible de supprimer les stop words avec NLTK et de traiter les valeurs manquantes et les données bruitées. Convertir les tokens en vecteurs à l'aide de techniques telles que TF-IDF, Doc2Vec ou Word2Vec.
1. **Stockage des Recettes :** Organiser les recettes dans un format structuré comme CSV, en associant chaque recette à des attributs clé-valeur (Attributs : les noms, les ingrédients, les étapes de préparation, les temps de cuisson, les restrictions alimentaires, les vues, les goûts, les sauvegardes …).
1. **Collecte des Métadonnées :** Enregistrer des métadonnées telles que l'URL source, la date de publication, et l'auteur si possible.
1. **Modélisation :** Le choix du modèle de recommandation va dépendre des données qu’on va collecter, plusieurs modèles de recommandation peuvent être utilisés, notamment le Filtrage basé sur le Contenu, le Filtrage Collaboratif, les Modèles Hybrides, la Factorisation de Matrices et les Modèles d'Apprentissage Profond.
1. **Entraînement**
1. **Evaluation** 



**Selima Gadri**

**Ines Ouhichi**
