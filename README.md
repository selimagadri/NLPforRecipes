# NLPforRecipes


**Project Description :**

**Objective:** Collect a large dataset of recipes from various French cooking websites to build a corpus of recipes (in French).

**Use case:** Recipe recommendation: Use the corpus to create a recommendation system that suggests recipes based on the user's culinary preferences, dietary restrictions or available ingredients.

**Data sources:** websites or cooking platforms that provide a wide range of recipes. Popular sources include: Marmiton, Cuisine AZ.

**Steps for building the corpus of recipes and modeling:**.

1. **Selecting Data Sources:** Choose websites or culinary platforms to extract recipes, respecting the conditions of use (Marmiton, Cuisine AZ).
1. **Web Data Extraction:** Use web scraping tools (BeautifulSoup, Scrapy ...) to collect recipe details, such as names, ingredients, preparation steps, cooking times, dietary restrictions. Also collect data on user interactions with recipes, such as views, tastes and saves, in order to personalize recommendations.
1. **Data clean-up:** Ensure data consistency by standardizing ingredient names, removing HTML tags, and correcting format variations. It is also possible to remove stop words with NLTK and deal with missing values and noisy data. Convert tokens into vectors using techniques such as TF-IDF, Doc2Vec or Word2Vec.
1. **Recipe storage:** Organize recipes in a structured format such as CSV, associating each recipe with key-value attributes (Attributes: names, ingredients, preparation steps, cooking times, dietary restrictions, views, tastes, backups ...).
1. **Metadata Collection:** Record metadata such as source URL, publication date, and author if possible.
1. **Modeling:** The choice of recommendation model will depend on the data to be collected. Several recommendation models can be used, including Content-Based Filtering, Collaborative Filtering, Hybrid Models, Matrix Factoring and Deep Learning Models.
1. **Training**
1. **Evaluation** 



**Selima Gadri \& Ines Ouhichi**
