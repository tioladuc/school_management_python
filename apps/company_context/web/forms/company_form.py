from django import forms


class CompanyForm(forms.Form):
    code = forms.CharField(
        max_length=50,
        label="Company Code",
    )

    name = forms.CharField(
        max_length=250,
        label="Company Name",
    )

    email = forms.EmailField(
        label="Email",
    )

    phone = forms.CharField(
        max_length=50,
        required=False,
        label="Phone",
    )

    address = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"rows": 3}),
        label="Address",
    )

    status = forms.ChoiceField(
        choices=[
            ("ACTIVE", "Active"),
            ("SUSPENDED", "Suspended"),
            ("TERMINATED", "Terminated"),
        ],
        initial="ACTIVE",
    )

    tenant_database = forms.CharField(
        max_length=150,
        required=False,
        label="Tenant Database",
    )