from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('user', views.UserViewSet)
router.register('location', views.LocationViewSet)
router.register('group', views.GroupViewSet)
router.register('member', views.MemberViewSet)
router.register('meeting', views.MeetingViewSet)
router.register('attendee', views.AttendeeViewSet)
router.register('badge', views.BadgeViewSet)
router.register('award', views.AwardViewSet)
router.register('meeting_comment', views.MeetingCommentViewSet)
router.register('group_comment', views.GroupCommentViewSet)

urlpatterns = [
	path('api/v1/', include(router.urls)),
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]