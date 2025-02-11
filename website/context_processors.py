# context_processors.py
from .models import CompanyInfo

def company_info(request):
    company = CompanyInfo.objects.first()  # Assuming only one entry exists
    return {
        'company': company
    }
