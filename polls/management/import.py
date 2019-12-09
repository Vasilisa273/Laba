from __future__ import unicode_literals

import re
from django.contrib.sessions.backends import file
from django.core.management.base import BaseCommand
from polls.models import RusWord, EnWord


class Command(BaseCommand):

    can_import_settings = True

    def add_arguments(self, parser):
        file.add_arguments("path_docx", nargs='+', type=str)

    def handle(self, *args, **options):
        rusword = RusWord.objects.all()
        for cur_rusword in rusword:
            cur_rusword.delete()

        enword = EnWord.objects.all()
        for cur_enword in enword:
            cur_enword.delete()

        arg = options["path_docx"]
        str1 = str(arg[0])
        self.process_file(str1)

    def process_file(self, file1):
