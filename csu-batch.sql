-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 13, 2022 at 08:32 PM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 7.3.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `csu-batch`
--

-- --------------------------------------------------------

--
-- Table structure for table `fcfs`
--

CREATE TABLE `fcfs` (
  `process_id` varchar(50) NOT NULL,
  `arrival` varchar(50) NOT NULL,
  `burst` varchar(50) NOT NULL,
  `exit_time` varchar(50) NOT NULL,
  `turnaround` varchar(50) NOT NULL,
  `wait` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `fcfs`
--

INSERT INTO `fcfs` (`process_id`, `arrival`, `burst`, `exit_time`, `turnaround`, `wait`) VALUES
('P1', '1', '2', '2', '1', '-1'),
('P2', '2', '1', '3', '1', '0');

-- --------------------------------------------------------

--
-- Table structure for table `help_table`
--

CREATE TABLE `help_table` (
  `id` int(11) NOT NULL,
  `commands` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `help_table`
--

INSERT INTO `help_table` (`id`, `commands`) VALUES
(1, 'run'),
(2, 'quit'),
(3, 'help');

-- --------------------------------------------------------

--
-- Table structure for table `performance`
--

CREATE TABLE `performance` (
  `no_of_jobs` varchar(50) NOT NULL,
  `avg_turnaround` varchar(50) NOT NULL,
  `avg_wait` varchar(50) NOT NULL,
  `avg_cpu` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `performance`
--

INSERT INTO `performance` (`no_of_jobs`, `avg_turnaround`, `avg_wait`, `avg_cpu`) VALUES
('3', '15.0', '11.666666666666666', '7.5'),
('4', '15.5', '13.0', '7.75'),
('2', '3.5', '1.5', '1.75'),
('2', '3.5', '1.5', '1.75'),
('2', '3.5', '1.5', '1.75'),
('3', '3.3333333333333335', '2.6666666666666665', '1.6666666666666667'),
('3', '3.3333333333333335', '2.6666666666666665', '1.6666666666666667');

-- --------------------------------------------------------

--
-- Table structure for table `priority`
--

CREATE TABLE `priority` (
  `process_id` varchar(50) NOT NULL,
  `arrival` varchar(50) NOT NULL,
  `priority` varchar(50) NOT NULL,
  `origin_burst` varchar(50) NOT NULL,
  `completion` varchar(50) NOT NULL,
  `turnaround` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `priority`
--

INSERT INTO `priority` (`process_id`, `arrival`, `priority`, `origin_burst`, `completion`, `turnaround`) VALUES
('1', '1', '1', '3', '6', '3'),
('2', '2', '2', '2', '4', '2');

-- --------------------------------------------------------

--
-- Table structure for table `sjf`
--

CREATE TABLE `sjf` (
  `process_id` varchar(50) NOT NULL,
  `arrival` varchar(50) NOT NULL,
  `burst` varchar(50) NOT NULL,
  `completed` varchar(50) NOT NULL,
  `completion` varchar(50) NOT NULL,
  `turnaround` varchar(50) NOT NULL,
  `wait` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `sjf`
--

INSERT INTO `sjf` (`process_id`, `arrival`, `burst`, `completed`, `completion`, `turnaround`, `wait`) VALUES
('1', '1', '2', '1', '3', '2', '0'),
('2', '2', '1', '1', '4', '2', '1');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
