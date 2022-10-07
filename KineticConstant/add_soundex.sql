USE brenda;
SET SQL_SAFE_UPDATES = 0;
ALTER TABLE `Km` ADD COLUMN `soundex` CHAR(50);
UPDATE `Km` SET `soundex`= SOUNDEX(speciesname) WHERE speciesname=speciesname;
ALTER TABLE `Kcat_km` ADD COLUMN `soundex` CHAR(50);
UPDATE `Kcat_km` SET `soundex`= SOUNDEX(speciesname) WHERE speciesname=speciesname;
SET SQL_SAFE_UPDATES = 1;
