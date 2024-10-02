from django.core.management.base import BaseCommand
from assets_management.models import AssetValueMapping

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        mappings = [
            {'qualitative_value': 'Very Low', 'crisp_value': 0.1},
            {'qualitative_value': 'Low', 'crisp_value': 0.3},
            {'qualitative_value': 'Medium', 'crisp_value': 0.5},
            {'qualitative_value': 'High', 'crisp_value': 0.7},
            {'qualitative_value': 'Very High', 'crisp_value': 0.9},
        ]

        for mapping in mappings:
            AssetValueMapping.objects.update_or_create(
                qualitative_value=mapping['qualitative_value'],
                defaults={'crisp_value': mapping['crisp_value']}
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded AssetValueMapping table'))