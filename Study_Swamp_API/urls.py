from django.urls import include, path
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from . import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet, basename='users')
router.register('locations', views.LocationViewSet)
router.register('groups', views.GroupViewSet)
router.register('members', views.MemberViewSet)
router.register('meetings', views.MeetingViewSet)
router.register('attendees', views.AttendeeViewSet)
router.register('awards', views.AwardViewSet)
router.register('meeting_comments', views.MeetingCommentViewSet)
router.register('group_comments', views.GroupCommentViewSet)

urlpatterns = [
	# DRF API endpoints
	path('api/v1/', include(router.urls)),
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

	# Schema view (OpenAPI spec in JSON or YAML)
	path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

	# Swagger UI (uses schema endpoint)
	path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

	# ReDoc UI (also uses schema endpoint)
	path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]