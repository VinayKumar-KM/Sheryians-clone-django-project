from django.db import models

# Create your models here.

class Course(models.Model):
    cou_name=models.CharField()
    batch_type=models.CharField()
    language=models.CharField()
    dis_type=models.CharField()
    actual_price=models.IntegerField()
    offer=models.IntegerField()
    schedule_type=models.CharField()
    total_content=models.IntegerField()
    image=models.ImageField(upload_to='image/',null=True)

    @property
    def final_price(self):
        if self.offer:
            dis=(self.actual_price*self.offer)//100
            return self.actual_price-dis
        return self.actual_price