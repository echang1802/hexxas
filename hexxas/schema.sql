
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  email TEXT NOT NULL,
  battles INTEGER DEFAULT 0,
  battles_won INTEGER DEFAULT 0,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE teams (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  owner_id INTEGER NOT NULL,
  hexxa_1_id INTEGER NOT NULL,
  hexxa_2_id INTEGER NOT NULL,
  hexxa_3_id INTEGER NOT NULL,
  tier INTEGER NOT NULL,
  battles INTEGER DEFAULT 0,
  battles_won INTEGER DEFAULT 0,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (owner_id) REFERENCES users (id),
  FOREIGN KEY (hexxa_1_id) REFERENCES hexxas (id),
  FOREIGN KEY (hexxa_2_id) REFERENCES hexxas (id),
  FOREIGN KEY (hexxa_3_id) REFERENCES hexxas (id)
);

CREATE TABLE hexxas (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nickname TEXT NOT NULL,
  hexxa_template_id INTEGER NOT NULL,
  owner_id INTEGER NOT NULL,
  team_id INTEGER DEFAULT NULL,
  experience INTEGER DEFAULT 0,
  tier INTEGER DEFAULT 10,
  element_id TEXT NOT NULL,
  resistance TEXT NOT NULL,
  atk_1_id INTEGER NOT NULL,
  atk_1_power INTEGER NOT NULL,
  atk_1_frequency INTEGER NOT NULL,
  atk_1_selected INTEGER NOT NULL,
  atk_2_id INTEGER NOT NULL,
  atk_2_power INTEGER NOT NULL,
  atk_2_frequency INTEGER NOT NULL,
  atk_2_selected INTEGER NOT NULL,
  atk_3_id INTEGER NOT NULL,
  atk_3_power INTEGER NOT NULL,
  atk_3_frequency INTEGER NOT NULL,
  atk_3_selected INTEGER NOT NULL,
  atk_4_id INTEGER NOT NULL,
  atk_4_power INTEGER NOT NULL,
  atk_4_frequency INTEGER NOT NULL,
  atk_4_selected INTEGER NOT NULL,
  atk_5_id INTEGER NOT NULL,
  atk_5_power INTEGER NOT NULL,
  atk_5_frequency INTEGER NOT NULL,
  atk_5_selected INTEGER NOT NULL,
  atk_6_id INTEGER NOT NULL,
  atk_6_power INTEGER NOT NULL,
  atk_6_frequency INTEGER NOT NULL,
  atk_6_selected INTEGER NOT NULL,
  total_atk_frequency INTEGER NOT NULL,
  total_fights INTEGER DEFAULT 0,
  battles INTEGER DEFAULT 0,
  battles_won INTEGER DEFAULT 0,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (hexxa_template_id) REFERENCES hexxas_templates (id),
  FOREIGN KEY (owner_id) REFERENCES user (id),
  FOREIGN KEY (team_id) REFERENCES teams (id),
  FOREIGN KEY (element_id) REFERENCES elements (id),
  FOREIGN KEY (atk_1_id) REFERENCES attacks (id),
  FOREIGN KEY (atk_2_id) REFERENCES attacks (id),
  FOREIGN KEY (atk_3_id) REFERENCES attacks (id),
  FOREIGN KEY (atk_4_id) REFERENCES attacks (id),
  FOREIGN KEY (atk_5_id) REFERENCES attacks (id),
  FOREIGN KEY (atk_6_id) REFERENCES attacks (id)
);

CREATE TABLE hexxas_templates (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  element_id INTEGER NOT NULL,
  atk_1_id INTEGER NOT NULL,
  atk_2_id INTEGER NOT NULL,
  atk_3_id INTEGER NOT NULL,
  atk_4_id INTEGER NOT NULL,
  atk_5_id INTEGER NOT NULL,
  atk_6_id INTEGER NOT NULL,
  atk_7_id INTEGER NOT NULL,
  atk_8_id INTEGER NOT NULL,
  atk_9_id INTEGER NOT NULL,
  atk_10_id INTEGER NOT NULL,
  FOREIGN KEY (element_id) REFERENCES elements (id),
  FOREIGN KEY (atk_1_id) REFERENCES attacks (id),
  FOREIGN KEY (atk_2_id) REFERENCES attacks (id),
  FOREIGN KEY (atk_3_id) REFERENCES attacks (id),
  FOREIGN KEY (atk_4_id) REFERENCES attacks (id),
  FOREIGN KEY (atk_5_id) REFERENCES attacks (id),
  FOREIGN KEY (atk_6_id) REFERENCES attacks (id),
  FOREIGN KEY (atk_7_id) REFERENCES attacks (id),
  FOREIGN KEY (atk_8_id) REFERENCES attacks (id),
  FOREIGN KEY (atk_9_id) REFERENCES attacks (id),
  FOREIGN KEY (atk_10_id) REFERENCES attacks (id)
);

