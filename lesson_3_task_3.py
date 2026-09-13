from address import Address
from mailing import Mailing

to_adrs = Address(199000, "Москва", "Тверская", 10, 5)
from_adrs = Address(199000, "Санкт-Петербург", "Невский проспект", 12, 50)

mail = Mailing(to_address=to_adrs, from_address=from_adrs, coast=300.0, track="trfinrekll19909")

# 2. Исправлено: добавлен синтаксис f-строк f"..." вместо f ...
track_info = f"Отправление {mail.track}"
from_info = f"из {from_adrs.formatted()}"
to_info = f"в {mail.to_address.formatted()}"
coast_info = f"Стоимость {mail.coast} рублей."

# Вывод результата на экран
print(f"{track_info} {from_info} {to_info}. {coast_info}")
