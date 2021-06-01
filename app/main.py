from app.scrap_weather_data import scrap_web_data
from app.configuration_parser import db_details, config_reader
from app.db_operations import database_insert

if __name__ == '__main__':
    weather_links = config_reader('weather_links')
    print(weather_links)
    weather_data = scrap_web_data(weather_links['token'], weather_links['data'])
    print(weather_data)
    connection = db_details('db_credentials')

    database_insert(connection, weather_data)
