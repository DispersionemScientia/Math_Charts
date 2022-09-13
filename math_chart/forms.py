from django import forms

class ChartsForm(forms.Form):
    x = forms.FloatField(label='x:')
    y = forms.FloatField(label='y:')

class SquareForm(forms.Form):
    a = forms.FloatField(label='a:')
    b = forms.FloatField(label='b:')
    c = forms.FloatField(label='c:')

class TrigonometryForm(forms.Form):
    a = forms.FloatField(label='a:')
    b = forms.FloatField(label='b:')
    c = forms.FloatField(label='c:')
    d = forms.FloatField(label='d:')
