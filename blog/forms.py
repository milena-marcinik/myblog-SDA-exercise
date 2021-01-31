from django import forms


class ContactForm(forms.Form):
    required_css_class = "required"
    # initial="Podaj swoje imie"
    yourname = forms.CharField(max_length=20, min_length=3, label="Twoje imie",
                               widget=forms.TextInput(attrs={'placeholder': 'wpisz imie'}))
    email = forms.EmailField(label='Adres email')
    subject = forms.CharField(max_length=30, label="Temat zapytania")
    message = forms.CharField(widget=forms.Textarea, label="Tresc wiadomosci")
    age = forms.IntegerField(label="Twoj wiek", required=False)
