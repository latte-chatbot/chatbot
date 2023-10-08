-- Tabela para guardar informações do usuário
CREATE TABLE IF NOT EXISTS usuario_info (
    user_id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100)
);