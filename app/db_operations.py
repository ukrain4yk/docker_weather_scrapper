from psycopg2 import Error

import log_handler

"""Logger initialization"""
logger = log_handler.get_logger(__name__)

"""SQL queries definitions"""
INSERT_QUERY_HEADER = """insert into public.weather_data(
                                    pressure, wind_speed, wind_direction,
                                    temp_2, temp_5, temp_dew_p, humidity, 
                                    fall_moment, fall_type, visibility, 
                                    uv_sun, uv_gen, dust_pm10, dust_pm25, 
                                    ozone, date) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,
                                    %s,%s,%s,%s,%s,%s,%s,%s)"""


def database_insert(db_connection, weather_data):
    global cursor
    try:
        logger.info('PostgreSQL connection initiated')
        cursor = db_connection.cursor()
        cursor.execute(INSERT_QUERY_HEADER, weather_data[-1])
        logger.debug('Weather data details to insert: %s', str(weather_data[-1]))

        db_connection.commit()
        count = cursor.rowcount
        logger.info("%s Record inserted successfully into table", str(count))

    except (Exception, Error) as error:
        logger.error('Failed to insert record into table. Info: s%', str(error))
    finally:
        # closing database connection.
        if db_connection:
            cursor.close()
            db_connection.close()
            logger.info("PostgreSQL connection is closed")


# Additional data to test
# Record data to insert
# record_to_insert1 = ('1004.8','1.2','ESE','10.5','12.7','2.98','59.6','brak','d.','20','184','136.7','15.9','12.3','')
# record_to_insert2 = ('1005.9','0.4','SSE','6.8','3.9','3.46','79.2','brak','---','20','0','0','37.3','21.1', '')
# Query execution for above data
# cursor.execute(INSERT_QUERY_HEADER, record_to_insert1)
# cursor.execute(INSERT_QUERY_HEADER, record_to_insert2)
