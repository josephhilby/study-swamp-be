from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import *


class AssignOnCreateMixin:
    """
    Mixin to help prevent users from spoofing others.
    Bypass for superuser
    """
    def perform_create(self, serializer):
        user = self.request.user
        if not user.is_superuser:
            serializer.save(user=user)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return User.objects.all()

        return User.objects.filter(is_superuser=False)

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAuthenticated()]


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class MemberViewSet(AssignOnCreateMixin, viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer


class AttendeeViewSet(AssignOnCreateMixin, viewsets.ModelViewSet):
    queryset = Attendee.objects.all()
    serializer_class = AttendeeSerializer


class AwardViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AwardSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Award.objects.all()
        return Award.objects.filter(user=user)


class MeetingCommentViewSet(AssignOnCreateMixin, viewsets.ModelViewSet):
    queryset = MeetingComment.objects.all()
    serializer_class = MeetingCommentSerializer


class GroupCommentViewSet(AssignOnCreateMixin, viewsets.ModelViewSet):
    queryset = GroupComment.objects.all()
    serializer_class = GroupCommentSerializer
