from django.db import models


class pop_skills(models.Model):
    skill = models.CharField('Навык', max_length=50)
    skill_count = models.CharField('Количество', max_length=12)

    def __str__(self):
        return self.skill

    class Meta:
        verbose_name = 'Навыки'
        verbose_name_plural = 'Навыки'


class pop_skills_fsprogrammer(models.Model):
    skill = models.CharField('Навык', max_length=50)
    skill_count = models.CharField('Количество', max_length=12)

    def __str__(self):
        return self.skill

    class Meta:
        verbose_name = 'Навыки Фуллстак'
        verbose_name_plural = 'Навыки Фуллстак'


class zp_prof(models.Model):
    year = models.CharField('год', max_length=4)
    salary = models.CharField('заработная плата', max_length=12)

    def __str__(self):
        return self.year

    class Meta:
        verbose_name = 'ЗП для всех проф по годам'
        verbose_name_plural = 'ЗП для всех проф по годам'


class zp_fsprog(models.Model):
    year = models.CharField('год', max_length=4)
    salary = models.CharField('заработная плата', max_length=12)

    def __str__(self):
        return self.year

    class Meta:
        verbose_name = 'ЗП для фуллстак по годам'
        verbose_name_plural = 'ЗП для фуллстак по годам'


class vacancy_count(models.Model):
    year = models.CharField('год', max_length=4)
    count = models.CharField('кол-во вакансий', max_length=12)

    def __str__(self):
        return self.year

    class Meta:
        verbose_name = 'Кол-во вакансий для всех проф'
        verbose_name_plural = 'Кол-во вакансий для всех проф'


class vacancy_fsprog_count(models.Model):
    year = models.CharField('год', max_length=4)
    count = models.CharField('кол-во вакансий', max_length=12)

    def __str__(self):
        return self.year

    class Meta:
        verbose_name = 'Кол-во вакансий для фуллстак'
        verbose_name_plural = 'Кол-во вакансий для фуллстак'


