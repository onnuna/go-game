from database.db_config import execute_query, fetch_results

def insert_game_result(player1, player2, winner):
    """
    Wstawia wynik gry do bazy danych.
    - player1: Nazwa gracza 1
    - player2: Nazwa gracza 2
    - winner: Nazwa zwycięzcy
    """
    query = """
    INSERT INTO wyniki (gracz1, gracz2, zwyciezca) 
    VALUES (%s, %s, %s)
    """
    params = (player1, player2, winner)
    execute_query(query, params)

def get_game_results():
    """
    Pobiera ostatnie 100 wyników gier z bazy danych.
    """
    query = "SELECT * FROM wyniki ORDER BY data_gry DESC LIMIT 100"
    return fetch_results(query)
