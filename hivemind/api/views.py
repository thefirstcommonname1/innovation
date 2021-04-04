from django.shortcuts import render, redirect
from django.template import loader
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
from beem.account import Account
from beem.discussions import Query, Discussions
# defining private keys inside source code is not secure way but possible
h = Hive(keys=['5JfPgUtjyCsPedXjBqJmjGR7X8T1G18sT9DUa3fxwcBRTsSoYt2', '5JCz4JT3Dnr51AbgZHbviwNcn9GAU8cJsENNdZffVMRZYe2HLWG'])
a = Account('tippynerdo', blockchain_instance=h)

# Create your views here.

def index(request):
  q=Query(limit=100, tag="")
  d=Discussions()
  posts = d.get_discussions('trending', q, limit=100)
  template = loader.get_template('api/index.html')
  context = {'posts': posts}
  return HttpResponse(template.render(context, request))
    
def makepost(request):
  if request.method == 'POST':
    author = request.POST.get('author') # need a get route that renders the form with 'author' as name
    title = request.POST.get('title') # same shit
    body = request.POST.get('body') # same shit
    tag_first = request.POST.get('tag1')
    tag_second = request.POST.get('tag2')
    whatever = request.POST.get('privatekey')
    
    taglist = [tag_first, tag_second]
    
    permlink = ''.join(random.choices(string.digits, k=10))

    client = Hive('https://api.hive.blog', keys=['5JfPgUtjyCsPedXjBqJmjGR7X8T1G18sT9DUa3fxwcBRTsSoYt2',
    '5JCz4JT3Dnr51AbgZHbviwNcn9GAU8cJsENNdZffVMRZYe2HLWG'])
    tx = TransactionBuilder(blockchain_instance=client)
    tx.appendOps(Comment(**{
        "parent_author": '',
        "parent_permlink": taglist[0],
        "author": author,
        "permlink": permlink,
        "title": title,
        "body": body,
      "json_metadata": json.dumps({"tags": taglist})
    }))


    tx.appendWif('5JfPgUtjyCsPedXjBqJmjGR7X8T1G18sT9DUa3fxwcBRTsSoYt2')
    signed_tx = tx.sign()
    broadcast_tx = tx.broadcast(trx_id=True)
    print(broadcast_tx)
    return redirect('index')
  else:
    return render(request, 'api/form_post.html')