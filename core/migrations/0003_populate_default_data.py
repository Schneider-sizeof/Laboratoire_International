"""
Data migration: populate default SiteSettings, TeamMember, and Partner records.
"""
from django.db import migrations


def create_defaults(apps, schema_editor):
    SiteSettings = apps.get_model('core', 'SiteSettings')
    TeamMember = apps.get_model('core', 'TeamMember')
    Partner = apps.get_model('core', 'Partner')

    # Create singleton SiteSettings
    if not SiteSettings.objects.exists():
        SiteSettings.objects.create(pk=1)

    # Create default team members
    if not TeamMember.objects.exists():
        TeamMember.objects.create(
            name='Dr. Youssef El Mansouri',
            initials='YM',
            role_fr='Directeur Général & Biologiste',
            role_en='General Director & Biologist',
            role_ar='المدير العام وعالم الأحياء',
            role_es='Director General y Biólogo',
            role_de='Generaldirektor & Biologe',
            role_nl='Algemeen Directeur & Bioloog',
            role_it='Direttore Generale e Biologo',
            bio_fr="Plus de 20 ans d'expérience en biologie médicale. Diplômé de la Faculté de Médecine et Pharmacie de Rabat.",
            bio_en="Over 20 years of experience in medical biology. Graduate of the Faculty of Medicine and Pharmacy of Rabat.",
            bio_ar="أكثر من 20 عامًا من الخبرة في البيولوجيا الطبية. خريج كلية الطب والصيدلة بالرباط.",
            bio_es="Más de 20 años de experiencia en biología médica. Graduado de la Facultad de Medicina y Farmacia de Rabat.",
            bio_de="Über 20 Jahre Erfahrung in der medizinischen Biologie. Absolvent der Fakultät für Medizin und Pharmazie in Rabat.",
            bio_nl="Meer dan 20 jaar ervaring in medische biologie. Afgestudeerd aan de Faculteit Geneeskunde en Farmacie van Rabat.",
            bio_it="Oltre 20 anni di esperienza in biologia medica. Laureato presso la Facoltà di Medicina e Farmacia di Rabat.",
            order=1,
        )
        TeamMember.objects.create(
            name='Dr. Fatima Zahra Benali',
            initials='FB',
            role_fr='Biologiste Spécialiste',
            role_en='Specialist Biologist',
            role_ar='أخصائية في علم الأحياء',
            role_es='Bióloga Especialista',
            role_de='Fachbiologin',
            role_nl='Specialist Bioloog',
            role_it='Biologa Specialista',
            bio_fr="Spécialiste en hématologie et immunologie. Formation complémentaire à l'Institut Pasteur de Paris.",
            bio_en="Specialist in hematology and immunology. Additional training at the Pasteur Institute in Paris.",
            bio_ar="متخصصة في أمراض الدم والمناعة. تدريب إضافي في معهد باستور بباريس.",
            bio_es="Especialista en hematología e inmunología. Formación complementaria en el Instituto Pasteur de París.",
            bio_de="Spezialistin für Hämatologie und Immunologie. Zusatzausbildung am Institut Pasteur in Paris.",
            bio_nl="Specialist in hematologie en immunologie. Aanvullende opleiding bij het Pasteur Instituut in Parijs.",
            bio_it="Specialista in ematologia e immunologia. Formazione complementare presso l'Istituto Pasteur di Parigi.",
            order=2,
        )
        TeamMember.objects.create(
            name='Dr. Karim Tazi',
            initials='KT',
            role_fr='Responsable Qualité',
            role_en='Quality Manager',
            role_ar='مسؤول الجودة',
            role_es='Responsable de Calidad',
            role_de='Qualitätsmanager',
            role_nl='Kwaliteitsmanager',
            role_it='Responsabile Qualità',
            bio_fr="Expert en assurance qualité des laboratoires. Certifié ISO 15189 et accrédité COFRAC.",
            bio_en="Expert in laboratory quality assurance. ISO 15189 certified and COFRAC accredited.",
            bio_ar="خبير في ضمان جودة المختبرات. حاصل على شهادة ISO 15189 واعتماد COFRAC.",
            bio_es="Experto en aseguramiento de calidad de laboratorios. Certificado ISO 15189 y acreditado COFRAC.",
            bio_de="Experte für Qualitätssicherung in Laboratorien. ISO 15189 zertifiziert und COFRAC akkreditiert.",
            bio_nl="Expert in kwaliteitsborging van laboratoria. ISO 15189 gecertificeerd en COFRAC geaccrediteerd.",
            bio_it="Esperto in garanzia della qualità dei laboratori. Certificato ISO 15189 e accreditato COFRAC.",
            order=3,
        )

    # Create default partners
    if not Partner.objects.exists():
        Partner.objects.create(
            name='Cerba Lab',
            icon='fas fa-globe-europe',
            description_fr="Réseau européen de diagnostic de référence. Leader en biologie spécialisée avec plus de 50 ans d'expertise.",
            description_en="European reference diagnostic network. Leader in specialized biology with over 50 years of expertise.",
            description_ar="شبكة التشخيص المرجعية الأوروبية. رائدة في علم الأحياء المتخصص مع أكثر من 50 عامًا من الخبرة.",
            description_es="Red europea de diagnóstico de referencia. Líder en biología especializada con más de 50 años de experiencia.",
            description_de="Europäisches Referenz-Diagnostiknetzwerk. Marktführer in spezialisierter Biologie mit über 50 Jahren Erfahrung.",
            description_nl="Europees referentie diagnostisch netwerk. Marktleider in gespecialiseerde biologie met meer dan 50 jaar ervaring.",
            description_it="Rete diagnostica europea di riferimento. Leader nella biologia specializzata con oltre 50 anni di esperienza.",
            order=1,
        )
        Partner.objects.create(
            name='Laboratoire National Mohammed VI',
            icon='fas fa-landmark',
            description_fr="Laboratoire national de référence du Maroc. Partenaire pour les analyses spécialisées et le contrôle qualité.",
            description_en="Morocco's national reference laboratory. Partner for specialized analyses and quality control.",
            description_ar="المختبر الوطني المرجعي بالمغرب. شريك في التحاليل المتخصصة ومراقبة الجودة.",
            description_es="Laboratorio nacional de referencia de Marruecos. Socio para análisis especializados y control de calidad.",
            description_de="Marokkos nationales Referenzlabor. Partner für spezialisierte Analysen und Qualitätskontrolle.",
            description_nl="Nationaal referentielaboratorium van Marokko. Partner voor gespecialiseerde analyses en kwaliteitscontrole.",
            description_it="Laboratorio nazionale di riferimento del Marocco. Partner per analisi specializzate e controllo qualità.",
            order=2,
        )


def reverse_defaults(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_partner_sitesettings_teammember_blogcategory_name_it_and_more'),
    ]

    operations = [
        migrations.RunPython(create_defaults, reverse_defaults),
    ]
