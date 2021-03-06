/*
Navicat MySQL Data Transfer

Source Server         : local
Source Server Version : 50544
Source Host           : localhost:3306
Source Database       : pixiv

Target Server Type    : MYSQL
Target Server Version : 50544
File Encoding         : 65001

Date: 2016-01-20 19:41:28
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for info_log
-- ----------------------------
DROP TABLE IF EXISTS `info_log`;
CREATE TABLE `info_log` (
  `page` varchar(255) NOT NULL,
  `mode` varchar(255) NOT NULL,
  `per_page` varchar(255) DEFAULT NULL,
  `date` datetime NOT NULL,
  PRIMARY KEY (`date`,`page`,`mode`)
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
  `rank` int(11) NOT NULL,
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
  PRIMARY KEY (`id`,`rank`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of pictures
-- ----------------------------

-- ----------------------------
-- Table structure for stats
-- ----------------------------
DROP TABLE IF EXISTS `stats`;
CREATE TABLE `stats` (
  `id` int(11) NOT NULL,
  `date` datetime NOT NULL,
  `views_count` int(11) DEFAULT NULL,
  `score` int(11) DEFAULT NULL,
  `scored_count` int(11) DEFAULT NULL,
  `commented_count` int(11) DEFAULT NULL,
  `favorited_count` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`,`date`)
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
  `username` varchar(255) DEFAULT NULL,
  `accesstoken` varchar(255) DEFAULT NULL,
  `session` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of sys_log
-- ----------------------------
INSERT INTO `sys_log` VALUES ('2016-01-20 17:57:05', 'gm415579', null, null);
INSERT INTO `sys_log` VALUES ('2016-01-20 17:58:01', 'gm415579', null, null);
INSERT INTO `sys_log` VALUES ('2016-01-20 17:58:43', 'gm415579', null, null);
INSERT INTO `sys_log` VALUES ('2016-01-20 18:58:02', 'gm415579', null, null);
INSERT INTO `sys_log` VALUES ('2016-01-20 18:59:54', 'gm415579', null, null);
INSERT INTO `sys_log` VALUES ('2016-01-20 19:02:09', 'gm415579', null, null);
INSERT INTO `sys_log` VALUES ('2016-01-20 19:06:10', 'gm415579', null, null);
INSERT INTO `sys_log` VALUES ('2016-01-20 19:07:21', 'gm415579', null, null);
INSERT INTO `sys_log` VALUES ('2016-01-20 19:07:34', 'gm415579', null, null);
INSERT INTO `sys_log` VALUES ('2016-01-20 19:08:25', 'gm415579', null, null);
INSERT INTO `sys_log` VALUES ('2016-01-20 19:09:21', 'gm415579', null, null);
INSERT INTO `sys_log` VALUES ('2016-01-20 19:15:12', 'gm415579', null, null);
INSERT INTO `sys_log` VALUES ('2016-01-20 19:15:53', 'gm415579', null, null);
INSERT INTO `sys_log` VALUES ('2016-01-20 19:16:04', 'gm415579', null, null);
INSERT INTO `sys_log` VALUES ('2016-01-20 19:26:34', 'gm415579', null, null);
INSERT INTO `sys_log` VALUES ('2016-01-20 19:26:49', 'gm415579', null, null);
INSERT INTO `sys_log` VALUES ('2016-01-20 19:29:36', 'gm415579', null, null);
INSERT INTO `sys_log` VALUES ('2016-01-20 19:32:00', 'gm415579', null, null);
INSERT INTO `sys_log` VALUES ('2016-01-20 19:32:12', 'gm415579', null, null);
INSERT INTO `sys_log` VALUES ('2016-01-20 19:35:38', 'gm415579', null, null);
INSERT INTO `sys_log` VALUES ('2016-01-20 19:36:44', 'gm415579', null, null);

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
