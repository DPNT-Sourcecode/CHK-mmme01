

AVAILABLE_STOCK = {
    'A': {'price': 50, 'deal_qtys': [5, 3], 'deal_px': [200, 130]},
    'B': {'price': 30, 'deal_qtys': [2],    'deal_px': [45], },
    'C': {'price': 20},
    'D': {'price': 15},
    'E': {'price': 40},
}

SPECIAL_OFFERS = {
    'E': {'offer_qty': 2, 'offer_on': 'D', 'offer_px_delta': AVAILABLE_STOCK['D']['price']}
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

    for item in skus:
        if not validate_entry(item):
            print('%s is not a valid entry' % item)
            return -1

        if item in items_count:
            items_count[item] = items_count[item] + 1
        else:
            items_count[item] = 1

    return calculate_total(items_count) if items_count else 0

def calculate_total(stock):
    stock, total = calculate_offers(stock, 0)
    stock, total = calculate_deals(stock, total)

    return total

def calculate_offers(stock, cum_sum):
    """
    Return how much we've saved with offers and adjust any stock amounts if needed.

    :param stock:
    :return:
    """
    for (item, qty) in stock.items():
        if item not in SPECIAL_OFFERS:
            continue

        offer_qty = SPECIAL_OFFERS[item]['offer_qty']
        if qty >= offer_qty and SPECIAL_OFFERS[item]['offer_on'] in stock.keys():
            if qty % offer_qty == 0:
                # so we subtract the offers and then minus a qty from the offer on
                # could be an issue here with us buying more on item E deals than we've of D
                # cum_sum -= (qty / offer_qty) * SPECIAL_OFFERS[item]['offer_px_delta']
                stock[SPECIAL_OFFERS[item]['offer_on']] = stock[SPECIAL_OFFERS[item]['offer_on']] - (qty / offer_qty)
            else:
                temp_qty = qty - (qty % offer_qty)
                # cum_sum -= (temp_qty / offer_qty) * SPECIAL_OFFERS[item]['offer_px_delta']
                stock[SPECIAL_OFFERS[item]['offer_on']] = stock[SPECIAL_OFFERS[item]['offer_on']] - (temp_qty / offer_qty)

    print stock, cum_sum
    return stock, cum_sum



def calculate_deals(stock, cum_sum):
    """
    This needs to calculate all the possible combinations of deals and offers that are the cheapest for these items.
    I think the way I've designed this is not the best. If I was to start over then i would consider a recursive or
    dynamic programming approach that would call itself to find cheapest combinations. I think the current implementation
    is getting to complication to continue. This is a fun way to interview though as it feels more lifelike than a
    hacker rank of leet code problem. I enjoyed doing this but am going to stop my code here.

    :param stock:
    :param cum_sum:
    :return:
    """
    for (item, qty) in stock.items():
        item_px = AVAILABLE_STOCK[item]['price']
        if AVAILABLE_STOCK[item].get('deal_qtys'):
            for (deal_qty, deal_px) in zip(AVAILABLE_STOCK[item].get('deal_qtys'), AVAILABLE_STOCK[item].get('deal_px')):
                if qty >= deal_qty:
                    if qty % deal_qty == 0:
                        price = deal_px * (qty / deal_qty)

                    else:
                        price = item_px * (qty % deal_qty)  # price of items not bought within deal
                        price += (qty - (qty % deal_qty)) / deal_qty * deal_px
                    qty -= deal_qty

                else:
                    price = item_px * qty
                    qty = 0
                if not qty:
                    break
        else:
            price = item_px * qty

        cum_sum += price

    print stock, cum_sum
    return stock, cum_sum

def validate_entry(item):
    return item in AVAILABLE_STOCK

if __name__ == '__main__':
    # print checkout("A") #expected: 50, got: -200
    # print checkout('ABCDE')#- {"method": "checkout", "params": ["ABCDE"], "id": "CHK_R2_012"}, expected: 155, got: -95
    print checkout('AAA')# {"method": "checkout", "params": ["AAA"], "id": "CHK_R2_015"}, expected: 130, got: 150
    print checkout('AAAA')# - {"method": "checkout", "params": ["AAAA"], "id": "CHK_R2_016"}, expected: 180, got: 200
    print checkout('AAAAAA')# - {"method": "checkout", "params": ["AAAAAA"], "id": "CHK_R2_018"}, expected: 250, got: 50
    print checkout('AAAAA')


