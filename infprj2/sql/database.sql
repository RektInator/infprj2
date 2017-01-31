-- --------------------------------------------------------
-- Host:                         178.62.226.124
-- Server version:               5.7.17-0ubuntu0.16.04.1 - (Ubuntu)
-- Server OS:                    Linux
-- HeidiSQL Version:             9.3.0.4984
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- Dumping database structure for opseilen
DROP DATABASE IF EXISTS `opseilen`;
CREATE DATABASE IF NOT EXISTS `opseilen` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `opseilen`;


-- Dumping structure for table opseilen.accounts
DROP TABLE IF EXISTS `accounts`;
CREATE TABLE IF NOT EXISTS `accounts` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'user id',
  `username` varchar(64) NOT NULL DEFAULT '0' COMMENT 'username',
  `password` varchar(64) NOT NULL DEFAULT '0' COMMENT 'hashed pw',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Data exporting was unselected.


-- Dumping structure for table opseilen.savegames
DROP TABLE IF EXISTS `savegames`;
CREATE TABLE IF NOT EXISTS `savegames` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `players` int(11) NOT NULL DEFAULT '0',
  `currentplayer` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Data exporting was unselected.


-- Dumping structure for table opseilen.savegames_player
DROP TABLE IF EXISTS `savegames_player`;
CREATE TABLE IF NOT EXISTS `savegames_player` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sid` int(11) NOT NULL,
  `name` varchar(64) NOT NULL DEFAULT '0',
  `ourturn` tinyint(1) NOT NULL DEFAULT '0',
  `posx` int(11) NOT NULL DEFAULT '0',
  `posy` int(11) NOT NULL DEFAULT '0',
  `poscol` int(11) NOT NULL DEFAULT '0',
  `did_generate_question` tinyint(1) NOT NULL DEFAULT '0',
  `dice_roll` int(11) NOT NULL DEFAULT '0',
  `did_answer` tinyint(1) NOT NULL DEFAULT '0',
  `isAI` tinyint(1) NOT NULL DEFAULT '0',
  `did_choose_row` tinyint(1) NOT NULL DEFAULT '0',
  `moves_left` int(11) NOT NULL DEFAULT '0',
  `score` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Data exporting was unselected.


-- Dumping structure for table opseilen.score
DROP TABLE IF EXISTS `score`;
CREATE TABLE IF NOT EXISTS `score` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `score` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Data exporting was unselected.


-- Dumping structure for table opseilen.servers
DROP TABLE IF EXISTS `servers`;
CREATE TABLE IF NOT EXISTS `servers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(50) DEFAULT NULL,
  `port` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Data exporting was unselected.
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
