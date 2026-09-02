from smartphone import Smartphone

catalog = [
   Smartphone("Apple", "iPhone 15", "+1-234-567-8901"),
   Smartphone("Samsung", "Galaxy S24", "+1-987-654-3210"),
   Smartphone("Xiaomi", "14 Pro", "+7-999-111-2233")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model} - {smartphone.phone_number}")