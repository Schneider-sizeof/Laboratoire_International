"""
Management command to populate analysis categories and individual analyses.
Creates 7 categories and ~67 analyses with FR/EN/AR content.
"""
from django.core.management.base import BaseCommand
from core.models import AnalysisCategory, Analysis


CATEGORIES = [
    {'slug': 'biochimie', 'name_fr': 'Biochimie', 'name_en': 'Biochemistry', 'name_ar': 'الكيمياء الحيوية', 'icon': 'fas fa-flask', 'color': 'primary', 'order': 1},
    {'slug': 'hematologie', 'name_fr': 'Hématologie', 'name_en': 'Hematology', 'name_ar': 'أمراض الدم', 'icon': 'fas fa-microscope', 'color': 'danger', 'order': 2},
    {'slug': 'serologie-immunologie', 'name_fr': 'Sérologie & Immunologie', 'name_en': 'Serology & Immunology', 'name_ar': 'علم المصليات والمناعة', 'icon': 'fas fa-shield-alt', 'color': 'accent', 'order': 3},
    {'slug': 'auto-immunite', 'name_fr': 'Auto-immunité', 'name_en': 'Autoimmunity', 'name_ar': 'المناعة الذاتية', 'icon': 'fas fa-user-shield', 'color': 'primary', 'order': 4},
    {'slug': 'hormonologie-fertilite', 'name_fr': 'Hormonologie & Fertilité', 'name_en': 'Hormones & Fertility', 'name_ar': 'الهرمونات والخصوبة', 'icon': 'fas fa-baby', 'color': 'warning', 'order': 5},
    {'slug': 'microbiologie', 'name_fr': 'Microbiologie', 'name_en': 'Microbiology', 'name_ar': 'علم الأحياء الدقيقة', 'icon': 'fas fa-virus', 'color': 'success', 'order': 6},
    {'slug': 'pcr-biologie-moleculaire', 'name_fr': 'PCR & Biologie Moléculaire', 'name_en': 'PCR & Molecular Biology', 'name_ar': 'تفاعل البوليميراز والبيولوجيا الجزيئية', 'icon': 'fas fa-dna', 'color': 'accent', 'order': 7},
]

