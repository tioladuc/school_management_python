
from dataclasses import dataclass

from django.views import View
from apps.company_context.web import views
from apps.company_context.web.views.administration.academic_year_views import AcademicYearView
from apps.company_context.web.views.company_views import CompanyListView
from apps.company_context.web.views.school_views import SchoolListView


@dataclass(frozen=True)
class AdministrationUtility:
    menuGroupCode: str
    menuGroupName: str
    menuTitleCode: str
    menuTitleName: str
    groupProfiles: list
    containerView: View
    isCurrentGroup: bool = False
    isCurrentMenu: bool = False

@dataclass(frozen=True)
class AdministrationGroupUtility:
    menuGroupCode: str
    menuGroupName: str

def getBasicAdministrationUtilities() -> list[AdministrationUtility]:
    examCode = "exa"
    examTitle = "Exam Admin"
    subjectCode = "clasub"
    subjectTitle = "Class + Subject Admin"
    financeCode = "finan"
    financeTitle = "Finance Admin"
    instalmentCode = "install"
    instalmentTitle = "Installment Admin"
    paymentCode = "paym"
    paymentTitle = "Payment Admin"
    return [
        #Exam Administration
            AdministrationUtility(
                menuGroupCode=examCode,
                menuGroupName=examTitle,
                menuTitleCode="seq",
                menuTitleName="Sequence Management",
                groupProfiles=["ADMIN", "MANAGER"],
                containerView=SchoolListView,  # Replace with your actual view class
            ),
            AdministrationUtility(
                menuGroupCode=examCode,
                menuGroupName=examTitle,
                menuTitleCode="term",
                menuTitleName="Term Management",
                groupProfiles=["ADMIN", "MANAGER"],
                containerView=SchoolListView,  # Replace with your actual view class
            ),
            AdministrationUtility(
                menuGroupCode=examCode,
                menuGroupName=examTitle,
                menuTitleCode="year",
                menuTitleName="Year Academic Management",
                groupProfiles=["ADMIN", "MANAGER"],
                containerView=AcademicYearView,  # Replace with your actual view class
            ),
        #Class + Subject Administration
            AdministrationUtility(
                menuGroupCode=subjectCode,
                menuGroupName=subjectTitle,
                menuTitleCode="classgrp",
                menuTitleName="Class Group",
                groupProfiles=["ADMIN", "MANAGER"],
                containerView=CompanyListView,  # Replace with your actual view class
            ),
            AdministrationUtility(
                menuGroupCode=subjectCode,
                menuGroupName=subjectTitle,
                menuTitleCode="classroom",
                menuTitleName="Class Room",
                groupProfiles=["ADMIN", "MANAGER"],
                containerView=CompanyListView,  # Replace with your actual view class
            ),
            AdministrationUtility(
                menuGroupCode=subjectCode,
                menuGroupName=subjectTitle,
                menuTitleCode="subgrp",
                menuTitleName="Subject Group",
                groupProfiles=["ADMIN", "MANAGER"],
                containerView=CompanyListView,  # Replace with your actual view class
            ),
            AdministrationUtility(
                menuGroupCode=subjectCode,
                menuGroupName=subjectTitle,
                menuTitleCode="subj",
                menuTitleName="Subject",
                groupProfiles=["ADMIN", "MANAGER"],
                containerView=CompanyListView,  # Replace with your actual view class
            ),
        #Finance Administration
            AdministrationUtility(
                menuGroupCode=financeCode,
                menuGroupName=financeTitle,
                menuTitleCode="fincat",
                menuTitleName="Finance Category",
                groupProfiles=["ADMIN", "MANAGER"],
                containerView=CompanyListView,  # Replace with your actual view class
            ),
            AdministrationUtility(
                menuGroupCode=financeCode,
                menuGroupName=financeTitle,
                menuTitleCode="finsubcat",
                menuTitleName="Fiance SubCategory",
                groupProfiles=["ADMIN", "MANAGER"],
                containerView=CompanyListView,  # Replace with your actual view class
            ),
        #Installment Administration
            AdministrationUtility(
                menuGroupCode=instalmentCode,
                menuGroupName=instalmentTitle,
                menuTitleCode="instal",
                menuTitleName="Installment",
                groupProfiles=["ADMIN", "MANAGER"],
                containerView=CompanyListView,  # Replace with your actual view class
            ),
            AdministrationUtility(
                menuGroupCode=instalmentCode,
                menuGroupName=instalmentTitle,
                menuTitleCode="instalbase",
                menuTitleName="Installment Base",
                groupProfiles=["ADMIN", "MANAGER"],
                containerView=CompanyListView,  # Replace with your actual view class
            ),
        #Payment Administration
            AdministrationUtility(
                menuGroupCode=paymentCode,
                menuGroupName=paymentTitle,
                menuTitleCode="paycat",
                menuTitleName="Payment Category",
                groupProfiles=["ADMIN", "MANAGER"],
                containerView=CompanyListView,  # Replace with your actual view class
            ),
            AdministrationUtility(
                menuGroupCode=paymentCode,
                menuGroupName=paymentTitle,
                menuTitleCode="payrecuritem",
                menuTitleName="Pay Recursive Item",
                groupProfiles=["ADMIN", "MANAGER"],
                containerView=CompanyListView,  # Replace with your actual view class
            ),
            AdministrationUtility(
                menuGroupCode=paymentCode,
                menuGroupName=paymentTitle,
                menuTitleCode="paystaticitem",
                menuTitleName="Pay Static Item",
                groupProfiles=["ADMIN", "MANAGER"],
                containerView=CompanyListView,  # Replace with your actual view class
            ),
        ]
    
def getAdministrationUtilityForUrl(request = None)-> list[AdministrationUtility]:
    data = getBasicAdministrationUtilities()
    return data

def getAdministrationGroupUtilityForMenu(request = None)-> list[dict]:
    data = getAdministrationUtilityForUrl(request)
    
    group_data = {}
    for item in data:
        if item.menuGroupCode not in group_data:
            group_data[item.menuGroupCode] = {
                "menuGroupCode": item.menuGroupCode,
                "menuGroupName": item.menuGroupName,
                "isCurrentGroup": ("/"+item.menuGroupCode+"/") in request.path,
                "menuTitles": []
            }
        group_data[item.menuGroupCode]["menuTitles"].append({
            "menuTitleCode": item.menuTitleCode,
            "menuTitleName": item.menuTitleName,
            "isCurrentMenu": ("/"+item.menuGroupCode+"/"+ item.menuTitleCode +"/") in request.path,
            "groupProfiles": item.groupProfiles,
            "containerView": item.containerView
        })
    return list(group_data.values())

def print_request(request):
    print("\n========== DJANGO REQUEST ATTRIBUTES ==========")

    for attr in dir(request):
        if attr.startswith("__"):
            continue

        try:
            value = getattr(request, attr)

            if not callable(value):
                print(f"{attr} = {value}")

        except Exception as e:
            print(f"{attr} = <Error: {e}>")

    print("========== END REQUEST ==========\n")