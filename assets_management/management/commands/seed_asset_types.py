from django.core.management.base import BaseCommand
from assets_management.models import AssetType

class Command(BaseCommand):
    def handle(self, *args, **options):
        asset_types = [
            {'name': 'Hardware', 'description': 'Physical computing equipment used to store, process, and manage data.'},
            {'name': 'Software', 'description': 'Programs and applications critical for business operations.'},
            {'name': 'Data', 'description': 'Digital information that is valuable to the organization.'},
            {'name': 'Physical Infrastructure', 'description': 'Tangible physical assets that support business operations.'},
            {'name': 'Digital Content', 'description': 'Online presence and digital communication channels.'},
            {'name': 'Intellectual Property', 'description': 'Legal rights and proprietary information critical to competitive advantage.'},
            {'name': 'Processes', 'description': 'Established methods and protocols for conducting business activities.'},
            {'name': 'Contracts', 'description': 'Legal agreements that define business relationships and obligations.'},
            {'name': 'Machinery', 'description': 'Equipment used in production and service delivery.'},
            {'name': 'Vehicles', 'description': 'Transportation assets used for logistics and business operations.'},
            {'name': 'Documents', 'description': 'Written records that provide guidelines, records, and plans.'},
            {'name': 'Communication Systems', 'description': 'Tools and systems used for internal and external communication.'},
            {'name': 'Network Infrastructure', 'description': 'Devices that support network connectivity and security.'},
            {'name': 'Security Systems', 'description': 'Physical and digital systems to protect assets and ensure security.'},
            {'name': 'Cloud Services', 'description': 'Online services and resources hosted on cloud infrastructure.'},
            {'name': 'Training Materials', 'description': 'Resources and programs designed for employee skill development.'},
            {'name': 'Customer Interfaces', 'description': 'Systems used for interacting with and managing customer relationships.'},
            {'name': 'Research & Development', 'description': 'Assets related to the development of new products and technologies.'},
            {'name': 'Financial Instruments', 'description': 'Assets related to financial investments and risk management.'},
            {'name': 'Legal Assets', 'description': 'Legal documents and filings relevant to business operations.'},
            {'name': 'Environmental Assets', 'description': 'Assets related to environmental impact and sustainability practices.'},
        ]

        for asset_type in asset_types:
            AssetType.objects.get_or_create(name=asset_type['name'], defaults={'description': asset_type['description']})

        self.stdout.write(self.style.SUCCESS('Successfully seeded AssetType data'))
