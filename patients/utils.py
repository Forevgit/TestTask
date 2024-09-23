# from django.db.models import F, ExpressionWrapper, IntegerField
# from datetime import date
#
# def annotate_with_age(queryset):
#     """Annotation for calculating patients' age."""
#     today = date.today()
#
#     return queryset.annotate(
#         age=ExpressionWrapper(
#             today.year - F('date_of_birth__year') - (
#                 (today.month, today.day) < (F('date_of_birth__month'), F('date_of_birth__day'))
#             ),
#             output_field=IntegerField()
#         )
#     )
