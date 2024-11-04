-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 19, 2024 at 10:33 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `project_scientific_conferences`
--

-- --------------------------------------------------------

--
-- Table structure for table `articles`
--

CREATE TABLE `articles` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `authors` varchar(255) NOT NULL,
  `abstract` text NOT NULL,
  `pdf_link` varchar(255) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `articles`
--

INSERT INTO `articles` (`id`, `title`, `authors`, `abstract`, `pdf_link`, `created_at`) VALUES
(1, 'Optimizing Server Refresh Cycles: The Case of Circular Economy With an Aging Moore’s Law', 'Rabih Bashroush, Noir Rteil, Richard Kenny, Astrid Wynne', 'Demand for digital services is increasing significantly. Addressing energy efficiency at the data center mechanical and\r\nelectrical infrastructure level is starting to suffer from the law of diminishing returns. IT equipment, specifically servers, account for a\r\nsignificant part of the overall facility energy consumption and environmental impact, and thus, present a major opportunity, not the least\r\nfrom a circular economy perspective. To reduce the environmental impact of servers, it is important to realize the effect of\r\nmanufacturing, operating, and disposing of servers on the environment. This work presents new insights into the effect of refreshing\r\nservers with remanufactured and refurbished servers on energy efficiency and the environment. The research takes into consideration\r\nthe latest changes in CPU design trends and Moore’s law. The study measures and analyzes the use phase energy consumption of\r\nremanufactured servers vs new servers with various hardware configurations. Case studies are used to evaluate the potential impact of\r\nrefurbished server refresh from an economic as well as environmental perspectives.', 'Optimizing_Server_Refresh_Cycles_The_Case_for_Circular_Economy_With_an_Aging_Moores_Law.pdf', '2024-06-12 21:22:55'),
(2, 'How smartphone advertising influences consumers\' purchase intention', 'José Martins, Catarina Costa, Tiago Oliveira, Ramiro Gonçalves, Frederico Branco', 'In the last decade, the use of smartphones has grown steadily. The way consumers interact with brands has\r\nchanged owing to the accessibility of internet connection on smartphones, and ubiquitous mobility. It is crucial\r\nto understand the factors that motivate consumers to interact with smartphone advertisements and therefore\r\nwhat stimulates their decision to purchase. To achieve this goal, we proposed a conceptual model that combines\r\nDucoffe\'s web advertising model and flow experience theory. Based on the data collected from 303 Portuguese\r\nrespondents we empirically tested the conceptual model using a partial least squares (PLS) estimation. The\r\nresults showed that advertising value, flow experience, web design quality, and brand awareness explain purchase\r\nintention. The study provides results that allow marketers and advertisers to understand how smartphone\r\nadvertisements contribute to consumer purchase intention.', 'How smartphone advertising influences consumers\' purchase intention.pdf', '2024-06-13 19:44:08'),
(3, 'How old are you really Cognitive age in technology acceptance', 'Se-Joon Hong,  Carrie Siu Man Lui, Jungpil Hahn, Jae Yun Moon, Tai Gyu Kim', 'With increasing trends toward global aging and accompanying tendencies of (older) individuals to feel younger than they actually are, an important research question to ask is whether factors influencing IT acceptance\r\nare the same across individuals who perceive themselves to be as old as they actually are (i.e., cognitive\r\nage = chronological age) and those that perceive themselves to be younger than they actually are (i.e., cognitive age b chronological age). We conduct an empirical analysis comparing these two groups in the context\r\nof mobile data services (MDS). Our results show that for the “young at heart,” perceived usefulness, perceived\r\nease of use and perceived enjoyment play significant roles in their IT acceptance decisions, whereas for those\r\nwho perceive themselves to be as old as they actually are, perceived ease of use and subjective norms were\r\nsignificant. Practical implications regarding use of cognitive age as a basis for customer segmentation in IT industries as well as theoretical implications about meaningful age in human computer interaction research are\r\noffered and discussed.', 'How old are you really Cognitive age in technology acceptanceHow old are you really Cognitive age in technology acceptance.pdf', '2024-06-15 02:12:24'),
(4, 'Deep learning', 'Yann LeCun, Yoshua Bengio & Geoffrey Hinton', 'Deep learning allows computational models that are composed of multiple processing layers to learn representations of\r\ndata with multiple levels of abstraction. These methods have dramatically improved the state-of-the-art in speech recognition,\r\nvisual object recognition, object detection and many other domains such as drug discovery and genomics. Deep\r\nlearning discovers intricate structure in large data sets by using the backpropagation algorithm to indicate how a machine\r\nshould change its internal parameters that are used to compute the representation in each layer from the representation in\r\nthe previous layer. Deep convolutional nets have brought about breakthroughs in processing images, video, speech and\r\naudio, whereas recurrent nets have shone light on sequential data such as text and speech.', 'Deep learning.pdf', '2024-06-15 14:53:42'),
(5, 'Quantum Computing in the NISQ era and beyond', 'John Preskill', 'Noisy Intermediate-Scale Quantum (NISQ) technology will be available in\r\nthe near future. Quantum computers with 50-100 qubits may be able to perform\r\ntasks which surpass the capabilities of today’s classical digital computers, but\r\nnoise in quantum gates will limit the size of quantum circuits that can be\r\nexecuted reliably. NISQ devices will be useful tools for exploring many-body\r\nquantum physics, and may have other useful applications, but the 100-qubit\r\nquantum computer will not change the world right away — we should regard\r\nit as a significant step toward the more powerful quantum technologies of the\r\nfuture. Quantum technologists should continue to strive for more accurate\r\nquantum gates and, eventually, fully fault-tolerant quantum computing.', 'Quantum Computing in the NISQ era and beyond.pdf', '2024-06-15 14:54:18'),
(6, 'Tissue Engineering', 'Robert Langer', 'Tissue engineering is an interdisciplinary field that applies\r\nthe principles of engineering and the life sciences to the\r\ndevelopment of biological substitutes that restore, maintain,\r\nor improve tissue function.', 'Tissue_Engineering.pdf', '2024-06-15 14:55:13');

