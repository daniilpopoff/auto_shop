import requests
from bs4 import BeautifulSoup


class CarParser:
    def __init__(self):
        self.base_url = " https://www.mashina.kg/search/all/?"  #https://mashina.kg/cars/passenger-cars/
    def get_pages_links(self):
        """
        Возвращает список ссылок на страницы с машинами.
        """
        pages_links = []
        for page_num in range(1, 1001):
            pages_links.append(f"{self.base_url}?page={page_num}")
        return pages_links

    def parse_page(self, page_link):
        """
        Парсит страницу с машинами.
        """
        resp = requests.get(page_link)
        soup = BeautifulSoup(resp.content, "html.parser")
        cars = soup.find_all("div", class_="car-item")
        for car in cars:
            yield self.parse_car(car)

    def parse_car(self, car):
        """
        Парсит одну машину.
        """
        data = {}
        data["year"] = car.find("span", class_="year").text
        data["mileage"] = car.find("span", class_="mileage").text
        data["body"] = car.find("span", class_="body").text
        data["color"] = car.find("span", class_="color").text
        data["engine"] = car.find("span", class_="engine").text
        data["transmission"] = car.find("span", class_="transmission").text
        data["drive"] = car.find("span", class_="drive").text
        data["steering_wheel"] = car.find("span", class_="steering_wheel").text
        data["status"] = car.find("span", class_="status").text
        data["customs"] = car.find("span", class_="customs").text
        data["exchange"] = car.find("span", class_="exchange").text
        data["availability"] = car.find("span", class_="availability").text
        data["region"] = car.find("span", class_="region").text
        data["city"] = car.find("span", class_="city").text
        data["account"] = car.find("span", class_="account").text
        price_soms = car.find("span", class_="price_soms")
        if price_soms is not None:
            data["price_soms"] = price_soms.text
        else:
            data["price_soms"] = ""
        data["price_dollars"] = car.find("span", class_="price_dollars").text
        data["title"] = car.find("h1").text
        return data

    def parse_all_pages(self):
        """
    Парсит все страницы с машинами.
    """
        pages_links = self.get_pages_links()
        for page_link in pages_links:
            for car_data in self.parse_page(page_link):
                yield car_data


if __name__ == "__main__":
    parser = CarParser()

    for car_data in parser.parse_all_pages():
        print(car_data)






