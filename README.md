# web-3-tp-gabarit

Gabarit d'application Flask pour le cours de Web 3

1. copier/coller le fichier example.env pour créer un fichier .env

2. Pour rouler l'application:

    `docker compose up --build -d`

3. Pour rouler le script d'initialisation de cartes pokémons:

    `docker compose exec app python -m scripts.init_pokemon_card`
