from django.contrib import admin

# Register your models here.
from blog.models import Entry, Category, Tag


@admin.register(Entry)  # wtedy nie rejestruje juz tego jak tam na dole
class EntryAdmin(admin.ModelAdmin):  # klasa bedzie decydowala o tym jak w adminie bedzie ywgladac moja klasa
    # konfiguracja wyswietania listy
    list_display = ('title', 'publication_datetime', 'category')  # jakie pola maja byc wyswietlane
    ordering = ('-id',)
    search_fields = ('title', 'category__name')
    list_filter = ('category', 'publication_datetime')
    # konfiguracja edycji/tworzenia
    # fields = (('title', 'category'),)  # jakie pola w edycji chce pokazac
    fieldsets = (("Naglowek 1", {'description': "To jest jakis opis do naglowka 1", "fields": ('title', 'category')}),
                 ("Naglowek 2", {'description': "To jest jakis opis do naglowka 2", "fields": ('tags',)}),

    )


# admin.site.register(Entry, EntryAdmin)
admin.site.register(Category)
admin.site.register(Tag)
