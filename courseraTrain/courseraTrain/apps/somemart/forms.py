from django import forms


class ItemForm(forms.Form):
    title = forms.CharField(label='title', required=True, min_length=1, max_length=64)
    description = forms.CharField(label='description', required=True, min_length=1, max_length=1024)
    price = forms.IntegerField(min_value=1, max_value=1000000)


class ReviewForm(forms.Form):
    text = forms.CharField(label='text', required=True, min_length=1, max_length=1024)
    grade = forms.IntegerField(min_value=1, max_value=10, required=True)
