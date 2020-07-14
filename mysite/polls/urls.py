from polls.views import *

urlpatterns = [

	path('student/',StudentAPIView.as_views(), name='student')


]