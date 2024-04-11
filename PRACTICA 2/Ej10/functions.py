def generate_structure (names:str, goals:tuple, goals_avoided:tuple, assists:tuple):
  """ 
  Genera un diccionario con la información de los jugadores.
  Parameters:
  names (str): Una cadena que contiene los nombres de los jugadores separados por comas.
  goals (tuple): Una lista de enteros que representa la cantidad de goles marcados por cada jugador.
  goals_avoided (tuple): Una lista de enteros que representa la cantidad de goles evitados por cada jugador.
  assists (tuple): Una lista de enteros que representa la cantidad de asistencias realizadas por cada jugador.

  Returns:
  dict: Un diccionario donde las claves son los nombres de los jugadores y los valores son diccionarios
  con la información de cada jugador, incluyendo 'Goles', 'Goles evitados' y 'Asistencias'.
  """

  special_characters = (' ', "'", '\n')

  for character in special_characters:
    if character in names:
      names=names.replace (character,'')
  
  names= names.split (',')

  players_info = {}
  for i, player in enumerate(names):
    players_info[player] = {'Goles': goals[i] , 
                            'Goles evitados': goals_avoided [i], 
                            'Asistencias': assists[i]}
  return players_info

def getgoleador (structure:dict):
  """
  Parameters:
  structure (dict): estructura con los jugadores y sus respectivos goles.
  Returns:
  str: Nombre del jugador con más goles.
  """

  maxgoles=0
  goleador =""
  for jugador,info in structure.items():
    goles= info.get ('Goles')
    if goles>maxgoles:
      maxgoles=goles
      goleador=jugador
  
  return goleador, maxgoles 

def getmip (structure:dict):
  """
  Parameters:
  structure (dict): estructura con los jugadores y sus respectivos goles.
  Returns:
  str: Nombre del jugador mas influyente (most influential player).
  """

  maxpoints=0
  mip = ""
  for jugador,info in structure.items():
    points= info.get ('Goles') * 1.5 +  info.get ('Goles evitados') * 1.25 + info.get ('Asistencias')
    if points> maxpoints:
      maxpoints=points
      mip=jugador
  
  return mip

def getpromediogeneral (goals:tuple):
  """
  Parameters:
  goals (tuple): Una lista de enteros que representa la cantidad de goles marcados por cada jugador.
  Returns:
  promedy (float): promedio de goles por partido del equipo en general. 
  """

  promedy=sum(goals) / 25 
  return promedy

def promedypermatch (goals:tuple):
  promedy= max(goals)/25
  return promedy