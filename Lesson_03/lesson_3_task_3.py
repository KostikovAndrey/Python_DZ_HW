from address import Address
from mailing import Mailing

from_address = Address(
    "106000",
    "Королёв",
    "Ленина",
    "19",
    "33"
)

to_address = Address(
    "111000",
    "Архангельск",
    "Горная",
    "44",
    "21"
)

mailing = Mailing(to_address, from_address, 550, "TRACK123456789")

print(
    f"Отправление {mailing.track} "
    f"из {mailing.from_address.index}, {mailing.from_address.city}, "
    f"{mailing.from_address.street}, {mailing.from_address.house} - "
    f"{mailing.from_address.apartment} "
    f"в {mailing.to_address.index}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.house} - "
    f"{mailing.to_address.apartment}. "
    f"Стоимость {mailing.cost} рублей."
)
