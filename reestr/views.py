# -*- coding: utf-8 -*-
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Album
from django.http import HttpResponse
import xlwt


class IndexView(generic .ListView):
    template_name = 'reestr/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic .DetailView):
    model = Album
    template_name = 'reestr/detail.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['first_name', 'middle_name', 'last_name', 'date_of_birht', 'place_of_birth',
              'address', 'street', 'house', 'date_of_entry', 'condition',
              'type_doc', 'seria_doc', 'number_doc', 'date_doc', 'subject_doc', 'whence_came', 'document']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['first_name', 'middle_name', 'last_name', 'date_of_birht', 'place_of_birth',
              'address', 'street', 'house', 'date_of_entry', 'condition',
              'type_doc', 'seria_doc', 'number_doc', 'date_doc', 'subject_doc', 'whence_came', 'document']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('reestr:index')

class IrpinView(generic .TemplateView):
    template_name = 'reestr/irpin.html'
    model = Album

def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="reestr.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Reestr')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Прізвище', 'Ім’я', 'По батькові', 'Дата народження', 'Місце народження', 'Адреса', 'Вулиця',
               'Будинок', 'Дата реєстрації', 'Дія',
               'Тип документа', 'Серія', 'Номер документа', 'Дата видачі', 'Суб’єкт, що видав', 'Звідки прибув' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Album.objects.all().values_list('first_name', 'middle_name', 'last_name', 'date_of_birht',
                                           'place_of_birth', 'address', 'street', 'house', 'date_of_entry', 'condition',
                                           'type_doc', 'seria_doc', 'number_doc', 'date_doc', 'subject_doc', 'whence_came',)
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response




