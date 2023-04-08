from rest_framework.permissions import BasePermission, SAFE_METHODS


class OwnerCanChange(BasePermission):
    """
    Проверка прав пользователя на удаление объекта.
    Объект может быть удален только создателем.
    """

    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in SAFE_METHODS
            or (request.user.is_authenticated and request.user == obj.user)
        )
