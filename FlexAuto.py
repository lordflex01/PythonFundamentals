import requests
from bs4 import BeautifulSoup
import csv

print ("Bienvenue sur FlexAuto, votre moteur de recherche pour des annonces automobiles.")
brand = input("Marque: ")
model = input("Modèle: ")
year = input("Année: ")
price = input("Budget: ")


# Nous devons d'abord fournir l'url de notre cible 
base_url = f'https://www.autoscout24.fr/lst/{brand}/{model}?atype=C&cy=F&desc=0&fregfrom={year}&priceto={price}&sort=standard&source=homepage_search-mask&ustate=N%2CU'

page = requests.get(base_url) 
# request.get() exécute une requête GET en utilisant l’URL transmise comme paramètre. 
# Il renvoie ensuite un objet Response contenant la réponse du serveur à la requête HTTP.
# Si la requête HTTP est exécutée avec succès, page.status_code contiendra 200
print(page.status_code)

# Vous devez faire attention à la propriété page.text. 
# Elle contient le document HTML renvoyé par le serveur au format chaîne.
# Pour analyser le document HTML renvoyé par le serveur suite à la requête GET, passez page.text au constructeur BeautifulSoup() 
soup = BeautifulSoup(page.text, 'html.parser')

# La variable soup contient maintenant un objet BeautifulSoup.
# Il s’agit d’une structure arborescente générée à partir de l’analyse syntaxique du document HTML.
# Tout d’abord, vous avez besoin d’une structure de données dans laquelle stocker les données collectées.
cars = []

# Nous allons créé la fonction pour scraper 
def scraping(soup, cars):
    # Beautiful Soup propose différentes approches pour sélectionner des éléments du DOM.
    cars_elements = soup.find_all('article', class_='cldt-summary-full-item listing-impressions-tracking list-page-item ListItem_article__qyYw7')
    # renvoie une liste des éléments HTML correspondant à la condition de sélecteur passée par paramètre(car).
    # Nous allons effectuer une itération pour récuperer les données des citations
    for car_element in cars_elements:
        # renvoie le premier élément HTML correspondant à la stratégie de sélecteur d’entrée (text)
        text = car_element.find('span', class_='ListItem_version__5EWfi').text
        # renvoie le premier élément HTML correspondant à la stratégie de sélecteur d’entrée (price)
        price = car_element.find('p', class_='Price_price__APlgs PriceAndSeals_current_price__ykUpx').text

        # Pour faciliter les choses, Beautiful Soup utilise également la méthode select(). 
        # Cela vous permet d’appliquer directement un sélecteur CSS 
        car_details = car_element.select('.VehicleDetailTable_container__XhfV1 .VehicleDetailTable_item__4n35N')

        # Puisqu’il y a plusieurs chaînes de balises tag associées à la citation, vous devez stocker celles-ci dans une liste.
        details = []
        for car_detail in car_details:
            details.append(car_detail.text)

        # Vous pouvez ensuite transformer ces données extraites en dictionnaire et les ajouter à la liste des citations.
        cars.append(
            {
                'text': text,
                'price': price,
                'details': ' - '.join(details) # Concate tous les details en une chaine de caractere 
            }
        )

# Pour finir nous allons faire appel à la fonction pour l'éxecuter 
scraping(soup,cars)


# Nous allons ensuite exporter la liste de dictionnaires contenant les données des citations dans un fichier CSV
csv_file = open('cars.csv', 'w', encoding='utf-8', newline='') # Créer et ouvrir le fichier cars.csv
writer = csv.writer(csv_file, delimiter=';') # Donner les droits pour insérer les données
writer.writerow(['Description', 'Price', 'Details']) # Créer les en-têtes (colonnes)
for car in cars: # Insérer les données pour chaque colonne 
    writer.writerow(car.values())
csv_file.close() # Fermer le fichier csv
