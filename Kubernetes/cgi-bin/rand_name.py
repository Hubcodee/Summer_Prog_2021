import requests
import random


def words_fetch():
    url = "https://svnweb.freebsd.org/csrg/share/dict/propernames?revision=61767&view=co"

    names = requests.get(url).text

    words = names.split()

    name = random.choice(words)
    return name
