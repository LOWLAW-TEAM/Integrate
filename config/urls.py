from django.urls import path, include
from django.contrib import admin
from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns
from allauth.socialaccount import views as socialaccount_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from member import views as member_views
from chatbot import views as chatbot_views
from searchengine import views as se_views
from member.api_views import api_login
from member.api_views import api_register

urlpatterns = [
    
    path('', member_views.home, name='home'),

    path('register/', member_views.register, name='register'),
    path('user_admin/', member_views.user_admin, name='user_admin'),
    path('login/', member_views.user_login, name='login'),
    path('login/', member_views.CustomAuthToken.as_view(), name='custom_auth_token'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout/', member_views.user_logout, name='logout'),
    path('admin/', admin.site.urls),
    path('mypage/', member_views.mypage, name='mypage'),
    path('user-delete/', member_views.user_delete, name='user_delete'),

    path('messages/', chatbot_views.messages, name='messages'),
    path('button_law/', chatbot_views.button_law, name='button_law'),
    path('button_prec/', chatbot_views.button_prec, name='button_prec'),
    path('chatbot/', chatbot_views.chatbot, name='chatbot'),

    path('searchengine/', se_views.searchengine, name='searchengine'),
    path('search/', se_views.search, name='search'),
    #path('search_engine', se_views.search_engine, name='search_engine'),

    # api_urls 
    path('api/login/', api_login, name='api_login'),
    path('api/register/', api_register, name='api_register'),
    # path('api/token/', obtain_auth_token, name='api_token'),

    # 로그인 성공 시 홈 화면으로 리다이렉트하는 URL 패턴 추가
    path('home/', member_views.home, name='home_redirect'),
]
