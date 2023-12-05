from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Topic(models.Model):
    """
    Сущность темы задач
    """
    name = models.CharField(unique=True, max_length=150, verbose_name='Наименование темы',
                            help_text='Математика, перебор, графы ...')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'
        ordering = ('name',)


class Task(models.Model):
    """
    Сущность задачи
    """
    contest_id = models.PositiveIntegerField(verbose_name='id Конкурсной задачи', **NULLABLE,
                                             help_text='1, 2, 3, ...')
    contest_index = models.CharField(max_length=10, verbose_name='index Конкурсной задачи',
                                     help_text='A, B, C, ...')
    name = models.CharField(max_length=255, verbose_name='Наименование задачи', **NULLABLE)
    type = models.CharField(max_length=150, verbose_name='Тип задачи', help_text='PROGRAMMING, QUESTION, ...')
    points = models.PositiveIntegerField(**NULLABLE, verbose_name='Количество баллов',
                                         help_text='Максимальное количество баллов за задачу')
    rating = models.PositiveIntegerField(**NULLABLE, verbose_name='Рейтинг',
                                         help_text='Рейтинг задачи (сложность)')
    solved_count = models.PositiveIntegerField(default=0, verbose_name='Количество решений',
                                               help_text='Количество людей, решивших задачу')
    category = models.ManyToManyField(Topic, verbose_name='Темы задачи', help_text='Теги задачи')

    def __str__(self):
        return f'Задача: {str(self.contest_id) + str(self.contest_index)}   {self.name}' \
               f'\n       Баллы:   {self.points}' \
               f'\n       Рейтинг:   {self.rating}' \
               f'\n       Количество решений задач:   {self.solved_count}'

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        unique_together = ('contest_id', 'contest_index')
        ordering = ('solved_count',)
