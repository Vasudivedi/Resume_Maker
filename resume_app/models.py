from django.db import models

# Create your models here.
from typing import ClassVar
from django.db import models
from django.core import validators

# Board/University Model
class BoardOrUniversity(models.Model):
    Name = models.CharField(max_length=50)
    Location = models.TextField(max_length=100)

    class Meta:
        db_table = 'BoardOrUniversity'
        verbose_name_plural = 'Board Or Universities'


    def __str__(self) -> str:
        return  self.Name

      

# Course/Stream
class CourseOrStream(models.Model):
    Name = models.CharField(max_length=50)
    Type = models.CharField(max_length=10)
    Duration = models.IntegerField(validators=[validators.MinValueValidator(1), validators.MaxValueValidator(4)])

    class Meta:
        db_table = 'Course Or Stream'

    def __str__(self) -> str:
        return  self.Name    

# Create your models here.
class Master(models.Model):
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=12)
    IsActive = models.BooleanField(default=False)
    DateCreated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'master'

    def __str__(self) -> str:
        return self.Email

gender_choice = (
    ('m', 'male'),
    ('f', 'female'),
)

class User(models.Model):
    Master = models.ForeignKey(Master, on_delete=models.CASCADE)
    UserName = models.CharField(max_length=25, unique=True, blank=True)
    Image = models.FileField(upload_to="users/profile/", default="avatar.png")
    About = models.TextField(max_length=255, default="")
    FullName = models.CharField(max_length=30, default="")
    Mobile = models.CharField(max_length=10, default="")
    Gender = models.CharField(max_length=10, choices=gender_choice)
    BirthDate = models.DateField(auto_created=True, blank=True)
    
    Country = models.CharField(max_length=20, default="")
    State = models.CharField(max_length=20, default="")
    City = models.CharField(max_length=20, default="")
    Address = models.TextField(max_length=255, default="")

    class Meta:
        db_table = 'user'

    def __str__(self) -> str:
         return self.FullName   

skill_choices = (
    (30, 'beginner'),
    (60, 'intermediate'),
    (100, 'advance'),
)
class Skill(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.CharField(max_length=50)
    level = models.CharField(max_length=10, choices=skill_choices)

    class Meta:
        db_table = 'skill'

class Education(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    BoardUniversity = models.ForeignKey(BoardOrUniversity, on_delete=models.CASCADE)
    CourseStream = models.ForeignKey(CourseOrStream, on_delete=models.CASCADE)
    StartDate = models.DateField(auto_created=True, blank=True)
    EndDate = models.DateField(auto_created=True, blank=True)
    Score = models.DecimalField(null=True, max_digits=4, decimal_places=2, validators=[validators.MinValueValidator(0.00)])
    IsPercent = models.BooleanField(default=True)
    Description = models.CharField(max_length=100)
    IsCompleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'education'

      

class Experience(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    JobTitle = models.CharField(max_length=100)
    Company = models.CharField(max_length=100)
    StartDate = models.DateField(auto_created=True, blank=True)
    EndDate = models.DateField(auto_created=True, blank=True)
    Description = models.CharField(max_length=100)

    class Meta:
        db_table = 'experience'
  
    

class Reference(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Link = models.URLField(max_length=100)
    Description = models.CharField(max_length=100)

    class Meta:
        db_table = 'reference'

    
class Project(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    # Image = models.FileField(upload_to="projects/", default="project.png")
    Title = models.CharField(max_length=50)
    Category = models.CharField(max_length=20)
    Description = models.CharField(max_length=100)

    class Meta:
        db_table = 'project'

class SocialLink(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=20)
    Link = models.URLField(max_length=100)

    class Meta:
        db_table = 'SocialLink'

    def __str__(self) -> str:
        return self.Name    
    