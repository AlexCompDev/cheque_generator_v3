import random
import xml.etree.ElementTree as ET


class Bar:
    def __init__(self):
        self.old_barcodes = []
        self.new_barcodes = []

    def getnew(self, n):
        """Генерация новых баркодов."""
        for _ in range(n):
            barcode = str(random.randint(1000000000000, 9999999999999))
            self.new_barcodes.append(barcode)
            self.old_barcodes.append(barcode)  # Сохраняем новые баркоды как старые
        return self.new_barcodes[-n:]

    def getold(self, n):
        """Получение старых баркодов."""
        if n > len(self.old_barcodes):
            raise ValueError(
                "Количество старых баркодов превышает количество сгенерированных баркодов"
            )
        return self.old_barcodes[-n:]


def generate_random_date(include_time=False):
    """Генерация случайной даты."""
    day = str(random.randint(1, 31)).zfill(2)
    month = str(random.randint(1, 12)).zfill(2)
    year = str(random.randint(2020, 2022))
    if include_time:
        hour = str(random.randint(0, 23)).zfill(2)
        minute = str(random.randint(0, 59)).zfill(2)
        second = str(random.randint(0, 59)).zfill(2)
        return f"{day}-{month}-{year}T{hour}:{minute}:{second}"
    return f"{day}-{month}-{year}"


# Создание корневого элемента
root = ET.Element("Cheque")

# Случайный выбор между Header и HeaderTTN
if random.choice([True, False]):
    header = ET.SubElement(root, "Header")
    header_date = ET.SubElement(header, "Date")
    header_date.text = generate_random_date(include_time=True)
    header_kassa = ET.SubElement(header, "Kassa")
    header_kassa.text = str(random.randint(1, 100))
    header_shift = ET.SubElement(header, "Shift")
    header_shift.text = str(random.randint(1, 10))
    header_number = ET.SubElement(header, "Number")
    header_number.text = str(random.randint(1, 100))
    header_type = ET.SubElement(header, "Type")
    header_type.text = random.choice(["Продажа", "Возврат"])
else:
    header = ET.SubElement(root, "HeaderTTN")
    header_date = ET.SubElement(header, "Date")
    header_date.text = generate_random_date()
    header_bill_number = ET.SubElement(header, "BillNumber")
    header_bill_number.text = str(random.randint(1, 100))
    header_ttn_number = ET.SubElement(header, "TTNNumber")
    header_ttn_number.text = str(random.randint(1, 100))
    header_type = ET.SubElement(header, "Type")
    header_type.text = random.choice(["Продажа", "Возврат"])

# Создание объекта Bar
bar = Bar()

# Генерация баркодов
num_barcodes_to_generate = 20
bar.getnew(num_barcodes_to_generate)  # Генерация и сохранение баркодов

# Случайное количество старых и новых баров
num_old_bars = random.randint(1, 10)
num_new_bars = random.randint(1, 10)

# Генерация старых баров
old_bars = bar.getold(num_old_bars)

# Генерация новых баров
new_bars = bar.getnew(num_new_bars)

# Создание элемента Content
content = ET.SubElement(root, "Content")

# Генерация новых баров
for new_bar in new_bars:
    bottle = ET.SubElement(content, "Bottle")
    bottle_barcode = ET.SubElement(bottle, "Barcode")
    bottle_barcode.text = new_bar
    bottle_ean = ET.SubElement(bottle, "EAN")
    bottle_ean.text = str(random.randint(1000000000000, 9999999999999))
    bottle_price = ET.SubElement(bottle, "Price")
    bottle_price.text = str(round(random.uniform(1.0, 100.0), 2))

# Случайное количество позиций Nomark
num_nomarks = random.randint(1, 10)

# Генерация позиций Nomark
for _ in range(num_nomarks):
    nomark = ET.SubElement(content, "Nomark")
    nomark_pos_identity = ET.SubElement(nomark, "PosIdentity")
    nomark_pos_identity.text = str(random.randint(100000, 999999))
    nomark_price = ET.SubElement(nomark, "Price")
    nomark_price.text = str(round(random.uniform(1.0, 100.0), 2))

# Создание XML-строки
xml = ET.tostring(root, encoding="utf-8", method="xml")
xml = xml.decode("utf-8")  # Декодируем байты в строку

# Сохранение XML в файл
with open("cheque.xml", "w", encoding="utf-8") as f:
    f.write(xml)

# Вывод XML на стандартный вывод
print(xml)
(round(random.uniform(1.0, 100.0), 2))
