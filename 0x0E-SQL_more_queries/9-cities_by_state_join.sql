-- lists all cities contained in the database
SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN states ON statess.id = cities.state_id ORDER BY cities_id
