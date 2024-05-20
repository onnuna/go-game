-- Tworzenie bazy danych
CREATE DATABASE IF NOT EXISTS go_game_db;

-- Używanie bazy danych
USE go_game_db;

-- Tworzenie tabeli do przechowywania wyników gier
CREATE TABLE IF NOT EXISTS wyniki (
    id INT AUTO_INCREMENT PRIMARY KEY,
    gracz1 VARCHAR(50) NOT NULL,
    gracz2 VARCHAR(50) NOT NULL,
    zwyciezca VARCHAR(50) NOT NULL,
    data_gry DATETIME DEFAULT CURRENT_TIMESTAMP
);
