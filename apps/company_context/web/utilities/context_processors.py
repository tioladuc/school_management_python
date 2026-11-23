# from url_route_name import UrlRouteName

from apps.company_context.web.utilities.url_route_name import UrlRouteName
from apps.company_context.web.utilities.admin_utility import (
    getAdministrationUtilityForUrl,
    getAdministrationGroupUtilityForMenu
)



def url_routes(request):
    return {
        'UrlRouteName': UrlRouteName
    }

def administration_menu(request):
    return {
        "administration_menu": getAdministrationUtilityForUrl(request),
        "administration_menu_group": getAdministrationGroupUtilityForMenu(request)
    }