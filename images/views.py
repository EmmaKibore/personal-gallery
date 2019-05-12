from django.shortcuts import render
from django.http import HttpResponse,Http404
import datetime as dt

def newsToday(request):
    date = dt.date.today()
    news = Article.news_today(date)
    return render(request, 'all-news/today-news.html', {"date": date,"news":news})



    html = f'''
        <html>
            <body>
                <h1> News for{day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)



def past_days_images(request,past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(images_today)

    images = Article.days_news(date)    
    return render(request, 'all-news/past-news.html',{"date": date,"news":news})           

    # day = convert_dates(date)
    # html = f'''
    # <html>
    #     <body>
    #         <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
    #     </body>
    # </html>
    #     '''
    # return HttpResponse(html) 

def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})  

def article(request,article_id):
    try:
        article = Article.objects.get(id = article_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-news/article.html", {"article":article})                     
