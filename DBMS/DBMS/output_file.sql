-- MySQL dump 10.13  Distrib 8.0.33, for Linux (x86_64)
--
-- Host: localhost    Database: OnlineShopping
-- ------------------------------------------------------
-- Server version	8.0.33-0ubuntu0.22.04.4

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Cart`
--

DROP TABLE IF EXISTS `Cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Cart` (
  `Id` varchar(20) NOT NULL,
  `P_Id` varchar(20) NOT NULL,
  `Pname` varchar(50) DEFAULT NULL,
  `Price` bigint DEFAULT NULL,
  `Qty` int DEFAULT NULL,
  PRIMARY KEY (`Id`,`P_Id`),
  KEY `P_Id` (`P_Id`,`Pname`,`Price`),
  CONSTRAINT `Cart_ibfk_1` FOREIGN KEY (`Id`) REFERENCES `Customer` (`Id`),
  CONSTRAINT `Cart_ibfk_2` FOREIGN KEY (`P_Id`, `Pname`, `Price`) REFERENCES `Products` (`P_Id`, `Pname`, `Price`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Cart`
--

LOCK TABLES `Cart` WRITE;
/*!40000 ALTER TABLE `Cart` DISABLE KEYS */;
INSERT INTO `Cart` VALUES ('011573','147302','Shirt',999,1),('011573','871334','Shorts',750,1),('033123','000101','Shirt',1560,1),('033123','259801','T-Shirt',560,2),('033123','761827','Pants',1999,1);
/*!40000 ALTER TABLE `Cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Customer`
--

DROP TABLE IF EXISTS `Customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Customer` (
  `Id` varchar(20) NOT NULL,
  `Username` varchar(20) DEFAULT NULL,
  `Password` varchar(20) DEFAULT NULL,
  `Fname` varchar(20) NOT NULL,
  `Lname` varchar(20) NOT NULL,
  `Address` varchar(20) NOT NULL,
  `Phone` bigint NOT NULL,
  PRIMARY KEY (`Id`,`Fname`,`Lname`,`Address`,`Phone`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customer`
--

LOCK TABLES `Customer` WRITE;
/*!40000 ALTER TABLE `Customer` DISABLE KEYS */;
INSERT INTO `Customer` VALUES ('011573','Bryan05','bry573','Bryan','John','Kpt,Mangalore',9900380315),('033123','Maxi29','maxon1203','Maxon','Fernandes','Bejai,Mangalore',9535090276);
/*!40000 ALTER TABLE `Customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Order_details`
--

DROP TABLE IF EXISTS `Order_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Order_details` (
  `Order_Id` varchar(20) NOT NULL,
  `Id` varchar(20) DEFAULT NULL,
  `Arriving_by` date DEFAULT NULL,
  PRIMARY KEY (`Order_Id`),
  KEY `Id` (`Id`),
  CONSTRAINT `Order_details_ibfk_1` FOREIGN KEY (`Id`) REFERENCES `Customer` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Order_details`
--

LOCK TABLES `Order_details` WRITE;
/*!40000 ALTER TABLE `Order_details` DISABLE KEYS */;
INSERT INTO `Order_details` VALUES ('223452','033123','2023-08-29'),('775543','011573','2023-09-01');
/*!40000 ALTER TABLE `Order_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Payment`
--

DROP TABLE IF EXISTS `Payment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Payment` (
  `Pay_Id` varchar(20) NOT NULL,
  `Id` varchar(20) NOT NULL,
  `Amount` bigint NOT NULL,
  `Pay_type` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`Pay_Id`,`Id`,`Amount`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Payment`
--

LOCK TABLES `Payment` WRITE;
/*!40000 ALTER TABLE `Payment` DISABLE KEYS */;
INSERT INTO `Payment` VALUES ('094521','033123',4352,'Gpay/UPI'),('110875','011573',1789,'Cash');
/*!40000 ALTER TABLE `Payment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Products`
--

DROP TABLE IF EXISTS `Products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Products` (
  `P_Id` varchar(20) NOT NULL,
  `Pname` varchar(50) NOT NULL,
  `Description` varchar(50) DEFAULT NULL,
  `Category` varchar(50) DEFAULT NULL,
  `Price` bigint NOT NULL,
  PRIMARY KEY (`P_Id`,`Pname`,`Price`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Products`
--

LOCK TABLES `Products` WRITE;
/*!40000 ALTER TABLE `Products` DISABLE KEYS */;
INSERT INTO `Products` VALUES ('000101','Shirt','Colour:Black, Slim Fit, Size:M','Formals For Men',1560),('125682','Kurta','Colour:White, Embroidery, Size:M','Ethnic For Women',2499),('147302','Shirt','Colour:Red, Slim Fit, Size:L','Formals For Men',999),('237856','Kurta','Colour:Musted Yellow ,Size:L','Ethnic For Women',5599),('259801','T-Shirt','Colour:Olive Green, Oversize M','Casuals For Men',560),('452390','Pants','Colour:Light Blue, Baggy, Size:S','Casuals Women',1750),('572901','Saree','Colour:Orange,Silk','Ethnic For Women',7599),('689132','T-Shirt','Colour:Red Stripes, Slim Fit,Size:L','Casuals For Men',599),('761827','Pants','Colour:Grey, Joggers,Size:M','Casuals For Men',1999),('871334','Shorts','Colour:Beige, Size:L','Casuals For Men',750);
/*!40000 ALTER TABLE `Products` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-21 19:45:22
