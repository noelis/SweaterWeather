from os import environ

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
# weather_pws = urllib2.urlopen('http://api.wunderground.com/api/' + '/conditions/q/pws:' + pws_id + '.json' )


def get_weather(pws_id, neighborhood_name):
    """ Make request to Weather Underground for temp in specific SF neighborhood."""

    # get Weather Underground API key using os.environ from secrets.sh
    app_key = environ["KEY"]

    # using the requests module, build the API url to get the weather conditions at a specific weather station (SF neighborhood)
    api_response = requests.get('http://api.wunderground.com/api/' + app_key + '/conditions/q/pws:' + pws_id + '.json')

    # turn the response into a string (using content so it turns it into a string, instead of text which turns it into unicode)
    json_string= api_response.content

    # converts json string into a dictionary
    converted_json = json.loads(api_response.content)

    
