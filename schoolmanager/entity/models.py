from django.db import models
from .constants import Shape
from django.core.validators import MaxValueValidator, MinValueValidator


class Teacher(models.Model):
    full_name = models.CharField(max_length=40)
    date_of_joining = models.DateField()
    subject = models.ManyToManyField("Subject")
    salary = models.FloatField(validators=[MinValueValidator(1.0)])
    web_lecture = models.BooleanField(default=False) 

    def __str__(self):
        return f"Teacher: {self.full_name}"


class Student(models.Model):
    full_name = models.CharField(max_length=40)
    date_of_joining = models.DateField()
    standard = models.PositiveSmallIntegerField(validators=[MaxValueValidator(1), MinValueValidator(10)])
    roll_no = models.PositiveIntegerField(unique=True)
    rank = models.PositiveIntegerField()
    point_of_contact = models.ManyToManyField("Relative")

    def __str__(self):
        return f"Student: {self.full_name}"



class ClassRoom(models.Model):
    seating_capacity = models.IntegerField(default=15, validators=[MinValueValidator(15)])
    web_lecture_support = models.BooleanField(default=False)
    shape = models.PositiveSmallIntegerField(choices=[(shape.value, shape.name) for shape in Shape])

    def __str__(self):
        return f"Classroom: {self.shape}"


class Subject(models.Model):
    name = models.CharField(max_length=40)
    chapters = models.ManyToManyField("Chapter")
    duration = models.IntegerField(default=30,validators=[MinValueValidator(30), MaxValueValidator(120)])
    total_duration = models.IntegerField()

    def __str__(self):
        return f"Subject: {self.name}"



class Relative(models.Model):
    full_name = models.CharField(max_length=40)
    contact_number = models.CharField(max_length=10)
    relation = models.CharField(max_length=40)

    def __str__(self):
        return f"Relative: {self.full_name}"


class Chapter(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return f"Chapter: {self.name}"