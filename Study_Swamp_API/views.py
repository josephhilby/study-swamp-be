from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from .models import (User, Location, Group, Member,
                     Meeting, Attendee, Badge,
                     Award, MeetingComment, GroupComment)
from .serializers import (UserSerializer, LocationSerializer, GroupSerializer,
                          MemberSerializer, MeetingSerializer, AttendeeSerializer,
                          BadgeSerializer, AwardSerializer, MeetingCommentSerializer,
                          GroupCommentSerializer)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return User.objects.all()

        return User.objects.filter(is_superuser=False)


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


class BadgeViewSet(viewsets.ModelViewSet):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer


class AwardViewSet(viewsets.ModelViewSet):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer


class MeetingCommentViewSet(viewsets.ModelViewSet):
    queryset = MeetingComment.objects.all()
    serializer_class = MeetingCommentSerializer


class GroupCommentViewSet(viewsets.ModelViewSet):
    queryset = GroupComment.objects.all()
    serializer_class = GroupCommentSerializer
