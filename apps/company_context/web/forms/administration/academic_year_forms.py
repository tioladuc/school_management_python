from django import forms


class AcademicYearForm(forms.Form):

    year = forms.IntegerField(
        label="Academic Year",
        min_value=2000,
        max_value=2100,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "2026",
            }
        ),
    )

    start_date = forms.DateField(
        label="Start Date",
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "class": "form-control",
            }
        ),
    )

    end_date = forms.DateField(
        label="End Date",
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "class": "form-control",
            }
        ),
    )

    status = forms.ChoiceField(
        label="Status",
        choices=[
            ("ACTIVE", "Active"),
            ("INACTIVE", "Inactive"),
        ],
        widget=forms.Select(
            attrs={
                "class": "form-select",
            }
        ),
    )

    def clean(self):
        cleaned_data = super().clean()

        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        if start_date and end_date and start_date >= end_date:
            self.add_error(
                "end_date",
                "The end date must be after the start date.",
            )

        return cleaned_data