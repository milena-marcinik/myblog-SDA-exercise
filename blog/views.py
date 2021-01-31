import datetime
import calendar

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
from django.urls import reverse

from blog.models import Entry, Category


def get_calendar(year, month):
    last_day = calendar.monthrange(year, month)[1]  # zwraca tupla ktory podaje pierwszy dzien miesiaca i ostatni
    start = datetime.date(year, month, 1)  # bo chce wiedziec jakim dnim tygodnia jst pierwszy dzien
    start_week_day = start.isoweekday()  # nr dnia tygodnia liczac od 1
    tmp = last_day + start_week_day - 1  # przesuwam sie o tyl ile dni ile na poczatku brakowalo
    weeks, rest = divmod(tmp, 7)  # rest to reszta z dzielenia wszystkich dni przez 7
    data = []

    day = 1  # ktory dzien miesiaca aktualnie rozwazam
    idx = 1

    for _ in range(weeks):
        tmp = []
        for _ in range(1, 8):
            if idx < start_week_day:
                tmp.append(None)
            else:
                tmp.append(day)
                day = day + 1
            idx = idx + 1
        data.append(tmp)

    if rest:
        tmp = []
        for _ in range(1, 8):
            if day <= last_day:
                tmp.append(day)
                day = day + 1
            else:
                tmp.append(None)
        data.append(tmp)

    return data


def main_page(request):
    actual = datetime.date.today()
    data = get_calendar(actual.year, actual.month)
    ctx = {'data': data}
    return render(request=request, template_name="blog/main_page.html", context=ctx)


def send_email(request):
    print(request.GET)
    print("WYSYLAM MAILA")
    return redirect(reverse('blog_main_page'))


def all_entries(request):
    data = Entry.objects.all()
    ctx = {'data': data}
    return render(request=request, template_name="blog/all_entries.html", context=ctx)


def show_entry(request, entry_id):
    try:
        entry = Entry.objects.get(id=entry_id)
    except ObjectDoesNotExist:
        raise Http404
    ctx = {'object': entry}
    return render(request=request, template_name="blog/entry.html", context=ctx)


def niedziela(request):
    entries = Entry.objects.all().order_by('-publication_datetime')[:3]
    categories = Category.objects.all().order_by('name')
    ctx = {'entries': entries, 'categories': categories}
    return render(request=request, template_name="blog/niedziela.html", context=ctx)


def entry_detail(request, entry_id):
    try:
        entry = Entry.objects.get(id=entry_id)
    except ObjectDoesNotExist:
        return Http404
    return render(request=request, template_name='blog/entry_detail.html', context={'object': entry})


def category_detail(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except ObjectDoesNotExist:
        return Http404
    return render(request=request, template_name='blog/category_detail.html', context={'object': category})
