SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";

USE `tp`

CREATE OR REPLACE TABLE pokemon_card (
    `id` varchar(25) NOT NULL PRIMARY KEY,
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
    `evolvesFrom` varchar(100),
    `evolvesTo` varchar(100),
    `rarity` varchar(100)
);

CREATE OR REPLACE TABLE collection_items (
    `id` int(10) unsigned NOT NULL auto_increment PRIMARY KEY,
    `card_id` varchar(25) NOT NULL,
    `added_date` datetime NOT NULL default CURRENT_TIMESTAMP,
    `condition` varchar(50) NOT NULL,
    `cost` decimal(10,0) NOT NULL default '0',
    `status` varchar(50) NOT NULL,
    `photo` varchar(50),
    CONSTRAINT `fk_card_id`
        FOREIGN KEY (card_id) REFERENCES pokemon_card (id)
        ON DELETE CASCADE
        ON UPDATE RESTRICT
);
