from django.db import models
from django.conf import settings 
from taggit.managers import TaggableManager

# settings.AUTH_USER_MODEL
# Create your models here.

# Get absolute url?


class Tip_category (models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


class Category (models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


class Tip (models.Model):
    author= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category= models.ForeignKey('Tip_category', related_name='tips',  on_delete=models.CASCADE)
    title= models.CharField(max_length=50, blank=False, null=False, unique=True)
    body = models.TextField( blank=False, null=False)
    photo_field = models.ImageField( upload_to='uploads/')
    pub_date= models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


class Ingridient(models.Model):

    INGRIDIENT_CHOICES = (
        ('A', 'Alcoholic'),
        ('N', 'Non-alcoholic'),
        ('O', 'Other'),
    )

    name = models.CharField(max_length=50, unique=True, blank=False, null=False)
    photo_field = models.ImageField( upload_to='uploads/')
    measurement = models.CharField(max_length=10, blank=False, null=False)
    ing_type = models.CharField(max_length=1, choices=INGRIDIENT_CHOICES)
    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


class Cocktail (models.Model):

    METHOD_CHOICES = (
        ('Simple', 'S'),
        ('Sheyker required', 'H'),
        ('Blender required', 'B'),
    )
    author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category= models.ForeignKey('Category', on_delete=models.CASCADE)
    title= models.CharField(max_length=50, blank=False, null=False, unique=True)
    photo_field = models.ImageField( upload_to='uploads/')
    body = models.TextField( blank=False, null=False)
    method = models.CharField(max_length=20, choices=METHOD_CHOICES)
    pub_date= models.DateTimeField( auto_now_add=True)
    updated_at= models.DateTimeField( auto_now=True, blank=True, null=True)
    liked= models.ManyToManyField(settings.AUTH_USER_MODEL, default=None, blank=True, related_name="liked" )
    tags = TaggableManager()
    ingridient = models.ManyToManyField("Ingridient", through="Ingridient_cocktail")

    def get_tags_display(self):
        return self.tags.values_list('name', flat=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

    @property
    def num_likes(self):
        return self.liked.all().count()


LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)

class Like(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE )
    cocktail=models.ForeignKey(Cocktail,  related_name='likes', on_delete=models.CASCADE )
    value=models.CharField(choices=LIKE_CHOICES, default='Like', max_length=6)

    def __str__(self):
        return f'{self.user} --- {self.cocktail}'


class Ingridient_cocktail (models.Model):

    ING_CHOICES = (
        ('O', 'optional'),
        ('R', 'required'),
    )
    cocktail = models.ForeignKey('Cocktail',  on_delete=models.CASCADE)
    ingridient = models.ForeignKey('Ingridient',  on_delete=models.CASCADE)
    amount= models.FloatField()
    ing_types = models.CharField(max_length=1, choices=ING_CHOICES)

    def __str__(self):
        return str(self.cocktail) + str(self.ingridient)
    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


class Comment (models.Model):

    author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField( blank=False, null=False)
    cocktail= models.ForeignKey('Cocktail', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author} --- {self.body}'
    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
