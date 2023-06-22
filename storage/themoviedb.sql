-- MariaDB dump 10.19  Distrib 10.6.12-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: extraordinaryproject
-- ------------------------------------------------------
-- Server version	10.6.12-MariaDB-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Movies`
--

DROP TABLE IF EXISTS `Movies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Movies` (
  `id` int(11) NOT NULL,
  `original_language` varchar(20) DEFAULT NULL,
  `title` varchar(150) DEFAULT NULL,
  `vote_average` decimal(2,1) DEFAULT NULL,
  `vote_count` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Movies`
--

LOCK TABLES `Movies` WRITE;
/*!40000 ALTER TABLE `Movies` DISABLE KEYS */;
INSERT INTO `Movies` VALUES (13,'en','Forrest Gump',8.5,24822),(122,'en','The Lord of the Rings: The Return of the King',8.5,21738),(129,'ja','Spirited Away',8.5,14439),(155,'en','The Dark Knight',8.5,29906),(238,'en','The Godfather',8.7,18109),(240,'en','The Godfather Part II',8.6,10933),(278,'en','The Shawshank Redemption',8.7,23982),(389,'en','12 Angry Men',8.5,7354),(429,'it','The Good, the Bad and the Ugly',8.5,7467),(497,'en','The Green Mile',8.5,15522),(680,'en','Pulp Fiction',8.5,25328),(769,'en','GoodFellas',8.5,11356),(11216,'it','Cinema Paradiso',8.5,3793),(19404,'hi','Dilwale Dulhania Le Jayenge',8.6,4151),(372058,'ja','Your Name.',8.5,9944),(496243,'ko','Parasite',8.5,15899),(569094,'en','Spider-Man: Across the Spider-Verse',8.7,1557),(704264,'en','Primal: Tales of Savagery',8.5,266),(772071,'es','Cuando Sea Joven',8.5,243);
/*!40000 ALTER TABLE `Movies` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-22 13:38:43
