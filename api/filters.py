# import django_filters as filters
#
#
# class RequestFilter(filters.FilterSet):
# 	filters.A
#     category_id = filters.BaseInFilter(field_name='category_id',
#                                                method='filter_by_category_id')
#
#     # noinspection PyUnusedLocal
#     @staticmethod
#     def filter_by_category_id(full_qs, field_name, value):
# 	    if value.lower() == 'true':
# 		    return full_qs.exclude(setting=1)
# 	    return full_qs.filter(setting=value)
#