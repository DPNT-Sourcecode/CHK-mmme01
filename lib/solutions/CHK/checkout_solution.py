

AVAILABLE_STOCK = {
    'A': {'price': 50, 'deal_qty': 3, 'deal_px': 130},
    'B': {'price': 30, 'deal_qty': 2, 'deal_px': 45 },
    'C': {'price': 20},
    'D': {'price': 15},
}



# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    """
    Im presuming that skus is going to look something like this

    'ABCDABBCA'

    :param skus:
    :return:
    """
    items_count = {}
    skus = skus.upper()

    for item in skus:
        if not validate_entry(item):
            print('%s is not a valid entry' % item)
            return -1

        if item in items_count:
            items_count[item] = items_count[item] + 1
        else:
            items_count[item] = 1

    return calculate_total(items_count)

def calculate_total(stock):
    print stock
    cum_sum = 0
    for (item, qty) in stock.items():
        item_px = AVAILABLE_STOCK[item]
        if AVAILABLE_STOCK[item].get('deal_qty'):
            deal_qty = AVAILABLE_STOCK[item].get('deal_qty')
            if qty >= deal_qty:
                if qty % deal_qty == 0:
                    price = AVAILABLE_STOCK[item]['deal_px'] * (qty / deal_qty)
                else:
                    price =
            else:
                price = item_px * qty
        else:
            price = item_px * qty
        cum_sum += price

    return cum_sum

def validate_entry(item):
    return item in AVAILABLE_STOCK

if __name__ == '__main__':
    print checkout('abcdabc')