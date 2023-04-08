from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    """
    Проверка прав пользователя на удаление объекта.
    Объект может быть удален только создателем.
    Для всех пользователей разрешен доступ на чтение.
    """

    def has_object_permission(self, request, view, obj):
        return bool(request.method in SAFE_METHODS or obj.user == request.user)
