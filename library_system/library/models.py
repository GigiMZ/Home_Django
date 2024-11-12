from django.db import models


class Library(models.Model):
    name = models.CharField(max_length=50)


class Book(models.Model):
    title = models.CharField(max_length=50)


class Member(models.Model):
    name = models.CharField(max_length=50)
    joined_date = models.DateField()
    lib_id = models.ForeignKey(Library, on_delete=models.DO_NOTHING, related_name='lib_id')
    book_id = models.ManyToManyField(Book, related_name='book_id')


class LibraryCard(models.Model):
    card_number = models.CharField(max_length=100)
    issued_date = models.DateField()
    member_id = models.OneToOneField(Member, on_delete=models.CASCADE, related_name='card')
