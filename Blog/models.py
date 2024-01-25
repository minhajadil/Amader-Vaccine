from django.db import models
from Account.models import AccountModel



class Category(models.Model):
    type = models.CharField(max_length=20)
    slug = models.SlugField(max_length=100,unique=True, null=True, blank=True)

    def __str__(self) -> str:
        return self.type
    



class Posts(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(AccountModel,on_delete=models.CASCADE)
    date =models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='Post/uploads/')


    def __str__(self) -> str:
        return self.title
    