-- --------------------------------------------------------

--
-- Table structure for table `comments`
--

CREATE TABLE `comments` (
  `id` int(11) NOT NULL,
  `article_id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `message` text NOT NULL,
  `approved` tinyint(1) DEFAULT 0,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `comments`
--

INSERT INTO `comments` (`id`, `article_id`, `username`, `message`, `approved`, `created_at`) VALUES
(11, 4, 'Afonso Ferreira', 'Very interesting article!', 1, '2024-06-16 18:31:25');

-- --------------------------------------------------------

--
-- Table structure for table `conferences`
--

CREATE TABLE `conferences` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `address` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `conferences`
--

INSERT INTO `conferences` (`id`, `name`, `start_date`, `end_date`, `address`) VALUES
(1, 'International Conference on Advanced Science and Technology (ICAST)', '2024-07-05', '2024-07-07', 'Faculdade De Direito Da Universidade Nova De Lisboa, Tv. Estêvão Pinto, 1099-032 Lisboa'),
(2, 'Every Corner', '2024-06-28', '2024-06-28', 'Faculdade De Direito Da Universidade Nova De Lisboa, Tv. Estêvão Pinto, 1099-032 Lisboa');

-- --------------------------------------------------------

--
-- Table structure for table `information_requests`
--

CREATE TABLE `information_requests` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `message` text NOT NULL,
  `answered` tinyint(1) DEFAULT 0,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `information_requests`
--

INSERT INTO `information_requests` (`id`, `user_id`, `username`, `message`, `answered`, `created_at`) VALUES
(2, 2, 'Afonso Ferreira', 'How can find room A120?', 1, '2024-06-18 20:59:34');

-- --------------------------------------------------------

--
-- Table structure for table `replies`
--

CREATE TABLE `replies` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `message` text DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `request_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `replies`
--

INSERT INTO `replies` (`id`, `user_id`, `message`, `created_at`, `request_id`) VALUES
(2, 2, 'When you enter Colégio Almada Negreiros its at your left at the end of the corridor.', '2024-06-18 21:00:34', 2);

-- --------------------------------------------------------

--
-- Table structure for table `sessions`
--

CREATE TABLE `sessions` (
  `id` int(11) NOT NULL,
  `conference_id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `start_time` datetime NOT NULL,
  `end_time` datetime NOT NULL,
  `room` varchar(255) DEFAULT NULL,
  `day` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `sessions`
--

INSERT INTO `sessions` (`id`, `conference_id`, `title`, `start_time`, `end_time`, `room`, `day`) VALUES
(1, 1, 'Advancements in Artificial Intelligence', '2024-07-05 09:00:00', '2024-07-05 10:30:00', 'A14', 1),
(2, 1, 'Innovations in Quantum Computing', '2024-07-06 11:00:00', '2024-07-06 12:30:00', 'A120', 2),
(3, 1, 'Advances in Biomedical Engineering', '2024-07-07 10:00:00', '2024-07-07 11:30:00', 'A14', 3),
(4, 2, 'Overview ', '2024-06-28 10:00:00', '2024-06-28 12:30:00', 'A14', 1),
(8, 2, 'Tissue Engineering', '2024-06-28 14:00:00', '2024-06-28 16:30:00', 'A120', 1);

-- --------------------------------------------------------

--
-- Table structure for table `session_articles`
--

CREATE TABLE `session_articles` (
  `id` int(11) NOT NULL,
  `session_id` int(11) NOT NULL,
  `article_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `session_articles`
--

INSERT INTO `session_articles` (`id`, `session_id`, `article_id`) VALUES
(1, 4, 1),
(2, 4, 3),
(3, 4, 5),
(5, 1, 4),
(6, 2, 5),
(7, 3, 6),
(20, 8, 6);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(100) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `email`, `created_at`) VALUES
(2, 'Afonso Ferreira', '$2y$10$uV/FswyHn8Wyrz7Jg.wHfuBB7FNmdrYPc/cQKOxSWgoCgYWo6OtOm', '20221829@novaims.unl.pt', '2024-06-13 10:55:07'),
(3, 'Admin', '$2y$10$pu/DXM/7zo.zfD1oYyEcDuzRerJDMUWopdzfUpQGl5KdHVhRc/aRi', 'admin@gmail.com', '2024-06-13 11:03:09'),
(4, 'Rodrigo Lebre', '$2y$10$JqSyuEZ.CAMGj3pZe.bpB.hB/g3BE.LtAqvKWLQdnk77Ch60XsRIe', '20221837@novaims.unl.pt', '2024-06-16 16:09:01');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `articles`
--
ALTER TABLE `articles`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `comments`
--
ALTER TABLE `comments`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `conferences`
--
ALTER TABLE `conferences`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `information_requests`
--
ALTER TABLE `information_requests`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `replies`
--
ALTER TABLE `replies`
  ADD PRIMARY KEY (`id`),
  ADD KEY `request_id` (`request_id`);

--
-- Indexes for table `sessions`
--
ALTER TABLE `sessions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `conference_id` (`conference_id`);

--
-- Indexes for table `session_articles`
--
ALTER TABLE `session_articles`
  ADD PRIMARY KEY (`id`),
  ADD KEY `session_id` (`session_id`),
  ADD KEY `article_id` (`article_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `articles`
--
ALTER TABLE `articles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `comments`
--
ALTER TABLE `comments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `conferences`
--
ALTER TABLE `conferences`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `information_requests`
--
ALTER TABLE `information_requests`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `replies`
--
ALTER TABLE `replies`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `sessions`
--
ALTER TABLE `sessions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `session_articles`
--
ALTER TABLE `session_articles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `information_requests`
--
ALTER TABLE `information_requests`
  ADD CONSTRAINT `information_requests_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `replies`
--
ALTER TABLE `replies`
  ADD CONSTRAINT `replies_ibfk_1` FOREIGN KEY (`request_id`) REFERENCES `information_requests` (`id`);

--
-- Constraints for table `sessions`
--
ALTER TABLE `sessions`
  ADD CONSTRAINT `sessions_ibfk_1` FOREIGN KEY (`conference_id`) REFERENCES `conferences` (`id`);

--
-- Constraints for table `session_articles`
--
ALTER TABLE `session_articles`
  ADD CONSTRAINT `session_articles_ibfk_1` FOREIGN KEY (`session_id`) REFERENCES `sessions` (`id`),
  ADD CONSTRAINT `session_articles_ibfk_2` FOREIGN KEY (`article_id`) REFERENCES `articles` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
