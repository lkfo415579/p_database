/*
Navicat MySQL Data Transfer

Source Server         : local
Source Server Version : 50544
Source Host           : localhost:3306
Source Database       : pixiv

Target Server Type    : MYSQL
Target Server Version : 50544
File Encoding         : 65001

Date: 2016-01-12 21:35:11
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for info_log
-- ----------------------------
DROP TABLE IF EXISTS `info_log`;
CREATE TABLE `info_log` (
  `page` varchar(255) DEFAULT NULL,
  `mode` varchar(255) DEFAULT NULL,
  `per_page` varchar(255) DEFAULT NULL,
  `date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of info_log
-- ----------------------------

-- ----------------------------
-- Table structure for pictures
-- ----------------------------
DROP TABLE IF EXISTS `pictures`;
CREATE TABLE `pictures` (
  `id` int(11) NOT NULL,
  `reuploaded_time` datetime DEFAULT NULL,
  `is_liked` varchar(255) DEFAULT NULL,
  `page_count` int(11) DEFAULT NULL,
  `height` int(11) DEFAULT NULL,
  `created_time` datetime DEFAULT NULL,
  `tools` varchar(255) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `width` int(11) DEFAULT NULL,
  `book_style` varchar(255) DEFAULT NULL,
  `age_limit` varchar(255) DEFAULT NULL,
  `metadata` varchar(255) DEFAULT NULL,
  `is_manga` varchar(255) DEFAULT NULL,
  `publicity` varchar(255) DEFAULT NULL,
  `tags` varchar(255) DEFAULT NULL,
  `image_files_name` varchar(255) DEFAULT NULL,
  `content_type` varchar(255) DEFAULT NULL,
  `caption` varchar(255) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  `sanity_level` varchar(255) DEFAULT NULL,
  `favorite_id` int(11) DEFAULT NULL,
  `previous_rank` int(11) DEFAULT NULL,
  `rank` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of pictures
-- ----------------------------
INSERT INTO `pictures` VALUES ('47866898', '2014-12-31 00:48:48', null, '4', '877', '2014-12-31 00:48:00', null, '「目の描き方を考える。」', '620', 'none', 'all-age', null, null, '0', null, null, null, null, 'manga', 'white', null, null, null);
INSERT INTO `pictures` VALUES ('47878234', '2014-12-31 16:22:52', null, '1', '684', '2014-12-31 16:22:00', null, '２０１４最後の夕焼け', '1200', 'none', 'all-age', null, null, '0', null, null, null, null, 'illustration', 'white', null, null, null);
INSERT INTO `pictures` VALUES ('47899157', '2015-01-01 00:59:42', null, '1', '1206', '2015-01-01 00:59:00', null, 'あけまして', '1154', 'none', 'all-age', null, null, '0', null, null, null, null, 'illustration', 'white', null, null, null);

-- ----------------------------
-- Table structure for stats
-- ----------------------------
DROP TABLE IF EXISTS `stats`;
CREATE TABLE `stats` (
  `id` int(11) DEFAULT NULL,
  `views_count` int(11) DEFAULT NULL,
  `score` int(11) DEFAULT NULL,
  `scored_count` int(11) DEFAULT NULL,
  `commented_count` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of stats
-- ----------------------------

-- ----------------------------
-- Table structure for sys_log
-- ----------------------------
DROP TABLE IF EXISTS `sys_log`;
CREATE TABLE `sys_log` (
  `start_date` datetime DEFAULT NULL,
  `accesstoken` varchar(255) DEFAULT NULL,
  `session` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sys_log
-- ----------------------------

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `profile` varchar(255) DEFAULT NULL,
  `account` varchar(255) DEFAULT NULL,
  `stats` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `is_friend` varchar(255) DEFAULT NULL,
  `is_premium` varchar(255) DEFAULT NULL,
  `is_following` varchar(255) DEFAULT NULL,
  `is_follower` varchar(255) DEFAULT NULL,
  `profile_image_urls` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`,`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
