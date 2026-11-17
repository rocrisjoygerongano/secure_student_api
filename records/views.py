
from rest_framework.permissions import BasePermission, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from .models import StudentRecord
from .serializers import StudentRecordSerializer


class IsAdminOrFaculty(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and (
                request.user.is_staff
                or request.user.groups.filter(name='faculty_user').exists()
            )
        )


class IsAuthorizedRecordViewer(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        return (
            user.is_authenticated
            and (
                user.is_staff
                or user.groups.filter(
                    name__in=['faculty_user', 'student_user']
                ).exists()
            )
        )


class StudentRecordViewSet(ModelViewSet):
    queryset = StudentRecord.objects.all()
    serializer_class = StudentRecordSerializer

    def get_permissions(self):
        if self.action in ['create', 'destroy']:
            permission_classes = [IsAdminUser]

        elif self.action in ['update', 'partial_update']:
            permission_classes = [IsAdminOrFaculty]

        else:
            permission_classes = [IsAuthorizedRecordViewer]

        return [permission() for permission in permission_classes]

    def get_queryset(self):
        user = self.request.user

        if user.is_staff or user.groups.filter(name='faculty_user').exists():
            return StudentRecord.objects.all()

        if user.groups.filter(name='student_user').exists():
            return StudentRecord.objects.filter(owner=user)

        return StudentRecord.objects.none()
