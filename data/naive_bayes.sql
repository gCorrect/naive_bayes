-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 22, 2022 at 05:58 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `naive_bayes`
--

-- --------------------------------------------------------

--
-- Table structure for table `play_tennis`
--

CREATE TABLE `play_tennis` (
  `outlook` varchar(25) NOT NULL,
  `outlook_num_val` float NOT NULL,
  `temperature` varchar(25) NOT NULL,
  `temperature_num_val` float NOT NULL,
  `humidity` varchar(25) NOT NULL,
  `humidity_num_val` float NOT NULL,
  `wind` varchar(25) NOT NULL,
  `wind_num_val` float NOT NULL,
  `play_tennis` varchar(5) NOT NULL,
  `play_tennis_num_val` int(2) DEFAULT NULL,
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `play_tennis`
--

INSERT INTO `play_tennis` (`outlook`, `outlook_num_val`, `temperature`, `temperature_num_val`, `humidity`, `humidity_num_val`, `wind`, `wind_num_val`, `play_tennis`, `play_tennis_num_val`, `id`) VALUES
('Sunny', 0, 'Hot', 1, 'High', 1, 'Weak', 0.5, 'No', 0, 1),
('Sunny', 0, 'Hot', 1, 'High', 1, 'Strong', 1, 'No', 0, 2),
('Overcast', 0.5, 'Hot', 1, 'High', 1, 'Weak', 0.5, 'Yes', 1, 3),
('Rain', 1, 'Mild', 0.5, 'High', 1, 'Weak', 0.5, 'Yes', 1, 4),
('Rain', 1, 'Cool', 0, 'Normal', 0.5, 'Weak', 0.5, 'Yes', 1, 5),
('Rain', 1, 'Cool', 0, 'Normal', 0.5, 'Strong', 1, 'No', 0, 6),
('Overcast', 0.5, 'Cool', 0, 'Normal', 0.5, 'Strong', 1, 'Yes', 1, 7),
('Sunny', 0, 'Mild', 0.5, 'High', 1, 'Weak', 0.5, 'No', 0, 8),
('Sunny', 0, 'Cool', 0, 'Normal', 0.5, 'Weak', 0.5, 'Yes', 1, 9),
('Rain', 1, 'Mild', 0.5, 'Normal', 0.5, 'Weak', 0.5, 'Yes', 1, 10),
('Sunny', 0, 'Mild', 0.5, 'Normal', 0.5, 'Strong', 1, 'Yes', 1, 11),
('Overcast', 0.5, 'Mild', 0.5, 'High', 1, 'Strong', 1, 'Yes', 1, 12),
('Overcast', 0.5, 'Hot', 1, 'Normal', 0.5, 'Weak', 0.5, 'Yes', 1, 13),
('Rain', 1, 'Mild', 0.5, 'High', 1, 'Strong', 1, 'No', 0, 14);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `play_tennis`
--
ALTER TABLE `play_tennis`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `play_tennis`
--
ALTER TABLE `play_tennis`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
