from django.db import models

class DataStore(models.Model):
    name = models.CharField(max_length=100)
    fatherName=models.CharField(max_length=100)
    age = models.IntegerField()
    caste= models.CharField(max_length=100)
    DOB = models.DateField()
    adharaNo = models.IntegerField()
   
    rollno10th = models.IntegerField()
    Marks10th = models.IntegerField()

    rollno12th = models.IntegerField()
    Marks12th = models.IntegerField()

    

    gateScore = models.IntegerField()
    gateRollNo = models.IntegerField()
    gateRank = models.IntegerField()

    graduationSGPA = models.IntegerField()
    graduationYear= models.IntegerField()
    graduationCourse= models.CharField(max_length=100)
    university= models.CharField(max_length=100)
    institute= models.CharField(max_length=100)


    doc10th=models.FileField(upload_to="10th")
    doc12th=models.FileField(upload_to="12th")
    docGate=models.FileField(upload_to="gate")
    docGraduation = models.FileField(upload_to="graduation")
    docDocile=models.FileField(upload_to="docile")
    docCasteCertificate= models.FileField(upload_to="castecertificate")




# Create your models here.
