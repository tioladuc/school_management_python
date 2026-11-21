
from dataclasses import dataclass

from django.views import View
from apps.company_context.web import views
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
    return [
            AdministrationUtility(
                menuGroupCode="exa",
                menuGroupName="Exam Administration",
                menuTitleCode="seq",
                menuTitleName="Sequence Management",
                groupProfiles=["ADMIN", "MANAGER"],
                containerView=SchoolListView,  # Replace with your actual view class
            ),
            AdministrationUtility(
                menuGroupCode="exa",
                menuGroupName="Exam Administration",
                menuTitleCode="term",
                menuTitleName="Term Management",
                groupProfiles=["ADMIN", "MANAGER"],
                containerView=SchoolListView,  # Replace with your actual view class
            ),
            AdministrationUtility(
                menuGroupCode="exa",
                menuGroupName="Exam Administration",
                menuTitleCode="year",
                menuTitleName="Year Academic Management",
                groupProfiles=["ADMIN", "MANAGER"],
                containerView=CompanyListView,  # Replace with your actual view class
            ),        
        ]
    
def getAdministrationUtilityForUrl(request = None)-> list[AdministrationUtility]:
    data = getBasicAdministrationUtilities()
    return data

def getAdministrationGroupUtilityForMenu(request = None)-> list[dict]:
    data = getAdministrationUtilityForUrl(request)
    #print_request(request)
    print(request.path, " WWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
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