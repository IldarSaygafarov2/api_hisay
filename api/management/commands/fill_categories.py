import docx2txt
import re
import os

from api.models import Category, CategoryHashtag
from django.conf import settings
from django.core.management.base import BaseCommand


def make_list_from_text(text: str):
    lines = list(filter(lambda line: line != '', text.split("\n")))
    return [line for line in lines if not line.endswith(":")]


def get_categories_from_file(filename: str):
    text = docx2txt.process(filename)
    lines = make_list_from_text(text)
    result = {}

    for line in lines:

        tags = re.findall(r'#[a-zа-яё_-]+', line)
        for tag in tags:
            if tag in line:
                line = line.replace(tag, '').strip()
        result[line] = tags

    return result


class Command(BaseCommand):
    help = "Заполняем категории и их хештеги"

    def handle(self, *args, **options):
        path = os.path.join(settings.BASE_DIR, r'categories.docx')

        categories = get_categories_from_file(path)
        for item in categories:
            obj = Category.objects.create(name=item)
            obj.save()

            print(f'{item} was created', end="")

            for tag in categories[item]:
                tag_obj = CategoryHashtag.objects.create(
                    tag=tag,
                    category=obj
                )
                tag_obj.save()
                print(tag, sep=" ")
