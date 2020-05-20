from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.conf import settings
#from django.contrib.syndication.views import Feed
from .key import key
import dropbox
import re
#from transliterate import translit, get_available_language_codes


base_url = '/bookz'
    
def get_connect(request):
    try:
        dbx=dropbox.Dropbox(key)
    except:
        dbx='connection problems'
    return dbx

def beautify(text):
        text = re.sub(r'-|_|\s+|/bookz/', ' ', text).strip().capitalize()
        ldi = text.rfind('.')
        if text.find('.') > 0: 
            text = re.sub(r'\.', ' ', text[:ldi])
        else:
            text    
        return text

def get_book(request):
    template_name = 'libviadrb/book.html'
    dbx = get_connect(request)
    try:
        path_from_url = request.GET['book']
        if path_from_url:
            dim = path_from_url[(path_from_url.rfind('.'))+1:]
            name = beautify(path_from_url)
            link = dbx.files_get_temporary_link(path_from_url).link
            #tr_name = translit(name,'ru')
        return render(request, template_name, {'link':link, 'path':path_from_url, 'name':name, 'dim':dim})
    except:
        name = 'Sorry, something went wrong ¯\_(ツ)_/¯'
        return render(request, template_name, {'name':name})


def get_books_list(request):
    template_name = 'libviadrb/library.html'
        
    dbx=get_connect(request)
    try:
        path = request.GET['fld']
    except:
        path = base_url
    
    lst = dbx.files_list_folder(path)
    books={}
    folders={}
    
    for i in lst._entries_value:
        path_url = i.path_lower
        if isinstance(i, dropbox.files.FileMetadata):
            books[beautify(i._name_value)]=path_url
        else:
            folders[beautify(i._name_value)]=path_url
    return render(request, template_name, {'books': sorted(books.items()), 'folders': sorted(folders.items())})

def opds(request):
    template_name = 'libviadrb/opds.xml'
    dbx=get_connect(request)
    try:
        path = request.GET['fld']
    except:
        path = base_url
        
    lst = dbx.files_list_folder(path)
    books={}
    folders={}
    
    for i in lst._entries_value:
        path_url = i.path_lower
        if isinstance(i, dropbox.files.FileMetadata):
            books[i._name_value]=path_url
        else:
            folders[i._name_value]=path_url
    
    return render(request, template_name, {'books': sorted(books.items()), 'folders': sorted(folders.items())})

def opds_get_book(request):
    template_name = 'libviadrb/opds.xml'
    dbx = get_connect(request)
    if request.method == 'GET' and 'book' in request.GET:
        path_from_url = request.GET['book']
        if path_from_url:
            dim = path_from_url[(path_from_url.rfind('.')):]
            name = beautify(path_from_url)
            link = dbx.files_get_temporary_link(path_from_url).link
    return render(request, template_name, {'link':link, 'path':path_from_url, 'name':name, 'dim':dim})
    
    
    #return HttpResponse(link, content_type='text/plain; charset=utf-8')
    
    


#return HttpResponse(settings.BASE_DIR, content_type='text/plain; charset=utf-8')

        
# return HttpResponse(data, content_type='text/plain; charset=utf-8')
#context = {'name':data.keys(), 'ids':data.values()}
#return render(request, template_name, {'data': sorted(data.items())})


#HttpResponse(dl, content_type='text/plain; charset=utf-8')
# Create your views here.
