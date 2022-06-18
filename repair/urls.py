<<<<<<< HEAD


from django.urls import path

from .views import *

urlpatterns = [
	path('', dashboard),
	path('enquiryForm/', enquiryForm),
	path('enquiryReceipt/', enquiryReceipt),
	path('enquiryReceiptFrameContent/',enquiryReceiptFrameContent),
	path('updateRequest/', updateRequest),
	path('updateForm/', updateForm),
	path('updateTestDetails/',updateTestDetails),
	
	# path('updateTestDetails/<int:pk>',updateTestDetails),
	path('updateRepairDetails/',updateRepairDetails),
	
	path('finalReceipt/', finalReceipt),
	path('finalReceiptFrameContent/',finalReceiptFrameContent),
	path('pendingRepairRequest/', pendingRepairRequest),
	path('pendingRepairList/', pendingRepairList),
	path('checkStatusRequest/', checkStatusRequest),
	path('checkStatusShow/', checkStatusShow),
=======


from django.urls import path

from .views import *

urlpatterns = [
	path('', dashboard),
	path('enquiryForm/', enquiryForm),
	path('enquiryReceipt/', enquiryReceipt),
	path('enquiryReceiptFrameContent/',enquiryReceiptFrameContent),
	path('updateRequest/', updateRequest),
	path('updateForm/', updateForm),
	path('updateTestDetails/',updateTestDetails),
	
	# path('updateTestDetails/<int:pk>',updateTestDetails),
	path('updateRepairDetails/',updateRepairDetails),
	
	path('finalReceipt/', finalReceipt),
	path('finalReceiptFrameContent/',finalReceiptFrameContent),
	path('pendingRepairRequest/', pendingRepairRequest),
	path('pendingRepairList/', pendingRepairList),
	path('checkStatusRequest/', checkStatusRequest),
	path('checkStatusShow/', checkStatusShow),
>>>>>>> 82835c48c97b5622541c6cb9e52efcec4ece4bb2
]