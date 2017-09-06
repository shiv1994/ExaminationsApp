import django_tables2 as tables

from .models import MembershipExamUser

class MembershipExamUserTable(tables.Table):
    class Meta:
        model = MembershipExamUser
        fields = ('examPaper.status', 'firstExaminer.phone')
        attrs = {"class": "table-striped table-bordered"}

empty_text = "There are no exam papers matching the criteria."