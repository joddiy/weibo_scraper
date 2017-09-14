CREATE TABLE `weibo_hotsearch` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `topic` varchar(30) CHARACTER SET utf8 NOT NULL COMMENT '热搜关键字',
  `cid` varchar(30) CHARACTER SET utf8 NOT NULL COMMENT '评论id',
  `uid` varchar(30) CHARACTER SET utf8 NOT NULL COMMENT '用户id',
  `uname` varchar(30) CHARACTER SET utf8 NOT NULL COMMENT '用户名',
  `data` varchar(255) NOT NULL,
  `commit_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '发布时间',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`id`),
  KEY `idx_uid` (`uid`) USING BTREE,
  KEY `idx_uname` (`uname`) USING BTREE,
  KEY `idx_commit_time` (`commit_time`) USING BTREE,
  KEY `idx_create_time` (`create_time`) USING BTREE,
  KEY `idx_topic` (`topic`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=1648 DEFAULT CHARSET=utf8mb4 COMMENT='微博热搜';
