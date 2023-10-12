from recombee_api_client.api_client import RecombeeClient, Region
from recombee_api_client.api_requests import *
import pandas as pd

# edit the Db and private token
client = RecombeeClient('-myDb-', '-private_token-', region=Region.EU_WEST)

books_df = pd.read_excel('./book_dataset.xlsx')

client.send(AddItemProperty('title', 'string'))
client.send(AddItemProperty('author', 'string'))
client.send(AddItemProperty('publisher', 'string'))
client.send(AddItemProperty('ISBN_13', 'double'))
client.send(AddItemProperty('pages', 'double'))


requests = [SetItemValues(
    row['id'],
    {
        "title": row['title'],
        "author":  row['author'],
        "publisher": row['publisher'],
        "ISBN_13": row['ISBN_13'],
        "pages": row['pages']
    },
    cascade_create=True
) for i, row in books_df.iterrows()]
client.send(Batch(requests))
