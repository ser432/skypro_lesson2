from address import Address
from mailing import Mailing

to_addr = Address("123456", "Москва", "Ленина", "10", "11")
from_addr = Address("654321", "Санкт-Петербург", "Невский", "20", "22")

shipment = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=350,
    track="TRACK123456"
)

to = shipment.to_address
from_ = shipment.from_address

print(
    f"Отправление {shipment.track} из {from_.index}, {from_.city}, "
    f"{from_.street}, {from_.house} - {from_.apartment} в {to.index}, "
    f"{to.city}, {to.street}, {to.house} - {to.apartment}. "
    f"Стоимость {shipment.cost} рублей."
)
