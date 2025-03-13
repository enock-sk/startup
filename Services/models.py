from django.db import models

# Create your models here.
# index models here
class PortfolioItems(models.Model):
    heading = models.CharField(max_length=100)
    link_image=models.ImageField(upload_to='portfolio_ImageLink')
    description = models.TextField()
    title=models.CharField(max_length=20)
    image = models.ImageField(upload_to='Portfolio_Items/')
    created_at = models.DateTimeField(auto_now_add=True)
