from django.core.paginator import Paginator

from yatube.settings import POST_PAGES


def paginator(request, posts):
    paginator = Paginator(posts, POST_PAGES)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj
