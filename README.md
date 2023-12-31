# NLPforRecipes

## **Project Structure**

- **Scraper:** [recipes.py](recipescraper/recipescraper/spiders/recipes.py) - Python script for scraping recipes from the Marmiton website.
- **Notebooks:**
  - [Data Exploration Notebook](data_exploration.ipynb) - Jupyter notebook containing code for data exploration.
  - [Preprocessing and Training Notebook](NLPRecipesClassificationTypeOfRecipe.ipynb) - Jupyter notebook containing code for data preprocessing and model training.
- **Dataset:** [dataset](https://drive.google.com/file/d/1mTUZPUXeXSPW1N-oA9Ubp7XjgPovSxaQ/view?usp=drive_link) - CSV File containing the dataset used for training and evaluation.
- **Checkpoints:** [final_checkpoints.pth]([checkpoints/](https://drive.google.com/file/d/1iHag8JuQYJoT6geBgv1FV00Pb0RPH0oc/view?usp=sharing)) - File containing model checkpoints.

## **Project Description :**

**Objective:** Collect a large dataset of recipes from various French cooking websites to build a corpus of recipes (in French).

**Data sources:** websites or cooking platforms that provide a wide range of recipes. Popular sources include: Marmiton, Cuisine AZ.

**Steps for building the corpus of recipes and modeling:**.

1. **Selecting Data Sources:** Choose websites or culinary platforms to extract recipes, respecting the conditions of use (Marmiton, Cuisine AZ).
1. **Web Data Extraction:** Use web scraping tools (BeautifulSoup, Scrapy ...) to collect recipe details, such as names, ingredients, preparation steps, cooking times, dietary restrictions. Also collect data on user interactions with recipes, such as views, tastes and saves, in order to personalize recommendations.
1. **Data cleaning:** Ensure data consistency by standardizing ingredient names, removing HTML tags, and correcting format variations. It is also possible to remove stop words with NLTK and deal with missing values and noisy data.
1. **Recipe storage:** Organize recipes in a structured format such as CSV, associating each recipe with key-value attributes (Attributes: names, ingredients, preparation steps, cooking times, dietary restrictions, views, tastes, backups ...).
1. **Metadata Collection:** Record metadata such as source URL, publication date, and author if possible.
1. **Modeling**
1. **Training**
1. **Evaluation** 



**Selima Gadri \& Ines Ouhichi**
