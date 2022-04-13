/*
 Navicat Premium Data Transfer

 Source Server         : 127.0.0.1
 Source Server Type    : MySQL
 Source Server Version : 50718
 Source Host           : localhost:3306
 Source Schema         : stat

 Target Server Type    : MySQL
 Target Server Version : 50718
 File Encoding         : 65001

 Date: 20/02/2020 15:42:41
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for pushservice
-- ----------------------------
DROP TABLE IF EXISTS `pushservice`;
CREATE TABLE `pushservice`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pushDateStr` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `title` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `summary` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `infoSource` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `sourceUrl` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `pushDate` date NOT NULL,
  `updateTime` timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP(0),
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of pushservice
-- ----------------------------
INSERT INTO `pushservice` VALUES (1, '4小时前', '钻石公主号2名新冠肺炎感染者死亡', '据日本广播协会电视台20日报道，2名在“钻石公主”号邮轮上感染冠肺炎的患者死亡。这首次出现在“钻石公主”号邮轮感染新冠肺炎后死亡的病例。截至目前，日本国内新冠肺炎死亡病例增至3例。\n', '人民日报', 'http://m.weibo.cn/2803301701/4473995094751309', '2020-02-20', '2020-02-20 15:35:13');
INSERT INTO `pushservice` VALUES (2, '4小时前', '全国13地新增病例为0', '2月19日0-24时，上海、江苏、辽宁、福建、山西、贵州、宁夏、云南、青海、新疆、西藏报告无新增新冠肺炎确诊病例；19日8时—20日8时，内蒙古报告无新增确诊病例；18日20时至19日20时，甘肃报告无新增确诊病例。且其余省区市新增确诊病例均为个位数。\n', '人民日报', 'http://m.weibo.cn/2803301701/4473991953264899', '2020-02-20', '2020-02-20 15:35:13');
INSERT INTO `pushservice` VALUES (3, '4小时前', '湖北以外新增病例16连降', '据国家卫健委数据统计，2月19日0—24时，全国除湖北以外地区新增确诊病例45例，连续第16日呈下降态势。前几日这一数据分别为：890例（3日）、731例（4日）、707例（5日)、696例（6日）、558例（7日）、509例（8日）、444例（9日）、381例（10日）、377例（11日）、312例（12日）、267例（13日）、221例（14日）、166例（15日）、115例（16日），79例（17日），56例（18日）。\n', '人民网', 'http://m.weibo.cn/2286908003/4473983589954353', '2020-02-20', '2020-02-20 15:35:13');
INSERT INTO `pushservice` VALUES (4, '5小时前', '全国新增394例新冠肺炎，累计确诊新冠肺炎74576例', '2月19日0—24时，31个省（自治区、直辖市）和新疆生产建设兵团报告新增确诊病例394例，新增死亡病例114例，新增疑似病例1277例。截至2月19日24时，据31个省（自治区、直辖市）和新疆生产建设兵团报告，现有确诊病例56303例，累计治愈出院病例16155例，累计死亡病例2118例，累计报告确诊病例74576例，现有疑似病例4922例。累计追踪到密切接触者589163人，尚在医学观察的密切接触者126363人。', '人民日报', 'http://m.weibo.cn/2803301701/4473982336318492', '2020-02-20', '2020-02-20 15:35:13');
INSERT INTO `pushservice` VALUES (5, '5小时前', '韩国累计确诊82例新冠肺炎', '据韩国卫生部门消息：截至当地时间20日上午9时，韩国新型冠状病毒感染者人数已达82人。新增的31例确诊患者中，有30人来自韩国南部的大邱市及周边的庆尚北道地区。经初步流行病学调查，18日该地区出现首例确诊病例，此后新增的确诊感染者大部分都与其有关联。', '央视新闻', 'http://m.weibo.cn/2656274875/4473980846903958', '2020-02-20', '2020-02-20 15:35:13');

SET FOREIGN_KEY_CHECKS = 1;
