import ast

import django_filters as filters


class RequestFilter(filters.FilterSet):
	category_id = filters.Filter(
		field_name='category_id', method='filter_by_category_id')
	
	is_digital_categories = filters.BooleanFilter()
	status = filters.CharFilter()

	# noinspection PyUnusedLocal
	@staticmethod
	def filter_by_category_id(full_qs, field_name, value):
		category_id = ast.literal_eval(value)
		return full_qs.filter(digital_categories__in=category_id)
