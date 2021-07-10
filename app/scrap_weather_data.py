import json
import requests
import urllib3
from datetime import datetime

from bs4 import BeautifulSoup


def scrap_web_data(w_token_url, w_data_url):
    # Remove warnings while using HTTPS/SSL
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    # Getting token from web page to get CSV with weather data
    get_token = requests.get(w_token_url, verify=False).text
    token = json.loads(get_token)
    # Getting CSV file with data from web page
    get_csv_data = requests.get(w_data_url + token['token'], verify=False).text
    # Parsing HTML tags to get pure text
    soup_parser_for_data = BeautifulSoup(get_csv_data, "lxml")
    weather_list_not_filtered = soup_parser_for_data.text.strip().split('\n')
    # Creating a list with cleaned values
    weather_list_clean = list(filter(None, weather_list_not_filtered))

    """Weather data extracting: details, headers, values as dict"""
    if len(weather_list_clean) == 0:
        # Return time when measured on meteo-station
        weather_forecast_time_details = str(weather_list_clean[0])
        # Remove first element which is datatime
        weather_list_clean.pop(0)
        weather_headers = list(
            weather_list_clean[i] for i in range(0, len(weather_list_clean), 2)
        )
        weather_dict_ready = list(
            weather_list_clean[i+1] for i in range(0, len(weather_list_clean), 2)
        )

        if len(weather_dict_ready) != 15:
            weather_dict_ready.append('')
            weather_headers.append('O3')
        elif len(weather_dict_ready) == 15:
            pass

        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        weather_dict_ready.append(dt_string)
        weather_headers.append('Time stamp')
        return weather_forecast_time_details, weather_headers, weather_dict_ready
    else:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        return None, None, ('0', '0', 'S', '0', '0', '0', '0', 'brak', '---', '0', '0', '0', '0', '0', '', dt_string)

# Extra content
# Create a dictionary with INT keys + values
# weather_dict_1 = {str(math.trunc(i/2)): weather_list_clean[i+1] for i in range(0, len(weather_list_clean), 2)}
# weather_dict_2 = {weather_list_clean[i+1]: weather_list_clean[i] for i in range(0, len(weather_list_clean), 2)}
