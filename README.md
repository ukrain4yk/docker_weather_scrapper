# docker_weather_scrapper
Python app to fill DB with weather data

Application get data from web page as string and insert it to DB
Docker configuration avaible to run app in container (in my case DB runs on separate server)

In application used libraries:

urllib3 - remove exception with HTTPS certs
requests - to get data from web page (web page using token + url and return CSV string)
beautifulsoup4 & lxml- to parce csv (using lxml) into text and then to list 
psycopg2 - library to get conneciton to DB, in my case it's Postgres
schedule - library to run funtion on sertain scheduled time (simular to CRON in Linux)

# Ukrain4yk
