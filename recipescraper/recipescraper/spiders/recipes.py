import scrapy


class RecipesSpider(scrapy.Spider):
    name = "recipes"
    allowed_domains = ["www.marmiton.org"]
    start_urls = ["https://www.marmiton.org/recettes/index/categorie/aperitif-ou-buffet/",
                  "https://www.marmiton.org/recettes/index/categorie/entree/",
                  "https://www.marmiton.org/recettes/index/categorie/plat-principal/",
                  "https://www.marmiton.org/recettes/index/categorie/dessert/",
                  
    ]
    def parse(self, response):
     



    # Extract the URLs of every recipe item on the current page
    
        recipe_urls = response.css('a.recipe-card-link::attr(href)').getall()

        # Process and yield each recipe URL
        # Generate requests for each recipe URL
        for url in recipe_urls:
            yield scrapy.Request(url, callback=self.parse_recipe_page)

        # Check the current URL and extract the total number of pages dynamically
        if "aperitif-ou-buffet" in response.url:
            total_pages = 6  # Update with the correct number of pages 85
        elif "entree" in response.url:
            total_pages = 5  # Update with the correct number of pages 186
        elif "plat-principal" in response.url:
            total_pages = 8  # Update with the correct number of pages 568
        elif "dessert" in response.url:
            total_pages = 7  # Update with the correct number of pages 428
        else:
         # Handle other cases
            total_pages = 0


        # Generate the URLs for the remaining pages
        for page_number in range(2, total_pages + 1):  # Start from page 2 since page 1 is already scraped
            page_url = response.urljoin(f'{page_number}')

            # Use response.follow to generate a request for the current page URL
            yield response.follow(page_url, callback=self.parse)




    def parse_recipe_page(self, response):
        pass