from django.db import models

class Author(models.Model):
    name = models.CharField(
        max_length=50)
    surname = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    recipe_count = models.PositiveIntegerField(
        default=0,
    )
    image = models.ImageField(
        upload_to='authors',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.surname}"


    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class Task(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField('название', max_length=50)
    discription = models.CharField('описание', max_length=500)
    recipe = models.CharField('рецепт', max_length=5000)
    time_of_cook = models.CharField('время готовки', max_length=50)
    recipe_tip = models.CharField('советы к рецепту', max_length=1000)
    recipe_image = models.ImageField(upload_to='recipe/image')
    file = models.FileField(upload_to='recipe')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
       return self.title

    class Meta:
       verbose_name = 'Song'
       verbose_name_plural = 'Songs'



class Proposal(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    message = models.TextField()


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


