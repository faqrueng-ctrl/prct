from django.db import models


class DataRecord(models.Model):
    class Priority(models.TextChoices):
        LOW = 'low', 'Низкий'
        MEDIUM = 'medium', 'Средний'
        HIGH = 'high', 'Высокий'
        CRITICAL = 'critical', 'Критический'

    title = models.CharField('Название', max_length=120)
    category = models.CharField('Категория', max_length=80)
    status = models.CharField('Статус', max_length=80)
    priority = models.CharField(
        'Приоритет',
        max_length=20,
        choices=Priority.choices,
        default=Priority.MEDIUM,
    )
    description = models.TextField('Описание', blank=True)
    is_active = models.BooleanField('Активно', default=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата изменения', auto_now=True)

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ['-created_at', 'title']

    def __str__(self):
        return self.title
