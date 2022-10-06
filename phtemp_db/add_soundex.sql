USE brenda;
ALTER TABLE `Phtemp` ADD COLUMN `soundex` CHAR(50);
SET SQL_SAFE_UPDATES = 0;
UPDATE `Phtemp` SET `soundex`= SOUNDEX(speciesname) WHERE speciesname=speciesname;
SET SQL_SAFE_UPDATES = 1;