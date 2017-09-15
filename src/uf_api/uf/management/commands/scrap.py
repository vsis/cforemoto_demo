from decimal import Decimal
from datetime import datetime, date, timedelta
from django.core.management.base import BaseCommand, CommandError
from uf.scraper import scrap_uf
from uf.models import UF

class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            values = scrap_uf()
        except:
            print("Scraper error. Check your conection and bcentral.cl, and try again")
            return
        current_date = date(2017,1,1)
        for value in values:
            new_uf = UF(value=value, date=current_date)
            new_uf.save()
            current_date = current_date + timedelta(days=1)
        print("Done")
