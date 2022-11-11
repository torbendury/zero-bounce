INSERT INTO categories(name) VALUES ('places');
INSERT INTO categories(name) VALUES ('classes');
INSERT INTO categories(name) VALUES ('factions');
INSERT INTO categories(name) VALUES ('vehicles');
INSERT INTO categories(name) VALUES ('monsters');
INSERT INTO categories(name) VALUES ('events');
INSERT INTO categories(name) VALUES ('weapons');

-- Places
INSERT INTO entries(name, categoryId, visibleToPlayer) SELECT DISTINCT 'Haven', id, FALSE FROM categories WHERE name='places';
INSERT INTO entries(name, categoryId, visibleToPlayer) SELECT DISTINCT 'Buxtehude', id, FALSE FROM categories WHERE name='places';
INSERT INTO entries(name, categoryId, visibleToPlayer) SELECT DISTINCT 'Pirmasens', id, FALSE FROM categories WHERE name='places';
-- Classes
INSERT INTO entries(name, categoryId, visibleToPlayer) SELECT DISTINCT 'Berserk', id, FALSE FROM categories WHERE name='classes';
INSERT INTO entries(name, categoryId, visibleToPlayer) SELECT DISTINCT 'Omen', id, FALSE FROM categories WHERE name='classes';
-- Factions
INSERT INTO entries(name, categoryId, visibleToPlayer) SELECT DISTINCT 'Raven', id, FALSE FROM categories WHERE name='factions';
INSERT INTO entries(name, categoryId, visibleToPlayer) SELECT DISTINCT 'Daemons', id, FALSE FROM categories WHERE name='factions';
-- Vehicles
INSERT INTO entries(name, categoryId, visibleToPlayer) SELECT DISTINCT 'Rover', id, FALSE FROM categories WHERE name='vehicles';
INSERT INTO entries(name, categoryId, visibleToPlayer) SELECT DISTINCT 'Helicopter', id, FALSE FROM categories WHERE name='vehicles';
INSERT INTO entries(name, categoryId, visibleToPlayer) SELECT DISTINCT 'Horse', id, FALSE FROM categories WHERE name='vehicles';
-- Monsters
INSERT INTO entries(name, categoryId, visibleToPlayer) SELECT DISTINCT 'Crawler', id, FALSE FROM categories WHERE name='monsters';
-- Events
INSERT INTO entries(name, categoryId, visibleToPlayer) SELECT DISTINCT 'Cosmic Intervention', id, FALSE FROM categories WHERE name='events';
-- Weapons
INSERT INTO entries(name, categoryId, visibleToPlayer) SELECT DISTINCT 'Harkon-A12', id, FALSE FROM categories WHERE name='weapons';
INSERT INTO entries(name, categoryId, visibleToPlayer) SELECT DISTINCT 'Fork', id, FALSE FROM categories WHERE name='weapons';
