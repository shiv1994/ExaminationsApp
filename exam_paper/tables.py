import django_tables2 as tables

from .models import MembershipExamUser

from django_tables2.utils import A


class MembershipExamUserTable(tables.Table):
    paper = tables.LinkColumn(viewname='allExamsFirstExaminerPaperDetail', args=[A('pk')], orderable=False, text='Open Details')

    class Meta:
        model = MembershipExamUser
        fields = ('examPaper.course.courseCode', 'examPaper.status', 'firstExaminer.phone', 'examPaper.course.faculty')
        attrs = {"class": "table-striped table-bordered", "width": "200%"}
        empty_text = "There are no exam papers matching the criteria."


class MembershipExamUserTableSecond(tables.Table):
    paper = tables.LinkColumn(viewname='allExamsSecondExaminerPaperDetail', args=[A('pk')], orderable=False, text='Open Details')

    class Meta:
        model = MembershipExamUser
        fields = ('examPaper.course.courseCode', 'examPaper.status', 'firstExaminer.phone', 'examPaper.course.faculty')
        attrs = {"class": "table-striped table-bordered", "width": "200%"}
        empty_text = "There are no exam papers matching the criteria."
