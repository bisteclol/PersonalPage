from django import template
from portfolioPage.models import Job

register = template.Library()

@register.assignment_tag
def get_job_list():
    joblist = Job.objects.filter(company='CGI')
    return {'joblist': joblist}

