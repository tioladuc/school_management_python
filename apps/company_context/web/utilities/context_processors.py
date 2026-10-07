# from url_route_name import UrlRouteName

from apps.company_context.web.utilities.url_route_name import UrlRouteName


def url_routes(request):
    return {
        'UrlRouteName': UrlRouteName
    }
    