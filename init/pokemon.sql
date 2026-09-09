SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";

USE `tp`

CREATE OR REPLACE TABLE pokemon_card (
    `id` varchar(25) NOT NULL,
    `card_set` varchar(50) NOT NULL,
    `series` varchar(50) NOT NULL,
    `publisher` varchar(50) NOT NULL,
    `generation` varchar(50) NOT NULL,
    `release_date` datetime NOT NULL,
    `artist` varchar(100) NOT NULL,
    `name` varchar(100) NOT NULL,
    `set_num` int(10) NOT NULL,
    `pokedex_numb` int(10),
    `types` varchar(250),
    `supertype` varchar(100) NOT NULL,
    `level` int(10),
    `hp` int(10),
    `evolvesFrom` varchar(100),
    `evolvesTo` varchar(100),
    `rarity` varchar(100)
);
