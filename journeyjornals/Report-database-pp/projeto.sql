-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 20, 2023 at 11:03 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `projeto`
--

-- --------------------------------------------------------

--
-- Table structure for table `comments`
--

CREATE TABLE `comments` (
  `id` int(11) NOT NULL,
  `publication_id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `comment` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `comments`
--

INSERT INTO `comments` (`id`, `publication_id`, `username`, `comment`) VALUES
(16, 5, 'Afonso', 'Beautifull in ruins imagine in its glory times. ');

-- --------------------------------------------------------

--
-- Table structure for table `likes`
--

CREATE TABLE `likes` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `publication_id` int(11) NOT NULL,
  `like` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `likes`
--

INSERT INTO `likes` (`id`, `username`, `publication_id`, `like`) VALUES
(25, 'Afonso', 7, 1),
(28, 'Afonso', 9, 1),
(31, '', 5, 1),
(34, 'Admin', 12, 1),
(35, 'Afonso', 12, 1);

-- --------------------------------------------------------

--
-- Table structure for table `publication`
--

CREATE TABLE `publication` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `title` varchar(255) NOT NULL,
  `location` varchar(500) NOT NULL,
  `description` varchar(5000) NOT NULL,
  `aproved` tinyint(1) DEFAULT 0,
  `image_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `publication`
--

INSERT INTO `publication` (`id`, `username`, `title`, `location`, `description`, `aproved`, `image_name`) VALUES
(5, 'Afonso', 'Mausoleum of Halicarnassus', '<iframe src=\"https://www.google.com/maps/embed?pb=!1m16!1m12!1m3!1d7629.92629658053!2d27.41716112600555!3d37.03579960597385!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!2m1!1shalicarnassus!5e0!3m2!1sen!2spt!4v1687054480953!5m2!1sen!2spt\" width=\"600\" height=\"450\" style=\"border:0;\" allowfullscreen=\"\" loading=\"lazy\" referrerpolicy=\"no-referrer-when-downgrade\"></iframe>', 'The Mausoleum of Halicarnassus was a grand tomb built for Mausolus, the ruler of the ancient kingdom\r\n                    of Caria, in present-day Bodrum, Turkey. The construction of this monumental structure took around\r\n                    30 years and was completed in 353 BC.\r\n\r\n                    The Mausoleum was considered one of the Seven Wonders of the Ancient World due to its exquisite\r\n                    artistry and grandeur. It stood about 148 feet tall and was adorned with stunning sculptures and\r\n                    intricate carvings. The interior housed the tombs of Mausolus and his wife Artemisia.\r\n\r\n                    Today, the Mausoleum of Halicarnassus is in ruins, but visitors can still explore the remnants of\r\n                    this once magnificent structure and marvel at the craftsmanship that went into its creation. A visit\r\n                    to the site is a fascinating glimpse into ancient history and an opportunity to witness one of the\r\n                    greatest architectural achievements of the ancient world.', 1, 'mausoleu-halicarnasso.jpg'),
(7, 'Rodrigo', 'Machu Picchu', '<iframe src=\"https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d23616.207090617372!2d-72.51242408587751!3d-13.226059162250177!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x916d9a5f89555555%3A0x3a10370ea4a01a27!2sMachu%20Picchu!5e0!3m2!1sen!2spt!4v1687099347332!5m2!1sen!2spt\" width=\"600\" height=\"450\" style=\"border:0;\" allowfullscreen=\"\" loading=\"lazy\" referrerpolicy=\"no-referrer-when-downgrade\"></iframe>', 'Machu Picchu is an ancient Incan city nestled high in the Andes\r\n                    Mountains of Peru. A visit to this awe-inspiring UNESCO World Heritage site is a once-in-a-lifetime\r\n                    experience that offers breathtaking views of the surrounding mountains and valleys. Visitors can\r\n                    explore the ruins of the city, which include impressive stone buildings, terraced fields, and\r\n                    intricate irrigation systems. The highlight of the visit is undoubtedly the iconic Sun Gate, which\r\n                    offers a stunning panoramic view of Machu Picchu and the surrounding landscape. The journey to Machu\r\n                    Picchu is an adventure in itself, as visitors can choose to hike the famous Inca Trail or take a\r\n                    scenic train ride through the Andes. A visit to Machu Picchu is a must for any traveler interested\r\n                    in history, culture, and natural beauty.', 1, 'machu-picchu.jpg'),
(9, 'Afonso', 'Niagara Falls', '<iframe src=\"https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d186585.5679602636!2d-79.25318841170582!3d43.05406465439995!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89d3445eec824db9%3A0x46d2c56156bda288!2sNiagara%20Falls%2C%20ON%2C%20Canada!5e0!3m2!1sen!2spt!4v1687102287753!5m2!1sen!2spt\" width=\"600\" height=\"450\" style=\"border:0;\" allowfullscreen=\"\" loading=\"lazy\" referrerpolicy=\"no-referrer-when-downgrade\"></iframe>', 'Niagara Falls is a breathtaking natural wonder located on the border\r\n                    between the United States and Canada. Visiting the falls is an unforgettable experience, as you\r\n                    witness the sheer power of the water as it cascades over the edge and crashes down into the river\r\n                    below.\r\n\r\n                    As you approach the falls, you can hear the roar of the water and feel the mist on your face. There\r\n                    are several ways to experience the falls, including boat tours, observation decks, and even\r\n                    helicopter rides. One of the most popular ways to see the falls is by taking a Maid of the Mist boat\r\n                    tour, which takes you right up to the base of the falls.\r\n\r\n                    The falls themselves are actually made up of three separate waterfalls - the Horseshoe Falls, the\r\n                    American Falls, and the Bridal Veil Falls - each with its own unique characteristics and views. The\r\n                    Horseshoe Falls are the largest and most powerful of the three, with water dropping over 165 feet\r\n                    into the river below.\r\n\r\n                    In addition to the falls themselves, there are plenty of other activities to enjoy in the Niagara\r\n                    Falls area, including hiking, biking, and exploring nearby parks and nature reserves. The\r\n                    surrounding area is also home to several wineries, museums, and historical sites, making it a great\r\n                    destination for a fun and educational family vacation.\r\n\r\n                    Overall, a visit to the Niagara Falls is a truly awe-inspiring experience that will leave you with\r\n                    memories that last a lifetime.', 1, 'niagara-falls.jpg'),
(12, 'Afonso', 'The Great Pyramid of Giza', '<iframe src=\"https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3456.0066417813346!2d31.131621610456868!3d29.97923912155399!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x14584587ac8f291b%3A0x810c2f3fa2a52424!2sThe%20Great%20Pyramid%20of%20Giza!5e0!3m2!1sen!2spt!4v1687289278703!5m2!1sen!2spt\" width=\"600\" height=\"450\" style=\"border:0;\" allowfullscreen=\"\" loading=\"lazy\" referrerpolicy=\"no-referrer-when-downgrade\"></iframe>', 'As I stood before the colossal structure, my heart swelled with awe. The Great Pyramid of Giza, an ancient wonder that had withstood the test of time, loomed majestically before me. It was an extraordinary privilege to embark on a journey through the annals of history, exploring the enigmatic secrets concealed within its ancient walls. The air was thick with anticipation as I entered the pyramid\'s labyrinthine passages. Dimly lit by flickering torches, the narrow corridors whispered tales of pharaohs, their mighty reigns, and the relentless labor of the builders. It was a humbling experience, tracing the footsteps of those who had long passed into the realms of legend. As I ventured deeper into the pyramid, a sense of reverence and mystery enveloped me. The architecture astounded me with its precision, the stones seamlessly fitted together like an intricate puzzle. How did the ancient Egyptians accomplish such engineering marvels without the modern tools we take for granted today? With every step, I marveled at the ingenuity of the ancient Egyptians. The massive stones seemed to vibrate with the weight of history, bearing witness to the stories of countless generations. The hieroglyphs adorning the walls revealed glimpses of a forgotten world—a language lost in time, a civilization rich with wisdom and spiritual beliefs. Reaching the burial chamber, my anticipation peaked. As I stood in the presence of the sarcophagus, I couldn\'t help but ponder the grandeur of the pharaohs who once lay in eternal rest within these chambers. The secrets they took with them remain veiled, yet the pyramids stand as a testament to their indomitable power and unyielding ambition. Leaving the burial chamber behind, I ascended to the pyramid\'s apex. From this vantage point, the breathtaking panorama unfolded before me. The vast Egyptian landscape stretched out in all directions, and the Nile River flowed serenely, mirroring the ageless wisdom of the pyramids. I couldn\'t help but marvel at the cosmic alignment of the pyramids with the stars, a testament to the ancient Egyptians\' profound connection to the heavens. Leaving the Great Pyramid of Giza behind, I carried with me a profound sense of wonder and admiration. This monument, standing tall for over four millennia, spoke of a civilization\'s mastery, their eternal quest for immortality and their unwavering legacy. The visit had revealed but a fraction of the mysteries held within, leaving me eager to further explore the treasures of ancient Egypt. As I departed, I couldn\'t help but feel a profound gratitude for being granted a glimpse into the world of the pharaohs. The Great Pyramid of Giza, an enduring marvel of human achievement, had left an indelible mark on my soul, forever linking me to the enigmatic tapestry of ancient history.', 1, 'pyramid1.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `registuser`
--

CREATE TABLE `registuser` (
  `id` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `registuser`
--

INSERT INTO `registuser` (`id`, `username`, `email`, `password`) VALUES
(1, 'Admin', 'admin@gmail.com', 'admin'),
(2, 'Afonso', 'af.ferreira2004@gmail.com', 'cavalo'),
(3, 'Rodrigo', '20221837@novaims.unl.pt', 'leão');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `comments`
--
ALTER TABLE `comments`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `likes`
--
ALTER TABLE `likes`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `publication`
--
ALTER TABLE `publication`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `registuser`
--
ALTER TABLE `registuser`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `comments`
--
ALTER TABLE `comments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `likes`
--
ALTER TABLE `likes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT for table `publication`
--
ALTER TABLE `publication`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `registuser`
--
ALTER TABLE `registuser`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
