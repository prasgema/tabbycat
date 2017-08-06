# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 07:45
from __future__ import unicode_literals

from django.db import migrations


NAMES = {"novice": "Novice", "esl": "ESL", "efl": "EFL"}
SEQS = {"novice": 3, "esl": 1, "efl": 2}


def convert_speaker_categories(apps, schema_editor)
    Speaker = apps.get_model("participants", "Speaker")
    SpeakerCategory = apps.get_model("participants", "SpeakerCategory")
    TournamentPreferenceModel = apps.get_model("options", "TournamentPreferenceModel")

    categories = {} # (tournament, category): SpeakerCategory object

    def get_category(speaker, field):
        key = (speaker.team.tournament.slug, field)
        if key not in categories:
            categories[key] = SpeakerCategory.objects.create(tournament=speaker.team.tournament,
                name=field)
        return categories[key]

    for speaker in Speaker.objects.all():
        categories = []
        for field in ['novice', 'esl', 'efl']:
        if getattr(speaker, category, False):
            category = get_category(speaker, field)
            categories.append(category)
        speaker.categories.set(categories)


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0030_auto_20170807_0726'),
        ('options', '0008_rename_position_names_to_side_names'),
    ]

    operations = [
        migrations.RunPython(convert_speaker_categories, reverse_code=migrations.RunPython.noop)
    ]
