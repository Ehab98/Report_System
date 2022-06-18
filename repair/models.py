<<<<<<< HEAD
from django.db import models

# Create your models here.
class Enquiry(models.Model):
	PROBLEM_CATEGORY_CHOICES = (
		('HW','Hardware'),
		('SW','Software'),
	)

	STATUS_CHOICES = (
		('EN','Enquired'),
		('CH','Checked'),		# This is amazing
		('RE','Repaired'),		# Changed from Update Form when Components are added and Repair Charge is added
		('CO','Completed'),		# Changed to when Final Receipt is Generated
		('RJ','Rejected'),
	)
	Device_Type_CHOICES =(
		('TOM','Tom'),
		('PCM','Pcm'),
	)

	receiptID = models.AutoField(primary_key=True)
	enquiryDate = models.DateField()
	customerName = models.CharField(max_length = 50)
	contactNo = models.CharField(max_length = 20)
	address = models.TextField(blank=True)
	deviceType = models.CharField(max_length = 3, choices = Device_Type_CHOICES)
	serialNo = models.CharField(max_length = 50, blank=True)
	problemCategory = models.CharField(max_length = 3, choices = PROBLEM_CATEGORY_CHOICES)
	problem = models.CharField(max_length = 50)
	problemDescription = models.TextField(blank=True)
	deviceCondition = models.TextField(blank=True)
	
	status = models.CharField(max_length = 3, choices = STATUS_CHOICES ,default='EN')

	def __str__(self):
		return str(self.receiptID) + " : "  + self.status + " : "  + self.customerName 

class TestDetail(models.Model):

	Enquiry = models.ForeignKey(Enquiry, on_delete=models.CASCADE)
	actualProblem = models.CharField(max_length = 50)
	actualProblemDescription = models.TextField(blank=True)
	
	def __str__(self):
		return str(self.Enquiry.receiptID) + " : " + str(self.Enquiry.status) + " : " + self.Enquiry.customerName + " : " + self.actualProblem

class RepairDetail(models.Model):
	Enquiry = models.ForeignKey(Enquiry, on_delete=models.CASCADE)


	def __str__(self):
		return str(self.Enquiry.receiptID) + " : " + str(self.Enquiry.status) + " : " + self.Enquiry.customerName

class trialPeriod(models.Model):
	ID = models.AutoField(primary_key=True)
	counter = models.IntegerField()
=======
from django.db import models

# Create your models here.
class Enquiry(models.Model):
	PROBLEM_CATEGORY_CHOICES = (
		('HW','Hardware'),
		('SW','Software'),
	)

	STATUS_CHOICES = (
		('EN','Enquired'),
		('CH','Checked'),		# This is amazing
		('RE','Repaired'),		# Changed from Update Form when Components are added and Repair Charge is added
		('CO','Completed'),		# Changed to when Final Receipt is Generated
		('RJ','Rejected'),
	)
	Device_Type_CHOICES =(
		('TOM','Tom'),
		('PCM','Pcm'),
	)

	receiptID = models.AutoField(primary_key=True)
	enquiryDate = models.DateField()
	customerName = models.CharField(max_length = 50)
	contactNo = models.CharField(max_length = 20)
	address = models.TextField(blank=True)
	deviceType = models.CharField(max_length = 3, choices = Device_Type_CHOICES)
	serialNo = models.CharField(max_length = 50, blank=True)
	problemCategory = models.CharField(max_length = 3, choices = PROBLEM_CATEGORY_CHOICES)
	problem = models.CharField(max_length = 50)
	problemDescription = models.TextField(blank=True)
	deviceCondition = models.TextField(blank=True)
	
	status = models.CharField(max_length = 3, choices = STATUS_CHOICES ,default='EN')

	def __str__(self):
		return str(self.receiptID) + " : "  + self.status + " : "  + self.customerName 

class TestDetail(models.Model):

	Enquiry = models.ForeignKey(Enquiry, on_delete=models.CASCADE)
	actualProblem = models.CharField(max_length = 50)
	actualProblemDescription = models.TextField(blank=True)
	
	def __str__(self):
		return str(self.Enquiry.receiptID) + " : " + str(self.Enquiry.status) + " : " + self.Enquiry.customerName + " : " + self.actualProblem

class RepairDetail(models.Model):
	Enquiry = models.ForeignKey(Enquiry, on_delete=models.CASCADE)


	def __str__(self):
		return str(self.Enquiry.receiptID) + " : " + str(self.Enquiry.status) + " : " + self.Enquiry.customerName

class trialPeriod(models.Model):
	ID = models.AutoField(primary_key=True)
	counter = models.IntegerField()
>>>>>>> 82835c48c97b5622541c6cb9e52efcec4ece4bb2
	date = models.DateField()