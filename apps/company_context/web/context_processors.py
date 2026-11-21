from apps.company_context.web.utilities.admin_utility import (
    getAdministrationUtilityForUrl,
    getAdministrationGroupUtilityForMenu
)


def administration_menu(request):
    return {
        "administration_menu": getAdministrationUtilityForUrl(request),
        "administration_menu_group": getAdministrationGroupUtilityForMenu(request)
    }