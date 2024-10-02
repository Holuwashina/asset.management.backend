from django.core.management.base import BaseCommand
from assets_management.models import AssetValueMapping, Department

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        departments = [
            {"name": "IT/Technology", "qualitative_value": "Very High", "reason": "Critical for maintaining systems, data security, and operations."},
            {"name": "Finance", "qualitative_value": "Very High", "reason": "Essential for financial health, budgeting, and compliance."},
            {"name": "Human Resources", "qualitative_value": "High", "reason": "Important for workforce management, compliance, and organizational culture."},
            {"name": "Sales and Marketing", "qualitative_value": "High", "reason": "Key for revenue generation, market presence, and business growth."},
            {"name": "Operations", "qualitative_value": "High", "reason": "Central to daily business functions, service delivery, and efficiency."},
            {"name": "Customer Service", "qualitative_value": "Medium", "reason": "Impacts customer satisfaction and retention; moderate impact on business."},
            {"name": "Research and Development", "qualitative_value": "Very High", "reason": "Crucial for innovation, product development, and future growth."},
            {"name": "Legal", "qualitative_value": "High", "reason": "Vital for compliance, risk management, and legal affairs."},
            {"name": "Procurement", "qualitative_value": "Medium", "reason": "Affects cost management, supply chain efficiency, and vendor relations."},
            {"name": "Facilities Management", "qualitative_value": "Medium", "reason": "Manages physical infrastructure; moderate impact on operations."},
            {"name": "Quality Assurance", "qualitative_value": "High", "reason": "Ensures product/service quality and standards; crucial for customer satisfaction."},
            {"name": "Risk Management", "qualitative_value": "High", "reason": "Essential for identifying, assessing, and mitigating risks."},
            {"name": "IT Security", "qualitative_value": "Very High", "reason": "Critical for protecting digital assets and information from threats."},
            {"name": "Compliance", "qualitative_value": "High", "reason": "Ensures adherence to regulatory requirements and standards."},
            {"name": "Product Management", "qualitative_value": "High", "reason": "Drives product strategy, development, and market alignment."},
            {"name": "Customer Experience", "qualitative_value": "Medium", "reason": "Influences overall customer satisfaction and brand perception."},
            {"name": "Supply Chain Management", "qualitative_value": "Medium", "reason": "Manages logistics, inventory, and supplier relationships."},
            {"name": "Engineering", "qualitative_value": "High", "reason": "Critical for technical development and product support."},
            {"name": "Data Management", "qualitative_value": "Very High", "reason": "Vital for organizing, protecting, and leveraging organizational data."},
            {"name": "Internal Audit", "qualitative_value": "High", "reason": "Ensures accuracy of financial records and compliance with policies."},
            {"name": "Training and Development", "qualitative_value": "Medium", "reason": "Supports employee skill development and organizational growth."},
            {"name": "Strategic Planning", "qualitative_value": "High", "reason": "Guides long-term goals and business direction."},
            {"name": "Administration", "qualitative_value": "Medium", "reason": "Handles day-to-day administrative tasks and support."},
            {"name": "Legal and Compliance", "qualitative_value": "High", "reason": "Manages legal issues and ensures regulatory compliance."},
            {"name": "IT Support", "qualitative_value": "High", "reason": "Provides critical support for IT systems and user issues."},
            {"name": "Research and Analysis", "qualitative_value": "High", "reason": "Important for market research, data analysis, and strategic insights."},
            {"name": "Business Development", "qualitative_value": "High", "reason": "Focuses on growing the business, exploring new markets, and forging partnerships."},
            {"name": "Innovation Management", "qualitative_value": "Very High", "reason": "Drives new ideas, technologies, and processes to keep the business competitive."},
            {"name": "Corporate Strategy", "qualitative_value": "High", "reason": "Develops and implements the long-term vision and strategic objectives."},
            {"name": "Investor Relations", "qualitative_value": "High", "reason": "Manages communication and relationships with investors and stakeholders."},
            {"name": "Public Relations", "qualitative_value": "Medium", "reason": "Manages the company's public image and media relations."},
            {"name": "Health and Safety", "qualitative_value": "High", "reason": "Ensures workplace safety and compliance with health regulations."},
            {"name": "Environmental Sustainability", "qualitative_value": "High", "reason": "Focuses on reducing environmental impact and promoting sustainability practices."},
            {"name": "Technology Support", "qualitative_value": "High", "reason": "Provides support for technological tools and infrastructure."},
            {"name": "Digital Transformation", "qualitative_value": "Very High", "reason": "Oversees the integration of digital technology into all areas of the business."},
            {"name": "Contract Management", "qualitative_value": "Medium", "reason": "Manages contracts, negotiations, and legal agreements."},
            {"name": "Vendor Management", "qualitative_value": "Medium", "reason": "Oversees relationships with external vendors and service providers."},
        ]

        for dept in departments:
            asset_value_mapping = AssetValueMapping.objects.get(qualitative_value=dept['qualitative_value'])
            Department.objects.get_or_create(
                name=dept['name'], 
                asset_value_mapping=asset_value_mapping, 
                reason=dept['reason']
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded the Department data'))
