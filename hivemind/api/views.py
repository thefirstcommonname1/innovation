from django.shortcuts import render
from django.http import HttpResponse
import random
import string
import getpass
import json
import pprint
import beem
from beem import Hive
from beem.transactionbuilder import TransactionBuilder
from beembase.operations import Comment
# Create your views here.

def index(request):
  return HttpResponse("Return 'render()' with index.html instead when view is rdy")
    
def makepost(request):
  if request.method == 'POST':
    author = request.POST.get('author') # need a get route that renders the form with 'author' as name
    title = request.POST.get('title') # same shit
    body = request.POST.get('body') # same shit

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

    return(HttpResponse(str(broadcast_tx)))
  else:
    return render(request, 'form_post.html')