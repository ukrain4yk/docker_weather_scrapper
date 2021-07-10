import schedule
import time

from scrap_weather_data import scrap_web_data
from configuration_parser import db_details, config_reader
from db_operations import database_insert


if __name__ == '__main__':
    def run_script():
        weather_links = config_reader('weather_links')
        weather_data = scrap_web_data(weather_links['token'], weather_links['data'])
        connection = db_details('db_credentials')
        database_insert(connection, weather_data)

    schedule.every(1).minute.do(run_script)

    while True:
        schedule.run_pending()
        time.sleep(1)
