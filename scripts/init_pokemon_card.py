import csv
from bd import creer_connexion
from datetime import datetime

FILE_PATH = "/app/data/pokemon-tcg-data-master 1999-2023.csv"

if __name__ == "__main__":
    with open(FILE_PATH, mode="r") as f:
        csv_reader = csv.reader(f)
        header = next(csv_reader)

        with creer_connexion() as connexion:
            with connexion.get_curseur() as curseur:
                for row in csv_reader:
                    try:

                        card_id = row[0].strip() if row[0] else None
                        card_set = row[1].strip() if row[1] else None
                        series = row[2].strip() if row[2] else None
                        publisher = row[3].strip() if row[3] else None
                        generation = (
                            row[4].strip() if row[4] and row[4].strip() else None
                        )
                        release_date_str = row[5].strip() if row[5] else None
                        artist = row[6].strip() if row[6] else None
                        name = row[7].strip() if row[7] else None
                        set_num = int(row[8]) if row[8] and row[8].strip() else None
                        types = row[9].strip() if row[9] else None
                        supertype = row[10].strip() if row[10] else None
                        level = int(row[12]) if row[12] and row[12].strip() else None
                        hp = int(row[13]) if row[13] and row[13].strip() else None
                        evolvesFrom = row[14].strip() if row[14] else None
                        evolvesTo = row[15].strip() if row[15] else None
                        rarity = row[21].strip() if row[21] else None
                        national_pokedex_number = row[23].strip() if row[23] else None

                        # format pokedex number
                        pokedex_numb = None
                        if national_pokedex_number:
                            try:
                                pokedex_numb = int(
                                    national_pokedex_number.strip("[]'\" ")
                                )
                            except:
                                pokedex_numb = None

                        # format datetime

                        release_date = datetime.strptime(release_date_str, "%m/%d/%Y")

                        # insert into database
                        insert_card_request = """
                        INSERT INTO pokemon_card (
                            id, card_set, series, publisher, generation, release_date, 
                            artist, name, set_num, pokedex_numb, types, supertype, 
                            level, hp, evolvesFrom, evolvesTo, rarity
                        ) VALUES (
                            %s, %s, %s, %s, %s, %s, 
                            %s, %s, %s, %s, %s, %s, 
                            %s, %s, %s, %s, %s
                        )
                        """

                        curseur.execute(
                            insert_card_request,
                            (
                                card_id,
                                card_set,
                                series,
                                publisher,
                                generation,
                                release_date,
                                artist,
                                name,
                                set_num,
                                pokedex_numb,
                                types,
                                supertype,
                                level,
                                hp,
                                evolvesFrom,
                                evolvesTo,
                                rarity,
                            ),
                        )

                        print(f"Inserted card: {name}")

                    except Exception as e:
                        print(f"Error processing card {card_id}: {e}")
                        continue

                # Commit the transaction
                connexion.commit()
                print("Init successful")
