from django.shortcuts import render

def company_list(request):
    from .models import CompanyRevenue  # Move import inside function
    companies = CompanyRevenue.objects.all()
    return render(request, 'company_table.html', {'companies': companies})

