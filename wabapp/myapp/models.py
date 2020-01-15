from django.db import models

# Create your models here.
class PrimeMinister(models.Model):
    #Id 
    pid = models.AutoField(primary_key=True)
    # ชื่อ(name)
    name = models.CharField(max_length=500)
    #วันเดือนปีเกิด(dob)
    dob = models.DateField()
    #รูป url(imageurl)
    imgurl = models.CharField(max_length=500,default='')
    #วันที่รับตำแห่ง(startdate)
    startdate = models.DateField()
    #วันที่พ้นตำแหน่ง(enddate)
    enddate = models.DateField()
    #พรรค(party)
    party = models.CharField(max_length=500,default='')
    #

    def __str__(self):
        return f'{self.name} จากพรรค{self.party}'