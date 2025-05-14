from mongoengine import connect
import configparser


config = configparser.ConfigParser()
config.read('config/config.ini')

mongo_user = config.get('DB', 'user')
mongo_pass = config.get('DB', 'pass')
db_name = config.get('DB', 'db_name')
domain = config.get('DB', 'domain')

conn = connect(host=f"""mongodb+srv://{mongo_user}:{mongo_pass}@{domain}/{db_name}?retryWrites=true&w=majority""", ssl=True)
