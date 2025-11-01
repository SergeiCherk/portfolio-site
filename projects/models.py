from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название проекта")
    description = models.TextField(verbose_name="Описание")
    tech_stack = models.CharField(max_length=300, verbose_name="Технологии", 
                                  help_text="Через запятую: Python, Django, React")
    github_link = models.URLField(verbose_name="Ссылка на GitHub", blank=True)
    live_link = models.URLField(verbose_name="Ссылка на демо", blank=True)
    image = models.ImageField(upload_to='projects/', verbose_name="Изображение", 
                             blank=True, null=True)  # <- null=True уже есть
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False, verbose_name="Избранный проект")
    
    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title