import requests

import json

# dictionary mapping the SF neighborhoods to Personal Weather Station ID
NEIGHBORHOODS = {
    'noe valley': 'KCASANFR3',
    'mission': 'KCASANFR944',
    'hunters point': 'KCASANFR2',
    'potrero hill': 'KCASANFR526',
    'soma': 'KCASANFR231',
    'downtown': 'KCASANFR236',
    'north beach': 'KCASANFR137',
    'marina': 'KCASANFR1018',
    'presidio': 'KCASANFR148',
    'richmond': 'KCASANFR128',
    'sunset': 'KCASANFR287',
    'twin peaks': 'KCASANFR34',
    'mission_bay': 'KCASANFR14',
    'pacific heights': 'KCASANFR874',
    'castro': 'KCASANFR938',
    'haight': 'KCASANFR384',
    'excelsior': 'KCASANFR663',
    'ingleside': 'KCASANFR100',
    'lake merced': 'KCASANFR409',
    'bayview': 'KCASANFR348'
}

# #API URL that calls the specific weather station
# apiUrl_base = 'http://api.wunderground.com/api/' + weather_key 


def get_weather(pws_id, neighborhood_name):
    """ Make request to Weather Underground for temp in specific SF neighborhood."""

    # weather_pws = urllib2.urlopen(apiUrl_base + '/conditions/q/pws:' + pws_id + '.json' )
    response = requests.get(api_url)