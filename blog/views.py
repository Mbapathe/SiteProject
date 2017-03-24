from django.shortcuts import render, render_to_response
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def projects(request):
    return render(request, 'blog/projects.html', {})

def me(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	posts_list = Post.objects.all().order_by('-published_date')
	paginator = Paginator(posts_list, 5)
	page = request.GET.get('page')
	
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
		
	return render(request, 'blog/me.html', {'posts':posts})

def blog(request):
	posts_list = Post.objects.all().order_by('-published_date')
	paginator = Paginator(posts_list, 5)
	page = request.GET.get('page')
	
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	
	return render_to_response('blog/blog.html', {'posts':posts})
    #return render(request, 'blog/blog.html', {'posts':posts})

def post_detail(request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'blog/post_detail.html', {'post': post})
		
