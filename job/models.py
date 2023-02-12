from django.db import models
from django.utils.text import slugify

# choise
JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

# Save Image 
def image_upload(instance,filename):
    imagename , extension = filename.split(".")
    return "jobs/%s.%s"%(instance.id,extension)


# Create your models here.
class Job(models.Model): #table
    title = models.CharField(max_length=100) # column
    # location
    job_type =  models.CharField(max_length=50,choices=JOB_TYPE)
    description = models.TextField(max_length=100)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experiences = models.IntegerField(default=1)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)
    
    slug = models.SlugField(blank=True, null=True)
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super(Job,self).save(*args, **kwargs)
        
        
    def __str__(self):
        return self.title
    
class Category(models.Model): # Table
    name = models.CharField(max_length=30) 
    
       
    def __str__(self):
       return self.name