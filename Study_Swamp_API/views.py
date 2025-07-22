from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import *


class AssignOnCreateMixin:
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


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


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class MeetingViewSet(viewsets.ModelViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer


class AttendeeViewSet(viewsets.ModelViewSet):
    queryset = Attendee.objects.all()
    serializer_class = AttendeeSerializer


class AwardViewSet(viewsets.ModelViewSet):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer


class MeetingCommentViewSet(viewsets.ModelViewSet):
    queryset = MeetingComment.objects.all()
    serializer_class = MeetingCommentSerializer


class GroupCommentViewSet(AssignOnCreateMixin, viewsets.ModelViewSet):
    queryset = GroupComment.objects.all()
    serializer_class = GroupCommentSerializer
