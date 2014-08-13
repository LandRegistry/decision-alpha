def check_change_name_marriage(data):
	iso_country_code = data.get('iso-country-code', None) 
	if iso_country_code == 'GB':
		return True
	else:
		return False