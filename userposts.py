import random
import string
import getpass
import json
import pprint
import beem
from beem import Hive
from beem.transactionbuilder import TransactionBuilder
from beembase.operations import Comment


author = input('Username: ')
title = input('Post Title: ')
body = input('Post Body: ')

taglimit = 2
taglist = []
for i in range(1, taglimit+1):
    print(i)
    tag = input(' Tag: ')
    taglist.append(tag)

permlink = ''.join(random.choices(string.digits, k=10))

client = Hive('http://127.0.0.1:8090')
tx = TransactionBuilder(blockchain_instance=client)
tx.apendOps(Comment(**{
    "parent_author": '',
    "parent_permlink": taglist[0],
    "author": author,
    "permlink": permlink,
    "title": title,
    "body": body,
    "json_metadata": json.dumps({"tags": taglist})
}))

wif_posting_key = getpass.getpass('Posting key: ')
tx.appendWif(wif_posting_key)
signed_tx = tx.sign()
broadcast_tx = tx.broadcast(trx_id=True)

print("Post created successfully: ", +str(broadcast_tx))
