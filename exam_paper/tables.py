import django_tables2 as tables

from .models import MembershipExamUser

from django_tables2.utils import A

class MembershipExamUserTable(tables.Table):

    class Meta:
        model = MembershipExamUser
        paper = tables.LinkColumn('examPaperDetail', args=[A('pk')])
        fields = ('examPaper.course.courseCode', 'examPaper.status', 'firstExaminer.phone', 'examPaper.course.faculty', 'paper')
        attrs = {"class": "table-striped table-bordered"}
    empty_text = "There are no exam papers matching the criteria."