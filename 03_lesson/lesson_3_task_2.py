from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 18", "+79111111111"),
    Smartphone("Samsung", "Galaxy S26", "+79222222222"),
    Smartphone("Xiaomi", "17 Pro", "+79333333333"),
    Smartphone("Google", "Pixel 11", "+79444444444"),
    Smartphone("OnePlus", "15", "+79555555555")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
