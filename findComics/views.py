from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Comic


def main(request):
    return render(request, 'findComics/main.html')


def index(request):
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')
    search_kind = request.GET.get('search')
    comic_list = Comic.objects.order_by('-id')
    if kw:
        comic_list = comic_list.filter(
            Q(title__icontains=kw) |
            Q(author__icontains=kw)
            # Q(publisher__icontains=kw) |
            # Q(bookcase__icontains=kw)
        ).distinct()

    paginator = Paginator(comic_list, 10)
    page_obj = paginator.get_page(page)
    context = {'comic_list' : page_obj, 'page' : page, 'kw' : kw}
    return render(request, 'findComics/comic_list.html', context)


def details(request, comic_id):
    comic = get_object_or_404(Comic, pk=comic_id)
    context = {'comic' : comic}
    return render(request, 'findComics/comic_details.html', context)

