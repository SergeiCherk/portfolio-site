from django.db import models

class AboutMe(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    bio = models.TextField(verbose_name="О себе")
    photo = models.ImageField(upload_to='about/', verbose_name="Фото")
    resume = models.FileField(upload_to='resume/', verbose_name="Резюме PDF", 
                             blank=True)
    
    # Социальные сети
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    telegram = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    
    class Meta:
        verbose_name = "Обо мне"
        verbose_name_plural = "Обо мне"
    
    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=50, verbose_name="Навык")
    icon = models.CharField(max_length=50, verbose_name="Иконка", 
                           help_text="Название иконки (например: python, django)")
    level = models.IntegerField(default=50, verbose_name="Уровень (0-100)")
    
    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"
    
    def __str__(self):
        return self.name