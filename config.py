from os import environ  
  
class Config:
     API_ID = int(environ.get("API_ID", '22561857')) 
     API_HASH = environ.get("API_HASH", "6581d3daf4b40f722a22ddb5ca1281c2") 
     BOT_TOKEN = environ.get("BOT_TOKEN", "6558508467:AAE71Fy7bWSpD-2qd-LPH9tAnL2GW8T1Qe4")  
     BOT_SESSION = environ.get("BOT_SESSION", "bot")  
     DATABASE_URI = environ.get("DATABASE", "mongodb+srv://Zishan:Zishan@cluster0.pnwq7om.mongodb.net/?retryWrites=true&w=majority") 
     DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0") 
     BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '5672857559').split()] 
  
class temp(object): 
     lock = {} 
     CANCEL = {} 
     forwardings = 0 
     BANNED_USERS = [] 
     IS_FRWD_CHAT = [] 
 
