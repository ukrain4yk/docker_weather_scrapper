import json
import requests
import urllib3
from datetime import datetime
from bs4 import BeautifulSoup

import log_handler

logger = log_handler.get_logger(__name__)


def scrap_web_data(w_token_url, w_data_url):
    """Function to scrap weather data from url"""
    try:
        # Get date/time now to use in weather data tuple
        date_now = datetime.now()
        dt_string = date_now.strftime("%d/%m/%Y %H:%M:%S")

        """Gathering data as list from weather webpage"""
        logger.debug(f"Token url has been passed - 'str(w_token_url)'")
        logger.debug('Token url has been passed - %s', str(w_data_url))

        # Remove warnings while using HTTPS/SSL
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        # Getting token from web page to get CSV with weather data
        get_token = requests.get(w_token_url, verify=False).text
        token = json.loads(get_token)
        logger.info('Session token from web page, %s', str(token['token']))

        # Getting CSV file with data from web page
        get_csv_data = requests.get(w_data_url + token['token'], verify=False).text

        # Parsing HTML tags to get pure text
        soup_parser_for_data = BeautifulSoup(get_csv_data, "lxml")
        weather_list_not_filtered = soup_parser_for_data.text.strip().split('\n')

        # Remove logger debug since got a nested tuple with Greek 'alfa' character
        # Solved by using local variable "ENV PYTHONUTF8 1" to docker file
        # logger.debug('Weather dict: %s', str(weather_list_not_filtered))
        # Creating a list with cleaned values
        weather_list_clean = list(filter(None, weather_list_not_filtered))
        logger.debug('Weather List with only values: %s', str(weather_list_clean))

        """Weather data extracting: details, headers, values as dict"""

        # Return time when measured on meteo-station
        weather_forecast_time_details = str(weather_list_clean[0])
        logger.debug('Weather list received, %s', str(weather_forecast_time_details))
        logger.info('Weather list received, %s', bool(weather_forecast_time_details))

        # Remove first element which is timestamp when measured
        weather_list_clean.pop(0)

        weather_headers = list(
            weather_list_clean[i] for i in range(0, len(weather_list_clean), 2)
        )
        logger.debug('Weather header names: %s', str(weather_headers))
        weather_dict_ready = list(
            weather_list_clean[i + 1] for i in range(0, len(weather_list_clean), 2)
        )
        logger.debug('Weather values: %s', str(weather_dict_ready))

        if len(weather_dict_ready) == 14:
            weather_dict_ready.append('')
            weather_headers.append('O3')
        elif len(weather_dict_ready) == 15:
            pass
        else:
            raise IndexError

        # Add Date tag to tuple of weather values
        weather_dict_ready.append(dt_string)
        weather_headers.append('Time stamp')
        return weather_forecast_time_details, weather_headers, weather_dict_ready
    except IndexError as err:
        logger.error('Empty list passed, ' + str(err))

# Extra content
# Create a dictionary with INT keys + values
# weather_dict_1 = {str(math.trunc(i/2)): weather_list_clean[i+1] for i in range(0, len(weather_list_clean), 2)}
# weather_dict_2 = {weather_list_clean[i+1]: weather_list_clean[i] for i in range(0, len(weather_list_clean), 2)}