ANALYSES = [
    # ===== BIOCHIMIE =====
    {'cat': 'biochimie', 'slug': 'glycemie-tanger', 'order': 1,
     'name_fr': 'Glycémie à jeun & postprandiale', 'name_en': 'Fasting & Postprandial Blood Glucose', 'name_ar': 'تحليل السكر في الدم',
     'description_fr': 'La glycémie mesure le taux de sucre (glucose) dans le sang. La glycémie à jeun est réalisée après 8 à 12 heures sans manger, tandis que la glycémie postprandiale est mesurée 2 heures après un repas. Ce test est essentiel pour le dépistage et le suivi du diabète.',
     'description_en': 'Blood glucose measures the sugar (glucose) level in your blood. Fasting glucose is taken after 8-12 hours without eating, while postprandial glucose is measured 2 hours after a meal. This test is essential for diabetes screening and monitoring.',
     'description_ar': 'يقيس تحليل السكر في الدم مستوى الجلوكوز. يتم إجراء تحليل السكر الصائم بعد 8 إلى 12 ساعة من الصيام، بينما يتم قياس السكر بعد الأكل بساعتين. هذا الفحص ضروري للكشف عن مرض السكري ومتابعته.',
     'why_fr': 'Le dépistage du diabète est recommandé à partir de 45 ans ou plus tôt en cas de facteurs de risque (surpoids, antécédents familiaux). Un suivi régulier permet d\'ajuster le traitement et de prévenir les complications.',
     'why_en': 'Diabetes screening is recommended from age 45 or earlier if risk factors are present (overweight, family history). Regular monitoring helps adjust treatment and prevent complications.',
     'why_ar': 'يُنصح بإجراء فحص السكري من سن 45 أو قبل ذلك في حالة وجود عوامل خطر. المتابعة المنتظمة تساعد على ضبط العلاج والوقاية من المضاعفات.',
     'delay_fr': 'Résultats en 2 à 4 heures', 'delay_en': 'Results in 2 to 4 hours', 'delay_ar': 'النتائج خلال 2 إلى 4 ساعات'},

    {'cat': 'biochimie', 'slug': 'hemoglobine-glyquee-hba1c-tanger', 'order': 2,
     'name_fr': 'Hémoglobine glyquée (HbA1c)', 'name_en': 'Glycated Hemoglobin (HbA1c)', 'name_ar': 'الهيموجلوبين السكري',
     'description_fr': 'L\'HbA1c reflète la moyenne de votre glycémie sur les 2 à 3 derniers mois. Contrairement à la glycémie à jeun qui donne un instantané, l\'HbA1c offre une vision globale du contrôle glycémique. Un taux normal est inférieur à 5.7%.',
     'description_en': 'HbA1c reflects your average blood sugar over the past 2-3 months. Unlike fasting glucose which provides a snapshot, HbA1c offers a comprehensive view of glycemic control. A normal level is below 5.7%.',
     'description_ar': 'يعكس الهيموجلوبين السكري متوسط مستوى السكر في الدم خلال الشهرين إلى ثلاثة أشهر الماضية. المستوى الطبيعي أقل من 5.7%.',
     'why_fr': 'Indispensable pour le suivi du diabète. Permet au médecin d\'évaluer l\'efficacité du traitement et d\'ajuster la prise en charge. Recommandé tous les 3 mois pour les diabétiques.',
     'delay_fr': 'Résultats en 4 à 6 heures', 'delay_en': 'Results in 4 to 6 hours', 'delay_ar': 'النتائج خلال 4 إلى 6 ساعات'},

    {'cat': 'biochimie', 'slug': 'bilan-lipidique-cholesterol-tanger', 'order': 3,
     'name_fr': 'Bilan lipidique complet', 'name_en': 'Complete Lipid Panel', 'name_ar': 'تحليل الدهون الكامل',
     'description_fr': 'Le bilan lipidique mesure les différentes graisses dans le sang : cholestérol total, triglycérides, HDL (bon cholestérol) et LDL (mauvais cholestérol). Ce bilan est fondamental pour évaluer le risque cardiovasculaire et prévenir les maladies cardiaques.',
     'description_en': 'The lipid panel measures different fats in your blood: total cholesterol, triglycerides, HDL (good cholesterol) and LDL (bad cholesterol). This test is fundamental for cardiovascular risk assessment and heart disease prevention.',
     'description_ar': 'يقيس تحليل الدهون الكامل مختلف الدهون في الدم: الكوليسترول الكلي والدهون الثلاثية والكوليسترول الجيد والكوليسترول الضار.',
     'why_fr': 'Recommandé à partir de 20 ans, puis tous les 5 ans. Plus fréquent en cas de facteurs de risque cardiovasculaire (hypertension, diabète, tabagisme, surpoids).',
     'delay_fr': 'Résultats en 4 heures', 'delay_en': 'Results in 4 hours', 'delay_ar': 'النتائج خلال 4 ساعات'},

    {'cat': 'biochimie', 'slug': 'bilan-hepatique-tanger', 'order': 4,
     'name_fr': 'Bilan hépatique complet', 'name_en': 'Complete Liver Panel', 'name_ar': 'تحليل وظائف الكبد',
     'description_fr': 'Le bilan hépatique évalue la santé du foie en mesurant les enzymes hépatiques (ASAT, ALAT, GGT), les phosphatases alcalines et la bilirubine. Il permet de détecter les maladies du foie, les hépatites et de surveiller les effets des médicaments sur le foie.',
     'description_en': 'The liver panel evaluates liver health by measuring liver enzymes (AST, ALT, GGT), alkaline phosphatase and bilirubin. It helps detect liver diseases, hepatitis and monitor medication effects on the liver.',
     'description_ar': 'يقيّم تحليل وظائف الكبد صحة الكبد عن طريق قياس إنزيمات الكبد والبيليروبين. يساعد في الكشف عن أمراض الكبد والتهاب الكبد.',
     'why_fr': 'Prescrit en cas de fatigue inexpliquée, jaunisse, douleurs abdominales, ou pour surveiller un traitement médicamenteux pouvant affecter le foie.',
     'delay_fr': 'Résultats en 4 à 6 heures', 'delay_en': 'Results in 4 to 6 hours', 'delay_ar': 'النتائج خلال 4 إلى 6 ساعات'},

    {'cat': 'biochimie', 'slug': 'bilan-renal-tanger', 'order': 5,
     'name_fr': 'Bilan rénal', 'name_en': 'Kidney Function Panel', 'name_ar': 'تحليل وظائف الكلى',
     'description_fr': 'Le bilan rénal mesure l\'urée, la créatinine et l\'acide urique pour évaluer le fonctionnement des reins. Le débit de filtration glomérulaire (DFG) est calculé pour déterminer la capacité de filtration rénale.',
     'description_en': 'The kidney panel measures urea, creatinine and uric acid to evaluate kidney function. The glomerular filtration rate (GFR) is calculated to determine kidney filtration capacity.',
     'description_ar': 'يقيس تحليل وظائف الكلى اليوريا والكرياتينين وحمض اليوريك لتقييم عمل الكلى.',
     'why_fr': 'Recommandé pour les patients diabétiques, hypertendus, ou en cas de symptômes urinaires. Surveillance régulière importante pour prévenir l\'insuffisance rénale.',
     'delay_fr': 'Résultats en 4 heures', 'delay_en': 'Results in 4 hours', 'delay_ar': 'النتائج خلال 4 ساعات'},

    {'cat': 'biochimie', 'slug': 'ionogramme-sanguin-tanger', 'order': 6,
     'name_fr': 'Ionogramme sanguin', 'name_en': 'Blood Electrolyte Panel', 'name_ar': 'تحليل الأملاح المعدنية في الدم',
     'description_fr': 'L\'ionogramme mesure les principaux électrolytes du sang : sodium (Na), potassium (K), chlore (Cl), calcium (Ca) et magnésium (Mg). Ces minéraux sont essentiels au bon fonctionnement des muscles, du cœur et du système nerveux.',
     'description_en': 'The electrolyte panel measures key blood electrolytes: sodium (Na), potassium (K), chloride (Cl), calcium (Ca) and magnesium (Mg). These minerals are essential for proper muscle, heart and nervous system function.',
     'description_ar': 'يقيس تحليل الأملاح المعادن الرئيسية في الدم: الصوديوم والبوتاسيوم والكلور والكالسيوم والمغنيسيوم.',
     'why_fr': 'Prescrit en cas de fatigue, crampes musculaires, troubles du rythme cardiaque, ou lors de traitements diurétiques.',
     'delay_fr': 'Résultats en 4 heures', 'delay_en': 'Results in 4 hours', 'delay_ar': 'النتائج خلال 4 ساعات'},

    {'cat': 'biochimie', 'slug': 'bilan-martial-fer-tanger', 'order': 7,
     'name_fr': 'Bilan martial (Fer)', 'name_en': 'Iron Panel', 'name_ar': 'تحليل الحديد',
     'description_fr': 'Le bilan martial évalue les réserves de fer dans l\'organisme : fer sérique, ferritine et capacité de fixation du fer. Le fer est indispensable à la fabrication de l\'hémoglobine qui transporte l\'oxygène dans le sang.',
     'description_en': 'The iron panel evaluates iron stores in the body: serum iron, ferritin and iron binding capacity. Iron is essential for hemoglobin production which carries oxygen in the blood.',
     'description_ar': 'يقيّم تحليل الحديد مخزون الحديد في الجسم: الحديد في المصل والفيريتين وقدرة ربط الحديد.',
     'why_fr': 'Prescrit en cas de fatigue chronique, pâleur, essoufflement, ou pour surveiller une anémie ferriprive. Fréquent chez les femmes en âge de procréer.',
     'delay_fr': 'Résultats en 4 à 6 heures', 'delay_en': 'Results in 4 to 6 hours', 'delay_ar': 'النتائج خلال 4 إلى 6 ساعات'},

    {'cat': 'biochimie', 'slug': 'bilan-phosphocalcique-tanger', 'order': 8,
     'name_fr': 'Bilan phosphocalcique', 'name_en': 'Calcium-Phosphorus Panel', 'name_ar': 'تحليل الكالسيوم والفوسفور',
     'description_fr': 'Ce bilan mesure le calcium, le phosphore et le magnésium sanguins, ainsi que la vitamine D et la parathormone. Il évalue le métabolisme osseux et aide au diagnostic de l\'ostéoporose.',
     'description_en': 'This panel measures blood calcium, phosphorus and magnesium levels, as well as vitamin D and parathyroid hormone. It evaluates bone metabolism and helps diagnose osteoporosis.',
     'description_ar': 'يقيس هذا التحليل الكالسيوم والفوسفور والمغنيسيوم في الدم، وكذلك فيتامين د وهرمون الغدة الدرقية.',
     'why_fr': 'Recommandé pour les femmes ménopausées, les personnes âgées, en cas de douleurs osseuses ou de fractures fréquentes.',
     'delay_fr': 'Résultats en 24 heures', 'delay_en': 'Results in 24 hours', 'delay_ar': 'النتائج خلال 24 ساعة'},

    {'cat': 'biochimie', 'slug': 'marqueurs-cardiaques-tanger', 'order': 9,
     'name_fr': 'Marqueurs cardiaques (Troponine, BNP)', 'name_en': 'Cardiac Markers (Troponin, BNP)', 'name_ar': 'دلالات القلب',
     'description_fr': 'Les marqueurs cardiaques, notamment la troponine et le BNP, permettent de détecter une souffrance du muscle cardiaque. La troponine est le marqueur de référence pour diagnostiquer un infarctus du myocarde.',
     'description_en': 'Cardiac markers, including troponin and BNP, help detect heart muscle damage. Troponin is the reference marker for diagnosing myocardial infarction.',
     'description_ar': 'تساعد دلالات القلب، بما في ذلك التروبونين و BNP، في الكشف عن تلف عضلة القلب.',
     'why_fr': 'Prescrit en urgence en cas de douleur thoracique, essoufflement, ou suspicion d\'infarctus. Aussi utilisé pour le suivi de l\'insuffisance cardiaque.',
     'delay_fr': 'Résultats en 1 à 2 heures (urgence)', 'delay_en': 'Results in 1 to 2 hours (urgent)', 'delay_ar': 'النتائج خلال ساعة إلى ساعتين (حالة طوارئ)'},

    # ===== HÉMATOLOGIE =====
    {'cat': 'hematologie', 'slug': 'nfs-numeration-formule-sanguine-tanger', 'order': 1,
     'name_fr': 'NFS - Numération Formule Sanguine', 'name_en': 'Complete Blood Count (CBC)', 'name_ar': 'تحليل الدم الشامل',
     'description_fr': 'La NFS est l\'analyse de sang la plus prescrite. Elle compte les globules rouges, globules blancs et plaquettes, et mesure l\'hémoglobine. C\'est un examen de base pour dépister anémies, infections et troubles hématologiques.',
     'description_en': 'The CBC is the most commonly ordered blood test. It counts red blood cells, white blood cells and platelets, and measures hemoglobin. It\'s a basic test for screening anemias, infections and hematological disorders.',
     'description_ar': 'تحليل الدم الشامل هو أكثر فحوصات الدم شيوعاً. يعدّ كريات الدم الحمراء والبيضاء والصفائح الدموية ويقيس الهيموجلوبين.',
     'why_fr': 'Examen de routine recommandé lors de tout bilan de santé. Indispensable en cas de fatigue, fièvre, saignements inhabituels ou avant une intervention chirurgicale.',
     'delay_fr': 'Résultats en 2 heures', 'delay_en': 'Results in 2 hours', 'delay_ar': 'النتائج خلال ساعتين'},

    {'cat': 'hematologie', 'slug': 'vitesse-sedimentation-vs-tanger', 'order': 2,
     'name_fr': 'Vitesse de Sédimentation (VS)', 'name_en': 'Erythrocyte Sedimentation Rate (ESR)', 'name_ar': 'سرعة ترسب الدم',
     'description_fr': 'La VS mesure la vitesse à laquelle les globules rouges se déposent au fond d\'un tube. Une VS élevée indique la présence d\'une inflammation dans l\'organisme, sans préciser sa localisation.',
     'description_en': 'ESR measures how quickly red blood cells settle to the bottom of a tube. An elevated ESR indicates inflammation in the body without specifying its location.',
     'description_ar': 'يقيس سرعة ترسب كريات الدم الحمراء. ارتفاع السرعة يشير إلى وجود التهاب في الجسم.',
     'why_fr': 'Prescrite pour dépister ou surveiller une inflammation, une infection, ou une maladie auto-immune. Souvent associée à la CRP.',
     'delay_fr': 'Résultats en 2 heures', 'delay_en': 'Results in 2 hours', 'delay_ar': 'النتائج خلال ساعتين'},

    {'cat': 'hematologie', 'slug': 'bilan-coagulation-tp-tca-inr-tanger', 'order': 3,
     'name_fr': 'Bilan de coagulation (TP, TCA, INR)', 'name_en': 'Coagulation Panel (PT, aPTT, INR)', 'name_ar': 'تحليل تخثر الدم',
     'description_fr': 'Le bilan de coagulation mesure la capacité du sang à coaguler normalement. Le TP (taux de prothrombine), le TCA et l\'INR évaluent les différentes voies de la coagulation. Indispensable avant toute chirurgie.',
     'description_en': 'The coagulation panel measures the blood\'s ability to clot normally. PT, aPTT and INR evaluate different coagulation pathways. Essential before any surgery.',
     'description_ar': 'يقيس تحليل التخثر قدرة الدم على التجلط بشكل طبيعي. ضروري قبل أي عملية جراحية.',
     'why_fr': 'Obligatoire avant une opération chirurgicale. Utilisé aussi pour surveiller les traitements anticoagulants (AVK, héparine).',
     'delay_fr': 'Résultats en 3 à 4 heures', 'delay_en': 'Results in 3 to 4 hours', 'delay_ar': 'النتائج خلال 3 إلى 4 ساعات'},

    {'cat': 'hematologie', 'slug': 'groupe-sanguin-rhesus-tanger', 'order': 4,
     'name_fr': 'Groupe sanguin & Rhésus', 'name_en': 'Blood Type & Rh Factor', 'name_ar': 'فصيلة الدم والريزوس',
     'description_fr': 'La détermination du groupe sanguin (A, B, AB, O) et du facteur Rhésus (+/-) est essentielle pour les transfusions sanguines, les grossesses et les urgences médicales. Deux déterminations sont nécessaires pour confirmation.',
     'description_en': 'Blood type (A, B, AB, O) and Rh factor (+/-) determination is essential for blood transfusions, pregnancies and medical emergencies. Two determinations are needed for confirmation.',
     'description_ar': 'تحديد فصيلة الدم وعامل الريزوس ضروري لعمليات نقل الدم والحمل والطوارئ الطبية.',
     'why_fr': 'Obligatoire pour les femmes enceintes, avant une transfusion ou une chirurgie. Recommandé d\'avoir sa carte de groupe sanguin.',
     'delay_fr': 'Résultats en 24 heures', 'delay_en': 'Results in 24 hours', 'delay_ar': 'النتائج خلال 24 ساعة'},

    {'cat': 'hematologie', 'slug': 'd-dimeres-tanger', 'order': 5,
     'name_fr': 'D-Dimères', 'name_en': 'D-Dimer Test', 'name_ar': 'تحليل دي-دايمر',
     'description_fr': 'Les D-Dimères sont des fragments produits lors de la dégradation des caillots sanguins. Un taux élevé peut indiquer la présence d\'un caillot dans le corps (thrombose veineuse profonde, embolie pulmonaire).',
     'description_en': 'D-Dimers are fragments produced during blood clot breakdown. Elevated levels may indicate the presence of a clot (deep vein thrombosis, pulmonary embolism).',
     'description_ar': 'دي-دايمر هي شظايا تنتج عند تفكك الجلطات الدموية. ارتفاع المستوى قد يشير إلى وجود جلطة.',
     'why_fr': 'Prescrit en urgence en cas de suspicion de thrombose veineuse profonde ou d\'embolie pulmonaire.',
     'delay_fr': 'Résultats en 2 à 4 heures', 'delay_en': 'Results in 2 to 4 hours', 'delay_ar': 'النتائج خلال 2 إلى 4 ساعات'},

    # ===== SÉROLOGIE & IMMUNOLOGIE =====
    {'cat': 'serologie-immunologie', 'slug': 'serologie-hepatite-b-tanger', 'order': 1,
     'name_fr': 'Sérologie Hépatite B', 'name_en': 'Hepatitis B Serology', 'name_ar': 'تحليل التهاب الكبد ب',
     'description_fr': 'La sérologie de l\'hépatite B recherche les marqueurs du virus VHB dans le sang : antigène HBs (AgHBs), anticorps anti-HBs et anticorps anti-HBc. Elle permet de déterminer si vous êtes infecté, immunisé ou si vous devez vous faire vacciner.',
     'description_en': 'Hepatitis B serology tests for HBV markers in the blood: HBsAg, anti-HBs and anti-HBc antibodies. It determines whether you are infected, immune or need vaccination.',
     'description_ar': 'يبحث تحليل التهاب الكبد ب عن علامات فيروس الكبد ب في الدم لتحديد ما إذا كنت مصاباً أو محصناً.',
     'why_fr': 'Recommandé pour les professionnels de santé, les femmes enceintes, les voyageurs et toute personne à risque. Vérification de l\'immunité post-vaccinale.',
     'delay_fr': 'Résultats en 24 heures', 'delay_en': 'Results in 24 hours', 'delay_ar': 'النتائج خلال 24 ساعة'},

    {'cat': 'serologie-immunologie', 'slug': 'serologie-hepatite-c-tanger', 'order': 2,
     'name_fr': 'Sérologie Hépatite C', 'name_en': 'Hepatitis C Serology', 'name_ar': 'تحليل التهاب الكبد ج',
     'description_fr': 'La sérologie de l\'hépatite C détecte les anticorps anti-VHC dans le sang. Un résultat positif nécessite une confirmation par PCR pour vérifier la présence active du virus. L\'hépatite C est curable avec les traitements actuels.',
     'description_en': 'Hepatitis C serology detects anti-HCV antibodies in the blood. A positive result requires PCR confirmation to verify active virus presence. Hepatitis C is curable with current treatments.',
     'description_ar': 'يكشف تحليل التهاب الكبد ج عن الأجسام المضادة لفيروس الكبد ج. التهاب الكبد ج قابل للعلاج.',
     'why_fr': 'Dépistage recommandé pour toute personne ayant été exposée à un risque de contamination (soins dentaires, tatouage, transfusion avant 1992).',
     'delay_fr': 'Résultats en 24 heures', 'delay_en': 'Results in 24 hours', 'delay_ar': 'النتائج خلال 24 ساعة'},

    {'cat': 'serologie-immunologie', 'slug': 'serologie-hiv-tanger', 'order': 3,
     'name_fr': 'Sérologie HIV 1 & 2', 'name_en': 'HIV 1 & 2 Serology', 'name_ar': 'تحليل فيروس نقص المناعة',
     'description_fr': 'Le test HIV détecte les anticorps et l\'antigène p24 du virus de l\'immunodéficience humaine. Les tests de 4ème génération utilisés dans notre laboratoire permettent une détection précoce dès 2 semaines après l\'exposition.',
     'description_en': 'The HIV test detects antibodies and p24 antigen of the human immunodeficiency virus. Fourth-generation tests used in our laboratory allow early detection as soon as 2 weeks after exposure.',
     'description_ar': 'يكشف تحليل فيروس نقص المناعة عن الأجسام المضادة ومستضد p24. الاختبارات المستخدمة تسمح بالكشف المبكر.',
     'why_fr': 'Dépistage recommandé au moins une fois dans la vie. Test confidentiel réalisé dans le respect total de votre vie privée.',
     'delay_fr': 'Résultats en 24 heures', 'delay_en': 'Results in 24 hours', 'delay_ar': 'النتائج خلال 24 ساعة'},

    {'cat': 'serologie-immunologie', 'slug': 'serologie-toxoplasmose-tanger', 'order': 4,
     'name_fr': 'Sérologie Toxoplasmose', 'name_en': 'Toxoplasmosis Serology', 'name_ar': 'تحليل داء المقوسات',
     'description_fr': 'La sérologie de la toxoplasmose recherche les anticorps IgG et IgM contre le parasite Toxoplasma gondii. Ce test est crucial pendant la grossesse car une primo-infection peut être dangereuse pour le fœtus.',
     'description_en': 'Toxoplasmosis serology tests for IgG and IgM antibodies against the Toxoplasma gondii parasite. This test is crucial during pregnancy as a primary infection can be dangerous for the fetus.',
     'description_ar': 'يبحث تحليل داء المقوسات عن الأجسام المضادة ضد الطفيلي. هذا الفحص مهم أثناء الحمل.',
     'why_fr': 'Obligatoire pour les femmes enceintes non immunisées (contrôle mensuel). Aussi recommandé en cas d\'immunodépression.',
     'delay_fr': 'Résultats en 24 heures', 'delay_en': 'Results in 24 hours', 'delay_ar': 'النتائج خلال 24 ساعة'},

    {'cat': 'serologie-immunologie', 'slug': 'serologie-rubeole-tanger', 'order': 5,
     'name_fr': 'Sérologie Rubéole', 'name_en': 'Rubella Serology', 'name_ar': 'تحليل الحصبة الألمانية',
     'description_fr': 'La sérologie de la rubéole vérifie l\'immunité contre le virus de la rubéole. Une infection pendant la grossesse peut provoquer de graves malformations congénitales chez le fœtus.',
     'description_en': 'Rubella serology checks immunity against the rubella virus. Infection during pregnancy can cause severe birth defects.',
     'description_ar': 'يتحقق تحليل الحصبة الألمانية من المناعة ضد الفيروس. العدوى أثناء الحمل قد تسبب تشوهات خلقية.',
     'why_fr': 'Test obligatoire en début de grossesse. Si non immunisée, vaccination recommandée après l\'accouchement.',
     'delay_fr': 'Résultats en 24 heures', 'delay_en': 'Results in 24 hours', 'delay_ar': 'النتائج خلال 24 ساعة'},

    {'cat': 'serologie-immunologie', 'slug': 'serologie-syphilis-tanger', 'order': 6,
     'name_fr': 'Sérologie Syphilis (TPHA, VDRL)', 'name_en': 'Syphilis Serology (TPHA, VDRL)', 'name_ar': 'تحليل الزهري',
     'description_fr': 'Le dépistage de la syphilis utilise deux tests complémentaires : le TPHA (test spécifique) et le VDRL (test non spécifique). Leur combinaison permet un diagnostic fiable de cette infection sexuellement transmissible.',
     'description_en': 'Syphilis screening uses two complementary tests: TPHA (specific test) and VDRL (non-specific test). Their combination ensures reliable diagnosis of this sexually transmitted infection.',
     'description_ar': 'يستخدم فحص الزهري اختبارين متكاملين: TPHA و VDRL لتشخيص موثوق لهذه العدوى.',
     'why_fr': 'Dépistage obligatoire pendant la grossesse (1er trimestre). Recommandé lors de tout bilan IST.',
     'delay_fr': 'Résultats en 24 heures', 'delay_en': 'Results in 24 hours', 'delay_ar': 'النتائج خلال 24 ساعة'},

    {'cat': 'serologie-immunologie', 'slug': 'crp-facteur-rhumatoide-tanger', 'order': 7,
     'name_fr': 'CRP & Facteur Rhumatoïde', 'name_en': 'CRP & Rheumatoid Factor', 'name_ar': 'بروتين سي التفاعلي والعامل الروماتويدي',
     'description_fr': 'La CRP (protéine C-réactive) est un marqueur d\'inflammation aiguë. Le facteur rhumatoïde est un anticorps recherché dans le cadre du diagnostic de la polyarthrite rhumatoïde et d\'autres maladies auto-immunes.',
     'description_en': 'CRP (C-reactive protein) is an acute inflammation marker. Rheumatoid factor is an antibody tested in the diagnosis of rheumatoid arthritis and other autoimmune diseases.',
     'description_ar': 'بروتين سي التفاعلي هو علامة الالتهاب الحاد. العامل الروماتويدي يُفحص لتشخيص التهاب المفاصل الروماتويدي.',
     'why_fr': 'Prescrit en cas de douleurs articulaires, gonflement, raideur matinale, ou pour surveiller l\'activité d\'une maladie inflammatoire.',
     'delay_fr': 'Résultats en 4 à 6 heures', 'delay_en': 'Results in 4 to 6 hours', 'delay_ar': 'النتائج خلال 4 إلى 6 ساعات'},

    # ===== HORMONOLOGIE & FERTILITÉ =====
    {'cat': 'hormonologie-fertilite', 'slug': 'bilan-thyroidien-tsh-t3-t4-tanger', 'order': 1,
     'name_fr': 'Bilan thyroïdien (TSH, T3, T4)', 'name_en': 'Thyroid Panel (TSH, T3, T4)', 'name_ar': 'تحليل الغدة الدرقية',
     'description_fr': 'Le bilan thyroïdien mesure la TSH, la T3 libre et la T4 libre pour évaluer le fonctionnement de la glande thyroïde. Il permet de diagnostiquer l\'hypothyroïdie (thyroïde paresseuse) ou l\'hyperthyroïdie (thyroïde hyperactive).',
     'description_en': 'The thyroid panel measures TSH, free T3 and free T4 to evaluate thyroid gland function. It helps diagnose hypothyroidism (underactive thyroid) or hyperthyroidism (overactive thyroid).',
     'description_ar': 'يقيس تحليل الغدة الدرقية TSH و T3 و T4 لتقييم وظيفة الغدة الدرقية. يساعد في تشخيص قصور أو فرط نشاط الغدة الدرقية.',
     'why_fr': 'Recommandé en cas de fatigue, prise ou perte de poids inexpliquée, troubles de l\'humeur, palpitations ou problèmes de fertilité.',
     'delay_fr': 'Résultats en 24 heures', 'delay_en': 'Results in 24 hours', 'delay_ar': 'النتائج خلال 24 ساعة'},

    {'cat': 'hormonologie-fertilite', 'slug': 'bilan-hormonal-feminin-tanger', 'order': 2,
     'name_fr': 'Bilan hormonal féminin', 'name_en': 'Female Hormone Panel', 'name_ar': 'تحليل الهرمونات الأنثوية',
     'description_fr': 'Le bilan hormonal féminin mesure les hormones FSH, LH, estradiol et progestérone. Il est essentiel pour évaluer la fertilité, diagnostiquer les troubles du cycle menstruel et accompagner les protocoles de procréation médicalement assistée.',
     'description_en': 'The female hormone panel measures FSH, LH, estradiol and progesterone. It is essential for fertility evaluation, diagnosing menstrual cycle disorders and supporting assisted reproduction protocols.',
     'description_ar': 'يقيس تحليل الهرمونات الأنثوية هرمونات FSH و LH والإستراديول والبروجسترون لتقييم الخصوبة.',
     'why_fr': 'Prescrit en cas d\'infertilité, troubles du cycle, aménorrhée, ou dans le cadre d\'un bilan pré-FIV.',
     'delay_fr': 'Résultats en 24 heures', 'delay_en': 'Results in 24 hours', 'delay_ar': 'النتائج خلال 24 ساعة'},

    {'cat': 'hormonologie-fertilite', 'slug': 'beta-hcg-test-grossesse-tanger', 'order': 3,
     'name_fr': 'Beta-HCG quantitatif (Test de grossesse)', 'name_en': 'Quantitative Beta-HCG (Pregnancy Test)', 'name_ar': 'تحليل هرمون الحمل',
     'description_fr': 'Le dosage quantitatif de la Beta-HCG dans le sang est le test de grossesse le plus fiable. Il confirme la grossesse dès les premiers jours de retard des règles et permet de suivre son évolution. Le taux double environ toutes les 48 heures en début de grossesse.',
     'description_en': 'Quantitative Beta-HCG blood test is the most reliable pregnancy test. It confirms pregnancy from the first days of missed period and allows monitoring its progression.',
     'description_ar': 'تحليل هرمون الحمل الكمي في الدم هو أكثر اختبارات الحمل موثوقية. يؤكد الحمل من الأيام الأولى لتأخر الدورة.',
     'why_fr': 'Pour confirmer une grossesse, suivre son évolution, ou dans le cadre d\'un protocole de PMA. Résultat plus fiable que les tests urinaires.',
     'delay_fr': 'Résultats en 2 à 4 heures', 'delay_en': 'Results in 2 to 4 hours', 'delay_ar': 'النتائج خلال 2 إلى 4 ساعات'},

    {'cat': 'hormonologie-fertilite', 'slug': 'spermogramme-tanger', 'order': 4,
     'name_fr': 'Spermogramme', 'name_en': 'Semen Analysis', 'name_ar': 'تحليل السائل المنوي',
     'description_fr': 'Le spermogramme analyse la qualité du sperme : volume, concentration, mobilité et morphologie des spermatozoïdes. C\'est l\'examen de première intention dans le bilan de fertilité masculine. Un recueil au laboratoire dans des conditions optimales est recommandé.',
     'description_en': 'The semen analysis evaluates sperm quality: volume, concentration, motility and morphology. It is the first-line test in male fertility assessment. Collection at the laboratory under optimal conditions is recommended.',
     'description_ar': 'يحلل فحص السائل المنوي جودة الحيوانات المنوية: الحجم والتركيز والحركة والشكل. هو الفحص الأول في تقييم خصوبة الرجل.',
     'why_fr': 'Prescrit dans le cadre d\'un bilan de fertilité du couple après 12 mois de tentatives de conception sans succès. Une abstinence de 3 à 5 jours est recommandée avant le recueil.',
     'delay_fr': 'Résultats en 24 à 48 heures', 'delay_en': 'Results in 24 to 48 hours', 'delay_ar': 'النتائج خلال 24 إلى 48 ساعة'},

    {'cat': 'hormonologie-fertilite', 'slug': 'prolactine-tanger', 'order': 5,
     'name_fr': 'Prolactine', 'name_en': 'Prolactin', 'name_ar': 'هرمون البرولاكتين',
     'description_fr': 'La prolactine est une hormone produite par l\'hypophyse. Un taux élevé (hyperprolactinémie) peut causer des troubles du cycle menstruel, une galactorrhée et des problèmes de fertilité chez la femme, ou une baisse de la libido chez l\'homme.',
     'description_en': 'Prolactin is a hormone produced by the pituitary gland. Elevated levels can cause menstrual disorders, galactorrhea and fertility problems in women, or decreased libido in men.',
     'description_ar': 'البرولاكتين هرمون تنتجه الغدة النخامية. ارتفاع مستواه قد يسبب اضطرابات الدورة ومشاكل الخصوبة.',
     'why_fr': 'Prescrit en cas de troubles du cycle, galactorrhée, infertilité, ou suspicion d\'adénome hypophysaire.',
     'delay_fr': 'Résultats en 24 heures', 'delay_en': 'Results in 24 hours', 'delay_ar': 'النتائج خلال 24 ساعة'},

    {'cat': 'hormonologie-fertilite', 'slug': 'amh-hormone-anti-mullerienne-tanger', 'order': 6,
     'name_fr': 'AMH (Hormone Anti-Müllérienne)', 'name_en': 'AMH (Anti-Müllerian Hormone)', 'name_ar': 'هرمون مضاد مولر',
     'description_fr': 'L\'AMH est le meilleur marqueur de la réserve ovarienne. Elle reflète le nombre de follicules restants dans les ovaires et aide à prédire la réponse aux traitements de stimulation ovarienne. Son dosage peut être fait à n\'importe quel moment du cycle.',
     'description_en': 'AMH is the best marker of ovarian reserve. It reflects the number of remaining follicles in the ovaries and helps predict response to ovarian stimulation treatments.',
     'description_ar': 'هرمون مضاد مولر هو أفضل مؤشر لمخزون المبيض. يعكس عدد الجريبات المتبقية ويساعد في التنبؤ بالاستجابة للعلاج.',
     'why_fr': 'Indispensable avant tout protocole de FIV ou de stimulation ovarienne. Aussi utile pour évaluer la réserve ovarienne à tout âge.',
     'delay_fr': 'Résultats en 48 heures', 'delay_en': 'Results in 48 hours', 'delay_ar': 'النتائج خلال 48 ساعة'},

    # ===== MICROBIOLOGIE =====
    {'cat': 'microbiologie', 'slug': 'ecbu-analyse-urine-tanger', 'order': 1,
     'name_fr': 'ECBU - Examen Cytobactériologique des Urines', 'name_en': 'Urinalysis & Urine Culture', 'name_ar': 'تحليل البول الجرثومي',
     'description_fr': 'L\'ECBU est l\'examen de référence pour diagnostiquer les infections urinaires. Il identifie les bactéries responsables et teste leur sensibilité aux antibiotiques (antibiogramme) pour guider le traitement.',
     'description_en': 'Urinalysis and urine culture is the reference test for diagnosing urinary tract infections. It identifies responsible bacteria and tests their antibiotic sensitivity to guide treatment.',
     'description_ar': 'تحليل البول الجرثومي هو الفحص المرجعي لتشخيص التهابات المسالك البولية.',
     'why_fr': 'Prescrit en cas de brûlures urinaires, envies fréquentes d\'uriner, douleurs pelviennes, ou fièvre d\'origine inconnue. Le prélèvement du milieu de jet est essentiel.',
     'delay_fr': 'Résultats en 24 à 48 heures', 'delay_en': 'Results in 24 to 48 hours', 'delay_ar': 'النتائج خلال 24 إلى 48 ساعة'},

    {'cat': 'microbiologie', 'slug': 'coproculture-tanger', 'order': 2,
     'name_fr': 'Coproculture', 'name_en': 'Stool Culture', 'name_ar': 'زراعة البراز',
     'description_fr': 'La coproculture recherche les bactéries pathogènes dans les selles (Salmonella, Shigella, etc.). Elle est prescrite en cas de diarrhée prolongée, de gastro-entérite sévère ou de retour de voyage en zone à risque.',
     'description_en': 'Stool culture tests for pathogenic bacteria in feces (Salmonella, Shigella, etc.). It is prescribed for prolonged diarrhea, severe gastroenteritis or after travel to risk areas.',
     'description_ar': 'تبحث زراعة البراز عن البكتيريا المسببة للأمراض في البراز.',
     'why_fr': 'Prescrite en cas de diarrhée persistante (>3 jours), présence de sang ou de mucus dans les selles, ou au retour d\'un voyage tropical.',
     'delay_fr': 'Résultats en 48 à 72 heures', 'delay_en': 'Results in 48 to 72 hours', 'delay_ar': 'النتائج خلال 48 إلى 72 ساعة'},

    {'cat': 'microbiologie', 'slug': 'antibiogramme-tanger', 'order': 3,
     'name_fr': 'Antibiogramme', 'name_en': 'Antibiogram', 'name_ar': 'اختبار الحساسية للمضادات الحيوية',
     'description_fr': 'L\'antibiogramme teste la sensibilité d\'une bactérie aux différents antibiotiques. Il guide le médecin dans le choix du traitement le plus efficace et contribue à la lutte contre la résistance aux antibiotiques.',
     'description_en': 'The antibiogram tests bacterial sensitivity to different antibiotics. It guides the doctor in choosing the most effective treatment and helps fight antibiotic resistance.',
     'description_ar': 'يختبر اختبار الحساسية فعالية المضادات الحيوية المختلفة ضد البكتيريا.',
     'why_fr': 'Réalisé automatiquement lorsqu\'une bactérie pathogène est identifiée dans un prélèvement (ECBU, hémoculture, prélèvement vaginal, etc.).',
     'delay_fr': 'Résultats en 48 à 72 heures', 'delay_en': 'Results in 48 to 72 hours', 'delay_ar': 'النتائج خلال 48 إلى 72 ساعة'},

    # ===== PCR & BIOLOGIE MOLÉCULAIRE =====
    {'cat': 'pcr-biologie-moleculaire', 'slug': 'pcr-hepatite-b-c-tanger', 'order': 1,
     'name_fr': 'PCR Hépatite B & C quantitative', 'name_en': 'Quantitative Hepatitis B & C PCR', 'name_ar': 'تحليل PCR لالتهاب الكبد ب و ج',
     'description_fr': 'La PCR quantitative mesure la charge virale de l\'hépatite B ou C dans le sang. C\'est l\'examen le plus précis pour confirmer une infection active et surveiller l\'efficacité du traitement antiviral.',
     'description_en': 'Quantitative PCR measures the viral load of hepatitis B or C in the blood. It is the most accurate test to confirm active infection and monitor antiviral treatment effectiveness.',
     'description_ar': 'يقيس تحليل PCR الكمي الحمل الفيروسي لالتهاب الكبد ب أو ج في الدم.',
     'why_fr': 'Prescrit après une sérologie positive pour confirmer l\'infection active, et régulièrement pendant le traitement antiviral pour évaluer la réponse.',
     'delay_fr': 'Résultats en 3 à 5 jours', 'delay_en': 'Results in 3 to 5 days', 'delay_ar': 'النتائج خلال 3 إلى 5 أيام'},

    {'cat': 'pcr-biologie-moleculaire', 'slug': 'pcr-hpv-genotypage-tanger', 'order': 2,
     'name_fr': 'PCR HPV & Génotypage', 'name_en': 'HPV PCR & Genotyping', 'name_ar': 'تحليل فيروس الورم الحليمي',
     'description_fr': 'La PCR HPV détecte le virus du papillome humain et identifie les génotypes à haut risque (notamment HPV 16 et 18) responsables du cancer du col de l\'utérus. Le génotypage permet une prise en charge personnalisée.',
     'description_en': 'HPV PCR detects human papillomavirus and identifies high-risk genotypes (particularly HPV 16 and 18) responsible for cervical cancer. Genotyping enables personalized care.',
     'description_ar': 'يكشف تحليل فيروس الورم الحليمي عن الفيروس ويحدد الأنواع عالية الخطورة المسؤولة عن سرطان عنق الرحم.',
     'why_fr': 'Recommandé en complément du frottis cervico-vaginal, surtout après 30 ans. Dépistage essentiel du cancer du col de l\'utérus.',
     'delay_fr': 'Résultats en 3 à 5 jours', 'delay_en': 'Results in 3 to 5 days', 'delay_ar': 'النتائج خلال 3 إلى 5 أيام'},

    {'cat': 'pcr-biologie-moleculaire', 'slug': 'pcr-covid-19-tanger', 'order': 3,
     'name_fr': 'PCR COVID-19 (RT-PCR)', 'name_en': 'COVID-19 PCR (RT-PCR)', 'name_ar': 'تحليل PCR كوفيد-19',
     'description_fr': 'La RT-PCR COVID-19 est le test de référence pour le diagnostic de l\'infection par le SARS-CoV-2. Le prélèvement est réalisé par écouvillon nasopharyngé. Ce test détecte le matériel génétique du virus avec une grande précision.',
     'description_en': 'COVID-19 RT-PCR is the reference test for diagnosing SARS-CoV-2 infection. The sample is collected by nasopharyngeal swab. This test detects viral genetic material with high accuracy.',
     'description_ar': 'تحليل PCR كوفيد-19 هو الفحص المرجعي لتشخيص عدوى فيروس كورونا.',
     'why_fr': 'Requis pour les voyages internationaux, en cas de symptômes évocateurs, ou après un contact avec un cas confirmé.',
     'delay_fr': 'Résultats en 4 à 24 heures', 'delay_en': 'Results in 4 to 24 hours', 'delay_ar': 'النتائج خلال 4 إلى 24 ساعة'},

    {'cat': 'pcr-biologie-moleculaire', 'slug': 'pcr-chlamydia-mycoplasme-tanger', 'order': 4,
     'name_fr': 'PCR Chlamydia & Mycoplasme', 'name_en': 'Chlamydia & Mycoplasma PCR', 'name_ar': 'تحليل الكلاميديا والميكوبلازما',
     'description_fr': 'La PCR Chlamydia et Mycoplasme détecte avec précision ces infections sexuellement transmissibles souvent asymptomatiques. Non traitées, elles peuvent entraîner des complications sérieuses dont l\'infertilité.',
     'description_en': 'Chlamydia and Mycoplasma PCR precisely detects these often asymptomatic sexually transmitted infections. Untreated, they can lead to serious complications including infertility.',
     'description_ar': 'يكشف تحليل الكلاميديا والميكوبلازما عن هذه العدوى المنقولة جنسياً والتي غالباً تكون بدون أعراض.',
     'why_fr': 'Prescrit dans le cadre d\'un bilan de fertilité, en cas de symptômes urogénitaux, ou comme dépistage des IST. Le prélèvement peut être urinaire ou par écouvillon.',
     'delay_fr': 'Résultats en 3 à 5 jours', 'delay_en': 'Results in 3 to 5 days', 'delay_ar': 'النتائج خلال 3 إلى 5 أيام'},
]


class Command(BaseCommand):
    help = 'Populate analysis categories and individual analyses with FR/EN/AR content'

    def handle(self, *args, **options):
        self.stdout.write('Creating analysis categories...')
        cat_map = {}
        for cat_data in CATEGORIES:
            cat, created = AnalysisCategory.objects.update_or_create(
                slug=cat_data['slug'],
                defaults=cat_data
            )
            cat_map[cat_data['slug']] = cat
            status = 'CREATED' if created else 'UPDATED'
            self.stdout.write(f'  {status}: {cat.name_fr}')

        self.stdout.write(f'\nCreating {len(ANALYSES)} analyses...')
        for a_data in ANALYSES:
            cat_slug = a_data.pop('cat')
            a_data['category'] = cat_map[cat_slug]
            analysis, created = Analysis.objects.update_or_create(
                slug=a_data['slug'],
                defaults=a_data
            )
            a_data['cat'] = cat_slug  # restore for potential re-run
            status = 'CREATED' if created else 'UPDATED'
            self.stdout.write(f'  {status}: {analysis.name_fr}')

        total = Analysis.objects.count()
        self.stdout.write(self.style.SUCCESS(f'\nDone! {total} analyses in {AnalysisCategory.objects.count()} categories.'))
