

VALID_ENTRIES = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15
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

    calculate_total(items_count)

def calculate_total(stock):
    for (item, qty) in stock.items():


def validate_entry(item):
    return item in VALID_ENTRIES

if __name__ == '__main__':
    checkout('abcdabc')
