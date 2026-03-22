DROP TABLE book IF EXISTS;
DROP TABLE course IF EXISTS;

CREATE TABLE book (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
	title VARCHAR(256),
	author VARCHAR(128),
	categ SMALLINT,
	course_id INTEGER);

CREATE TABLE course (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
	intitule VARCHAR(256),
	codeNAF VARCHAR(8),
	teacher VARCHAR(128)
);
	
INSERT INTO book VALUES(
    (1, 'Architecture N-tier pour java ', 'J. Lafosse', 1, 1),
	(2, 'Test Selenium pour java ', 'ENI', 1, 1));
	
INSERT INTO course VALUES(
    (1, 'Applications reparties', 'NSY102', 'Torkhani'));