from django.db import models

class AboutMe(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    bio = models.TextField(verbose_name="О себе")
    photo = models.ImageField(upload_to='about/', verbose_name="Фото", 
                             blank=True, null=True)  # <- null=True
    resume = models.FileField(upload_to='resume/', verbose_name="Резюме PDF", 
                             blank=True, null=True)  # <- null=True
    
    # Социальные сети
    github = models.URLField(blank=True, verbose_name="GitHub")
    vk = models.URLField(blank=True, verbose_name="Вконтакте")
    habr = models.URLField(blank=True, verbose_name="Habr")
    telegram = models.URLField(blank=True, verbose_name="Telegram")
    email = models.EmailField(blank=True, verbose_name="Email")
    
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