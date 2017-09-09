CREATE TABLE weibo_hotsearch (
  id          BIGINT(11)  NOT NULL AUTO_INCREMENT
  COMMENT '主键',
  uid         VARCHAR(30) NOT NULL
  COMMENT '用户id',
  uname       VARCHAR(30) NOT NULL
  COMMENT '用户名',
  data        TEXT        NOT NULL
  COMMENT '微博内容',
  commit_time TIMESTAMP   NOT NULL
  COMMENT '发布时间',
  create_time TIMESTAMP   NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
  COMMENT '创建时间',
  PRIMARY KEY (id),
  KEY idx_uid (uid),
  KEY idx_uname (uname),
  KEY idx_commit_time (commit_time),
  KEY idx_create_time (create_time)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8
  COMMENT ='微博搜索';

