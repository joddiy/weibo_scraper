CREATE TABLE `find_celebrity` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `cate` varchar(10) NOT NULL COMMENT '分类',
  `uid` varchar(45) NOT NULL COMMENT '用户id',
  `uname` varchar(45) NOT NULL COMMENT '用户名',
  `cnum` int(11) NOT NULL COMMENT '微博数',
  `fnum` int(11) NOT NULL COMMENT '粉丝数',
  `lnum` int(11) NOT NULL COMMENT '关注数',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_uid` (`uid`),
  KEY `idx_cate` (`cate`),
  KEY `idx_uname` (`uname`),
  KEY `idx_num` (`cnum`,`fnum`,`lnum`)
) ENGINE=InnoDB AUTO_INCREMENT=1370 DEFAULT CHARSET=utf8mb4 COMMENT='名人榜';
SELECT * FROM main.find_celebrity;