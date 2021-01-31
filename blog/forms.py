from django import forms
from django.core.exceptions import ValidationError


# def test_walidatora(value):
#     print("walidujemy sobie")
#     print(value)
#     raise ValidationError("nie tak szybko!")
from django.forms import ModelForm


class EntryForm(ModelForm):
    

class ContactForm(forms.Form):
    required_css_class = "required"
    # initial="Podaj swoje imie"
    yourname = forms.CharField(max_length=20, min_length=3, label="Twoje imie",
                               widget=forms.TextInput(attrs={'placeholder': 'wpisz imie'}))
    email = forms.EmailField(label='Adres email')
    subject = forms.CharField(max_length=30, label="Temat zapytania")  # validators=[test_walidatora, ]
    message = forms.CharField(widget=forms.Textarea, label="Tresc wiadomosci")
    age = forms.IntegerField(label="Twoj wiek", required=False)

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18:
            raise ValidationError("Nie jestes pelnoletni")

    # def clean(self):
    #     self.cleaned_data['age'] = 100
    #     raise ValidationError("Blad z cleana")


class SearchForm(forms.Form):
    search = forms.CharField(label="Szukaj", required=False)


class CategoryForm(forms.Form):
    search = forms.CharField(label="Nazwa kategorii")



