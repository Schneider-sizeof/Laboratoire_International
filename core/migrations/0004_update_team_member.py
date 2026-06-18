"""
Data migration: update team member to only Dr. Tarik Driss.
"""
from django.db import migrations

def update_team(apps, schema_editor):
    TeamMember = apps.get_model('core', 'TeamMember')
    TeamMember.objects.all().delete()
    TeamMember.objects.create(
        name='Dr. Tarik Driss',
        initials='TD',
        role_fr='Médecin Biologiste',
        role_en='Medical Biologist',
        role_ar='طبيب إحيائي',
        role_es='Médico Biólogo',
        role_de='Medizinischer Biologe',
        role_nl='Medisch Bioloog',
        role_it='Medico Biologo',
        bio_fr="Ex biologiste à l'hôpital militaire Moulay Ismail Meknès. D.I.U en management de qualité Bordeaux.",
        bio_en="Former biologist at the Moulay Ismail Military Hospital in Meknes. D.I.U in quality management from Bordeaux.",
        bio_ar="إحيائي سابق بالمستشفى العسكري مولاي إسماعيل بمكناس. دبلوم جامعي في إدارة الجودة من بوردو.",
        bio_es="Ex biólogo en el Hospital Militar Moulay Ismail de Mequinez. D.I.U en gestión de calidad de Burdeos.",
        bio_de="Ehemaliger Biologe am Militärkrankenhaus Moulay Ismail in Meknes. D.I.U. in Qualitätsmanagement aus Bordeaux.",
        bio_nl="Voormalig bioloog in het Militair Hospitaal Moulay Ismail in Meknes. D.I.U in kwaliteitsmanagement uit Bordeaux.",
        bio_it="Ex biologo presso l'Ospedale Militare Moulay Ismail di Meknès. D.I.U in gestione della qualità di Bordeaux.",
        order=1,
    )

def reverse_update(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_populate_default_data'),
    ]

    operations = [
        migrations.RunPython(update_team, reverse_update),
    ]
