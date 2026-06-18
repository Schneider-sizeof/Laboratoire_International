"""
Views for Laboratoire International website.
All 7 pages + blog + legal + SEO endpoints.
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from django.utils.translation import gettext as _, get_language
from django.core.paginator import Paginator
from django.db.models import Q
from django.conf import settings
import json
import logging

from .models import BlogPost, BlogCategory, ContactSubmission, SiteSettings, TeamMember, Partner

logger = logging.getLogger(__name__)


# ============================================================
# Helper: get current language
# ============================================================
def _lang():
    return get_language() or 'fr'


# ============================================================
# Email helper
# ============================================================
def _send_contact_emails(submission, lang='fr'):
    """Send notification to admin and confirmation to visitor."""
    try:
        site = SiteSettings.load()
    except Exception:
        return

    if not site.notification_email or not site.smtp_user or not site.smtp_password:
        return

    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    try:
        # --- 1. Admin notification ---
        admin_html = f"""
        <html>
        <body style="font-family:Arial,sans-serif;background:#f8fafc;padding:20px;">
        <div style="max-width:600px;margin:0 auto;background:#fff;border-radius:12px;overflow:hidden;box-shadow:0 2px 8px rgba(0,0,0,0.1);">
            <div style="background:linear-gradient(135deg,#0f172a,#1e3a5f);padding:24px;color:#fff;">
                <h1 style="margin:0;font-size:20px;">📩 Nouveau message — {site.site_name}</h1>
            </div>
            <div style="padding:24px;">
                <table style="width:100%;border-collapse:collapse;">
                    <tr><td style="padding:8px 0;font-weight:bold;color:#475569;">Nom:</td><td style="padding:8px 0;">{submission.name}</td></tr>
                    <tr><td style="padding:8px 0;font-weight:bold;color:#475569;">Email:</td><td style="padding:8px 0;"><a href="mailto:{submission.email}">{submission.email}</a></td></tr>
                    <tr><td style="padding:8px 0;font-weight:bold;color:#475569;">Téléphone:</td><td style="padding:8px 0;">{submission.phone or 'Non renseigné'}</td></tr>
                    <tr><td style="padding:8px 0;font-weight:bold;color:#475569;">Service:</td><td style="padding:8px 0;">{submission.get_service_type_display()}</td></tr>
                    <tr><td style="padding:8px 0;font-weight:bold;color:#475569;">Date:</td><td style="padding:8px 0;">{submission.created_at.strftime('%d/%m/%Y %H:%M')}</td></tr>
                </table>
                <div style="margin-top:16px;padding:16px;background:#f1f5f9;border-radius:8px;">
                    <p style="margin:0;font-weight:bold;color:#475569;margin-bottom:8px;">Message:</p>
                    <p style="margin:0;white-space:pre-wrap;">{submission.message}</p>
                </div>
            </div>
        </div>
        </body>
        </html>
        """

        admin_msg = MIMEMultipart('alternative')
        admin_msg['Subject'] = f'[{site.site_name}] Nouveau message de {submission.name}'
        admin_msg['From'] = site.smtp_user
        admin_msg['To'] = site.notification_email
        admin_msg.attach(MIMEText(f"Nouveau message de {submission.name} ({submission.email}): {submission.message}", 'plain'))
        admin_msg.attach(MIMEText(admin_html, 'html'))

        # --- 2. Visitor confirmation ---
        thank_you_messages = {
            'fr': ('Merci pour votre message', 'Nous avons bien reçu votre message et nous vous répondrons dans les plus brefs délais.'),
            'en': ('Thank you for your message', 'We have received your message and will get back to you as soon as possible.'),
            'ar': ('شكراً لرسالتكم', 'لقد تلقينا رسالتكم وسنرد عليكم في أقرب وقت ممكن.'),
            'es': ('Gracias por su mensaje', 'Hemos recibido su mensaje y le responderemos lo antes posible.'),
            'de': ('Vielen Dank für Ihre Nachricht', 'Wir haben Ihre Nachricht erhalten und werden Ihnen so schnell wie möglich antworten.'),
            'nl': ('Bedankt voor uw bericht', 'We hebben uw bericht ontvangen en zullen zo snel mogelijk reageren.'),
            'it': ('Grazie per il vostro messaggio', 'Abbiamo ricevuto il vostro messaggio e vi risponderemo il prima possibile.'),
        }
        title, body = thank_you_messages.get(lang, thank_you_messages['fr'])

        visitor_html = f"""
        <html>
        <body style="font-family:Arial,sans-serif;background:#f8fafc;padding:20px;">
        <div style="max-width:600px;margin:0 auto;background:#fff;border-radius:12px;overflow:hidden;box-shadow:0 2px 8px rgba(0,0,0,0.1);">
            <div style="background:linear-gradient(135deg,#0f172a,#1e3a5f);padding:24px;color:#fff;text-align:center;">
                <h1 style="margin:0;font-size:22px;">{title}</h1>
            </div>
            <div style="padding:24px;text-align:center;">
                <p style="font-size:48px;margin:0 0 16px;">✅</p>
                <p style="font-size:16px;color:#475569;line-height:1.6;">{body}</p>
                <hr style="border:none;border-top:1px solid #e2e8f0;margin:24px 0;">
                <p style="font-size:14px;color:#94a3b8;">
                    {site.site_name}<br>
                    📞 {site.phone}<br>
                    📍 {site.address}
                </p>
            </div>
        </div>
        </body>
        </html>
        """

        visitor_msg = MIMEMultipart('alternative')
        visitor_msg['Subject'] = f'{title} — {site.site_name}'
        visitor_msg['From'] = site.smtp_user
        visitor_msg['To'] = submission.email
        visitor_msg.attach(MIMEText(f"{title}\n\n{body}\n\n{site.site_name}\n{site.phone}", 'plain'))
        visitor_msg.attach(MIMEText(visitor_html, 'html'))

        # Send both emails
        if site.smtp_use_tls:
            server = smtplib.SMTP(site.smtp_host, site.smtp_port)
            server.starttls()
        else:
            server = smtplib.SMTP_SSL(site.smtp_host, site.smtp_port)

        server.login(site.smtp_user, site.smtp_password)
        server.sendmail(site.smtp_user, site.notification_email, admin_msg.as_string())
        server.sendmail(site.smtp_user, submission.email, visitor_msg.as_string())
        server.quit()

        logger.info(f"Contact emails sent for submission from {submission.name}")

    except Exception as e:
        logger.error(f"Failed to send contact emails: {e}")


# ============================================================
# Page 1: Home
# ============================================================
def home(request):
    """Landing page with hero, services overview, stats, and partnerships."""
    lang = _lang()
    services_list = [
        {
            'icon': 'fas fa-flask',
            'title': _('Biochimie'),
            'description': _('Analyses biochimiques complètes incluant glycémie, cholestérol, bilan hépatique et rénal.'),
        },
        {
            'icon': 'fas fa-microscope',
            'title': _('Hématologie'),
            'description': _('Numération formule sanguine, vitesse de sédimentation, bilan de coagulation.'),
        },
        {
            'icon': 'fas fa-virus',
            'title': _('Microbiologie'),
            'description': _('Culture bactérienne, antibiogramme, examen cytobactériologique des urines.'),
        },
        {
            'icon': 'fas fa-dna',
            'title': _('Sérologie & Immunologie'),
            'description': _('Dépistage des maladies infectieuses, bilan immunitaire, tests sérologiques.'),
        },
        {
            'icon': 'fas fa-baby',
            'title': _('Fertilité & Gynécologie'),
            'description': _('Bilan hormonal, spermogramme, suivi de grossesse, dépistage prénatal.'),
        },
        {
            'icon': 'fas fa-vial',
            'title': _('PCR & Virologie'),
            'description': _('Tests PCR, charge virale, dépistage COVID-19, hépatites et autres virus.'),
        },
    ]
    stats = [
        {'number': '25+', 'label': _("Années d'Expérience")},
        {'number': '50K+', 'label': _('Analyses par An')},
        {'number': '99.9%', 'label': _('Taux de Précision')},
        {'number': '24/7', 'label': _('Service Continu')},
    ]
    testimonials = [
        {
            'name': 'Amina B.',
            'text': _('Service excellent et rapide. Les résultats sont disponibles en quelques heures. Je recommande vivement!'),
            'rating': 5,
        },
        {
            'name': 'Khalid M.',
            'text': _('Équipe très professionnelle et accueillante. Les analyses sont toujours précises.'),
            'rating': 5,
        },
        {
            'name': 'Sophie L.',
            'text': _('Le meilleur laboratoire de Tanger. Résultats rapides et personnel très compétent.'),
            'rating': 5,
        },
    ]

    # Partners from DB
    partners = Partner.objects.filter(is_active=True)

    # Latest blog posts for homepage
    latest_posts = BlogPost.objects.filter(status='published').order_by('-published_at')[:3]

    context = {
        'services': services_list,
        'stats': stats,
        'testimonials': testimonials,
        'partners': partners,
        'latest_posts': latest_posts,
        'lang': lang,
        'page_title': _('Accueil'),
        'meta_description': _(
            'Laboratoire International d\'Analyses Médicales à Tanger. '
            'Résultats en moins de 24h. Partenaire de Cerba Lab et du '
            'Laboratoire National Mohammed VI.'
        ),
    }
    return render(request, 'core/home.html', context)


# ============================================================
# Page 2: About
# ============================================================
def about(request):
    """About page with company history, values, team, and certifications."""
    lang = _lang()

    # Team from DB
    team = TeamMember.objects.filter(is_active=True)

    values = [
        {
            'icon': 'fas fa-award',
            'title': _('Excellence'),
            'description': _('Nous visons l\'excellence dans chaque analyse, avec des équipements de dernière génération.'),
        },
        {
            'icon': 'fas fa-heart',
            'title': _('Humanité'),
            'description': _('Chaque patient est accueilli avec bienveillance, respect et professionnalisme.'),
        },
        {
            'icon': 'fas fa-shield-alt',
            'title': _('Fiabilité'),
            'description': _('Des résultats fiables et reproductibles, conformes aux standards internationaux.'),
        },
        {
            'icon': 'fas fa-sync-alt',
            'title': _('Innovation'),
            'description': _('Investissement continu dans les technologies les plus avancées du diagnostic médical.'),
        },
    ]
    certifications = [
        {'name': 'ISO 15189', 'description': _('Accréditation des laboratoires de biologie médicale')},
        {'name': 'ISO 9001', 'description': _('Système de management de la qualité')},
        {'name': 'COFRAC', 'description': _('Comité Français d\'Accréditation')},
    ]
    context = {
        'team': team,
        'values': values,
        'certifications': certifications,
        'lang': lang,
        'page_title': _('À propos'),
        'meta_description': _(
            'Découvrez Laboratoire International, plus de 25 ans d\'expertise '
            'en analyses médicales à Tanger. Certifié ISO 15189.'
        ),
    }
    return render(request, 'core/about.html', context)


# ============================================================
# Page 3: Services
# ============================================================
def services(request):
    """Detailed services page with categories and test lists."""
    categories = [
        {
            'title': _('Biochimie'),
            'icon': 'fas fa-flask',
            'color': 'primary',
            'tests': [
                _('Glycémie à jeun & postprandiale'),
                _('Bilan lipidique complet (Cholestérol, Triglycérides, HDL, LDL)'),
                _('Bilan hépatique (ASAT, ALAT, GGT, Bilirubine)'),
                _('Bilan rénal (Urée, Créatinine, Acide urique)'),
                _('Bilan pancréatique (Amylase, Lipase)'),
                _('Ionogramme sanguin (Na, K, Cl, Ca, Mg)'),
                _('Protéines totales & Electrophorèse'),
                _('Marqueurs cardiaques (Troponine, BNP)'),
            ],
        },
        {
            'title': _('Hématologie'),
            'icon': 'fas fa-microscope',
            'color': 'danger',
            'tests': [
                _('NFS - Numération Formule Sanguine'),
                _('Vitesse de Sédimentation (VS)'),
                _('Bilan de coagulation (TP, TCA, INR)'),
                _('Groupe sanguin & Rhésus'),
                _('Test de Coombs direct & indirect'),
                _('Frottis sanguin'),
                _('Réticulocytes'),
                _('D-Dimères'),
            ],
        },
        {
            'title': _('Sérologie & Immunologie'),
            'icon': 'fas fa-shield-alt',
            'color': 'accent',
            'tests': [
                _('Sérologie HIV 1 & 2'),
                _('Sérologie Hépatite B (AgHBs, AntiHBs, AntiHBc)'),
                _('Sérologie Hépatite C'),
                _('Sérologie Syphilis (TPHA, VDRL)'),
                _('Sérologie Toxoplasmose'),
                _('Sérologie Rubéole'),
                _('CRP & Facteur Rhumatoïde'),
                _('Anticorps anti-nucléaires (ANA)'),
            ],
        },
        {
            'title': _('Hormonologie & Fertilité'),
            'icon': 'fas fa-baby',
            'color': 'warning',
            'tests': [
                _('Bilan thyroïdien (TSH, T3, T4)'),
                _('Bilan hormonal féminin (FSH, LH, Estradiol, Progestérone)'),
                _('Bilan hormonal masculin (Testostérone, PSA)'),
                _('Beta-HCG quantitatif'),
                _('Prolactine'),
                _('Cortisol & ACTH'),
                _('Spermogramme'),
                _('AMH (Hormone Anti-Müllérienne)'),
            ],
        },
        {
            'title': _('Microbiologie'),
            'icon': 'fas fa-virus',
            'color': 'success',
            'tests': [
                _('ECBU - Examen Cytobactériologique des Urines'),
                _('Coproculture'),
                _('Prélèvement vaginal & urétral'),
                _('Hémoculture'),
                _('Antibiogramme'),
                _('Examen parasitologique des selles'),
                _('Prélèvement de gorge'),
                _('Mycologie (champignons)'),
            ],
        },
        {
            'title': _('PCR & Biologie Moléculaire'),
            'icon': 'fas fa-dna',
            'color': 'accent',
            'tests': [
                _('PCR COVID-19 (RT-PCR)'),
                _('PCR Hépatite B & C quantitative'),
                _('PCR HIV - Charge virale'),
                _('PCR Tuberculose (GenXpert)'),
                _('PCR HPV & Génotypage'),
                _('PCR Chlamydia & Mycoplasme'),
                _('Tests de paternité'),
                _('Pharmacogénétique'),
            ],
        },
    ]
    context = {
        'categories': categories,
        'page_title': _('Nos Services'),
        'meta_description': _(
            'Découvrez nos services d\'analyses médicales : biochimie, hématologie, '
            'sérologie, PCR, microbiologie et plus. Résultats en moins de 24h.'
        ),
    }
    return render(request, 'core/services.html', context)


# ============================================================
# Page 4: Results (VisionLIS Redirect)
# ============================================================
def results(request):
    """Patient results page — redirect to VisionLIS portal."""
    faq_items = [
        {
            'question': _('Comment accéder à mes résultats ?'),
            'answer': _('Cliquez sur le bouton "Accéder à mes résultats" ci-dessus. Vous serez redirigé vers notre portail sécurisé VisionLIS où vous pourrez vous connecter avec vos identifiants.'),
        },
        {
            'question': _('Quels identifiants utiliser ?'),
            'answer': _('Utilisez le nom d\'utilisateur et le mot de passe qui vous ont été remis lors de votre visite au laboratoire.'),
        },
        {
            'question': _('Quand mes résultats seront-ils disponibles ?'),
            'answer': _('La plupart des résultats sont disponibles en moins de 24 heures. Certaines analyses spécialisées peuvent nécessiter un délai supplémentaire.'),
        },
        {
            'question': _('J\'ai oublié mes identifiants, que faire ?'),
            'answer': _('Contactez-nous par téléphone ou rendez-vous directement au laboratoire avec une pièce d\'identité pour récupérer vos identifiants.'),
        },
    ]
    context = {
        'faq_items': faq_items,
        'page_title': _('Mes Résultats'),
        'meta_description': _(
            'Accédez à vos résultats d\'analyses médicales en ligne. '
            'Connectez-vous à notre portail sécurisé VisionLIS.'
        ),
    }
    return render(request, 'core/results.html', context)


# ============================================================
# Page 5: Blog
# ============================================================
def blog_list(request):
    """Blog listing with category filter, search, and pagination."""
    lang = _lang()
    posts = BlogPost.objects.filter(status='published')

    # Category filter
    category_slug = request.GET.get('category', '')
    if category_slug:
        posts = posts.filter(category__slug=category_slug)

    # Search
    search_query = request.GET.get('q', '')
    if search_query:
        title_field = f'title_{lang}'
        content_field = f'content_{lang}'
        posts = posts.filter(
            Q(**{f'{title_field}__icontains': search_query}) |
            Q(**{f'{content_field}__icontains': search_query}) |
            Q(tags__icontains=search_query)
        )

    # Pagination
    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    categories = BlogCategory.objects.all()

    context = {
        'page_obj': page_obj,
        'categories': categories,
        'current_category': category_slug,
        'search_query': search_query,
        'lang': lang,
        'page_title': _('Blog'),
        'meta_description': _(
            'Articles et actualités sur les analyses médicales, '
            'la santé et le bien-être par Laboratoire International.'
        ),
    }
    return render(request, 'core/blog_list.html', context)


def blog_detail(request, slug):
    """Individual blog post page."""
    lang = _lang()
    post = get_object_or_404(BlogPost, slug=slug, status='published')

    # Increment view count
    BlogPost.objects.filter(pk=post.pk).update(views_count=post.views_count + 1)

    # Related posts
    related_posts = BlogPost.objects.filter(
        status='published', category=post.category
    ).exclude(pk=post.pk)[:3]

    context = {
        'post': post,
        'related_posts': related_posts,
        'lang': lang,
        'page_title': post.get_title(lang),
        'meta_description': post.get_meta_description(lang),
    }
    return render(request, 'core/blog_detail.html', context)


# ============================================================
# Page 6: Contact
# ============================================================
def contact(request):
    """Contact page with form, map, and business info."""
    context = {
        'page_title': _('Contact'),
        'meta_description': _(
            'Contactez Laboratoire International à Tanger. '
            'Appelez-nous ou envoyez-nous un message via notre formulaire de contact.'
        ),
    }
    return render(request, 'core/contact.html', context)


@require_POST
def contact_submit(request):
    """Handle contact form submission — save to DB, send emails, return JSON."""
    lang = _lang()
    try:
        data = json.loads(request.body)
        submission = ContactSubmission.objects.create(
            name=data.get('name', '').strip(),
            email=data.get('email', '').strip(),
            phone=data.get('phone', '').strip(),
            service_type=data.get('service_type', 'general'),
            message=data.get('message', '').strip(),
        )

        # Send email notifications (async-safe: won't block response on failure)
        try:
            _send_contact_emails(submission, lang)
        except Exception as e:
            logger.error(f"Email sending failed: {e}")

        return JsonResponse({
            'success': True,
            'message': str(_('Votre message a été envoyé avec succès! Nous vous contacterons bientôt.')),
        })
    except Exception as e:
        logger.error(f"Contact submission error: {e}")
        return JsonResponse({
            'success': False,
            'message': str(_('Une erreur est survenue. Veuillez réessayer.')),
        }, status=400)


# ============================================================
# Page 7: Legal Pages
# ============================================================
def legal_privacy(request):
    """Privacy Policy page."""
    context = {
        'page_title': _('Politique de Confidentialité'),
        'meta_description': _(
            'Politique de confidentialité de Laboratoire International. '
            'Comment nous protégeons vos données personnelles.'
        ),
    }
    return render(request, 'core/legal_privacy.html', context)


def legal_terms(request):
    """Terms of Service page."""
    context = {
        'page_title': _("Conditions d'Utilisation"),
        'meta_description': _(
            "Conditions générales d'utilisation du site web "
            "de Laboratoire International."
        ),
    }
    return render(request, 'core/legal_terms.html', context)


def legal_cookies(request):
    """Cookie Policy page."""
    context = {
        'page_title': _('Politique de Cookies'),
        'meta_description': _(
            'Comment Laboratoire International utilise les cookies '
            'sur son site web.'
        ),
    }
    return render(request, 'core/legal_cookies.html', context)


# ============================================================
# SEO: robots.txt
# ============================================================
def robots_txt(request):
    """Serve robots.txt."""
    try:
        site = SiteSettings.load()
        domain = site.site_domain
    except Exception:
        domain = getattr(settings, 'SITE_DOMAIN', 'laboratoireinternational.com')

    lines = [
        "User-agent: *",
        "Allow: /",
        "",
        f"Sitemap: https://{domain}/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
