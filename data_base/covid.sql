create schema if not exists "COVID";
set search_path to "COVID";

-- Table pays
CREATE TABLE IF NOT EXISTS pays (
    id_pays VARCHAR(255),
    nom_pays VARCHAR(255),
    geold VARCHAR(255),
    code_pays VARCHAR(255),
    pays_pop VARCHAR(255),
    continent VARCHAR(255)
);

-- Table date
CREATE TABLE IF NOT EXISTS date (
    id_date VARCHAR(255),
    annee int,
    mois VARCHAR(255),
    jours VARCHAR(255)
);

-- Table covid
CREATE TABLE IF NOT EXISTS COVID19 (
    id_pays VARCHAR(255) ,
    id_date VARCHAR(255) ,
    nb_cas float,
    deaths float,
    cum_num float
);
 alter table pays add primary key(id_pays);
 alter table date add primary key(id_date);
 alter table COVID19 add primary key(id_pays, id_date);
 --cle etrangers
 alter table COVID19 add foreign key(id_pays) references pays,
 add foreign key(id_date) references date;
  


commit;