/* Write a suite of tests to ensure proper operating order on the database.

These tests are not automated, and the queries are expected to be sent in real-time, so there will be scrolling back and forth in the terminal to verify that the operations are correct.
*/

-- Precondition:  The user table has 'root' with password 'toor' in it.
-- Postcondition:  The user table has the users 'root' and 'user' with password 'user'.

INSERT INTO user VALUES(NULL, 'root', 'toor');
INSERT INTO user VALUES(NULL, 'user', 'user');

SELECT * FROM user;

-- Precondition:  The song table is empty.
-- Postcondition:  The song table has 10 songs inserted.

INSERT INTO song VALUES('loc1', 'art1', 'ogg', 'tit1', 'gen1', 1, 'alb1', 128, 2000, 1);
INSERT INTO song VALUES('loc2', 'art1', 'ogg', 'tit2', 'gen1', 1, 'alb1', 128, 2000, 1);
INSERT INTO song VALUES('loc3', 'art1', 'ogg', 'tit3', 'gen1', 1, 'alb2', 128, 2004, 1);
INSERT INTO song VALUES('loc4', 'art1', 'ogg', 'tit4', 'gen1', 1, 'alb3', 128, 2004, 1);
INSERT INTO song VALUES('loc5', 'art2', 'ogg', 'tit5', 'gen1', 1, 'alb1', 128, 1999, 1);
INSERT INTO song VALUES('loc6', 'art2', 'ogg', 'tit6', 'gen1', 1, 'alb1', 128, 2007, 1);
INSERT INTO song VALUES('loc7', 'art2', 'ogg', 'tit7', 'gen1', 1, 'alb1', 128, 2011, 1);
INSERT INTO song VALUES('loc8', 'art2', 'ogg', 'tit8', 'gen1', 1, 'alb2', 128, 2008, 1);
INSERT INTO song VALUES('loc9', 'art2', 'ogg', 'tit9', 'gen2', 1, 'alb3', 128, 2008, 1);
INSERT INTO song VALUES('loc10', 'art2', 'ogg', 'tit10', 'gen3', 1, 'alb4', 128, 2008, 1);

SELECT COUNT(*) FROM song;

-- Precondition:  The duplicates table is empty.
-- Postcondition:  The duplicates table contains two entries.

INSERT INTO song VALUES('loc99', 'art2', 'ogg', 'tit8', 'gen1', 1, 'alb2', 128, 2008, 1);
INSERT INTO song VALUES('loc100', 'art1', 'ogg', 'tit1', 'gen1', 1, 'alb1', 128, 2008, 1);

SELECT COUNT(*) FROM duplicates;

-- Precondition:  The favorites table is empty.
-- Postcondition:  'user' labels a song as a favorite.

INSERT INTO favorites VALUES(2, 'loc1', 'art1', 'ogg', 'tit1');

SELECT COUNT(*) FROM favorites;

-- Precondition:  A song called 'tit1' has its normal filetype.
-- Postcondition:  The song is changed from OGG to MP3.  It is reflected in both song and favorites.

UPDATE song	SET filetype = 'MP3' WHERE title = 'tit1';

SELECT * FROM song WHERE title = 'tit1';
SELECT * FROM favorites WHERE title = 'tit1';
