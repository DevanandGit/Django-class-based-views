from django import forms

class Class3Form(forms.Form):
    name = forms.CharField(max_length=300)
    roll_no = forms.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.name}-{self.roll_no}"