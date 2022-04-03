from environs import Env


env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста
PASSWORD_MAIL = env.str("PASSWORD_MAIL")
PASSWORD_DB = env.str("PASSWORD_DB")
DB = env.str("DB")
USER = env.str("USER")
PORT = env.str("PORT")

