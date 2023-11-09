from django.urls import path
from apps.app_front import views

urlpatterns = [
    path('nas/', views.FirstDataFromSQLView.as_view(), name='get_nas'),
    path('nas/<int:pk>/', views.NasUpdateView.as_view(), name='update-nas'),
    path('add-nas/', views.NasCreateView.as_view(), name='add_nas'),

    path('radact/', views.RadactView.as_view(), name='radact'),

    path('radhuntgroup/', views.RadhuntgroupView.as_view(), name='radhuntgroup'),
    path('radhuntgroup/<int:pk>/', views.RadhuntgroupUpdateView.as_view(), name='update-radhuntgroup'),
    path('add-radhun', views.RadhuntgroupCreateView.as_view(), name='add_radhuntgroup'),

    path('radcheck/', views.RadcheckView.as_view(), name='radcheck'),
    path('add-radcheck/', views.RadcheckCreateView.as_view(), name='create-radcheck'),
    path('radcheck/<int:pk>', views.RadcheckUpdateView.as_view(), name='update-radcheck'),

    path('radreply/', views.RadreplyView.as_view(), name='radreply'),
    path('add-radreply/', views.RadreplyCreateView.as_view(), name='create-radreply'),
    path('radreply/<int:pk>', views.RadreplyUpdateView.as_view(), name='update-radreply'),

    path('radusergroup/', views.RadusergroupView.as_view(), name='radusergroup'),
    path('add-radusergroup/', views.RadusergroupCreateView.as_view(), name='add-radusergroup'),
    path('radusergroup/<int:pk>', views.RadusergroupUpdateView.as_view(), name='update-radusergroup'),

    path('radgroupcheck/', views.RadgroupcheckView.as_view(), name='radgroupcheck'),
    path('add-Radgroupcheck/', views.RadgroupcheckCreateView.as_view(), name='add-radgroupcheck'),
    path('radgroupcheck/<int:pk>', views.RadgroupcheckUpdateView.as_view(), name='update-radgroupcheck'),

    path('radgroupreply/', views.RadgroupreplyView.as_view(), name='radgroupreply'),
    path('add-radgroupreply/', views.RadgroupreplyCreateView.as_view(), name='add-radgroupreply'),
    path('radgroupreply/<int:pk>', views.RadgroupreplyUpdateView.as_view(), name='update-radgroupreply'),

    path('radpostauth/', views.RadpostauthView.as_view(), name='radpostauth'),

    path('dictionary/', views.DictionaryView.as_view(), name='dictionary')


]