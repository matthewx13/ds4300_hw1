-- Drop the 'twitterdb' schema if it exists
DROP SCHEMA IF EXISTS `twitterdb`;

-- Create the 'twitterdb' schema
CREATE SCHEMA `twitterdb`;

-- Switch to the 'twitterdb' schema
USE `twitterdb`;

-- -----------------------------------------------------
-- Table `tweet`
-- -----------------------------------------------------
CREATE TABLE `tweet` (
    `tweet_id` INT unsigned NOT NULL AUTO_INCREMENT,
    `user_id` INT DEFAULT NULL,
    `tweet_ts` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
    `tweet_text` VARCHAR(140) DEFAULT NULL,
    PRIMARY KEY (`tweet_id`)
);

-- -----------------------------------------------------
-- Table `follows`
-- -----------------------------------------------------
CREATE TABLE `follows` (
    `user_id` INT DEFAULT NULL,
    `follows_id` INT DEFAULT NULL
);

