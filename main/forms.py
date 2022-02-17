from django import forms
import datetime

class DateInput(forms.DateInput):
    input_type = 'date'

class TaskForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    date = forms.DateTimeField(label='Date', widget=DateInput(), initial=datetime.datetime.now())
    description = forms.CharField(label='Description', widget=forms.Textarea, max_length=200)
    complete = forms.BooleanField(label='Complete', required=False)