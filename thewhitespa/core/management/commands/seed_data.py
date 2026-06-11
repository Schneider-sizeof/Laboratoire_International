import datetime
from django.core.management.base import BaseCommand
from core.models import Service, Testimonial, TeamMember, BusinessHour


class Command(BaseCommand):
    help = 'Seed the database with sample data for The White Spa'

    def handle(self, *args, **options):
        self.stdout.write('Seeding data for The White Spa...')

        self._create_services()
        self._create_testimonials()
        self._create_team_members()
        self._create_business_hours()

        self.stdout.write(self.style.SUCCESS('✅ Database seeded successfully!'))

    def _create_services(self):
        services = [
            {
                'name': 'Traditional Hammam',
                'name_fr': 'Hammam Traditionnel',
                'description': 'Authentic Moroccan hammam experience with black soap scrub and ghassoul clay.',
                'description_fr': 'Expérience authentique du hammam marocain avec gommage au savon noir et argile ghassoul.',
                'price': 200,
                'duration_minutes': 60,
                'category': 'HAMMAM',
                'image': 'services/hammam.png',
                'is_featured': True,
                'order': 1,
            },
            {
                'name': 'Royal Hammam',
                'name_fr': 'Hammam Royal',
                'description': 'Premium hammam with argan oil massage, rose water rinse and deep hydration.',
                'description_fr': "Hammam premium avec massage à l'huile d'argan, rinçage à l'eau de rose et hydratation profonde.",
                'price': 400,
                'duration_minutes': 90,
                'category': 'HAMMAM',
                'image': 'services/hammam_royal.png',
                'is_featured': True,
                'order': 2,
            },
            {
                'name': 'Relaxing Massage',
                'name_fr': 'Massage Relaxant',
                'description': 'Full body relaxing massage with essential oils.',
                'description_fr': 'Massage relaxant du corps entier aux huiles essentielles.',
                'price': 300,
                'duration_minutes': 60,
                'category': 'MASSAGE',
                'image': 'services/massage.png',
                'is_featured': True,
                'order': 3,
            },
            {
                'name': 'Hot Stone Massage',
                'name_fr': 'Massage aux Pierres Chaudes',
                'description': 'Therapeutic hot stone massage for deep relaxation and muscle relief.',
                'description_fr': 'Massage thérapeutique aux pierres chaudes pour une relaxation profonde et un soulagement musculaire.',
                'price': 450,
                'duration_minutes': 75,
                'category': 'MASSAGE',
                'image': 'services/pierres_chaudes.png',
                'is_featured': False,
                'order': 4,
            },
            {
                'name': 'Facial Treatment',
                'name_fr': 'Soin Visage',
                'description': 'Deep cleansing facial with natural Moroccan ingredients.',
                'description_fr': 'Soin du visage en profondeur avec des ingrédients naturels marocains.',
                'price': 250,
                'duration_minutes': 45,
                'category': 'FACIAL',
                'image': 'services/soin_visage.png',
                'is_featured': False,
                'order': 5,
            },
            {
                'name': 'Body Scrub',
                'name_fr': 'Gommage Corps',
                'description': 'Exfoliating body scrub with natural ingredients for silky smooth skin.',
                'description_fr': 'Gommage exfoliant du corps avec des ingrédients naturels pour une peau douce et soyeuse.',
                'price': 150,
                'duration_minutes': 40,
                'category': 'BODY',
                'image': 'services/gommage.png',
                'is_featured': False,
                'order': 6,
            },
            {
                'name': 'VIP Package',
                'name_fr': 'Pack VIP',
                'description': 'Complete luxury experience: Royal Hammam + Hot Stone Massage + Facial Treatment.',
                'description_fr': 'Expérience luxe complète : Hammam Royal + Massage aux Pierres Chaudes + Soin Visage.',
                'price': 800,
                'duration_minutes': 180,
                'category': 'PACKAGE',
                'image': 'services/pack_vip.png',
                'is_featured': True,
                'order': 7,
            },
            {
                'name': 'Discovery Package',
                'name_fr': 'Pack Découverte',
                'description': 'Perfect introduction: Traditional Hammam + Relaxing Massage.',
                'description_fr': "Introduction parfaite : Hammam Traditionnel + Massage Relaxant.",
                'price': 400,
                'duration_minutes': 120,
                'category': 'PACKAGE',
                'image': 'services/pack_decouverte.png',
                'is_featured': True,
                'order': 8,
            },
        ]

        for data in services:
            Service.objects.update_or_create(
                name_fr=data['name_fr'],
                defaults=data,
            )
        self.stdout.write(f'  Created {len(services)} services')

    def _create_testimonials(self):
        testimonials = [
            {
                'client_name': 'Fatima El Amrani',
                'text': 'An exceptional experience! The Royal Hammam is simply divine.',
                'text_fr': "Une expérience exceptionnelle ! Le Hammam Royal est tout simplement divin. Je recommande vivement !",
                'rating': 5,
                'is_featured': True,
            },
            {
                'client_name': 'Nadia Bensouda',
                'text': 'The best spa in Tangier. Professional staff and a warm atmosphere.',
                'text_fr': "Le meilleur spa de Tanger. Un personnel professionnel et une ambiance chaleureuse. J'y retourne chaque semaine.",
                'rating': 5,
                'is_featured': True,
            },
            {
                'client_name': 'Karim Tazi',
                'text': 'The hot stone massage was incredible. A true moment of relaxation.',
                'text_fr': "Le massage aux pierres chaudes était incroyable. Un vrai moment de détente après une longue semaine.",
                'rating': 4,
                'is_featured': True,
            },
            {
                'client_name': 'Sophie Martin',
                'text': 'I discovered this spa during my vacation in Tangier and I was delighted.',
                'text_fr': "J'ai découvert ce spa pendant mes vacances à Tanger et j'ai été ravie. Qualité au top !",
                'rating': 5,
                'is_featured': True,
            },
            {
                'client_name': 'Youssef Alaoui',
                'text': 'The VIP package is worth every dirham. A complete experience.',
                'text_fr': "Le pack VIP vaut chaque dirham. Une expérience complète du début à la fin. Merci à toute l'équipe !",
                'rating': 5,
                'is_featured': False,
            },
        ]

        for data in testimonials:
            Testimonial.objects.update_or_create(
                client_name=data['client_name'],
                defaults=data,
            )
        self.stdout.write(f'  Created {len(testimonials)} testimonials')

    def _create_team_members(self):
        members = [
            {
                'name': 'Amina Rochdi',
                'role': 'Spa Director',
                'role_fr': 'Directrice du Spa',
                'bio': 'With over 15 years of experience in wellness, Amina leads The White Spa with passion.',
                'bio_fr': "Forte de plus de 15 ans d'expérience dans le bien-être, Amina dirige The White Spa avec passion et dévouement.",
                'order': 1,
            },
            {
                'name': 'Khalid Mansouri',
                'role': 'Massage Therapist',
                'role_fr': 'Masseur Kinésithérapeute',
                'bio': 'Specialized in therapeutic and relaxation massages, Khalid brings expertise and care.',
                'bio_fr': "Spécialisé dans les massages thérapeutiques et de relaxation, Khalid apporte expertise et bienveillance.",
                'order': 2,
            },
            {
                'name': 'Zineb Fassi',
                'role': 'Hammam Specialist',
                'role_fr': 'Spécialiste Hammam',
                'bio': 'Zineb masters traditional hammam techniques passed down through generations.',
                'bio_fr': "Zineb maîtrise les techniques traditionnelles du hammam transmises de génération en génération.",
                'order': 3,
            },
            {
                'name': 'Leila Berrada',
                'role': 'Aesthetician',
                'role_fr': 'Esthéticienne',
                'bio': 'Expert in facial and body treatments, Leila uses the best natural Moroccan products.',
                'bio_fr': "Experte en soins du visage et du corps, Leila utilise les meilleurs produits naturels marocains.",
                'order': 4,
            },
        ]

        for data in members:
            TeamMember.objects.update_or_create(
                name=data['name'],
                defaults=data,
            )
        self.stdout.write(f'  Created {len(members)} team members')

    def _create_business_hours(self):
        for day in range(7):
            BusinessHour.objects.update_or_create(
                day=day,
                defaults={
                    'open_time': datetime.time(10, 0),
                    'close_time': datetime.time(0, 0),
                    'is_closed': False,
                },
            )
        self.stdout.write('  Created business hours (10:00–00:00, 7 days)')
