-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 31, 2018 at 10:35 AM
-- Server version: 10.1.28-MariaDB
-- PHP Version: 7.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `kangangu`
--

-- --------------------------------------------------------

--
-- Table structure for table `classes`
--

CREATE TABLE `classes` (
  `class_id` int(11) NOT NULL,
  `class_name` varchar(45) DEFAULT NULL,
  `form_name` int(11) NOT NULL,
  `deleted` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `classes`
--

INSERT INTO `classes` (`class_id`, `class_name`, `form_name`, `deleted`) VALUES
(1, 'Form 1', 1, 0),
(2, 'Central', 1, 0),
(3, 'South', 2, 0),
(4, 'Alpha', 3, 0),
(5, 'South', 3, 0),
(6, 'Central', 2, 1),
(7, 'Alpha', 4, 0),
(8, 'South', 4, 0),
(9, 'Pluto', 1, 0),
(10, 'East', 1, 0),
(11, 'Alpha', 2, 0),
(12, 'West', 3, 0),
(13, 'West', 4, 0),
(14, 'qwerty', 2, 0),
(15, 'okml', 2, 0),
(16, 'qwerty', 3, 0),
(17, 'okml', 3, 0);

-- --------------------------------------------------------

--
-- Table structure for table `exams`
--

CREATE TABLE `exams` (
  `exam_id` int(11) NOT NULL,
  `exam_name` varchar(45) DEFAULT NULL,
  `form` varchar(9) NOT NULL,
  `term` varchar(11) DEFAULT NULL,
  `year` varchar(5) DEFAULT NULL,
  `created_at` date DEFAULT NULL,
  `deleted` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `exams`
--

INSERT INTO `exams` (`exam_id`, `exam_name`, `form`, `term`, `year`, `created_at`, `deleted`) VALUES
(1, 'Opener', '1', 'Two', '2016', '2018-06-12', 0),
(2, 'Midterm', '1', 'Two', '2017', '2018-06-12', 0),
(3, 'End Term', '1', 'Two', '2018', '2018-06-12', 0),
(4, 'Opener', '1', 'Two', '2017', '2018-06-12', 0),
(5, 'Opener', '1', 'One', '2018', '2018-06-13', 0),
(6, 'Opener', '1', 'Three', '2018', '2018-08-26', 0),
(7, 'Opener', '2', 'Three', '2018', '2018-08-26', 0),
(8, 'Opener', '3', 'Three', '2018', '2018-08-26', 0),
(9, 'Opener', '4', 'Three', '2018', '2018-08-26', 0);

-- --------------------------------------------------------

--
-- Table structure for table `exam_results`
--

CREATE TABLE `exam_results` (
  `exam_result_id` int(11) NOT NULL,
  `exam_id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  `eng` double DEFAULT NULL,
  `mat` double DEFAULT NULL,
  `kis` double DEFAULT NULL,
  `bio` double DEFAULT NULL,
  `geo` double DEFAULT NULL,
  `chem` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `exam_results`
--

INSERT INTO `exam_results` (`exam_result_id`, `exam_id`, `student_id`, `eng`, `mat`, `kis`, `bio`, `geo`, `chem`) VALUES
(1, 3, 1, 30, 20, 40, 50, 75, NULL),
(2, 3, 2, 58, 96, 34, 75, 61, NULL),
(3, 3, 3, 85, 20, 63, 50, 42, NULL),
(4, 3, 4, 47, 96, 65, 75, 25, NULL),
(5, 3, 5, 85, 20, 63, 50, 42, NULL),
(6, 3, 6, 47, 96, 65, 75, 25, NULL),
(7, 3, 7, 36, 45, 65, 48, 52, NULL),
(8, 3, 8, 47, 96, 65, 75, 25, NULL),
(9, 3, 9, 41, 69, 49, 75, 45, NULL),
(10, 3, 10, 36, 30, 48, 80, 74, NULL),
(11, 3, 11, 20, 30, 85, 45, 82, NULL),
(12, 3, 12, 18, 36, 24, 48, 62, NULL),
(13, 2, 6, 25, 35, 45, 55, 65, NULL),
(14, 2, 5, 44, 84, 75, 96, 58, NULL),
(15, 5, 6, 59, 35, 45, 85, 56, NULL),
(16, 3, 5, 25, 48, 57, 63, 28, NULL),
(17, 5, 1, 0, 0, 69, 0, NULL, NULL),
(18, 5, 11, 0, 0, 58, 0, NULL, NULL),
(19, 1, 2, 40, 62, 54, 70, 25, NULL),
(20, 1, 3, 74, 48, 59, 62, 35, NULL),
(21, 1, 5, 52, 59, 68, 70, 36, NULL),
(22, 1, 6, 40, 62, 54, 62, 53, NULL),
(23, 1, 1, 63, 59, 61, 60, 45, NULL),
(24, 1, 11, 50, 51, 43, 72, 42, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `forms`
--

CREATE TABLE `forms` (
  `form_name` int(11) NOT NULL,
  `no_of_streams` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `forms`
--

INSERT INTO `forms` (`form_name`, `no_of_streams`) VALUES
(1, 2),
(2, 2),
(3, 2),
(4, 2);

-- --------------------------------------------------------

--
-- Table structure for table `logged_in`
--

CREATE TABLE `logged_in` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `logged_in`
--

INSERT INTO `logged_in` (`id`, `user_id`) VALUES
(1, 13);

-- --------------------------------------------------------

--
-- Table structure for table `results`
--

CREATE TABLE `results` (
  `result_id` int(11) NOT NULL,
  `exam_id` int(11) NOT NULL,
  `student_id` int(11) DEFAULT NULL,
  `subject_id` int(11) NOT NULL,
  `marks` double DEFAULT NULL,
  `out_of` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `results`
--

INSERT INTO `results` (`result_id`, `exam_id`, `student_id`, `subject_id`, `marks`, `out_of`) VALUES
(1, 1, 1, 2, 50, 100),
(2, 1, 1, 1, 48, 50),
(3, 2, 3, 4, 20, 30),
(4, 2, 3, 3, 80, 100),
(5, 3, 3, 4, 20, 30),
(6, 3, 4, 3, 80, 100),
(7, 4, 3, 6, 15, 30),
(8, 4, 5, 3, 18, 100),
(9, 5, 3, 6, 15, 40),
(10, 5, 5, 3, 18, 20);

-- --------------------------------------------------------

--
-- Table structure for table `subjects`
--

CREATE TABLE `subjects` (
  `subject_id` int(11) NOT NULL,
  `subject_name` varchar(45) DEFAULT NULL,
  `subject_alias` varchar(9) NOT NULL,
  `compulsory` tinyint(4) DEFAULT NULL,
  `deleted` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `subjects`
--

INSERT INTO `subjects` (`subject_id`, `subject_name`, `subject_alias`, `compulsory`, `deleted`) VALUES
(1, 'English', 'ENG', 1, 0),
(2, 'Kiswahili', 'KIS', 1, 0),
(3, 'Mathematics', 'MAT', 1, 0),
(4, 'Biology', 'BIO', 2, 0),
(5, 'Geography', 'GEO', 2, 0),
(6, 'Chemistry', 'CHEM', 1, 0);

-- --------------------------------------------------------

--
-- Table structure for table `system_setup`
--

CREATE TABLE `system_setup` (
  `id` int(11) NOT NULL,
  `school_name` varchar(45) NOT NULL,
  `subjects_lower_forms` int(11) NOT NULL,
  `setup_complete` tinyint(1) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `system_setup`
--

INSERT INTO `system_setup` (`id`, `school_name`, `subjects_lower_forms`, `setup_complete`) VALUES
(1, 'Kangangu', 10, 1);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `reg_no` int(11) NOT NULL DEFAULT '0',
  `first_name` varchar(45) DEFAULT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `surname` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `phone_number` varchar(1210) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `gender` char(1) DEFAULT NULL,
  `username` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  `role` varchar(15) DEFAULT NULL,
  `alumnus` int(11) NOT NULL DEFAULT '0',
  `class_id` int(11) DEFAULT NULL,
  `subjects_taken` varchar(25) DEFAULT NULL,
  `subject1` int(11) DEFAULT NULL,
  `subject2` int(11) DEFAULT NULL,
  `kcpe_marks` int(11) DEFAULT NULL,
  `birth_cert_no` varchar(15) DEFAULT NULL,
  `next_of_kin_name` varchar(45) DEFAULT NULL,
  `next_of_kin_phone` varchar(10) DEFAULT NULL,
  `address` varchar(25) DEFAULT NULL,
  `national_id` varchar(15) DEFAULT NULL,
  `tsc_no` varchar(10) DEFAULT NULL,
  `status` varchar(45) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `deleted` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `reg_no`, `first_name`, `last_name`, `surname`, `email`, `phone_number`, `dob`, `gender`, `username`, `password`, `role`, `alumnus`, `class_id`, `subjects_taken`, `subject1`, `subject2`, `kcpe_marks`, `birth_cert_no`, `next_of_kin_name`, `next_of_kin_phone`, `address`, `national_id`, `tsc_no`, `status`, `created_at`, `deleted`) VALUES
(1, 0, 'Ngonjo', 'Mary...', 'Prisca', 'example@gmail.com', NULL, '1996-12-22', 'F', NULL, NULL, 'student', 0, 1, '4,2,5,3', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Active', '2018-05-11 00:00:00', 0),
(2, 0, 'Jane', 'Doe', 'Doe..', 'example@gmail.com', NULL, '0000-00-00', 'M', '', '', 'student', 0, 2, '1,2,3,4', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Active', '2018-05-23 19:00:00', 0),
(3, 0, 'Joy', 'Wangu', 'Kamau', 'example@gmail.com', NULL, '0000-00-00', 'M', '', '', 'student', 0, 2, '1,2', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Active', '0000-00-00 00:00:00', 0),
(4, 0, 'k', 'o', 'k', 'example@gmail.com', NULL, '0000-00-00', 'M', '', '', 'student', 0, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Active', '0000-00-00 00:00:00', 1),
(5, 0, 'Prisca', 'Mary', 'Ngonjo', 'example@gmail.com', NULL, '2018-05-23', 'F', '', '', 'student', 0, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Active', '0000-00-00 00:00:00', 0),
(6, 0, 'Jay ', 'Joy', 'Toy', 'example@gmail.com', NULL, '2018-05-23', 'M', '', '', 'student', 0, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Active', '2018-05-23 00:00:00', 0),
(7, 0, 'Derick', 'Kaleme', 'Kinuthia', 'example@gmail.com', NULL, '2018-05-23', 'M', '', '', 'student', 0, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Active', '2018-05-23 22:50:40', 0),
(8, 0, 'Brian', 'Kiarie', 'Kamau', 'example@gmail.com', NULL, '2018-05-23', 'M', '', '', 'student', 0, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Active', '2018-05-23 23:01:33', 0),
(10, 0, 'Tess', 'Hunter', 'Hathaway', 'example@gmail.com', NULL, '1996-05-28', 'F', '', '', 'student', 0, 3, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Active', '2018-05-28 22:03:13', 0),
(11, 0, 'Peris', 'Kate', 'Hunter', 'example@gmail.com', NULL, '1995-07-12', 'F', '', '', 'student', 0, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Active', '2018-05-28 22:15:42', 0),
(12, 0, 'Jake', 'Take', 'Hex', 'example@gmail.com', NULL, '2018-05-02', 'M', '', '', 'student', 0, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Active', '2018-05-28 22:18:16', 0),
(13, 0, 'Abdul...', 'Kashem...', 'Kashim', 'example@gmail.com', NULL, '2000-07-12', 'F', 'abdul', 'kashem', 'admin', 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Active', '2018-06-28 09:27:18', 0),
(14, 0, 'Joshua', 'Kiama', 'Kihara', 'josh@email.com', NULL, '1995-07-13', 'F', 'joshua', 'joshua', 'teacher', 0, 1, NULL, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Active', '2018-06-03 19:55:11', 0),
(15, 0, 'Harrison', 'Ouma', 'Oteke', 'harrison@email.com', NULL, '2018-03-06', 'M', 'harrison', 'harrison', 'teacher', 0, NULL, NULL, 5, 4, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Active', '2018-06-05 21:21:25', 0),
(16, 0, 'David', 'Kiama', 'Mwangi', 'david@gmail.com', NULL, '1996-02-02', 'F', 'david', 'david', 'teacher', 0, NULL, NULL, 4, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Active', '2018-06-07 21:16:14', 0),
(17, 0, 'Natasha', 'Tash', 'Sambu', 'nat@gmail.com', NULL, '1995-07-04', 'F', 'tash', 'tash', 'teacher', 0, NULL, NULL, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Active', '2018-07-06 11:46:32', 0),
(18, 0, 'Celian', 'Celine', 'Ngonjo', 'celine@gmail.com', NULL, '2002-09-10', 'F', 'celine', 'celine', 'teacher', 0, NULL, NULL, 3, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'Active', '2018-07-06 12:22:01', 0),
(19, 0, 'Tabitha', 'Kalondu', 'Mutuko', 'tabs@gmail.com', '0756478934', '1994-06-14', 'F', 'tabitha', 'tabitha', 'teacher', 0, NULL, NULL, 1, 2, NULL, NULL, NULL, NULL, '1234Thika', '22565487', '74858', 'Active', '2018-07-31 12:39:08', 0),
(20, 0, 'Jessica', 'Wambui', 'Mwangi', '', NULL, '2000-07-11', 'F', '', '', 'student', 1, 7, '1,3,5', NULL, NULL, 400, '3453466797', 'Kennedy', '0745678945', '1678 Nairobi', NULL, NULL, 'Active', '2018-07-31 14:03:13', 0),
(21, 0, 'Hudson', 'Hubbins', 'Hud', NULL, NULL, '2010-08-25', 'M', '', '', 'student', 1, 8, NULL, NULL, NULL, 400, 'qwe', 'qwer', '0718016164', '1234', NULL, NULL, 'Active', '2018-08-25 15:46:04', 0),
(22, 7276, 'Celine', 'Waithera', 'Ngonjo', NULL, NULL, '2002-09-10', 'F', '', '', 'student', 0, 4, NULL, NULL, NULL, 400, '235643443', 'Stephen', '0726765176', '1771', NULL, NULL, 'Active', '2018-08-31 11:06:00', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `classes`
--
ALTER TABLE `classes`
  ADD PRIMARY KEY (`class_id`),
  ADD KEY `fk_classes_forms1_idx` (`form_name`);

--
-- Indexes for table `exams`
--
ALTER TABLE `exams`
  ADD PRIMARY KEY (`exam_id`);

--
-- Indexes for table `exam_results`
--
ALTER TABLE `exam_results`
  ADD PRIMARY KEY (`exam_result_id`);

--
-- Indexes for table `forms`
--
ALTER TABLE `forms`
  ADD PRIMARY KEY (`form_name`);

--
-- Indexes for table `logged_in`
--
ALTER TABLE `logged_in`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `results`
--
ALTER TABLE `results`
  ADD PRIMARY KEY (`result_id`),
  ADD KEY `fk_results_exams1_idx` (`exam_id`);

--
-- Indexes for table `subjects`
--
ALTER TABLE `subjects`
  ADD PRIMARY KEY (`subject_id`),
  ADD UNIQUE KEY `subject_alias` (`subject_alias`),
  ADD UNIQUE KEY `subject_name` (`subject_name`);

--
-- Indexes for table `system_setup`
--
ALTER TABLE `system_setup`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `classes`
--
ALTER TABLE `classes`
  MODIFY `class_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `exams`
--
ALTER TABLE `exams`
  MODIFY `exam_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `exam_results`
--
ALTER TABLE `exam_results`
  MODIFY `exam_result_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `logged_in`
--
ALTER TABLE `logged_in`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `results`
--
ALTER TABLE `results`
  MODIFY `result_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `subjects`
--
ALTER TABLE `subjects`
  MODIFY `subject_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `system_setup`
--
ALTER TABLE `system_setup`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `classes`
--
ALTER TABLE `classes`
  ADD CONSTRAINT `fk_classes_forms1` FOREIGN KEY (`form_name`) REFERENCES `forms` (`form_name`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `results`
--
ALTER TABLE `results`
  ADD CONSTRAINT `fk_results_exams1` FOREIGN KEY (`exam_id`) REFERENCES `exams` (`exam_id`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
