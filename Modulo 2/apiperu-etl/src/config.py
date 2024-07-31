from decouple import config

class Config:
    api_token = config('API_TOKEN')
    api_url_ruc = config('API_URL_RUC') 
    mysql_host = config('MYSQL_HOST')
    mysql_user = config('MYSQL_USER')
    mysql_password = config('MYSQL_PASSWORD')
    mysql_database = config('MYSQL_DATABASE')