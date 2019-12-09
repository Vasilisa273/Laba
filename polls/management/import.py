from __future__ import unicode_literals

import re
import codecs
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

        new_mas = []
        splitted = codecs.open('import_laba', 'r', encoding='utf-8').read().splitlines()
        for spl in splitted:
            if spl != str(""):
                new_mas.append(spl)

        for new in new_mas:

            regex_enword_temp = re.search(r'^[a-zA-Z]', new)
            if regex_enword_temp is not None:
                regex_enword = regex_enword_temp.group()
            else:
                regex_enword =''

            regex_rusword_temp = re.search(r'^[а-яА-Я]', new)
            if regex_rusword_temp is not None:
                regex_rusword = regex_rusword_temp.group()
            else:
                regex_rusword =''

            english = regex_enword.encode('utf-8')
            russia = regex_rusword.encode('utf-8')

            enword = EnWord(enword=english)
            enword.save()
            rusword = RusWord(rusword=russia)
            rusword.save()

