CREATE TABLE `Location` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name`	TEXT NOT NULL,
	`address`	TEXT NOT NULL
);

CREATE TABLE `Customer` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name`    TEXT NOT NULL,
    `address`    TEXT NOT NULL,
    `email`    TEXT NOT NULL,
    `password`    TEXT NOT NULL
);

CREATE TABLE `Animal` (
	`id`  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name`  TEXT NOT NULL,
	`status` TEXT NOT NULL,
	`breed` TEXT NOT NULL,
	`customer_id` INTEGER NOT NULL,
	`location_id` INTEGER,
	FOREIGN KEY(`customer_id`) REFERENCES `Customer`(`id`),
	FOREIGN KEY(`location_id`) REFERENCES `Location`(`id`)
);


CREATE TABLE `Employee` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name`	TEXT NOT NULL,
	`address`	TEXT NOT NULL,
	`location_id` INTEGER NOT NULL,
	FOREIGN KEY(`location_id`) REFERENCES `Location`(`id`)

);



INSERT INTO `Location` VALUES (null, 'Nashville North', "72 North Road");
INSERT INTO `Location` VALUES (null, 'Nashville South', "100 South Street");
INSERT INTO `Location` VALUES (null, 'Nashville East', "200 East Ave");
INSERT INTO `Location` VALUES (null, 'Nashville West', "300 West Blvd");


INSERT INTO `Employee` VALUES (null, "Mario Kart", "100 Rainbow Road", 1);
INSERT INTO `Employee` VALUES (null, "Luigi Mansion", "100 Dead End Street", 2);
INSERT INTO `Employee` VALUES (null, "Wario", "200 Purple Park Place", 1);
INSERT INTO `Employee` VALUES (null, "Bowser", "300 Lava Way", 2);


INSERT INTO `Customer` VALUES (null, "Bilbo", "12 Rulemall Ave", "bill@bill.com", "bo");
INSERT INTO `Customer` VALUES (null, "Frodo", "12 Findem Street", "fro@fro.com", "do");
INSERT INTO `Customer` VALUES (null, "Gandolf", "12 Bringemall Drive", "gan@gan.com", "dolf");
INSERT INTO `Customer` VALUES (null, "Samwise", "12 Darkness Bindem Blvd", "sam@sam.com", "wise");


INSERT INTO `Animal` VALUES (null, "Aragog", "Feeding", "Acromantula", 4, 1);
INSERT INTO `Animal` VALUES (null, "Fluffy", "Sleeping", "Three Headed Dog", 3, 1);
INSERT INTO `Animal` VALUES (null, "Norbert", "Flying", "Norwegian Ridgeback", 2, 2);
INSERT INTO `Animal` VALUES (null, "Hedwig", "Delivering A Letter", "Snowy Owl", 2, 2);

SELECT * FROM `Animal`;
SELECT * FROM `Location`;
SELECT * FROM `Customer`;
SELECT * FROM `Employee`;


SELECT * FROM `Animal`
ORDER BY id DESC;

SELECT * FROM `Animal`
WHERE id = 5;