from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet, basename='users')
router.register('locations', views.LocationViewSet)
router.register('groups', views.GroupViewSet)
router.register('members', views.MemberViewSet)
router.register('meetings', views.MeetingViewSet)
router.register('attendees', views.AttendeeViewSet)
router.register('badges', views.BadgeViewSet)
router.register('awards', views.AwardViewSet)
router.register('meeting_comments', views.MeetingCommentViewSet)
router.register('group_comments', views.GroupCommentViewSet)

urlpatterns = [
	path('api/v1/', include(router.urls)),
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]