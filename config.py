env_vars = {
  # Get From my.telegram.org
  "API_HASH": "ef85493cd32eadcb5309b5957d8d1b86",
  # Get From my.telegram.org
  "API_ID": "22606849",
  #Get For @BotFather
  "BOT_TOKEN": "7938878446:AAEpNUP85j8yNe0A6r8crusIpeFUfA3crno",
  # Get For tembo.io
  "DATABASE_URL_PRIMARY": "mongodb+srv://meow:meow@meow.a6bo1.mongodb.net/?retryWrites=true&w=majority&appName=meow",
  # Logs Channel Username Without @
  "CACHE_CHANNEL": "Hindi_Kochikame",
  # Force Subs Channel username without @
  "CHANNEL": "Anime_Sovereign",
  # {chap_num}: Chapter Number
  # {chap_name} : Manga Name
  # Ex : Chapter {chap_num} {chap_name} @Manhwa_Sovereign
  "FNAME": "",
  # Put Thumb Link 
  "THUMB": ""
}

dbname = env_vars.get('DATABASE_URL_PRIMARY') or env_vars.get('DATABASE_URL') or 'sqlite:///test.db'

if dbname.startswith('postgres://'):
    dbname = dbname.replace('postgres://', 'postgresql://', 1)
    
