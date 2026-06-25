"""
Management command to create 3 neighborhood pages for local SEO.
"""
from django.core.management.base import BaseCommand
from core.models import NeighborhoodPage


NEIGHBORHOODS = [
    {
        'slug': 'laboratoire-analyses-tanger-ville',
        'latitude': 35.7595,
        'longitude': -5.8340,
        'name_fr': 'Tanger Ville',
        'name_en': 'Tangier City Center',
        'name_ar': 'مدينة طنجة',
        'title_fr': 'Laboratoire d\'analyses médicales à Tanger Ville',
        'title_en': 'Medical laboratory in Tangier City Center',
        'title_ar': 'مختبر التحاليل الطبية في مدينة طنجة',
        'meta_description_fr': 'Laboratoire International à Tanger Ville : analyses médicales, bilans sanguins, résultats rapides. Avenue Moulay Rachid.',
        'meta_description_en': 'Laboratoire International in Tangier City Center: medical tests, blood work, fast results. Avenue Moulay Rachid.',
        'meta_description_ar': 'المختبر الدولي في مدينة طنجة: تحاليل طبية، فحوصات دم، نتائج سريعة. شارع مولاي رشيد.',
        'content_fr': """<h2>Votre laboratoire d'analyses médicales au cœur de Tanger Ville</h2>

<p>Le <strong>Laboratoire International</strong> est idéalement situé <strong>Avenue Moulay Rachid</strong>, au cœur de Tanger Ville, à proximité des principaux cabinets médicaux et cliniques de la ville. Notre emplacement central vous permet un accès facile depuis tous les quartiers de Tanger.</p>

<h3>Un accès facile depuis tout Tanger</h3>

<p>Que vous veniez du centre-ville, de la Médina, de Marshan, de la Montagne ou des quartiers résidentiels, notre laboratoire est facilement accessible :</p>
<ul>
<li>À <strong>5 minutes en voiture</strong> du Grand Socco et de la Médina</li>
<li>À <strong>10 minutes</strong> de la gare Tanger Ville</li>
<li>Parking disponible à proximité</li>
<li>Desservi par les principales lignes de transport en commun</li>
</ul>

<h3>Plus de 200 analyses disponibles</h3>

<p>Notre laboratoire propose une gamme complète d'analyses médicales :</p>
<ul>
<li><strong>Biochimie</strong> : glycémie, bilan lipidique, bilan hépatique et rénal</li>
<li><strong>Hématologie</strong> : NFS, VS, bilan de coagulation</li>
<li><strong>Sérologie</strong> : hépatites, HIV, toxoplasmose, rubéole</li>
<li><strong>Hormones</strong> : thyroïde, fertilité, grossesse</li>
<li><strong>Microbiologie</strong> : ECBU, coproculture, antibiogramme</li>
<li><strong>PCR & biologie moléculaire</strong> : hépatites, HPV, COVID-19</li>
</ul>

<h3>Horaires d'ouverture</h3>

<p>Nous vous accueillons dans des conditions optimales de confort et d'hygiène :</p>
<ul>
<li><strong>Lundi à Vendredi</strong> : 7h00 - 19h00</li>
<li><strong>Samedi</strong> : 7h00 - 15h00</li>
<li><strong>Dimanche</strong> : Fermé</li>
</ul>

<p>Pour prendre rendez-vous ou obtenir des informations, n'hésitez pas à nous <a href="/fr/contact/">contacter</a> par téléphone ou WhatsApp.</p>""",
        'content_en': """<h2>Your medical laboratory in the heart of Tangier City</h2>

<p><strong>Laboratoire International</strong> is ideally located on <strong>Avenue Moulay Rachid</strong>, in the heart of Tangier. We offer over 200 types of medical analyses with results in under 24 hours.</p>

<h3>Opening hours</h3>
<ul>
<li><strong>Monday to Friday</strong>: 7:00 AM - 7:00 PM</li>
<li><strong>Saturday</strong>: 7:00 AM - 3:00 PM</li>
<li><strong>Sunday</strong>: Closed</li>
</ul>

<p><a href="/en/contact/">Contact us</a> for appointments or information.</p>""",
        'content_ar': """<h2>مختبركم للتحاليل الطبية في قلب مدينة طنجة</h2>

<p>يقع <strong>المختبر الدولي</strong> في موقع مثالي في <strong>شارع مولاي رشيد</strong> في قلب مدينة طنجة. نقدم أكثر من 200 نوع من التحاليل الطبية مع نتائج خلال أقل من 24 ساعة.</p>

<p><a href="/ar/contact/">تواصلوا معنا</a> للمواعيد أو الاستفسارات.</p>""",
    },
    {
        'slug': 'laboratoire-analyses-malabata-tanger',
        'latitude': 35.7850,
        'longitude': -5.7920,
        'name_fr': 'Malabata',
        'name_en': 'Malabata',
        'name_ar': 'مالاباطا',
        'title_fr': 'Laboratoire d\'analyses médicales proche de Malabata, Tanger',
        'title_en': 'Medical laboratory near Malabata, Tangier',
        'title_ar': 'مختبر تحاليل طبية قرب مالاباطا، طنجة',
        'meta_description_fr': 'Laboratoire International proche de Malabata à Tanger. Analyses médicales complètes, résultats rapides, équipements modernes.',
        'meta_description_en': 'Laboratoire International near Malabata in Tangier. Complete medical tests, fast results, modern equipment.',
        'meta_description_ar': 'المختبر الدولي قرب مالاباطا في طنجة. تحاليل طبية شاملة، نتائج سريعة، أجهزة حديثة.',
        'content_fr': """<h2>Laboratoire d'analyses médicales à proximité de Malabata</h2>

<p>Vous habitez le quartier de <strong>Malabata</strong> ou ses environs à Tanger ? Le <strong>Laboratoire International</strong> est votre laboratoire de proximité, situé à seulement quelques minutes en voiture sur l'Avenue Moulay Rachid.</p>

<h3>Pourquoi nous choisir depuis Malabata ?</h3>

<ul>
<li><strong>Proximité</strong> : à 10-15 minutes en voiture depuis Malabata</li>
<li><strong>Rapidité</strong> : résultats de la plupart des analyses en moins de 24h</li>
<li><strong>Expertise</strong> : équipe de biologistes expérimentés</li>
<li><strong>Équipements modernes</strong> : technologie de dernière génération</li>
<li><strong>Confort</strong> : salle d'attente climatisée, prélèvement indolore</li>
</ul>

<h3>Services les plus demandés par les résidents de Malabata</h3>

<p>Les habitants de Malabata et des quartiers environnants nous consultent fréquemment pour :</p>
<ul>
<li>Bilans de santé complets (check-up annuel)</li>
<li>Suivi de grossesse (Beta HCG, toxoplasmose, rubéole)</li>
<li>Bilans thyroïdiens et hormonaux</li>
<li>Dépistage des hépatites et IST</li>
<li>Bilans lipidiques et glycémie (suivi diabète)</li>
</ul>

<h3>Comment nous rejoindre depuis Malabata</h3>

<p>Depuis Malabata, prenez la route côtière vers le centre-ville. Le laboratoire se trouve sur l'Avenue Moulay Rachid. Le trajet prend environ 10 à 15 minutes selon le trafic.</p>

<p>N'hésitez pas à nous <a href="/fr/contact/">contacter</a> pour toute question ou pour prendre rendez-vous.</p>""",
        'content_en': """<h2>Medical laboratory near Malabata, Tangier</h2>

<p>Living in the <strong>Malabata</strong> area? <strong>Laboratoire International</strong> is your nearby laboratory, just 10-15 minutes by car on Avenue Moulay Rachid. Modern equipment, experienced team, and fast results.</p>

<p><a href="/en/contact/">Contact us</a> for appointments.</p>""",
        'content_ar': """<h2>مختبر تحاليل طبية قرب مالاباطا</h2>

<p>تسكنون في حي <strong>مالاباطا</strong>؟ <strong>المختبر الدولي</strong> هو مختبركم القريب، على بعد 10-15 دقيقة بالسيارة. أجهزة حديثة وفريق متمرس ونتائج سريعة.</p>

<p><a href="/ar/contact/">تواصلوا معنا</a> للمواعيد.</p>""",
    },
    {
        'slug': 'laboratoire-analyses-chu-tanger',
        'latitude': 35.7480,
        'longitude': -5.8610,
        'name_fr': 'CHU Tanger',
        'name_en': 'Tangier University Hospital',
        'name_ar': 'المستشفى الجامعي بطنجة',
        'title_fr': 'Laboratoire d\'analyses médicales près du CHU de Tanger',
        'title_en': 'Medical laboratory near Tangier University Hospital (CHU)',
        'title_ar': 'مختبر تحاليل طبية قرب المستشفى الجامعي بطنجة',
        'meta_description_fr': 'Laboratoire International proche du CHU de Tanger. Analyses complémentaires, résultats rapides, sans attente.',
        'meta_description_en': 'Laboratoire International near Tangier University Hospital. Complementary tests, fast results, no waiting.',
        'meta_description_ar': 'المختبر الدولي قرب المستشفى الجامعي بطنجة. تحاليل تكميلية، نتائج سريعة، بدون انتظار.',
        'content_fr': """<h2>Analyses médicales complémentaires près du CHU de Tanger</h2>

<p>Situé à proximité du <strong>Centre Hospitalier Universitaire (CHU) de Tanger</strong>, le <strong>Laboratoire International</strong> offre une alternative rapide et confortable pour vos analyses médicales. Que votre médecin exerce au CHU ou dans un cabinet privé, nous sommes à votre service.</p>

<h3>Pourquoi choisir notre laboratoire près du CHU ?</h3>

<ul>
<li><strong>Rapidité</strong> : résultats en quelques heures contre plusieurs jours à l'hôpital</li>
<li><strong>Confort</strong> : pas de longues files d'attente</li>
<li><strong>Horaires étendus</strong> : ouvert de 7h à 19h en semaine et le samedi matin</li>
<li><strong>Analyses spécialisées</strong> : PCR, auto-immunité, biologie moléculaire</li>
<li><strong>Résultats en ligne</strong> : consultez vos résultats depuis chez vous</li>
</ul>

<h3>Collaboration avec les médecins du CHU</h3>

<p>De nombreux médecins et spécialistes du CHU de Tanger orientent leurs patients vers notre laboratoire pour des analyses complémentaires nécessitant un délai court ou des techniques spécialisées. Notre équipe assure une communication fluide avec votre médecin traitant.</p>

<h3>Analyses les plus demandées</h3>

<p>Les patients venant du CHU nous sollicitent principalement pour :</p>
<ul>
<li>Bilans préopératoires complets</li>
<li>Marqueurs tumoraux et bilans de suivi</li>
<li>PCR et charges virales (hépatites, HIV)</li>
<li>Bilans d'auto-immunité</li>
<li>Spermogrammes et bilans de fertilité</li>
</ul>

<h3>Accès depuis le CHU</h3>

<p>Depuis le CHU de Tanger, le Laboratoire International est accessible en <strong>10 minutes en voiture</strong>. Nous sommes situés Avenue Moulay Rachid.</p>

<p><a href="/fr/contact/">Contactez-nous</a> pour plus d'informations ou consultez notre <a href="/fr/services/">liste complète de services</a>.</p>""",
        'content_en': """<h2>Medical laboratory near Tangier University Hospital (CHU)</h2>

<p>Located near <strong>Tangier University Hospital (CHU)</strong>, <strong>Laboratoire International</strong> offers a fast and comfortable alternative for your medical tests. Results in hours instead of days, no long queues, extended opening hours.</p>

<p><a href="/en/contact/">Contact us</a> for more information or see our <a href="/en/services/">full list of services</a>.</p>""",
        'content_ar': """<h2>مختبر تحاليل طبية قرب المستشفى الجامعي بطنجة</h2>

<p>يقع <strong>المختبر الدولي</strong> بالقرب من <strong>المستشفى الجامعي بطنجة</strong>، ويوفر بديلاً سريعاً ومريحاً لتحاليلكم الطبية. نتائج خلال ساعات، بدون طوابير طويلة.</p>

<p><a href="/ar/contact/">تواصلوا معنا</a> لمزيد من المعلومات.</p>""",
    },
]


class Command(BaseCommand):
    help = 'Create 3 neighborhood pages for local SEO targeting'

    def handle(self, *args, **options):
        for nb_data in NEIGHBORHOODS:
            page, created = NeighborhoodPage.objects.update_or_create(
                slug=nb_data['slug'],
                defaults=nb_data
            )
            status = 'CREATED' if created else 'UPDATED'
            self.stdout.write(f'  {status}: {page.name_fr}')

        total = NeighborhoodPage.objects.count()
        self.stdout.write(self.style.SUCCESS(f'\nDone! {total} neighborhood pages.'))
