def can_create_school(company, contract):
    return company.is_active and contract is not None and contract.is_active

def can_create_staff(company):
    return company.is_active
