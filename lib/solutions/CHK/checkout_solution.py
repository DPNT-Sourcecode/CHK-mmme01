

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


def validate_entry(item):
    return item in VALID_ENTRIES.keys()
