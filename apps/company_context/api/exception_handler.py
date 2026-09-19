from rest_framework.views import exception_handler as drf_exception_handler
from ...domain.exceptions import DomainError
from rest_framework.response import Response

def exception_handler(exc, context):
    if isinstance(exc, DomainError): return Response({'detail':str(exc)},status=400)
    return drf_exception_handler(exc,context)
