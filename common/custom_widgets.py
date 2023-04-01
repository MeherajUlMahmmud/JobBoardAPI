from django import forms
from django_filters.widgets import SuffixedMultiWidget


class CustomDateRangeFilterWidget(SuffixedMultiWidget):
    template_name = 'django_filters/widgets/multiwidget.html'
    suffixes = ['0', '1']
    attrs = {'type': 'date', 'class': 'form-control'}

    def __init__(self, attrs=attrs):
        widgets = (forms.TextInput, forms.TextInput)
        super().__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.start, value.stop]
        return [None, None]
