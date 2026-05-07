from rest_framework.permissions import BasePermission, IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from .models import StudentRecord
from .serializers import StudentRecordSerializer

class IsAdminOrFaculty(BasePermission):
    def has_permission(self, request, view):
        # Checks if user is in 'Admin' or 'Faculty' group
        return request.user.groups.filter(name__in=['Admin', 'Faculty']).exists()

class StudentRecordViewSet(ModelViewSet):
    queryset = StudentRecord.objects.all()
    serializer_class = StudentRecordSerializer

    def get_permissions(self):
        if self.action in ['create', 'destroy']:
            permission_classes = [IsAdminUser] # Admin only
        elif self.action in ['update', 'partial_update']:
            permission_classes = [IsAdminOrFaculty] # Admin or Faculty
        else:
            permission_classes = [IsAuthenticated] # Anyone logged in
        return [permission() for permission in permission_classes]
    
    def get_queryset(self):
        # Part A requirement: Students only see their own record
        user = self.request.user
        if user.groups.filter(name='Student').exists():
            return StudentRecord.objects.filter(owner=user)
        return StudentRecord.objects.all()