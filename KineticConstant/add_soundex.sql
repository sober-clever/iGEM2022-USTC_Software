USE brenda;
SET SQL_SAFE_UPDATES = 0;
ALTER TABLE `km` ADD COLUMN `soundex` CHAR(50);
UPDATE `km` SET `soundex`= SOUNDEX(speciesname) WHERE speciesname=speciesname;
ALTER TABLE `kcat_km` ADD COLUMN `soundex` CHAR(50);
UPDATE `kcat_km` SET `soundex`= SOUNDEX(speciesname) WHERE speciesname=speciesname;
SET SQL_SAFE_UPDATES = 1;
