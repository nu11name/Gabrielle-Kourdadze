from django.db import models
from PIL import Image
import os

def generate_thumbnail(image_path, thumbnail_path, size=(300, 300)):
    """
    Generates a low-resolution thumbnail for a given image.

    Args:
        image_path (str): Path to the original high-resolution image.
        thumbnail_path (str): Path to save the generated thumbnail.
        size (tuple): Desired size of the thumbnail (width, height).

    Returns:
        None
    """
    with Image.open(image_path) as img:
        img.thumbnail(size)
        os.makedirs(os.path.dirname(thumbnail_path), exist_ok=True)
        img.save(thumbnail_path, format="JPEG", quality=85)


# Painting Model
class Painting(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='paintings/')
    thumbnail = models.ImageField(upload_to='paintings/thumbnails/', blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image and not self.thumbnail:
            original_path = self.image.path
            thumbnail_path = os.path.join(
                os.path.dirname(original_path),
                "thumbnails",
                os.path.basename(original_path),
            )
            generate_thumbnail(original_path, thumbnail_path)
            self.thumbnail.name = os.path.join("paintings/thumbnails", os.path.basename(original_path))
            super().save(*args, **kwargs)



# Works on Paper Model
class WorkOnPaper(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='works-on-paper/')
    thumbnail = models.ImageField(upload_to='works-on-paper/thumbnails/', blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image and not self.thumbnail:
            original_path = self.image.path
            thumbnail_path = os.path.join(
                os.path.dirname(original_path),
                "thumbnails",
                os.path.basename(original_path),
            )
            generate_thumbnail(original_path, thumbnail_path)
            self.thumbnail.name = os.path.join("works-on-paper/thumbnails", os.path.basename(original_path))
            super().save(*args, **kwargs)

# Exhibition Categories Model (Locations)
class ExhibitionCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


# Exhibition Model
class Exhibition(models.Model):
    title = models.CharField(max_length=255)
    location = models.ForeignKey(ExhibitionCategory, on_delete=models.CASCADE, related_name="exhibitions")

    def __str__(self):
        return f"{self.title} - {self.location.name}"


# Exhibition Images Model
class ExhibitionImage(models.Model):
    exhibition = models.ForeignKey(Exhibition, on_delete=models.CASCADE, related_name='images')
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='exhibitions/')
    thumbnail = models.ImageField(upload_to='exhibitions/thumbnails/', blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image and not self.thumbnail:
            original_path = self.image.path
            thumbnail_path = os.path.join(
                os.path.dirname(original_path),
                "thumbnails",
                os.path.basename(original_path),
            )
            generate_thumbnail(original_path, thumbnail_path)
            self.thumbnail.name = os.path.join("exhibitions/thumbnails", os.path.basename(original_path))
            super().save(*args, **kwargs)


# Education Model
class Education(models.Model):
    education = models.CharField(max_length=500)


    def __str__(self):
        return f"{self.education}"


# Residencies Model
class Residency(models.Model):
    location = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.location}"


# Fair Model
class Fair(models.Model):
    title = models.CharField(max_length=500)
    date = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.title} ({self.date})"


# Group Exhibitions Model
class GroupExhibition(models.Model):
    title = models.CharField(max_length=500)
    date = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.title} ({self.date})"


# Personal Exhibitions Model
class PersonalExhibition(models.Model):
    title = models.CharField(max_length=500)
    date = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.title} ({self.date})"

class TextsPublications(models.Model):
    title_en = models.CharField(max_length=500)
    title_fr = models.CharField(max_length=500)
    subtitle_en = models.CharField(max_length=500)
    subtitle_fr = models.CharField(max_length=500)
    publication_en = models.TextField()
    publication_fr = models.TextField()

    def __str__(self):
        return self.title_en