from django import forms
from django_filters.widgets import SuffixedMultiWidget


class CustomTextField(forms.TextInput):
    def __init__(self, attrs=None):
        default_attrs = {'class': 'form-control', 'type': 'text'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)


class CustomNumberField(forms.TextInput):
    def __init__(self, attrs=None):
        default_attrs = {'class': 'form-control', 'type': 'number', 'min': 1}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)


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
