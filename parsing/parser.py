import requests
from bs4 import BeautifulSoup

car_info_dict = {
    "Year of Manufacture": None,
    "Mileage": None,
    "Body Type": None,
    "Color": None,
    "Engine": None,
    "Transmission": None,
    "Drive": None,
    "Steering": None,
    "Condition": None,
    "Customs": None,
    "Availability": None,
    "Region, City of Sale": None,
    "Registration": None
}

url = "https://www.mashina.kg/search/all/?page=1"

response = requests.get(url)
if response.status_code == 200:
    html_content = response.text

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    car_cards = soup.find_all('div', class_='list-item list-label')

    # Iterate through each car card and extract information
    for car_card in car_cards:
        # Extract the link to the car
        car_link = car_card.find('a')['href']
        full_car_link = f'https://www.mashina.kg{car_link}'  # Assuming the base URL is known

        # Now you can visit the full_car_link and extract more details
        car_response = requests.get(full_car_link)
        if car_response.status_code == 200:
            car_html_content = car_response.text
            car_soup = BeautifulSoup(car_html_content, 'html.parser')
            # print(car_html_content)
            all_car_data = car_soup.find_all("div", class_="field-row clr",)
            # print(type(all_car_data))
            list_of_pure_car_data = []
            for data_row  in all_car_data:
                # print(type(data_row))
                list_of_pure_car_data.append(data_row.find('div', class_='field-value').get_text(strip=True))
            print(list_of_pure_car_data)


            #     # for key in car_info_dict.keys():
            #     all_car_data[data_row_num] = list(all_car_data.find_all('div', class_= "field-value").get_text(strip=True))
            #
            # print(data_row_num)




            # как я буду парсить мне надо сначала найти tab-content
            # потом внури него прописать что следующий див сразу же
            # за классом в котором находятся данные из стринга
            # год выпуска пробег и тд в нем находятся данные для этой переменной



            # with open('car_details_parser.html', 'w', encoding='utf-8') as file:
            #     file.write(str(car_soup))
            # Extract additional information from the car's detailed page
            # car_title = car_soup.find('h2', class_='name').get_text(strip=True)
            # car_price = car_soup.find('strong').get_text(strip=True)
            # # Add more extraction logic as needed
    # with open('base_car_parser.html', 'w', encoding='utf-8') as file:
    #     file.write(str(soup))