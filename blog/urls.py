from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^$',views.home,name='home'),
    url(r'^techblog/$',views.PostListView.as_view(),name='post_list'),
    url(r'^about/$',views.AboutView.as_view(),name='about'),
    url(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^post/new/$', views.CreatePostView.as_view(), name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(), name='post_edit'),
    url(r'^drafts/$', views.DraftListView.as_view(), name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.PostDeleteView.as_view(), name='post_remove'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^team/$', views.team, name='team'),
    url(r'^iicheteam/$', views.iicheteam, name='iicheteam'),
    url(r'^cheateam17/$', views.cheateam17, name='cheateam17'),
    url(r'^iicheteam17/$', views.iicheteam17, name='iicheteam17'),
    url(r'^Chemical/$', views.Chemical, name='Chemical'),
    url(r'^aboutchea/$', views.aboutchea, name='aboutchea'),
    url(r'^news/$', views.news, name='news'),
    url(r'^intern/$', views.intern, name='intern'),
    url(r'^quote/$', views.quote, name='quote'),
    url(r'^placement/$', views.placement, name='placement'),
    url(r'^philia/$', views.philia, name='philia'),
    url(r'^quiz/$', views.quiz, name='quiz'),
    url(r'^piction/$', views.piction, name='piction'),
    url(r'^sports/$', views.sports, name='sports'),
    url(r'^photo/$', views.photo, name='photo'),
    url(r'^itc/$', views.itc, name='itc'),
]
