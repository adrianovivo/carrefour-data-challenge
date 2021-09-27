#Módulo de conexão ao Mongodb na conta criada gratuitamente na Cloud do MongoDB

from pymongo import MongoClient

from src.secrets import PASSWORD_MONGO

url_cloud = "mongodb+srv://appuser:{}@clustergcp.9xfz1.mongodb.net/ClusterGCP?retryWrites=true&w=majority".format(PASSWORD_MONGO)

client = MongoClient(url_cloud)

#criando database
db = client.dio_twitter

#criando collection
trends_collection = db.trends
