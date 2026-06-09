from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json


def home(request):
    """Landing page with hero, services overview, and stats."""
    services_list = [
        {
            'icon': 'fas fa-flask',
            'title': 'Biochimie',
            'description': 'Analyses biochimiques complètes incluant glycémie, cholestérol, bilan hépatique et rénal.',
        },
        {
            'icon': 'fas fa-microscope',
            'title': 'Hématologie',
            'description': 'Numération formule sanguine, vitesse de sédimentation, bilan de coagulation.',
        },
        {
            'icon': 'fas fa-virus',
            'title': 'Microbiologie',
            'description': 'Culture bactérienne, antibiogramme, examen cytobactériologique des urines.',
        },
        {
            'icon': 'fas fa-dna',
            'title': 'Sérologie & Immunologie',
            'description': 'Dépistage des maladies infectieuses, bilan immunitaire, tests sérologiques.',
        },
        {
            'icon': 'fas fa-baby',
            'title': 'Fertilité & Gynécologie',
            'description': 'Bilan hormonal, spermogramme, suivi de grossesse, dépistage prénatal.',
        },
        {
            'icon': 'fas fa-vial',
            'title': 'PCR & Virologie',
            'description': 'Tests PCR, charge virale, dépistage COVID-19, hépatites et autres virus.',
        },
    ]
    stats = [
        {'number': '25+', 'label': "Années d'Expérience"},
        {'number': '50K+', 'label': 'Analyses par An'},
        {'number': '99.9%', 'label': 'Taux de Précision'},
        {'number': '24/7', 'label': 'Service Continu'},
    ]
    context = {
        'services': services_list,
        'stats': stats,
    }
    return render(request, 'core/home.html', context)


def about(request):
    """About page with company history and team info."""
    team = [
        {
            'name': 'Dr. Youssef El Mansouri',
            'role': 'Directeur Général & Biologiste',
            'bio': 'Plus de 20 ans d\'expérience en biologie médicale. Diplômé de la Faculté de Médecine et Pharmacie de Rabat.',
        },
        {
            'name': 'Dr. Fatima Zahra Benali',
            'role': 'Biologiste Spécialiste',
            'bio': 'Spécialiste en hématologie et immunologie. Formation complémentaire à l\'Institut Pasteur de Paris.',
        },
        {
            'name': 'Dr. Karim Tazi',
            'role': 'Responsable Qualité',
            'bio': 'Expert en assurance qualité des laboratoires. Certifié ISO 15189 et accrédité COFRAC.',
        },
    ]
    values = [
        {
            'icon': 'fas fa-award',
            'title': 'Excellence',
            'description': 'Nous visons l\'excellence dans chaque analyse, avec des équipements de dernière génération.',
        },
        {
            'icon': 'fas fa-heart',
            'title': 'Humanité',
            'description': 'Chaque patient est accueilli avec bienveillance, respect et professionnalisme.',
        },
        {
            'icon': 'fas fa-shield-alt',
            'title': 'Fiabilité',
            'description': 'Des résultats fiables et reproductibles, conformes aux standards internationaux.',
        },
        {
            'icon': 'fas fa-sync-alt',
            'title': 'Innovation',
            'description': 'Investissement continu dans les technologies les plus avancées du diagnostic médical.',
        },
    ]
    context = {
        'team': team,
        'values': values,
    }
    return render(request, 'core/about.html', context)


def services(request):
    """Detailed services page."""
    categories = [
        {
            'title': 'Biochimie',
            'icon': 'fas fa-flask',
            'color': '#0ea5e9',
            'tests': [
                'Glycémie à jeun & postprandiale',
                'Bilan lipidique complet (Cholestérol, Triglycérides, HDL, LDL)',
                'Bilan hépatique (ASAT, ALAT, GGT, Bilirubine)',
                'Bilan rénal (Urée, Créatinine, Acide urique)',
                'Bilan pancréatique (Amylase, Lipase)',
                'Ionogramme sanguin (Na, K, Cl, Ca, Mg)',
                'Protéines totales & Electrophorèse',
                'Marqueurs cardiaques (Troponine, BNP)',
            ],
        },
        {
            'title': 'Hématologie',
            'icon': 'fas fa-microscope',
            'color': '#ef4444',
            'tests': [
                'NFS - Numération Formule Sanguine',
                'Vitesse de Sédimentation (VS)',
                'Bilan de coagulation (TP, TCA, INR)',
                'Groupe sanguin & Rhésus',
                'Test de Coombs direct & indirect',
                'Frottis sanguin',
                'Réticulocytes',
                'D-Dimères',
            ],
        },
        {
            'title': 'Sérologie & Immunologie',
            'icon': 'fas fa-shield-alt',
            'color': '#8b5cf6',
            'tests': [
                'Sérologie HIV 1 & 2',
                'Sérologie Hépatite B (AgHBs, AntiHBs, AntiHBc)',
                'Sérologie Hépatite C',
                'Sérologie Syphilis (TPHA, VDRL)',
                'Sérologie Toxoplasmose',
                'Sérologie Rubéole',
                'CRP & Facteur Rhumatoïde',
                'Anticorps anti-nucléaires (ANA)',
            ],
        },
        {
            'title': 'Hormonologie & Fertilité',
            'icon': 'fas fa-baby',
            'color': '#f59e0b',
            'tests': [
                'Bilan thyroïdien (TSH, T3, T4)',
                'Bilan hormonal féminin (FSH, LH, Estradiol, Progestérone)',
                'Bilan hormonal masculin (Testostérone, PSA)',
                'Beta-HCG quantitatif',
                'Prolactine',
                'Cortisol & ACTH',
                'Spermogramme',
                'AMH (Hormone Anti-Müllérienne)',
            ],
        },
        {
            'title': 'Microbiologie',
            'icon': 'fas fa-virus',
            'color': '#10b981',
            'tests': [
                'ECBU - Examen Cytobactériologique des Urines',
                'Coproculture',
                'Prélèvement vaginal & urétral',
                'Hémoculture',
                'Antibiogramme',
                'Examen parasitologique des selles',
                'Prélèvement de gorge',
                'Mycologie (champignons)',
            ],
        },
        {
            'title': 'PCR & Biologie Moléculaire',
            'icon': 'fas fa-dna',
            'color': '#06b6d4',
            'tests': [
                'PCR COVID-19 (RT-PCR)',
                'PCR Hépatite B & C quantitative',
                'PCR HIV - Charge virale',
                'PCR Tuberculose (GenXpert)',
                'PCR HPV & Génotypage',
                'PCR Chlamydia & Mycoplasme',
                'Tests de paternité',
                'Pharmacogénétique',
            ],
        },
    ]
    context = {'categories': categories}
    return render(request, 'core/services.html', context)


def results(request):
    """Patient results portal page (demo)."""
    return render(request, 'core/results.html')


def contact(request):
    """Contact page with form and map."""
    return render(request, 'core/contact.html')


@require_POST
def contact_submit(request):
    """Handle contact form submission (demo)."""
    try:
        data = json.loads(request.body)
        # In a real app, we'd save to DB and send email
        return JsonResponse({
            'success': True,
            'message': 'Votre message a été envoyé avec succès! Nous vous contacterons bientôt.'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': 'Une erreur est survenue. Veuillez réessayer.'
        }, status=400)
