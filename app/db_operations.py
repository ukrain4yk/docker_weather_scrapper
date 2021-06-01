from psycopg2 import Error

"""SQL queries definitions"""
INSERT_QUERY_HEADER = """insert into public.weather_data(
                                    pressure, wind_speed, wind_direction,
                                    temp_2, temp_5, temp_dew_p, humidity, 
                                    fall_moment, fall_type, visibility, 
                                    uv_sun, uv_gen, dust_pm10, dust_pm25, 
                                    ozone, date) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,
                                    %s,%s,%s,%s,%s,%s,%s,%s)"""


def database_insert(db_connection, weather_data):
    try:
        cursor = db_connection.cursor()
        cursor.execute(INSERT_QUERY_HEADER, weather_data[-1])

        db_connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into table")

    except (Exception, Error) as error:
        print("Failed to insert record into table. Info: ", error)
    finally:
        # closing database connection.
        if db_connection:
            cursor.close()
            db_connection.close()
            print("PostgreSQL connection is closed")


# Additional data to test
# Record data to insert
# record_to_insert1 = ('1004.8','1.2','ESE','10.5','12.7','2.98','59.6','brak','d.','20','184','136.7','15.9','12.3','')
# record_to_insert2 = ('1005.9','0.4','SSE','6.8','3.9','3.46','79.2','brak','---','20','0','0','37.3','21.1', '')
# Query execution for above data
# cursor.execute(postgres_insert_query, record_to_insert1)
# cursor.execute(postgres_insert_query, record_to_insert2)
