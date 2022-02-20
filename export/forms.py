from django import forms

class searchForm(forms.Form):
    '''
    create form
    '''
    start_date = forms.DateTimeField(required=True, widget=forms.widgets.DateInput(attrs={'type': 'datetime-local'}))
    end_date = forms.DateTimeField(required=True, widget=forms.widgets.DateInput(attrs={'type': 'datetime-local'}))

    def clean(self):
        '''
        check end_date not grater than of end_date
        '''
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        if end_date < start_date:
            raise forms.ValidationError("End date should be greater than start date.")