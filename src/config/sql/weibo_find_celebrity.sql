CREATE TABLE `main`.`find_celebrity` (
  `id` INT NOT NULL AUTO_INCREMENT COMMENT '主键',
  `cate` VARCHAR(10) NOT NULL COMMENT '分类',
  `uid` VARCHAR(45) NOT NULL COMMENT '用户id',
  `uname` VARCHAR(45) NOT NULL COMMENT '用户名',
  `cnum` INT NOT NULL COMMENT '微博数',
  `fnum` INT NOT NULL COMMENT '粉丝数',
  `lnum` INT NOT NULL COMMENT '关注数',
  PRIMARY KEY (`id`),
  INDEX `idx_cate` (`cate` ASC),
  INDEX `idx_uid` (`uid` ASC),
  INDEX `idx_uname` (`uname` ASC),
  INDEX `idx_num` (`cnum` ASC, `fnum` ASC, `lnum` ASC))
DEFAULT CHARACTER SET = utf8mb4
COMMENT = '名人榜';
