from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register('group', views.GroupViewSet)
router.register('member', views.MemberViewSet)
router.register('meeting', views.MeetingViewSet)
router.register('attendee', views.AttendeeViewSet)

urlpatterns = [
	path('api/v1/', include(router.urls)),
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]