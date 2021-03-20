/*
 Navicat Premium Data Transfer

 Source Server         : docker-mysql
 Source Server Type    : MySQL
 Source Server Version : 80017
 Source Host           : 192.168.1.129:33061
 Source Schema         : evolve_devops

 Target Server Type    : MySQL
 Target Server Version : 80017
 File Encoding         : 65001

 Date: 20/03/2021 18:06:22
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for students
-- ----------------------------
DROP TABLE IF EXISTS `students`;
CREATE TABLE `students` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `class` tinyint(3) DEFAULT NULL,
  `age` tinyint(3) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of students
-- ----------------------------
BEGIN;
INSERT INTO `students` VALUES (1, '张无忌', 2, 20);
INSERT INTO `students` VALUES (2, '周芷若', 1, 20);
INSERT INTO `students` VALUES (3, '赵敏', 1, 20);
INSERT INTO `students` VALUES (4, '虚竹', 2, 20);
INSERT INTO `students` VALUES (8, '段誉', 2, 18);
INSERT INTO `students` VALUES (9, '胡一刀', 1, 18);
INSERT INTO `students` VALUES (10, '扫地僧', 2, 99);
INSERT INTO `students` VALUES (11, '胖头陀', 1, 30);
INSERT INTO `students` VALUES (12, '杨逍', 1, 23);
INSERT INTO `students` VALUES (13, '令狐冲', 1, 23);
INSERT INTO `students` VALUES (14, '任盈盈', 2, 21);
INSERT INTO `students` VALUES (15, '向问天', 1, 30);
INSERT INTO `students` VALUES (16, '风清扬', 1, 26);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
