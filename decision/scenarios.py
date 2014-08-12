SEND_TO_CASEWORK = 100
SEND_TO_CHECKING = 200


def change_name_country(country_of_marriage):
    if country_of_marriage == 'UK':
        return SEND_TO_CASEWORK
    else:
        return SEND_TO_CHECKING