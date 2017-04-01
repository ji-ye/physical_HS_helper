-- sql commands used to create database
CREATE TABLE cards
  (db_index INT,
  artist TEXT,
  attack TEXT,
  cardClass TEXT,
  classes TEXT,
  collectible INT,
  collectionText TEXT,
  cost TEXT,
  dbfId TEXT,
  durability TEXT,
  elite TEXT,
  entourage TEXT,
  faction TEXT,
  flavor TEXT,
  health TEXT,
  hideStats TEXT,
  howToEarn TEXT,
  howToEarnGolden TEXT,
  id TEXT,
  mechanics TEXT,
  multiClassGroup TEXT,
  name TEXT,
  overload TEXT,
  playRequirements TEXT,
  playerClass TEXT,
  race TEXT,
  rarity TEXT,
  referencedTags TEXT,
  card_set TEXT,
  spellDamage TEXT,
  targetingArrowText TEXT,
  card_text TEXT,
  type TEXT,
CONSTRAINT pk_id PRIMARY KEY (id)
);

.separator ,
.import cards_enUS.csv cards

CREATE TABLE cards_zhCN
  (db_index INT,
  artist TEXT,
  attack TEXT,
  cardClass TEXT,
  classes TEXT,
  collectible INT,
  collectionText TEXT,
  cost TEXT,
  dbfId TEXT,
  durability TEXT,
  elite TEXT,
  entourage TEXT,
  faction TEXT,
  flavor TEXT,
  health TEXT,
  hideStats TEXT,
  howToEarn TEXT,
  howToEarnGolden TEXT,
  id TEXT,
  mechanics TEXT,
  multiClassGroup TEXT,
  name TEXT,
  overload TEXT,
  playRequirements TEXT,
  playerClass TEXT,
  race TEXT,
  rarity TEXT,
  referencedTags TEXT,
  card_set TEXT,
  spellDamage TEXT,
  targetingArrowText TEXT,
  card_text TEXT,
  type TEXT,
CONSTRAINT pk_id PRIMARY KEY (id)
);

.separator ,
.import cards_zhCN.csv cards_zhCN