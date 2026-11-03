
from django import forms


class SchoolForm(forms.Form):

    STATUS_CHOICES = [
        ("ACTIVE", "Active"),
        ("SUSPENDED", "Suspended"),
        ("TERMINATED", "Terminated"),
    ]

    code = forms.CharField(
        max_length=50,
        label="School Code",
    )

    name_fr = forms.CharField(
        max_length=250,
        label="School Name (French)",
    )

    name_en = forms.CharField(
        max_length=250,
        label="School Name (English)",
    )

    phone = forms.CharField(
        max_length=250,
        required=False,
        label="Phone",
    )

    email = forms.EmailField(
        max_length=250,
        required=False,
        label="Email",
    )

    address = forms.CharField(
        max_length=250,
        required=False,
        widget=forms.Textarea(attrs={"rows": 3}),
        label="Address",
    )

    autorization = forms.CharField(
        max_length=250,
        required=False,
        label="Authorization",
    )

    founder = forms.CharField(
        max_length=250,
        required=False,
        label="Founder",
    )

    principal = forms.CharField(
        max_length=250,
        required=False,
        label="Principal",
    )

    city = forms.CharField(
        max_length=150,
        label="City",
    )

    country = forms.CharField(
        max_length=100,
        label="Country",
    )

    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
        initial="ACTIVE",
        label="Status",
    )
