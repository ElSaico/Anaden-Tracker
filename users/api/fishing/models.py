from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    rod = models.PositiveIntegerField(default='1')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Weapon(models.Model):
    weapon = models.CharField(max_length=30, default='', blank=True)

    def __str__(self):
        return f'{self.id} - {self.weapon}'


class Loot(models.Model):
    loot = models.CharField(max_length=30, default='', blank=True)

    def __str__(self):
        return f'{self.id} - {self.loot}'


class Fish(models.Model):
    # User authentication
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fishes')

    # Description Fields of Fishes
    number = models.PositiveIntegerField(default='0')
    description = models.CharField(max_length=1, default='', blank=True)
    name = models.CharField(max_length=30, default='', blank=True)
    hook = models.CharField(max_length=12, default='Single Catch')
    actual_catch = models.PositiveIntegerField(default='0')
    stones = models.PositiveIntegerField(default='0')
    c_stones = models.PositiveIntegerField(default='0')
    rod = models.PositiveIntegerField(default='0', blank=True)
    bait = models.CharField(max_length=30, default='', blank=True)
    reel = models.CharField(max_length=20, default='', blank=True)
    xp = models.PositiveIntegerField(default='0')

    rarity = models.PositiveIntegerField(default='1')
    min_size = models.FloatField(default='0')
    max_size = models.FloatField(default='0')
    min_points = models.FloatField(default='0')
    max_points = models.FloatField(default='0')
    weak = models.CharField(max_length=10, default='none', blank=True)
    resist = models.CharField(max_length=10, default='none', blank=True)
    absorb = models.CharField(max_length=10, default='none', blank=True)
    weapon = models.ManyToManyField(Weapon, blank=True, default=None, related_name='weapons')
    loot = models.ManyToManyField(Loot, blank=True, default=None, related_name='loots')

    # Fishes' Spots
    lake_tiilen = models.BooleanField(default=False)
    dragon_palace = models.BooleanField(default=False)
    acteul = models.BooleanField(default=False)
    vasu_mountains = models.BooleanField(default=False)
    charol_plains = models.BooleanField(default=False)
    man_eating_marsh = models.BooleanField(default=False)
    baruoki = models.BooleanField(default=False)
    nauru_uplands = models.BooleanField(default=False)
    karek_swampland = models.BooleanField(default=False)
    rinde = models.BooleanField(default=False)
    serena_coast = models.BooleanField(default=False)
    rucyana_sands = models.BooleanField(default=False)
    elzion_airport = models.BooleanField(default=False)
    nilva = models.BooleanField(default=False)
    last_island = models.BooleanField(default=False)
    spacetime_rift = models.BooleanField(default=False)
    zol_plains = models.BooleanField(default=False)
    moonlight_forest = models.BooleanField(default=False)
    snake_neck_igoma = models.BooleanField(default=False)
    ancient_battlefield = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super(Fish, self).save(*args, **kwargs)

    def __str__(self):
        return f'User: {self.user} ({self.user.id}) - {self.name}'
