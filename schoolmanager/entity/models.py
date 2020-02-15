from django.db import models
from .constants import Shape
from django.core.validators import MaxValueValidator, MinValueValidator


class Teacher(models.Model):
    full_name = models.CharField(max_length=40)
    date_of_joining = models.DateField()
    subject = models.ManyToManyField("Subject")
    salary = models.FloatField(help_text="In LPA")


class Student(models.Model):
    full_name = models.CharField(max_length=40)
    date_of_joining = models.DateField()
    standard = models.PositiveSmallIntegerField(validators=[MaxValueValidator(1), MinValueValidator(10)])
    roll_no = models.PositiveIntegerField()
    rank = models.PositiveIntegerField()
    point_of_contact = models.ManyToManyField("Relative")


class ClassRoom(models.Model):
    seating_capacity = models.IntegerField(default=15, validators=[MinValueValidator(15)])
    web_lecture_support = models.BooleanField(default=False)
    shape = models.PositiveSmallIntegerField(choices=[(shape.value, shape.name) for shape in Shape])


class Subject(models.Model):
    chapters = models.ManyToManyField("Chapter")
    duration = models.IntegerField(default=30,validators=[MinValueValidator(30), MaxValueValidator(120)])
    total_duration = models.IntegerField()


class Relative(models.Model):
    full_name = models.CharField(max_length=40)
    contact_number = models.CharField(max_length=10)
    relation = models.CharField(max_length=40)


class Chapter(models.Model):
    name = models.CharField(max_length=40)
