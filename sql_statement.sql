-- sql statement, um aus der pokeapi/db.sqlite3 db alle pkmn mit typen zu kriegen;
-- dann muss ich nicht pokeapi dauerhaft spammen :D
SELECT
    p.name,
    p.pokemon_species_id AS species_id,
    MAX(CASE WHEN pt.slot = 1 THEN t.name ELSE NULL END) AS type_1,
    MAX(CASE WHEN pt.slot = 2 THEN t.name ELSE NULL END) AS type_2
FROM
    pokemon_v2_pokemon p
INNER JOIN
    pokemon_v2_pokemontype pt ON pt.pokemon_id = p.id
INNER JOIN
    pokemon_v2_type t ON pt.type_id = t.id
GROUP BY
    p.name, p.pokemon_species_id
ORDER BY
    p.pokemon_species_id;