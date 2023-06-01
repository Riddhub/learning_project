from django.shortcuts import render
from django.views.generic import DetailView, ListView

from djapp.models import Theme, Category


class ThemesListView(ListView):
    model = Theme
    template_name = 'djapp/index.html'
    context_object_name = 'themes'
    extra_context = {'title': 'ThemesListView'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = 'ThemeDetailView'
        context['categories'] = Category.objects.all()
        return context


# class CategoriesListView(ListView):
#     model = Category
#     template_name = 'djapp/index.html'
#     context_object_name = 'categories'
#     extra_context = {'title': 'CategoriesListView'}


def index(request):
    context = {
        'themes': Theme.objects.all(),
        'categories': Category.objects.all(),
    }
    return render(request, template_name='djapp/index.html', context=context)


class ThemeDetailView(DetailView):
    model = Theme
    template_name = 'djapp/theme_detail.html'
    pk_url_kwarg = 'theme_id'
    context_object_name = 'theme'
    extra_context = {'title': 'ThemeDetailView'}

