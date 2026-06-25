"""
Management command to create 10 SEO-optimized blog articles.
Each article targets local search queries related to medical analyses in Tanger.
"""
from django.core.management.base import BaseCommand
from django.utils import timezone
from core.models import BlogPost, BlogCategory


BLOG_POSTS = [
    {
        'slug': 'bilan-thyroidien-tanger',
        'category_slug': 'sante',
        'title_fr': 'Où faire un bilan thyroïdien à Tanger ?',
        'title_en': 'Where to get a thyroid test in Tangier?',
        'title_ar': 'أين تجري تحليل الغدة الدرقية في طنجة؟',
        'excerpt_fr': 'Découvrez tout sur le bilan thyroïdien à Tanger : TSH, T3, T4, prix, délais et où réaliser votre analyse.',
        'meta_description_fr': 'Bilan thyroïdien à Tanger : TSH, T3, T4 libre. Résultats en 24h au Laboratoire International. Découvrez pourquoi et quand faire ce test.',
        'content_fr': """<h2>Le bilan thyroïdien : un examen essentiel à Tanger</h2>

<p>La thyroïde est une petite glande située à la base du cou qui joue un rôle fondamental dans le métabolisme de l'organisme. Un dysfonctionnement thyroïdien peut affecter l'énergie, le poids, l'humeur et même la fertilité. Au <strong>Laboratoire International de Tanger</strong>, nous réalisons quotidiennement des bilans thyroïdiens complets avec des résultats fiables.</p>

<h2>Que comprend un bilan thyroïdien ?</h2>

<p>Le bilan thyroïdien standard comprend trois dosages principaux :</p>
<ul>
<li><strong>TSH (Thyréostimuline)</strong> : c'est le marqueur le plus important. Un taux élevé suggère une hypothyroïdie, un taux bas une hyperthyroïdie.</li>
<li><strong>T4 libre (Thyroxine)</strong> : hormone directement produite par la thyroïde. Son dosage complète l'interprétation de la TSH.</li>
<li><strong>T3 libre (Triiodothyronine)</strong> : forme active de l'hormone thyroïdienne dans les tissus.</li>
</ul>

<h2>Quand faut-il faire un bilan thyroïdien ?</h2>

<p>Votre médecin peut vous prescrire ce bilan en cas de :</p>
<ul>
<li>Fatigue persistante et inexpliquée</li>
<li>Prise ou perte de poids sans raison apparente</li>
<li>Troubles de l'humeur (anxiété, dépression)</li>
<li>Palpitations cardiaques</li>
<li>Problèmes de fertilité ou troubles du cycle menstruel</li>
<li>Antécédents familiaux de maladies thyroïdiennes</li>
</ul>

<h3>Les femmes sont plus touchées</h3>

<p>Les troubles thyroïdiens sont <strong>5 à 8 fois plus fréquents chez les femmes</strong> que chez les hommes. Un dépistage est particulièrement recommandé pendant la grossesse, car l'hypothyroïdie non traitée peut affecter le développement du fœtus.</p>

<h2>Comment se déroule l'examen au Laboratoire International de Tanger ?</h2>

<p>Le bilan thyroïdien est réalisé par une simple <strong>prise de sang</strong>. Aucune préparation spéciale n'est nécessaire : vous pouvez manger et boire normalement avant le prélèvement. Nous vous accueillons du lundi au vendredi de 7h à 19h et le samedi de 7h à 15h.</p>

<h3>Délai des résultats</h3>

<p>Les résultats de votre bilan thyroïdien sont disponibles en <strong>moins de 24 heures</strong>. Vous pouvez les consulter en ligne via notre portail sécurisé ou les récupérer directement au laboratoire.</p>

<h2>Pourquoi choisir le Laboratoire International de Tanger ?</h2>

<p>Situé <strong>Avenue Moulay Rachid à Tanger</strong>, notre laboratoire dispose d'équipements de dernière génération pour garantir la précision de vos résultats. Notre équipe de biologistes expérimentés est à votre disposition pour interpréter vos résultats et vous orienter.</p>

<p>Pour prendre rendez-vous ou obtenir plus d'informations, <a href="/fr/contact/">contactez-nous</a> par téléphone ou WhatsApp. Vous pouvez également consulter notre page dédiée au <a href="/fr/analyse/bilan-thyroidien-tsh-t3-t4-tanger/">bilan thyroïdien</a> pour plus de détails.</p>""",
        'content_en': """<h2>Thyroid testing: an essential check-up in Tangier</h2>

<p>The thyroid is a small gland at the base of the neck that plays a fundamental role in the body's metabolism. At <strong>Laboratoire International in Tangier</strong>, we perform complete thyroid panels daily with reliable results in under 24 hours.</p>

<h2>What does a thyroid panel include?</h2>

<p>A standard thyroid panel includes three main tests: <strong>TSH</strong> (the most important marker), <strong>Free T4</strong> (thyroxine produced by the thyroid), and <strong>Free T3</strong> (the active form of thyroid hormone).</p>

<h2>When should you get tested?</h2>

<p>Your doctor may prescribe this panel for persistent fatigue, unexplained weight changes, mood disorders, heart palpitations, fertility problems, or family history of thyroid disease. Women are 5-8 times more likely to develop thyroid disorders.</p>

<h2>Why choose Laboratoire International in Tangier?</h2>

<p>Located on Avenue Moulay Rachid in Tangier, our laboratory has state-of-the-art equipment. Results are available in less than 24 hours. <a href="/en/contact/">Contact us</a> to schedule your appointment.</p>""",
        'content_ar': """<h2>تحليل الغدة الدرقية في طنجة</h2>

<p>الغدة الدرقية غدة صغيرة تقع في قاعدة العنق وتلعب دوراً أساسياً في عملية الأيض. في <strong>المختبر الدولي بطنجة</strong>، نجري تحاليل الغدة الدرقية الشاملة يومياً مع نتائج موثوقة.</p>

<h2>ماذا يشمل تحليل الغدة الدرقية؟</h2>

<p>يشمل التحليل: <strong>TSH</strong> (أهم مؤشر)، <strong>T4 الحر</strong>، و<strong>T3 الحر</strong>. النتائج متوفرة خلال أقل من 24 ساعة.</p>

<p>للحصول على موعد، <a href="/ar/contact/">تواصلوا معنا</a> عبر الهاتف أو الواتساب.</p>""",
    },
    {
        'slug': 'prix-prise-de-sang-tanger',
        'category_slug': 'sante',
        'title_fr': 'Prise de sang à Tanger : guide complet',
        'title_en': 'Blood test in Tangier: complete guide',
        'title_ar': 'تحليل الدم في طنجة: دليل شامل',
        'excerpt_fr': 'Tout savoir sur la prise de sang à Tanger : préparation, types d\'analyses, délais et où faire votre bilan sanguin.',
        'meta_description_fr': 'Prise de sang à Tanger : préparation, analyses disponibles, délais de résultats. Laboratoire International, Avenue Moulay Rachid.',
        'content_fr': """<h2>La prise de sang : un geste simple et essentiel</h2>

<p>La prise de sang est l'acte médical le plus courant en biologie médicale. Au <strong>Laboratoire International de Tanger</strong>, nos préleveurs expérimentés réalisent des centaines de prélèvements chaque jour dans les meilleures conditions de confort et d'hygiène.</p>

<h2>Comment se préparer à une prise de sang ?</h2>

<p>La préparation dépend du type d'analyse prescrite :</p>
<ul>
<li><strong>Glycémie à jeun</strong> : 8 à 12 heures de jeûne (eau autorisée)</li>
<li><strong>Bilan lipidique</strong> : 12 heures de jeûne recommandées</li>
<li><strong>NFS, sérologies, hormones</strong> : pas de jeûne nécessaire en général</li>
<li><strong>Bilan thyroïdien</strong> : prélèvement possible à tout moment</li>
</ul>

<h3>Conseils pratiques</h3>

<p>Pensez à <strong>bien vous hydrater</strong> la veille du prélèvement (l'eau est toujours autorisée même à jeun). Apportez votre ordonnance et votre carte d'identité. Si vous prenez des médicaments, signalez-le au préleveur.</p>

<h2>Quelles analyses peut-on réaliser avec une prise de sang ?</h2>

<p>Notre laboratoire propose plus de <strong>200 types d'analyses</strong> à partir d'un simple prélèvement sanguin :</p>
<ul>
<li><strong>Biochimie</strong> : glycémie, bilan lipidique, bilan hépatique, bilan rénal</li>
<li><strong>Hématologie</strong> : NFS, VS, bilan de coagulation</li>
<li><strong>Sérologie</strong> : hépatites, HIV, toxoplasmose, rubéole</li>
<li><strong>Hormonologie</strong> : thyroïde, hormones féminines, Beta-HCG</li>
<li><strong>PCR</strong> : hépatite B/C, HPV, COVID-19</li>
</ul>

<h2>Délais de résultats</h2>

<p>La plupart de nos résultats sont disponibles en <strong>moins de 24 heures</strong>. Les analyses de routine (NFS, glycémie) peuvent être prêtes en 2 à 4 heures. Les analyses spécialisées (PCR, cultures) nécessitent 2 à 5 jours.</p>

<h2>Où faire sa prise de sang à Tanger ?</h2>

<p>Le <strong>Laboratoire International</strong> est situé Avenue Moulay Rachid, au cœur de Tanger. Nous sommes ouverts du lundi au vendredi de 7h à 19h et le samedi de 7h à 15h. Aucun rendez-vous n'est nécessaire pour les prélèvements simples.</p>

<p>Pour plus d'informations, consultez notre <a href="/fr/services/">liste complète de services</a> ou <a href="/fr/contact/">contactez-nous</a>.</p>""",
        'content_en': '<h2>Blood tests at Laboratoire International Tangier</h2><p>Our experienced phlebotomists perform hundreds of blood draws daily. Most results are available in under 24 hours. We offer over 200 types of analyses. Located on Avenue Moulay Rachid, open Monday-Friday 7am-7pm, Saturday 7am-3pm. <a href="/en/contact/">Contact us</a> for more information.</p>',
        'content_ar': '<h2>تحليل الدم في المختبر الدولي بطنجة</h2><p>يقوم فريقنا المتمرس بإجراء مئات التحاليل يومياً. معظم النتائج متاحة خلال أقل من 24 ساعة. نوفر أكثر من 200 نوع من التحاليل. <a href="/ar/contact/">تواصلوا معنا</a> لمزيد من المعلومات.</p>',
    },
    {
        'slug': 'spermogramme-tanger-deroulement',
        'category_slug': 'sante',
        'title_fr': 'Spermogramme à Tanger : comment ça se passe ?',
        'title_en': 'Semen analysis in Tangier: what to expect',
        'title_ar': 'تحليل السائل المنوي في طنجة: كيف يتم؟',
        'excerpt_fr': 'Guide complet sur le spermogramme à Tanger : préparation, déroulement, résultats et interprétation.',
        'meta_description_fr': 'Spermogramme à Tanger : préparation, déroulement et résultats au Laboratoire International. Bilan de fertilité masculine complet.',
        'content_fr': """<h2>Le spermogramme : examen clé de la fertilité masculine</h2>

<p>Le spermogramme est l'examen de première intention dans le bilan de fertilité masculine. Au <strong>Laboratoire International de Tanger</strong>, nous offrons des conditions optimales de recueil et d'analyse, avec des résultats détaillés selon les normes de l'OMS.</p>

<h2>Comment se préparer au spermogramme ?</h2>

<p>Pour des résultats fiables, il est recommandé de :</p>
<ul>
<li>Observer une <strong>abstinence sexuelle de 3 à 5 jours</strong> avant le recueil</li>
<li>Éviter l'alcool et le tabac dans les jours précédents</li>
<li>Signaler tout traitement médical en cours</li>
<li>Éviter la fièvre ou les bains chauds dans les semaines précédentes</li>
</ul>

<h2>Comment se déroule le recueil ?</h2>

<p>Le recueil se fait de préférence <strong>au laboratoire</strong>, dans une salle dédiée assurant intimité et confort. Le recueil sur place garantit les meilleures conditions d'analyse car l'échantillon est traité immédiatement. Si nécessaire, un recueil à domicile est possible sous certaines conditions (délai de transport inférieur à 30 minutes).</p>

<h2>Quels paramètres sont analysés ?</h2>

<p>Le spermogramme évalue plusieurs paramètres :</p>
<ul>
<li><strong>Volume</strong> de l'éjaculat (normal : 1,5 à 6 ml)</li>
<li><strong>Concentration</strong> en spermatozoïdes (normal : ≥15 millions/ml)</li>
<li><strong>Mobilité</strong> progressive (normal : ≥32%)</li>
<li><strong>Morphologie</strong> selon les critères stricts de Kruger</li>
<li><strong>Vitalité</strong> des spermatozoïdes</li>
</ul>

<h2>Délai et résultats</h2>

<p>Les résultats du spermogramme sont disponibles en <strong>24 à 48 heures</strong>. Un seul spermogramme anormal ne suffit pas à poser un diagnostic : un contrôle est généralement recommandé après 3 mois.</p>

<p>Pour prendre rendez-vous, <a href="/fr/contact/">contactez le Laboratoire International de Tanger</a>. Consultez aussi notre page sur le <a href="/fr/analyse/spermogramme-tanger/">spermogramme</a>.</p>""",
        'content_en': '<h2>Semen analysis at Laboratoire International Tangier</h2><p>We offer optimal conditions for sample collection and analysis according to WHO standards. Abstinence of 3-5 days is recommended. Results in 24-48 hours. <a href="/en/contact/">Contact us</a> for appointments.</p>',
        'content_ar': '<h2>تحليل السائل المنوي في المختبر الدولي بطنجة</h2><p>نوفر ظروفاً مثالية لجمع العينات والتحليل وفق معايير منظمة الصحة العالمية. النتائج خلال 24 إلى 48 ساعة. <a href="/ar/contact/">تواصلوا معنا</a> للمواعيد.</p>',
    },
    {
        'slug': 'pcr-hepatite-tanger-tout-savoir',
        'category_slug': 'sante',
        'title_fr': 'PCR hépatite à Tanger : tout ce qu\'il faut savoir',
        'title_en': 'Hepatitis PCR in Tangier: everything you need to know',
        'title_ar': 'تحليل PCR التهاب الكبد في طنجة: كل ما تحتاج معرفته',
        'excerpt_fr': 'Découvrez la PCR hépatite B et C à Tanger : indications, déroulement, charge virale et suivi au Laboratoire International.',
        'meta_description_fr': 'PCR hépatite B et C à Tanger : charge virale, suivi antiviral. Résultats en 3-5 jours au Laboratoire International.',
        'content_fr': """<h2>La PCR hépatite : un outil de diagnostic de précision</h2>

<p>La PCR (Polymerase Chain Reaction) est une technique de biologie moléculaire qui détecte et quantifie le matériel génétique du virus de l'hépatite B ou C dans le sang. Au <strong>Laboratoire International de Tanger</strong>, nous disposons d'équipements PCR de dernière génération pour des résultats fiables et précis.</p>

<h2>Quelle différence entre sérologie et PCR ?</h2>

<p>La <strong>sérologie</strong> détecte les anticorps produits par votre système immunitaire en réponse au virus. Elle indique si vous avez été exposé au virus. La <strong>PCR</strong> va plus loin : elle détecte directement le virus lui-même et mesure sa quantité (charge virale).</p>

<h2>Quand la PCR hépatite est-elle prescrite ?</h2>

<ul>
<li>Après une <strong>sérologie positive</strong> pour confirmer une infection active</li>
<li>Pour mesurer la <strong>charge virale</strong> avant le traitement</li>
<li>Pour <strong>surveiller l'efficacité</strong> du traitement antiviral</li>
<li>Pour vérifier la <strong>guérison virologique</strong> en fin de traitement</li>
</ul>

<h2>L'hépatite C est guérissable</h2>

<p>Grâce aux <strong>antiviraux à action directe</strong> (AAD), l'hépatite C est aujourd'hui guérissable dans plus de 95% des cas avec un traitement de 8 à 12 semaines. Le suivi par PCR est essentiel pour confirmer la guérison.</p>

<h2>Résultats et délais</h2>

<p>Les résultats de la PCR hépatite sont disponibles en <strong>3 à 5 jours ouvrables</strong>. La charge virale est exprimée en UI/ml (unités internationales par millilitre).</p>

<p>Pour plus d'informations, consultez nos pages sur la <a href="/fr/analyse/pcr-hepatite-b-c-tanger/">PCR hépatite</a> ou <a href="/fr/contact/">contactez-nous</a>.</p>""",
        'content_en': '<h2>Hepatitis PCR testing in Tangier</h2><p>PCR detects and quantifies hepatitis B or C viral genetic material. Results in 3-5 business days. Hepatitis C is now curable in over 95% of cases. <a href="/en/contact/">Contact us</a> at Laboratoire International for testing.</p>',
        'content_ar': '<h2>تحليل PCR التهاب الكبد في طنجة</h2><p>يكشف تحليل PCR عن المادة الوراثية لفيروس التهاب الكبد ب أو ج ويحدد كميتها. النتائج خلال 3 إلى 5 أيام. <a href="/ar/contact/">تواصلوا معنا</a> في المختبر الدولي.</p>',
    },
    {
        'slug': 'bilan-hormonal-feminin-tanger',
        'category_slug': 'sante',
        'title_fr': 'Bilan hormonal féminin à Tanger : quand et pourquoi ?',
        'title_en': 'Female hormone panel in Tangier: when and why?',
        'title_ar': 'تحليل الهرمونات الأنثوية في طنجة: متى ولماذا؟',
        'excerpt_fr': 'Guide complet du bilan hormonal féminin à Tanger : FSH, LH, estradiol, progestérone, AMH. Quand le faire et comment interpréter les résultats.',
        'meta_description_fr': 'Bilan hormonal féminin à Tanger : FSH, LH, estradiol, progestérone. Laboratoire International, résultats en 24h.',
        'content_fr': """<h2>Le bilan hormonal féminin : comprendre ses hormones</h2>

<p>Le bilan hormonal féminin est un ensemble d'analyses sanguines qui mesure les principales hormones impliquées dans le cycle menstruel et la fertilité. Au <strong>Laboratoire International de Tanger</strong>, nous réalisons ces dosages avec la plus grande précision.</p>

<h2>Quelles hormones sont dosées ?</h2>

<ul>
<li><strong>FSH (Hormone Folliculo-Stimulante)</strong> : stimule la croissance des follicules ovariens</li>
<li><strong>LH (Hormone Lutéinisante)</strong> : déclenche l'ovulation</li>
<li><strong>Estradiol (E2)</strong> : principale hormone féminine, produite par les ovaires</li>
<li><strong>Progestérone</strong> : prépare l'utérus à la nidation</li>
<li><strong>AMH (Hormone Anti-Müllérienne)</strong> : reflète la réserve ovarienne</li>
<li><strong>Prolactine</strong> : peut perturber le cycle si trop élevée</li>
</ul>

<h2>Quand réaliser le bilan ?</h2>

<p>Le moment du prélèvement est crucial :</p>
<ul>
<li><strong>FSH, LH, Estradiol</strong> : entre le 2ème et le 5ème jour du cycle</li>
<li><strong>Progestérone</strong> : au 21ème jour du cycle (phase lutéale)</li>
<li><strong>AMH, Prolactine</strong> : à tout moment du cycle</li>
</ul>

<h2>Pourquoi faire un bilan hormonal ?</h2>

<p>Ce bilan est prescrit en cas de :</p>
<ul>
<li>Difficultés à concevoir (infertilité)</li>
<li>Cycles irréguliers ou absence de règles</li>
<li>Préparation à une FIV ou stimulation ovarienne</li>
<li>Symptômes de ménopause précoce</li>
<li>Syndrome des ovaires polykystiques (SOPK)</li>
</ul>

<p>Consultez notre page sur le <a href="/fr/analyse/bilan-hormonal-feminin-tanger/">bilan hormonal féminin</a> ou <a href="/fr/contact/">prenez rendez-vous</a> au Laboratoire International de Tanger.</p>""",
        'content_en': '<h2>Female hormone panel in Tangier</h2><p>We measure FSH, LH, estradiol, progesterone, AMH, and prolactin. Timing is crucial — FSH/LH/estradiol on days 2-5 of cycle. Results in 24 hours. <a href="/en/contact/">Contact us</a> at Laboratoire International.</p>',
        'content_ar': '<h2>تحليل الهرمونات الأنثوية في طنجة</h2><p>نقيس FSH و LH والإستراديول والبروجسترون و AMH والبرولاكتين. النتائج خلال 24 ساعة. <a href="/ar/contact/">تواصلوا معنا</a> في المختبر الدولي بطنجة.</p>',
    },
    {
        'slug': 'test-grossesse-beta-hcg-tanger',
        'category_slug': 'sante',
        'title_fr': 'Test de grossesse sanguin (Beta HCG) à Tanger',
        'title_en': 'Blood pregnancy test (Beta HCG) in Tangier',
        'title_ar': 'تحليل الحمل (هرمون HCG) في طنجة',
        'excerpt_fr': 'Le test Beta HCG sanguin est le plus fiable pour confirmer une grossesse. Disponible au Laboratoire International de Tanger.',
        'meta_description_fr': 'Test de grossesse Beta HCG sanguin à Tanger. Résultats en 2-4h au Laboratoire International. Plus fiable que les tests urinaires.',
        'content_fr': """<h2>Le test Beta HCG : le test de grossesse le plus fiable</h2>

<p>Le dosage de la <strong>Beta-HCG</strong> (hormone chorionique gonadotrope) dans le sang est la méthode la plus fiable pour confirmer une grossesse. Contrairement aux tests urinaires vendus en pharmacie, le test sanguin est quantitatif : il mesure précisément le taux de l'hormone.</p>

<h2>Quand faire le test ?</h2>

<p>Le test Beta HCG sanguin peut détecter une grossesse <strong>dès 10 jours après la fécondation</strong>, soit environ 4 jours avant la date prévue des règles. Il est plus précoce et plus fiable que les tests urinaires.</p>

<h2>Comment interpréter les résultats ?</h2>

<ul>
<li><strong>Résultat négatif</strong> : taux inférieur à 5 UI/L</li>
<li><strong>Résultat positif</strong> : taux supérieur à 10 UI/L</li>
<li>En début de grossesse, le taux <strong>double environ toutes les 48 heures</strong></li>
</ul>

<h2>Résultats rapides</h2>

<p>Au <strong>Laboratoire International de Tanger</strong>, les résultats du test Beta HCG sont disponibles en <strong>2 à 4 heures</strong>. Pas besoin d'être à jeun pour ce prélèvement.</p>

<p>Pour plus d'informations, consultez notre page sur le <a href="/fr/analyse/beta-hcg-test-grossesse-tanger/">test Beta HCG</a> ou <a href="/fr/contact/">contactez-nous</a>.</p>""",
        'content_en': '<h2>Beta HCG blood pregnancy test in Tangier</h2><p>The most reliable method to confirm pregnancy. Can detect pregnancy as early as 10 days after fertilization. Results in 2-4 hours at Laboratoire International. <a href="/en/contact/">Contact us</a>.</p>',
        'content_ar': '<h2>تحليل الحمل في الدم في طنجة</h2><p>أكثر طريقة موثوقة لتأكيد الحمل. يمكن الكشف عن الحمل في وقت مبكر بعد 10 أيام من التخصيب. النتائج خلال 2-4 ساعات. <a href="/ar/contact/">تواصلوا معنا</a>.</p>',
    },
    {
        'slug': 'glycemie-diabete-test-tanger',
        'category_slug': 'sante',
        'title_fr': 'Glycémie et diabète : où faire le test à Tanger ?',
        'title_en': 'Blood sugar and diabetes testing in Tangier',
        'title_ar': 'تحليل السكر والسكري في طنجة',
        'excerpt_fr': 'Dépistage du diabète à Tanger : glycémie à jeun, HbA1c, courbe de charge en glucose. Guide complet.',
        'meta_description_fr': 'Test de glycémie et dépistage du diabète à Tanger. Résultats rapides au Laboratoire International, Avenue Moulay Rachid.',
        'content_fr': """<h2>Le diabète au Maroc : un enjeu de santé publique</h2>

<p>Le diabète touche environ <strong>2 millions de Marocains</strong>, et près de la moitié ne sont pas diagnostiqués. Le dépistage précoce est essentiel pour prévenir les complications graves (atteintes rénales, cardiovasculaires, oculaires). Au <strong>Laboratoire International de Tanger</strong>, nous proposons tous les tests nécessaires au dépistage et au suivi du diabète.</p>

<h2>Les différents tests disponibles</h2>

<h3>Glycémie à jeun</h3>
<p>C'est le test de base. Une glycémie normale à jeun est inférieure à <strong>1,10 g/L</strong>. Entre 1,10 et 1,26 g/L, on parle de prédiabète. Au-dessus de 1,26 g/L (confirmé par un deuxième test), le diagnostic de diabète est posé.</p>

<h3>Hémoglobine glyquée (HbA1c)</h3>
<p>L'HbA1c reflète la glycémie moyenne sur 2-3 mois. C'est l'examen de référence pour le <strong>suivi du diabète</strong>. L'objectif est généralement de maintenir l'HbA1c en dessous de 7%.</p>

<h3>Glycémie postprandiale</h3>
<p>Mesurée 2 heures après un repas, elle évalue la capacité de l'organisme à gérer le sucre après l'alimentation.</p>

<h2>Qui devrait se faire dépister ?</h2>

<ul>
<li>Toute personne de <strong>plus de 45 ans</strong></li>
<li>En cas de <strong>surpoids</strong> ou d'obésité</li>
<li>Si <strong>antécédents familiaux</strong> de diabète</li>
<li>Femmes ayant eu un <strong>diabète gestationnel</strong></li>
<li>En cas de <strong>soif excessive</strong>, envies fréquentes d'uriner, fatigue</li>
</ul>

<h2>Résultats rapides à Tanger</h2>

<p>La glycémie à jeun est disponible en <strong>2 à 4 heures</strong>. L'HbA1c en 4 à 6 heures. Consultez notre <a href="/fr/analyse/glycemie-tanger/">page glycémie</a> ou notre <a href="/fr/analyse/hemoglobine-glyquee-hba1c-tanger/">page HbA1c</a> pour plus de détails. <a href="/fr/contact/">Contactez-nous</a> pour prendre rendez-vous.</p>""",
        'content_en': '<h2>Diabetes testing in Tangier</h2><p>We offer fasting glucose, HbA1c, and postprandial glucose testing. Early screening is essential as diabetes affects ~2 million Moroccans. Results in 2-6 hours. <a href="/en/contact/">Contact Laboratoire International</a>.</p>',
        'content_ar': '<h2>تحليل السكري في طنجة</h2><p>نقدم تحليل السكر الصائم و HbA1c والسكر بعد الأكل. الكشف المبكر ضروري. النتائج خلال 2-6 ساعات. <a href="/ar/contact/">تواصلوا مع المختبر الدولي</a>.</p>',
    },
    {
        'slug': 'bilan-lipidique-cholesterol-tanger',
        'category_slug': 'sante',
        'title_fr': 'Bilan lipidique à Tanger : cholestérol et triglycérides',
        'title_en': 'Lipid panel in Tangier: cholesterol and triglycerides',
        'title_ar': 'تحليل الدهون في طنجة: الكوليسترول والدهون الثلاثية',
        'excerpt_fr': 'Tout sur le bilan lipidique à Tanger : cholestérol total, HDL, LDL, triglycérides. Évaluation du risque cardiovasculaire.',
        'meta_description_fr': 'Bilan lipidique à Tanger : cholestérol, triglycérides, HDL, LDL. Résultats en 4h au Laboratoire International.',
        'content_fr': """<h2>Le bilan lipidique : prévenir les maladies cardiovasculaires</h2>

<p>Les maladies cardiovasculaires sont la première cause de mortalité dans le monde. Le bilan lipidique est un outil essentiel de prévention. Au <strong>Laboratoire International de Tanger</strong>, nous réalisons des bilans lipidiques complets avec des résultats en 4 heures.</p>

<h2>Que mesure le bilan lipidique ?</h2>

<ul>
<li><strong>Cholestérol total</strong> : valeur globale, idéalement inférieur à 2 g/L</li>
<li><strong>Cholestérol LDL</strong> (« mauvais ») : se dépose dans les artères. L'objectif dépend de vos facteurs de risque</li>
<li><strong>Cholestérol HDL</strong> (« bon ») : protège les artères. Idéalement supérieur à 0,40 g/L</li>
<li><strong>Triglycérides</strong> : liés à l'alimentation et au surpoids. Normal : inférieur à 1,50 g/L</li>
</ul>

<h2>Comment se préparer ?</h2>

<p>Un <strong>jeûne de 12 heures</strong> est recommandé pour des résultats précis (surtout pour les triglycérides). L'eau est autorisée. Évitez l'alcool 48 heures avant.</p>

<h2>À quelle fréquence ?</h2>

<p>Un premier bilan est recommandé à partir de <strong>20 ans</strong>, puis tous les 5 ans en l'absence de facteurs de risque. Plus fréquemment si vous êtes hypertendu, diabétique, fumeur ou en surpoids.</p>

<p>Consultez notre <a href="/fr/analyse/bilan-lipidique-cholesterol-tanger/">page bilan lipidique</a> ou <a href="/fr/contact/">prenez rendez-vous</a>.</p>""",
        'content_en': '<h2>Lipid panel in Tangier</h2><p>We measure total cholesterol, LDL, HDL, and triglycerides. 12-hour fast recommended. Results in 4 hours. First screening recommended at age 20. <a href="/en/contact/">Contact Laboratoire International</a>.</p>',
        'content_ar': '<h2>تحليل الدهون في طنجة</h2><p>نقيس الكوليسترول الكلي و LDL و HDL والدهون الثلاثية. صيام 12 ساعة مطلوب. النتائج خلال 4 ساعات. <a href="/ar/contact/">تواصلوا مع المختبر الدولي</a>.</p>',
    },
    {
        'slug': 'ecbu-analyse-urine-tanger',
        'category_slug': 'sante',
        'title_fr': 'Analyse d\'urine (ECBU) à Tanger : guide pratique',
        'title_en': 'Urine test (urinalysis) in Tangier: practical guide',
        'title_ar': 'تحليل البول في طنجة: دليل عملي',
        'excerpt_fr': 'Tout savoir sur l\'ECBU à Tanger : comment recueillir l\'échantillon, indications, résultats au Laboratoire International.',
        'meta_description_fr': 'ECBU à Tanger : examen cytobactériologique des urines. Diagnostic infection urinaire. Résultats en 24-48h, Laboratoire International.',
        'content_fr': """<h2>L'ECBU : l'examen de référence des infections urinaires</h2>

<p>L'ECBU (Examen CytoBactériologique des Urines) est l'examen le plus prescrit pour diagnostiquer une infection urinaire. Au <strong>Laboratoire International de Tanger</strong>, nous analysons des centaines d'ECBU chaque semaine avec rigueur et précision.</p>

<h2>Quand faire un ECBU ?</h2>

<ul>
<li>Brûlures ou douleurs en urinant</li>
<li>Envies fréquentes et urgentes d'uriner</li>
<li>Urines troubles ou malodorantes</li>
<li>Douleurs dans le bas du ventre ou le dos</li>
<li>Fièvre d'origine indéterminée</li>
<li>Suivi systématique pendant la grossesse</li>
</ul>

<h2>Comment bien recueillir l'échantillon ?</h2>

<p>La qualité du prélèvement est <strong>essentielle</strong> pour éviter les contaminations :</p>
<ol>
<li>Se laver soigneusement les mains et la zone génitale</li>
<li>Éliminer le <strong>premier jet</strong> d'urine dans les toilettes</li>
<li>Recueillir le <strong>milieu de jet</strong> dans le pot stérile fourni par le laboratoire</li>
<li>Apporter l'échantillon au laboratoire dans les <strong>2 heures</strong> (ou conserver au réfrigérateur)</li>
</ol>

<h2>Que recherche l'ECBU ?</h2>

<p>L'ECBU comprend deux parties : l'<strong>examen cytologique</strong> (comptage des globules blancs, rouges, cristaux) et la <strong>culture bactériologique</strong> avec antibiogramme si des bactéries pathogènes sont identifiées.</p>

<h2>Délais de résultats</h2>

<p>Les premiers résultats (examen direct) sont disponibles en <strong>quelques heures</strong>. La culture complète avec antibiogramme nécessite <strong>24 à 48 heures</strong>.</p>

<p>Consultez notre <a href="/fr/analyse/ecbu-analyse-urine-tanger/">page ECBU</a> ou <a href="/fr/contact/">contactez-nous</a> pour plus d'informations.</p>""",
        'content_en': '<h2>Urinalysis (ECBU) in Tangier</h2><p>The reference test for urinary tract infections. Proper mid-stream collection is essential. Initial results in hours, full culture in 24-48h. <a href="/en/contact/">Contact Laboratoire International</a>.</p>',
        'content_ar': '<h2>تحليل البول في طنجة</h2><p>الفحص المرجعي لالتهابات المسالك البولية. جمع العينة بشكل صحيح ضروري. النتائج الأولية خلال ساعات، والزراعة الكاملة خلال 24-48 ساعة. <a href="/ar/contact/">تواصلوا معنا</a>.</p>',
    },
    {
        'slug': 'nfs-vs-analyse-sang-tanger',
        'category_slug': 'sante',
        'title_fr': 'NFS et vitesse de sédimentation à Tanger',
        'title_en': 'CBC and ESR blood test in Tangier',
        'title_ar': 'تحليل الدم الشامل وسرعة الترسب في طنجة',
        'excerpt_fr': 'La NFS et la VS sont les analyses de sang les plus prescrites. Tout savoir sur ces examens au Laboratoire International de Tanger.',
        'meta_description_fr': 'NFS et VS à Tanger : analyses de sang les plus courantes. Résultats en 2h au Laboratoire International, Avenue Moulay Rachid.',
        'content_fr': """<h2>NFS et VS : les analyses de sang de base</h2>

<p>La <strong>Numération Formule Sanguine (NFS)</strong> et la <strong>Vitesse de Sédimentation (VS)</strong> sont les deux analyses de sang les plus fréquemment prescrites par les médecins. Au <strong>Laboratoire International de Tanger</strong>, nous les réalisons avec des résultats disponibles en seulement 2 heures.</p>

<h2>La NFS : une photographie de votre sang</h2>

<p>La NFS compte et analyse les trois types de cellules sanguines :</p>
<ul>
<li><strong>Globules rouges</strong> (érythrocytes) et hémoglobine : transportent l'oxygène. Une baisse indique une anémie.</li>
<li><strong>Globules blancs</strong> (leucocytes) : défenses immunitaires. Une augmentation peut signaler une infection.</li>
<li><strong>Plaquettes</strong> (thrombocytes) : interviennent dans la coagulation. Un taux anormal nécessite une investigation.</li>
</ul>

<h2>La VS : un marqueur d'inflammation</h2>

<p>La VS mesure la vitesse à laquelle vos globules rouges se déposent dans un tube. Une VS élevée est un signal d'alarme non spécifique indiquant une inflammation, une infection, ou parfois une maladie auto-immune.</p>

<h2>Quand ces analyses sont-elles prescrites ?</h2>

<ul>
<li>Bilan de santé de routine</li>
<li>Fatigue, pâleur, essoufflement (suspicion d'anémie)</li>
<li>Fièvre ou infection</li>
<li>Surveillance d'une maladie chronique</li>
<li>Bilan préopératoire</li>
</ul>

<h2>Pas de jeûne nécessaire</h2>

<p>Bonne nouvelle : la NFS et la VS ne nécessitent <strong>pas de jeûne</strong>. Vous pouvez vous présenter à tout moment de la journée.</p>

<p>Consultez nos pages <a href="/fr/analyse/nfs-numeration-formule-sanguine-tanger/">NFS</a> et <a href="/fr/analyse/vitesse-sedimentation-vs-tanger/">VS</a>, ou <a href="/fr/contact/">contactez-nous</a>.</p>""",
        'content_en': '<h2>CBC and ESR in Tangier</h2><p>The two most commonly prescribed blood tests. No fasting required. Results in just 2 hours at Laboratoire International. <a href="/en/contact/">Contact us</a> for more information.</p>',
        'content_ar': '<h2>تحليل الدم الشامل وسرعة الترسب في طنجة</h2><p>أكثر تحليلين دم شيوعاً. لا حاجة للصيام. النتائج خلال ساعتين فقط في المختبر الدولي. <a href="/ar/contact/">تواصلوا معنا</a>.</p>',
    },
]


class Command(BaseCommand):
    help = 'Create 10 SEO-optimized blog posts targeting local search queries'

    def handle(self, *args, **options):
        # Ensure blog category exists
        cat, _ = BlogCategory.objects.get_or_create(
            slug='sante',
            defaults={
                'name_fr': 'Santé & Analyses',
                'name_en': 'Health & Tests',
                'name_ar': 'الصحة والتحاليل',
                'icon': 'fas fa-heartbeat',
                'order': 1,
            }
        )

        now = timezone.now()
        for i, post_data in enumerate(BLOG_POSTS):
            post_data.pop('category_slug', None)
            post, created = BlogPost.objects.update_or_create(
                slug=post_data['slug'],
                defaults={
                    **post_data,
                    'category': cat,
                    'status': 'published',
                    'published_at': now - timezone.timedelta(days=len(BLOG_POSTS) - i),
                    'author': 'Laboratoire International Tanger',
                }
            )
            status = 'CREATED' if created else 'UPDATED'
            self.stdout.write(f'  {status}: {post.title_fr}')

        total = BlogPost.objects.filter(status='published').count()
        self.stdout.write(self.style.SUCCESS(f'\nDone! {total} published blog posts.'))
