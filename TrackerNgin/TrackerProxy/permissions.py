from rest_framework.permissions import BasePermission
from TrackerNgin.TrackerProxy import RedisConnect


class LoggedIn(BasePermission):
    def has_permission(self, request, view):
        if request.headers['Id'] and request.headers['Token']:
            result=RedisConnect.TokenAuth(request.headers['Id'],request.headers['Token'])
            return result
        else:
            return False

