from django.db import models

# Create your models here.
# https://docs.djangoproject.com/en/1.10/ref/models/fields/#field-options

class Author(models.Model):
    name = models.CharField(max_length=100, unique=True) #is a string and take all type of data 
    email = models.EmailField(unique=True) #if wrong format then exeption
    active = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    last_logged_in = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " : " + self.email
    

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return self.name 
    


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE) #always must be on_delete!

    def __str__(self):
        return self.name
    


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
    





