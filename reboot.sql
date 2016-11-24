/*
Navicat MySQL Data Transfer

Source Server         : 93
Source Server Version : 50629
Source Host           : 172.16.0.93:3306
Source Database       : flask

Target Server Type    : MYSQL
Target Server Version : 50629
File Encoding         : 65001

Date: 2016-11-24 17:07:54
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for idc
-- ----------------------------
DROP TABLE IF EXISTS `idc`;
CREATE TABLE `idc` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `name_cn` varchar(45) DEFAULT NULL,
  `address` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of idc
-- ----------------------------
INSERT INTO `idc` VALUES ('2', 'aliyun', '阿里云', '杭州1区');

-- ----------------------------
-- Table structure for job
-- ----------------------------
DROP TABLE IF EXISTS `job`;
CREATE TABLE `job` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_name` char(50) DEFAULT NULL COMMENT '应用系统名称',
  `app_purpose` char(50) DEFAULT NULL COMMENT '系统用途说明',
  `language` char(10) DEFAULT NULL COMMENT '开发语言',
  `soft_version` varchar(100) DEFAULT NULL COMMENT '所需tomcat/jdk版本',
  `sys_resource` char(100) DEFAULT NULL COMMENT '对系统资源需求',
  `db_info` char(100) DEFAULT NULL COMMENT '是否使用数据库，容量需求',
  `other_relation` char(100) DEFAULT NULL COMMENT '其他关联系统',
  `sys_monitor` char(100) DEFAULT NULL COMMENT '监控方式(端口、api)',
  `app_user` char(20) DEFAULT NULL COMMENT '系统使用人员',
  `dever` char(20) DEFAULT NULL COMMENT '项目负责人',
  `test_host` char(20) DEFAULT NULL COMMENT '测试服务器',
  `pre_host` char(20) DEFAULT NULL COMMENT '预发布服务器',
  `real_host` char(20) DEFAULT NULL COMMENT '生产服务器',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of job
-- ----------------------------

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(45) NOT NULL,
  `cn_name` varchar(45) DEFAULT NULL,
  `password` varchar(45) NOT NULL,
  `email` varchar(45) DEFAULT NULL,
  `phone` varchar(45) DEFAULT NULL,
  `role` varchar(45) DEFAULT NULL,
  `status` int(11) NOT NULL COMMENT '0：激活，1：锁定',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', 'admin', '超级管理员', 'a75b19b4ee4815f24c490ac57cc422d3', '123@qq.com', '111', 'admin', '0');
INSERT INTO `user` VALUES ('4', 'test', 'test', 'ad765b4729f3cb933fed381d408ddfab', '123', '123', 'user', '0');
INSERT INTO `user` VALUES ('5', 'a', 'a', '944b6d5c64234b25e00be9618df620f4', '121', '112', 'user', '0');
INSERT INTO `user` VALUES ('6', 'pc', 'pc', 'e0606ed280e90376fdabc87c317c7099', '12', '12', 'user', '0');
INSERT INTO `user` VALUES ('8', 'bb', 'bb', '944b6d5c64234b25e00be9618df620f4', '1', '1', 'user', '0');
INSERT INTO `user` VALUES ('9', 'cc', 'vc', '9d7f008b447a5dbd042bd479dd578d32', '1', '1', 'user', '0');
INSERT INTO `user` VALUES ('10', 'dd', 'dd', 'e0606ed280e90376fdabc87c317c7099', '12', '12', 'user', '0');
INSERT INTO `user` VALUES ('11', 'ee', 'ee', '944b6d5c64234b25e00be9618df620f4', '1', '1', 'user', '0');
INSERT INTO `user` VALUES ('12', 'ff', 'ff', '944b6d5c64234b25e00be9618df620f4', '1', '1', 'user', '0');
INSERT INTO `user` VALUES ('14', 'fff', 'fff', 'd06008f36f96ffb168180d5cd5ef3bd3', '1', '1', 'admin', '0');
SET FOREIGN_KEY_CHECKS=1;
