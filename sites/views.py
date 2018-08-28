from django.views.generic import ListView, DetailView
from .models import Site
from django.db.models import Sum


class SiteListView(ListView):
    model = Site
    context_object_name = 'sites'


class SiteDetailView(DetailView):
    model = Site
    context_object_name = 'site'


class SummaryView(ListView):
    template_name = 'sites/summary_list.html'
    context_object_name = 'sites'

    def get_queryset(self):
        return Site.objects.all().annotate(sum_a=Sum('sitedetail__a'),sum_b=Sum('sitedetail__b'))


class SummaryAverageView(ListView):
    template_name = 'sites/summary_average_list.html'
    context_object_name = 'sites'

    def get_queryset(self):
        return Site.average_objects.averages_join()