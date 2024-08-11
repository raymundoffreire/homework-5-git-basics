def date_format(date):
    month = date[:2]
    day = date[:-5][-2:]
    year = date[-4:]
    return year + '-' + month + '-' + day
