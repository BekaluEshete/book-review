from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from reviews.views import root_view  # import this at the top

urlpatterns = [
    path('', root_view),  
    path('admin/', admin.site.urls),
    path('api/', include('reviews.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]