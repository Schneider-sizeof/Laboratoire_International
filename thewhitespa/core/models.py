from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Service(models.Model):
    CATEGORY_CHOICES = [
        ('HAMMAM', 'Hammam'),
        ('MASSAGE', 'Massage'),
        ('FACIAL', 'Soin Visage'),
        ('BODY', 'Soin Corps'),
        ('PACKAGE', 'Forfait'),
    ]

    name = models.CharField(max_length=200)
    name_fr = models.CharField(max_length=200, verbose_name='Nom (FR)')
    description = models.TextField(blank=True)
    description_fr = models.TextField(blank=True, verbose_name='Description (FR)')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration_minutes = models.PositiveIntegerField(default=60)
    image = models.ImageField(upload_to='services/', blank=True, default='')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='HAMMAM')
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.name_fr or self.name


class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    text = models.TextField()
    text_fr = models.TextField(blank=True, verbose_name='Texte (FR)')
    rating = models.PositiveIntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )
    date = models.DateField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date']
        verbose_name = 'Témoignage'
        verbose_name_plural = 'Témoignages'

    def __str__(self):
        return f"{self.client_name} — {self.rating}★"


class Booking(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'En attente'),
        ('CONFIRMED', 'Confirmé'),
        ('CANCELLED', 'Annulé'),
    ]

    first_name = models.CharField(max_length=100, verbose_name='Prénom')
    last_name = models.CharField(max_length=100, verbose_name='Nom')
    email = models.EmailField()
    phone = models.CharField(max_length=30, verbose_name='Téléphone')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='bookings')
    preferred_date = models.DateField(verbose_name='Date souhaitée')
    preferred_time = models.TimeField(verbose_name='Heure souhaitée')
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Réservation'
        verbose_name_plural = 'Réservations'

    def __str__(self):
        return f"{self.first_name} {self.last_name} — {self.service} ({self.preferred_date})"


class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    role_fr = models.CharField(max_length=100, verbose_name='Rôle (FR)')
    bio = models.TextField(blank=True)
    bio_fr = models.TextField(blank=True, verbose_name='Bio (FR)')
    image = models.ImageField(upload_to='team/', blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = "Membre de l'équipe"
        verbose_name_plural = "Membres de l'équipe"

    def __str__(self):
        return self.name


class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=200, blank=True)
    caption_fr = models.CharField(max_length=200, blank=True, verbose_name='Légende (FR)')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Image Galerie'
        verbose_name_plural = 'Images Galerie'

    def __str__(self):
        return self.caption_fr or self.caption or f"Image #{self.pk}"


class BusinessHour(models.Model):
    DAY_CHOICES = [
        (0, 'Lundi'),
        (1, 'Mardi'),
        (2, 'Mercredi'),
        (3, 'Jeudi'),
        (4, 'Vendredi'),
        (5, 'Samedi'),
        (6, 'Dimanche'),
    ]

    day = models.IntegerField(choices=DAY_CHOICES, unique=True)
    open_time = models.TimeField(default='10:00')
    close_time = models.TimeField(default='00:00')
    is_closed = models.BooleanField(default=False)

    class Meta:
        ordering = ['day']
        verbose_name = "Horaire d'ouverture"
        verbose_name_plural = "Horaires d'ouverture"

    def __str__(self):
        if self.is_closed:
            return f"{self.get_day_display()} — Fermé"
        return f"{self.get_day_display()} — {self.open_time:%H:%M} à {self.close_time:%H:%M}"
