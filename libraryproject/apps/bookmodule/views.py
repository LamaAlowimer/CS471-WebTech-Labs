from django.shortcuts import render  

def index(request):
    name = request.GET.get("name") or "world!"
   
    return render(request, "bookmodule/index.html", {"name": name})

def index2(request, val1 = 0):
    from django.http import HttpResponse
    return HttpResponse("value1 = " + str(val1))
def viewbook(request, bookId):
    # محاكاة لوجود كتب في قاعدة البيانات
    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
    book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
    
    targetBook = None
    if book1['id'] == bookId: targetBook = book1
    if book2['id'] == bookId: targetBook = book2
    
    context = {'book': targetBook} # تجهيز الكتاب لارساله لصفحة الـ HTML
    return render(request, 'bookmodule/show.html', context)