from django.urls import path

from apps.app_acl import views

urlpatterns = [
    path('logs/', views.TestAclList.as_view(), name='logs'),
    path('api/rule/<str:aclname>/', views.AclApiView.as_view(), name='api-acl-get'),
    path('api/rule/<str:aclname>', views.AclApiView.as_view(), name='api-acl-get'),
    path('api/adgroups/', views.AdgroupApiView.as_view(), name='api-adgroup-get'),
    path('api/adgroups', views.AdgroupApiView.as_view(), name='api-adgroup-get'),

    path('', views.AclIndexView.as_view(), name='acl-index'),

    path('adgroup/', views.AdgroupnameView.as_view(), name='adgroup'),
    path('add-adgroup/', views.AdgroupnameCreateView.as_view(), name='adgroup-add'),

    path('acl-rule/', views.AclruleView.as_view(), name='acl-rule'),

    path('acl-rule/<int:pk>', views.AclruleUpdateView.as_view(), name='acl-rule-update'),
    path('add-acl-rule/', views.AclruleCreateView.as_view(), name='acl-rule-add'),

]