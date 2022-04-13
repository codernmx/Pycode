create table confirmedStat(
	id int(11) NOT NULL AUTO_INCREMENT,
    province varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL, -- 可以是short name或者complite name
	city varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	confirmedCount int(11) DEFAULT NULL,
	suspectedCount int(11) DEFAULT NULL,
	curedCount int(11) DEFAULT NULL,
	deadCount int(11) DEFAULT NULL,
	updateTime timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	PRIMARY KEY(id)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


create table pushService(
	id int(11) NOT NULL AUTO_INCREMENT,
    pushDateStr varchar(60) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	title varchar(60) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	summary varchar(500) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	infoSource varchar(60) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	sourceUrl varchar(60) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	pushDate date NOT NULL,
	updateTime timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	PRIMARY KEY(id)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;