"""
Data migration: populate default BlogCategory and first BlogPost.
"""
from django.db import migrations
from django.utils import timezone

def create_blog_data(apps, schema_editor):
    BlogCategory = apps.get_model('core', 'BlogCategory')
    BlogPost = apps.get_model('core', 'BlogPost')
    
    # 1. Create Category
    category, created = BlogCategory.objects.get_or_create(
        slug='sante-prevention',
        defaults={
            'name_fr': 'Santé & Prévention',
            'name_en': 'Health & Prevention',
            'name_ar': 'الصحة والوقاية',
            'name_es': 'Salud y Prevención',
            'name_de': 'Gesundheit & Prävention',
            'name_nl': 'Gezondheid & Preventie',
            'name_it': 'Salute e Prevenzione',
            'icon': 'fas fa-heartbeat',
            'order': 1
        }
    )
    
    # 2. Create Blog Post
    title_fr = "L'importance du bilan sanguin annuel : un guide complet"
    excerpt_fr = "Découvrez pourquoi un bilan sanguin annuel est essentiel pour surveiller votre santé, détecter les maladies précocement et optimiser votre bien-être."
    content_fr = (
        "<p>Le bilan sanguin annuel est l'un des outils de médecine préventive les plus puissants dont nous disposons aujourd'hui. Souvent perçu comme une simple routine, il constitue en réalité une véritable fenêtre ouverte sur le fonctionnement interne de votre organisme.</p>"
        "<h2>Pourquoi faire un bilan sanguin annuel ?</h2>"
        "<p>Un bilan sanguin permet de détecter des déséquilibres ou des anomalies bien avant l'apparition des premiers symptômes. C'est particulièrement vrai pour des affections silencieuses comme le cholestérol élevé, le prédiabète ou certaines carences en vitamines.</p>"
        "<ul>"
        "<li><strong>Prévention active :</strong> Repérer les facteurs de risque cardiovasculaire ou métabolique.</li>"
        "<li><strong>Suivi personnalisé :</strong> Établir votre ligne de base pour comparer vos résultats d'une année sur l'autre.</li>"
        "<li><strong>Optimisation de la vitalité :</strong> Identifier les carences (fer, vitamine D) qui affectent votre énergie quotidienne.</li>"
        "</ul>"
        "<h2>Les principaux marqueurs analysés</h2>"
        "<p>Un bilan complet comprend généralement :</p>"
        "<p>1. <strong>La Numération Formule Sanguine (NFS) :</strong> pour évaluer les globules rouges, blancs et les plaquettes (détection de l'anémie ou d'infections).</p>"
        "<p>2. <strong>Le bilan lipidique :</strong> mesure du cholestérol LDL, HDL et des triglycérides pour évaluer la santé cardiovasculaire.</p>"
        "<p>3. <strong>La glycémie à jeun :</strong> pour le dépistage précoce du diabète.</p>"
        "<p>4. <strong>Les bilans rénal et hépatique :</strong> pour s'assurer du bon fonctionnement des reins et du foie.</p>"
        "<p>Prenez soin de votre santé : planifiez votre bilan annuel dès aujourd'hui. Nos biologistes au Laboratoire International sont à votre disposition pour vous accompagner.</p>"
    )
    
    # English
    title_en = "The Importance of an Annual Blood Test: A Complete Guide"
    excerpt_en = "Discover why an annual blood test is essential for monitoring your health, detecting diseases early, and optimizing your well-being."
    content_en = (
        "<p>An annual blood test is one of the most powerful preventive medicine tools we have today. Often perceived as a simple routine, it is in reality a window into the inner workings of your body.</p>"
        "<h2>Why have an annual blood test?</h2>"
        "<p>A blood test can detect imbalances or abnormalities long before the first symptoms appear. This is especially true for silent conditions such as high cholesterol, prediabetes, or vitamin deficiencies.</p>"
        "<ul>"
        "<li><strong>Active prevention:</strong> Identify cardiovascular or metabolic risk factors.</li>"
        "<li><strong>Personalized follow-up:</strong> Establish your baseline to compare your results from year to year.</li>"
        "<li><strong>Vitality optimization:</strong> Identify deficiencies (iron, vitamin D) that affect your daily energy.</li>"
        "</ul>"
        "<h2>The main markers analyzed</h2>"
        "<p>A complete profile generally includes:</p>"
        "<p>1. <strong>Complete Blood Count (CBC):</strong> to evaluate red cells, white cells, and platelets (detection of anemia or infections).</p>"
        "<p>2. <strong>Lipid panel:</strong> measurement of LDL, HDL cholesterol, and triglycerides to assess cardiovascular health.</p>"
        "<p>3. <strong>Fasting blood glucose:</strong> for early screening of diabetes.</p>"
        "<p>4. <strong>Renal and liver function panels:</strong> to ensure proper kidney and liver performance.</p>"
        "<p>Take care of your health: plan your annual check-up today. Our specialists at International Laboratory are here to guide you.</p>"
    )
    
    # Arabic
    title_ar = "أهمية فحص الدم السنوي: دليل شامل"
    excerpt_ar = "اكتشف لماذا يعتبر فحص الدم السنوي ضروريًا لمراقبة صحتك، والكشف المبكر عن الأمراض، وتحسين سلامتك."
    content_ar = (
        "<p>يعتبر فحص الدم السنوي أحد أقوى أدوات الطب الوقائي المتاحة لنا اليوم. وغالبًا ما يُنظر إليه على أنه مجرد روتين بسيط، لكنه في الواقع يمثل نافذة حقيقية على الأداء الداخلي لجسمك.</p>"
        "<h2>لماذا يجب إجراء فحص دم سنوي؟</h2>"
        "<p>يسمح فحص الدم بالكشف عن الاختلالات أو الاضطرابات قبل وقت طويل من ظهور الأعراض الأولى. ينطبق هذا بشكل خاص على الحالات الصامتة مثل ارتفاع الكوليسترول، أو مقدمات السكري، أو بعض نقص الفيتامينات.</p>"
        "<ul>"
        "<li><strong>الوقاية النشطة:</strong> تحديد عوامل الخطر القلبية الوعائية أو التمثيل الغذائي.</li>"
        "<li><strong>المتابعة الشخصية:</strong> تحديد خط الأساس الخاص بك لمقارنة نتائجك من سنة إلى أخرى.</li>"
        "<li><strong>تحسين الحيوية:</strong> تحديد حالات النقص (مثل الحديد، فيتامين د) التي تؤثر على طاقتك اليومية.</li>"
        "</ul>"
        "<h2>أهم المؤشرات التي يتم تحليلها</h2>"
        "<p>يتضمن الفحص الشامل عادةً ما يلي:</p>"
        "<p>1. <strong>تعداد الدم الكامل (NFS):</strong> لتقييم خلايا الدم الحمراء والبيضاء والصفائح الدموية (الكشف عن فقر الدم أو الالتهابات).</p>"
        "<p>2. <strong>فحص الدهون:</strong> قياس الكوليسترول الضار والنافع والدهون الثلاثية لتقييم صحة القلب والشرايين.</p>"
        "<p>3. <strong>سكر الدم صائم:</strong> للكشف المبكر عن مرض السكري.</p>"
        "<p>4. <strong>وظائف الكلى والكبد:</strong> لضمان عمل الكلى والكبد بشكل سليم.</p>"
        "<p>اعتني بصحتك: خطط لفحصك السنوي اليوم. طاقمنا في المختبر الدولي رهن إشارتكم لمرافقتكم.</p>"
    )
    
    # Spanish
    title_es = "La importancia del análisis de sangre anual: una guía completa"
    excerpt_es = "Descubra por qué un análisis de sangre anual es esencial para controlar su salud, detectar enfermedades a tiempo y optimizar su bienestar."
    content_es = (
        "<p>El análisis de sangre anual es una de las herramientas de medicina preventiva más potentes de las que disponemos hoy en día. A menudo percibido como una simple rutina, es en realidad una ventana abierta al funcionamiento interno de su cuerpo.</p>"
        "<h2>¿Por qué hacerse un análisis de sangre anual?</h2>"
        "<p>Un análisis de sangre permite detectar desequilibrios o anomalías mucho antes de que aparezcan los primeros síntomas. Esto es especialmente cierto en el caso de afecciones silenciosas como el colesterol alto, la prediabetes o ciertas deficiencias vitamínicas.</p>"
        "<ul>"
        "<li><strong>Prevención activa:</strong> Identificar factores de riesgo cardiovascular o metabólico.</li>"
        "<li><strong>Seguimiento personalizado:</strong> Establecer su línea base para comparar sus resultados de un año a otro.</li>"
        "<li><strong>Optimización de la vitalidad:</strong> Identificar deficiencias (hierro, vitamina D) que afectan su energía diaria.</li>"
        "</ul>"
        "<h2>Los principales marcadores analizados</h2>"
        "<p>Un perfil completo suele incluir:</p>"
        "<p>1. <strong>Hemograma completo:</strong> para evaluar glóbulos rojos, blancos y plaquetas (detección de anemia o infecciones).</p>"
        "<p>2. <strong>Perfil lipídico:</strong> medición de colesterol LDL, HDL y triglicéridos para evaluar la salud cardiovascular.</p>"
        "<p>3. <strong>Glucemia en ayunas:</strong> para la detección temprana de la diabetes.</p>"
        "<p>4. <strong>Pruebas de función renal y hepática:</strong> para asegurar el buen funcionamiento de los riñones y el hígado.</p>"
        "<p>Cuide su salud: planifique su chequeo anual hoy mismo. Nuestros especialistas en Laboratorio Internacional están a su disposición.</p>"
    )
    
    # German
    title_de = "Die Bedeutung des jährlichen Bluttests: Ein umfassender Leitfaden"
    excerpt_de = "Erfahren Sie, warum ein jährlicher Bluttest für die Überwachung Ihrer Gesundheit, die Früherkennung von Krankheiten und die Optimierung Ihres Wohlbefindens unerlässlich ist."
    content_de = (
        "<p>Der jährliche Bluttest ist eines der wirksamsten Instrumente der Vorsorgemedizin, die uns heute zur Verfügung stehen. Oft als einfache Routine wahrgenommen, ist er in Wirklichkeit ein Fenster in das Innere Ihres Körpers.</p>"
        "<h2>Warum ist ein jährlicher Bluttest sinnvoll?</h2>"
        "<p>Ein Bluttest kann Ungleichgewichte oder Anomalien erkennen, lange bevor erste Symptome auftreten. Dies gilt insbesondere für stille Erkrankungen wie hohen Cholesterinspiegel, Prädiabetes oder Vitaminmängel.</p>"
        "<ul>"
        "<li><strong>Aktive Vorsorge:</strong> Erkennung von kardiovaskulären oder metabolischen Risikofaktoren.</li>"
        "<li><strong>Persönliche Nachsorge:</strong> Erstellung Ihres Ausgangswerts, um Ihre Ergebnisse von Jahr zu Jahr zu vergleichen.</li>"
        "<li><strong>Optimierung der Vitalität:</strong> Identifizierung von Mängeln (Eisen, Vitamin D), die Ihre tägliche Energie beeinträchtigen.</li>"
        "</ul>"
        "<h2>Die wichtigsten analysierten Marker</h2>"
        "<p>Ein vollständiges Profil umfasst in der Regel:</p>"
        "<p>1. <strong>Kleines/Großes Blutbild (NFS):</strong> zur Bewertung der roten und weißen Blutkörperchen sowie der Blutplättchen (Erkennung von Anämie oder Infektionen).</p>"
        "<p>2. <strong>Lipidprofil:</strong> Messung von LDL- und HDL-Cholesterin sowie Triglyceriden zur Beurteilung der kardiovaskulären Gesundheit.</p>"
        "<p>3. <strong>Nüchternblutzucker:</strong> zur Früherkennung von Diabetes.</p>"
        "<p>4. <strong>Nieren- und Leberwerte:</strong> um die ordnungsgemäße Funktion von Nieren und Leber sicherzustellen.</p>"
        "<p>Achten Sie auf Ihre Gesundheit: Planen Sie Ihre jährliche Untersuchung noch heute. Unsere Spezialisten im Internationalen Labor sind für Sie da.</p>"
    )
    
    # Dutch
    title_nl = "Het belang van een jaarlijks bloedonderzoek: een complete gids"
    excerpt_nl = "Ontdek waarom een jaarlijks bloedonderzoek essentieel is voor het monitoren van uw gezondheid, het vroegtijdig opsporen van ziekten en het optimaliseren van uw welzijn."
    content_nl = (
        "<p>Een jaarlijks bloedonderzoek is een van de krachtigste preventieve hulpmiddelen die we vandaag de dag hebben. Vaak gezien als een simpele routine, is het in werkelijkheid een venster op de interne werking van uw lichaam.</p>"
        "<h2>Waarom een jaarlijks bloedonderzoek laten doen?</h2>"
        "<p>Een bloedtest kan onevenwichtigheden of afwijkingen opsporen lang voordat de eerste symptomen optreden. Dit geldt met nationaal referentielaboratorium, prediabetes of vitaminegebrek.</p>"
        "<ul>"
        "<li><strong>Actieve preventie:</strong> Identificeer cardiovasculaire of metabole risicofactoren.</li>"
        "<li><strong>Gepersonaliseerde opvolging:</strong> Stel uw basislijn vast om uw resultaten van jaar tot jaar te vergelijken.</li>"
        "<li><strong>Optimalisatie van vitaliteit:</strong> Identificeer tekorten (ijzer, vitamine D) die uw dagelijkse energie beïnvloeden.</li>"
        "</ul>"
        "<h2>De belangrijkste geanalyseerde markers</h2>"
        "<p>Een compleet profiel omvat over het algemeen:</p>"
        "<p>1. <strong>Volledig bloedbeeld (NFS):</strong> om rode en witte bloedcellen en bloedplaatjes te evalueren (opsporing van bloedarmoede of infecties).</p>"
        "<p>2. <strong>Lipidenprofiel:</strong> meting van LDL-, HDL-cholesterol en triglyceriden om de cardiovasculaire gezondheid te beoordelen.</p>"
        "<p>3. <strong>Nuchtere bloedsuikerspiegel:</strong> voor vroege opsporing van diabetes.</p>"
        "<p>4. <strong>Nier- en leverfunctietests:</strong> om te zorgen voor een goede werking van nieren en lever.</p>"
        "<p>Zorg voor uw gezondheid: plan vandaag nog uw jaarlijkse controle. Onze specialisten bij het Internationaal Laboratorium staan voor u klaar.</p>"
    )
    
    # Italian
    title_it = "L'importanza dell'esame del sangue annuale: una guida completa"
    excerpt_it = "Scopri perché un esame del sangue annuale è essenziale per monitorare la tua salute, rilevare precocemente le malattie e ottimizzare il tuo benessere."
    content_it = (
        "<p>L'esame del sangue annuale è uno degli strumenti di medicina preventiva più potenti che abbiamo oggi. Spesso percepito come una semplice routine, è in realtà una finestra aperta sul funzionamento interno del tuo corpo.</p>"
        "<h2>Perché fare un esame del sangue annuale?</h2>"
        "<p>Un esame del sangue consente di rilevare squilibri o anomalie molto prima che compaiano i primi sintomi. Ciò è particolarmente vero per condizioni silenziose come il colesterolo alto, il prediabete o alcune carenze vitaminiche.</p>"
        "<ul>"
        "<li><strong>Prevenzione attiva:</strong> Identificare i fattori di rischio cardiovascolare o metabolico.</li>"
        "<li><strong>Monitoraggio personalizzato:</strong> Stabilire la tua linea di base per confrontare i risultati anno dopo anno.</li>"
        "<li><strong>Ottimizzazione della vitalità:</strong> Identificare carenze (ferro, vitamina D) che influenzano la tua energia quotidiana.</li>"
        "</ul>"
        "<h2>I principali marcatori analizzati</h2>"
        "<p>Un profilo completo di solito include:</p>"
        "<p>1. <strong>Emocromo completo:</strong> per valutare globuli rossi, bianchi e piastrine (rilevazione di anemia o infezioni).</p>"
        "<p>2. <strong>Profilo lipidico:</strong> misurazione del colesterolo LDL, HDL e trigliceridi per valutare la salute cardiovascolare.</p>"
        "<p>3. <strong>Glicemia a diurno:</strong> per lo screening precoce del diabete.</p>"
        "<p>4. <strong>Esami della funzionalità renale ed epatica:</strong> per garantire il corretto funzionamento dei reni e del fegato.</p>"
        "<p>Prenditi cura della tua salute: pianifica oggi stesso il tuo controllo annuale. I nostri specialisti presso il Laboratorio Internazionale sono a tua disposizione.</p>"
    )

    if not BlogPost.objects.filter(slug='importance-bilan-sanguin-annuel').exists():
        BlogPost.objects.create(
            slug='importance-bilan-sanguin-annuel',
            status='published',
            category=category,
            author='Laboratoire International',
            tags='Bilan Sanguin, Prévention, Santé',
            is_featured=True,
            published_at=timezone.now(),
            
            title_fr=title_fr, excerpt_fr=excerpt_fr, content_fr=content_fr,
            title_en=title_en, excerpt_en=excerpt_en, content_en=content_en,
            title_ar=title_ar, excerpt_ar=excerpt_ar, content_ar=content_ar,
            title_es=title_es, excerpt_es=excerpt_es, content_es=content_es,
            title_de=title_de, excerpt_de=excerpt_de, content_de=content_de,
            title_nl=title_nl, excerpt_nl=excerpt_nl, content_nl=content_nl,
            title_it=title_it, excerpt_it=excerpt_it, content_it=content_it,
        )

def remove_blog_data(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_update_team_member'),
    ]

    operations = [
        migrations.RunPython(create_blog_data, remove_blog_data),
    ]
