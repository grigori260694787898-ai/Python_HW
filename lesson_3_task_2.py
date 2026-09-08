from smartphone import Smartphone

catalog = [
   Smartphone("Apple", "iPhone 15", "+1-234-567-8901"),
   Smartphone("Samsung", "Galaxy S24", "+1-987-654-3210"),
   Smartphone("Nokia", "2256", "+7-987-123-2244"),
   Smartphone("Sony Erection", "ProLap", "+7-789-213-2255"),
   Smartphone("LG", "G123", "+7-989-321-2266")
]


for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model} - {smartphone.phone_number}")