-- Insert templates

CREATE TABLE elements (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  ability_name TEXT NOT NULL,
  ability_text TEXT NOT NULL
);

-- Insert elements

CREATE TABLE attacks (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  element_id INTEGER NOT NULL,
  type_id INTEGER NOT NULL,
  "power" INTEGER NOT NULL,
  frequency INTEGER NOT NULL,
  ability FLOAT NOT NULL,
  FOREIGN KEY (element_id) REFERENCES elements (id),
  FOREIGN KEY (type_id) REFERENCES types (id)
);

-- Insert attacks

CREATE TABLE types (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL
);

-- Insert types

CREATE TABLE tiers (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  min_level TEXT NOT NULL,
  max_level TEXT NOT NULL
);

-- Insert tiers

CREATE TABLE decks (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  owner_id INTEGER NOT NULL,
  card_1_id INTEGER NOT NULL,
  card_2_id INTEGER NOT NULL,
  card_3_id INTEGER NOT NULL,
  card_4_id INTEGER NOT NULL,
  card_5_id INTEGER NOT NULL,
  card_6_id INTEGER NOT NULL,
  card_7_id INTEGER NOT NULL,
  card_8_id INTEGER NOT NULL,
  card_9_id INTEGER NOT NULL,
  card_10_id INTEGER NOT NULL,
  card_11_id INTEGER NOT NULL,
  card_12_id INTEGER NOT NULL,
  card_13_id INTEGER NOT NULL,
  card_14_id INTEGER NOT NULL,
  card_15_id INTEGER NOT NULL,
  card_16_id INTEGER NOT NULL,
  card_17_id INTEGER NOT NULL,
  card_18_id INTEGER NOT NULL,
  card_19_id INTEGER NOT NULL,
  card_20_id INTEGER NOT NULL,
  FOREIGN KEY (owner_id) REFERENCES users (id),
  FOREIGN KEY (card_1_id) REFERENCES cards (id),
  FOREIGN KEY (card_2_id) REFERENCES cards (id),
  FOREIGN KEY (card_3_id) REFERENCES cards (id),
  FOREIGN KEY (card_4_id) REFERENCES cards (id),
  FOREIGN KEY (card_5_id) REFERENCES cards (id),
  FOREIGN KEY (card_6_id) REFERENCES cards (id),
  FOREIGN KEY (card_7_id) REFERENCES cards (id),
  FOREIGN KEY (card_8_id) REFERENCES cards (id),
  FOREIGN KEY (card_9_id) REFERENCES cards (id),
  FOREIGN KEY (card_10_id) REFERENCES cards (id),
  FOREIGN KEY (card_11_id) REFERENCES cards (id),
  FOREIGN KEY (card_12_id) REFERENCES cards (id),
  FOREIGN KEY (card_13_id) REFERENCES cards (id),
  FOREIGN KEY (card_14_id) REFERENCES cards (id),
  FOREIGN KEY (card_15_id) REFERENCES cards (id),
  FOREIGN KEY (card_16_id) REFERENCES cards (id),
  FOREIGN KEY (card_17_id) REFERENCES cards (id),
  FOREIGN KEY (card_18_id) REFERENCES cards (id),
  FOREIGN KEY (card_19_id) REFERENCES cards (id),
  FOREIGN KEY (card_20_id) REFERENCES cards (id)
);

CREATE TABLE cards (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  element_id INTEGER NOT NULL,
  type_id INTEGER NOT NULL,
  attribute TEXT NOT NULL,
  value TEXT NOT NULL,
  legend TEXT,
  FOREIGN KEY (element_id) REFERENCES elements (id),
  FOREIGN KEY (type_id) REFERENCES types (id)
);

-- insert cards
