DROP TABLE IF EXISTS `users`;
CREATE TABLE users (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  nickname VARCHAR(255),
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  email VARCHAR(255),
  password VARCHAR(255),
  is_verified BOOLEAN,
  auth_type VARCHAR(50),
  date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  date_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS `products`;
CREATE TABLE `products` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` text,
  `image_url` varchar(255) DEFAULT NULL,
  `brand` varchar(255) DEFAULT NULL,
  `serving_size` int DEFAULT NULL,
  `calories` float DEFAULT NULL,
  `total_fat` float DEFAULT NULL,
  `saturated_fat` float DEFAULT NULL,
  `trans_fat` float DEFAULT NULL,
  `cholesterol` float DEFAULT NULL,
  `sodium` float DEFAULT NULL,
  `total_carbohydrates` float DEFAULT NULL,
  `dietary_fiber` float DEFAULT NULL,
  `sugars` float DEFAULT NULL,
  `protein` float DEFAULT NULL,
  `vitamin_a` float DEFAULT NULL,
  `vitamin_c` float DEFAULT NULL,
  `calcium` float DEFAULT NULL,
  `iron` float DEFAULT NULL,
  `date_created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `date_updated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
