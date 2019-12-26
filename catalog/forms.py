import django.forms as forms


class BookForm(forms.Form):
    title = forms.CharField(max_length=30)
    publisher = forms.CharField(max_length=20, required=False)
    authors = forms.CharField(label='Author(s)')
    price = forms.IntegerField(required=False, min_value=100, max_value=10000)
