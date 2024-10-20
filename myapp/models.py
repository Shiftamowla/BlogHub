from django.db import models
from django.contrib.auth.models import AbstractUser

class Custom_user(AbstractUser):
    USER=[
        ('viewers','Viewers'),
        ('blogger','Blogger')
    ]
    Gender=[
        ('male','Male'),
        ('female','Female'),
        ('other','Other')
    ]
    user_type=models.CharField(choices=USER,max_length=100,null=True)
    gender=models.CharField(choices=Gender,max_length=100,null=True)
    profile_picture=models.ImageField(upload_to='company_logos/', null=True)

    def  __str__(self):
        return f"{self.username}-{self.first_name}-{self.last_name}-{self.user_type}"
    
    
class viewersProfileModel(models.Model):
    
    PREFERRED_CONTENT=[
        ('articles', 'Articles'),
        ('videos', 'Videos'),
        ('podcasts', 'Both'),
    ]

    user=models.OneToOneField(Custom_user,on_delete=models.CASCADE,related_name='viewersProfile')
    Bio=models.TextField(max_length=100,null=True)
    interests = models.CharField(max_length=255, blank=True, null=True) 
    preferred_content_type = models.CharField(max_length=100, choices=PREFERRED_CONTENT, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username}"   
    
class BloggerProfileModel(models.Model):
    user = models.OneToOneField(Custom_user, on_delete=models.CASCADE,related_name='bloggersProfile')
    Bio = models.TextField(blank=True, null=True)
    website_url = models.URLField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return f"{self.user.username}"   
    
    
class BlogPostModel(models.Model):
    
    CATEGORY=[
        ('Technology','Technology'),
        ('Sports','Sports'),
        ('Entertainment','Entertainment'),
        ('Politics','Politics'),
        ('Business','Business'),
        ('Health','Health'),
        ('Education','Education'),
        ('Travel','Travel'),
        ('Food','Food'),
        ('Fashion','Fashion'),
    ]
    
    user=models.ForeignKey(Custom_user,on_delete=models.CASCADE)
    
    BlogTitle=models.CharField(max_length=500,null=True)
    BlogBody=models.TextField(max_length=1000,null=True)
    Category=models.CharField(choices=CATEGORY, max_length=100,null=True)
    Blog_Pic=models.ImageField(upload_to='Media/Blog_Pic',null=True)
    created = models.DateTimeField(auto_now_add=True,null=True)
    modified = models.DateTimeField(auto_now=True,null=True)
    
    
    def __str__(self):
        return f"Username: {self.user.username} - Blog Title : {self.BlogTitle} " 
