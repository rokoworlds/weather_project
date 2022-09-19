from dotenv import load_dotenv
import os
load_dotenv()


database_hostname = os.getenv('DATABASE_HOSTNAME')
database_port = os.getenv('DATABASE_PORT')
database_password = os.getenv('DATABASE_PASSWORD')
database_name = os.getenv('DATABASE_NAME')
database_username = os.getenv('DATABASE_USERNAME')
secret_key = os.getenv('SECRET_KEY')
api_key = os.getenv('API_KEY')
owm_endpoint = os.getenv('OWM_ENDPOINT')

