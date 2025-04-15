import uuid
from math import ceil
from datetime import datetime
from utils import is_alphanumeric

def process_receipt(receipt):
    points = 0

    points += sum(1 for c in receipt['retailer'] if is_alphanumeric(c))

    total = float(receipt['total'])
    if total == int(total):
        points += 50
    if (total * 100) % 25 == 0:
        points += 25

    items = receipt.get('items', [])
    points += (len(items) // 2) * 5

    for item in items:
        desc = item['shortDescription'].strip()
        price = float(item['price'])
        if len(desc) % 3 == 0:
            points += ceil(price * 0.2)

    day = int(receipt['purchaseDate'].split("-")[2])
    if day % 2 == 1:
        points += 6

    hour, minute = map(int, receipt['purchaseTime'].split(":"))
    if hour == 14:
        points += 10

    return str(uuid.uuid4()), points