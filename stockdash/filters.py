import django_filters
from stockdash.models import TotalReturn
from django.db import models


def get_choices(model, field):
    choices = []
    for k in model.objects.using('stockdb').values_list(field).distinct():
        choices.append((k[0], k[0]))
    return choices



class TotalReturnFilter(django_filters.FilterSet):
    sector = django_filters.ChoiceFilter(choices=get_choices(TotalReturn, 'sector'))

    industry = django_filters.ChoiceFilter(choices=get_choices(TotalReturn, 'industry'))

    symbolname=django_filters.CharFilter(label='Company Name',lookup_expr='icontains')

    marketcaplt=django_filters.NumberFilter(label='marketcap <',field_name='marketcap',lookup_expr='lt')
    marketcapgt=django_filters.NumberFilter(label='marketcap >',field_name='marketcap',lookup_expr='gt')

    return_1_daylt=django_filters.NumberFilter(label='return_1_day <',field_name='return_1_day',lookup_expr='lt')
    return_1_daygt=django_filters.NumberFilter(label='return_1_day >',field_name='return_1_day',lookup_expr='gt')

    return_7_daylt=django_filters.NumberFilter(label='return_7_day <',field_name='return_7_day',lookup_expr='lt')
    return_7_daygt=django_filters.NumberFilter(label='return_7_day >',field_name='return_7_day',lookup_expr='gt')

    return_14_daylt=django_filters.NumberFilter(label='return_14_day <',field_name='return_14_day',lookup_expr='lt')
    return_14_daygt=django_filters.NumberFilter(label='return_14_day >',field_name='return_14_day',lookup_expr='gt')

    return_30_daylt=django_filters.NumberFilter(label='return_30_day <',field_name='return_30_day',lookup_expr='lt')
    return_30_daygt=django_filters.NumberFilter(label='return_30_day >',field_name='return_30_day',lookup_expr='gt')

    marketcap_lt=django_filters.NumberFilter(label='marketcap <',field_name='marketcap',lookup_expr='lt')
    marketcap_gt=django_filters.NumberFilter(label='marketcap >',field_name='marketcap',lookup_expr='gt')

    class Meta:
        model = TotalReturn
        fields = ['sector', 'industry','symbolname']

