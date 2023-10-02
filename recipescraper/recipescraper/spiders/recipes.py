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
            total_pages = 1  # Update with the correct number of pages 85
        elif "entree" in response.url:
            total_pages = 1  # Update with the correct number of pages 186
        elif "plat-principal" in response.url:
            total_pages = 1  # Update with the correct number of pages 568
        elif "dessert" in response.url:
            total_pages = 1  # Update with the correct number of pages 428
        else:
         # Handle other cases
            total_pages = 0


        # Generate the URLs for the remaining pages
        for page_number in range(2, total_pages + 1):  # Start from page 2 since page 1 is already scraped
            page_url = response.urljoin(f'{page_number}')

            # Use response.follow to generate a request for the current page URL
            yield response.follow(page_url, callback=self.parse)

    def parse_recipe_page(self, response):


        #RECIPE NAME
        recipe_name = response.css('h1.SHRD__sc-10plygc-0.itJBWW::text').extract()

        #RECIPE TYPE
        recipe_type = response.css('span.SHRD__sc-10plygc-0.duPxyD::text').extract()[2]

        # RECIPE SUB-TYPE
        recipe_sub_type = response.css('span.SHRD__sc-10plygc-0.duPxyD::text').extract()[-2]

        # INGREDIENTS
        # Extract the elements containing ingredients information
        elements = response.css('div.RCP__sc-vgpd2s-1.fLWRho')
        # Initialize a list to store the cleaned ingredient data
        ingredients = []
        for element in elements:
            # Extract the individual components of an ingredient
            quantity_unit = element.css('span.SHRD__sc-10plygc-0.epviYI').css('::text').extract()
            ingredient_name1 = element.css('span.RCP__sc-8cqrvd-3.itCXhd::text').extract()
            ingredient_name2 = element.css('span.RCP__sc-8cqrvd-3.cDbUWZ::text').extract()
            additional_info = element.css('span.RCP__sc-8cqrvd-4.gKydlX::text').extract()
            # Initialize the ingredient data dictionary
            ingredient_data = {
                'quantite': None,
                'unite': None,
                'nom': None,
                'autre_info': None
            }
            # Split quantity and unit
            if quantity_unit:
                quantity_unit = [item.strip() for item in quantity_unit if item.strip()]
                if quantity_unit:
                    ingredient_data['quantite'] = quantity_unit[0]
                    ingredient_data['unite'] = ' '.join(quantity_unit[1:])
            # Consolidate ingredient_name1 and ingredient_name2 into a single nom field
            if ingredient_name1 or ingredient_name2:
                ingredient_data['nom'] = ' '.join((ingredient_name1 + ingredient_name2)).strip()
            # Additional info
            if additional_info:
                ingredient_data['autre_info'] = ' '.join(additional_info).strip()
            # Append the cleaned ingredient dictionary to the list
            ingredients.append(ingredient_data)

        # USTENSILES   
        # Extract the elements containing ustensiles information
        elements = response.css('div.RCP__sc-1641h7i-2.dUdOZp')
        # Initialize a list to store the cleaned ustensils data
        ustensils = []
        for element in elements:
            name_quantity = element.css('div.RCP__sc-1641h7i-3.iLcXC').css('::text').extract()
            # Initialize the ustensils data dictionary
            ustensil_data = {
                'quantite': None,
                'nom': None
            }
            name_quantity = [item.strip() for item in name_quantity if item.strip()]
            if name_quantity:
                ustensil_data['quantite'] = name_quantity[0]
                ustensil_data['nom'] = ' '.join(name_quantity[1:])
            ustensils.append(ustensil_data)

        # NUMBER OF PERSONS 
        number_of_persons = response.css('span.SHRD__sc-w4kph7-4.knYsyq::text').extract()

        # DIFFICULTY 
        dif = response.css('p.RCP__sc-1qnswg8-1.iDYkZP::text').extract()[1] 

        # PREP TIME
        prep_time_elements = response.css('span.SHRD__sc-10plygc-0.bzAHrL::text').extract()
        prep_time = {
            'total' : prep_time_elements[0].replace('\xa0', ' '),
            'prepartion' : prep_time_elements[1].replace('\xa0', ' ') if not prep_time_elements[1] == '-' else None,
            'repos' : prep_time_elements[2].replace('\xa0', ' ')  if not prep_time_elements[2] == '-' else None,
            'cuisson' : prep_time_elements[3].replace('\xa0', ' ')  if not prep_time_elements[3] == '-' else None
        }

        # STEPS
        # Extraction prepartion steps part
        steps_li = response.css('div.SHRD__sc-juz8gd-3.bsFPOd > ul > li')
        steps = {}
        for step in steps_li: 
            # Extract the step number
            step_num = step.css('h3.RCP__sc-1wtzf9a-1.ikYBNp::text').extract()
            step_num_str = ' '.join(step_num).strip()
            details = {
                'ingredients': None,
                'description' : None
            }
            # Extract the ingredients needed for this step
            ing_step = step.css('img::attr(alt)').extract()
            details['ingredients'] = [item.strip() for item in ing_step if item.strip()]
            # Extract the description of the step
            desc_step = step.css('p.RCP__sc-1wtzf9a-3.bFBrMO::text').extract()
            details['description'] = desc_step
            # Append the step
            steps[step_num_str] = details

        yield {
            'nom_de_recette' : recipe_name,
            'type_de_recette' : recipe_type,
            'type_du_plat' : recipe_sub_type,
            'ingredients': ingredients,
            'ustensiles': ustensils,
            'nombre_de_personnes': number_of_persons,
            'difficulte': dif,
            'temps de preparation' : prep_time,
            'etapes' : steps
        }
        #scrapy crawl -o out.csv recipes
        #add comments, stars(note), name of similar recipes



      