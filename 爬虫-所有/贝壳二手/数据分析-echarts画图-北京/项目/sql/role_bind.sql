/*
 Navicat MySQL Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50726
 Source Host           : localhost:3306
 Source Schema         : beike

 Target Server Type    : MySQL
 Target Server Version : 50726
 File Encoding         : 65001

 Date: 13/12/2021 21:39:18
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for role_bind
-- ----------------------------
DROP TABLE IF EXISTS `role_bind`;
CREATE TABLE `role_bind`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userId` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '用户id',
  `roleId` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NULL DEFAULT NULL COMMENT '角色id',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of role_bind
-- ----------------------------
INSERT INTO `role_bind` VALUES (1, '1', '1');
INSERT INTO `role_bind` VALUES (2, '1', '2');
INSERT INTO `role_bind` VALUES (3, '1', '3');

SET FOREIGN_KEY_CHECKS = 1;
