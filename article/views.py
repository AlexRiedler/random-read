from django.shortcuts import render
from utils import redis_conn
from article.models import Article

def show_random_article(request):
    articleid = redis_conn.srandmember(Article.ALL_PRIMARY_IDS_KEY)
    article = Article.objects.filter(id=articleid).first()
    if article is None:
        pass

    return render(request, "article/article.html", {
        "article": article,


    })
