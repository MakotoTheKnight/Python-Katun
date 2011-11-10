--PreCondition:  Vanilla Table

     INSERT INTO Song VALUES('C:/music/Song', 'Radiohead', '.mp3', 'Faust Arp', 
		'New Age', 5, 'SomeAlbum', 128, 1995, 'August');
--Post Condition:  Song should be inserted into table, with above values.

INSERT INTO user values(NULL, feltzn, 84ROBIN12);

--PreCondition:  1 song in Song
SELECT *
FROM Song;
--PostCondition:  Same

--PreCondition:  1 song in table

INSERT INTO Song VALUES('C:/music/Song', 'Philip Glass', '.wav', 'Violin Concerto #3', 
		'Orchestra', 7, 'Greatest of Philip Glass', 64, 2001, 'May');
--PostCondition:  2 songs in Song

--pre:  2 songs in song
SELECT *
FROM Song;
--post:  2 songs in Song
		
--PreCondition:  2 songs in table
INSERT INTO Song VALUES('C:/music/Song', '311', '.mp3', 'Come Original', 
		'Punk', 12, 'Transition', 64, 1999, 'October');
--PostCondition:  3 songs now in table


--Precondition:  0 songs in favorites table
INSERT INTO Favorites VALUES(1, 'C:/music/Favorites', 
	'311', '.mp3', 'Come Original');
--Postcondition:  1 song in favorites table, and 1 in contains

--PreCondition:  3 songs in Song table (since each song has an album)
SELECT * 
FROM Song;
--PostCondition:  Same as prec.

--PreCondition:  3 songs in Album table (since each song has an album)
SELECT * 
FROM Album;
--PostCondition:  Same as prec.

--PreCondition:  1 songs in Favorites table (since each song has an album)
SELECT * 
FROM Favorites;
--PostCondition:  Same as pre.

--PreCondition:  3 songs in table
UPDATE Song SET bitrate = 128 WHERE location.song = 'C:/music/Song' 
AND	Artist.Song = '311' AND filetype.Song = '.mp3' AND title.Song = 
	'Come Original');
--PostCondition:  3 songs in table, song 'Come Original" is updated with 
--new bitrate

--PreCondition:  3 songs in Song table (since each song has an album)
SELECT * 
FROM Song;
--PostCondition:  Same as prec.

--PreCondition:  3 songs in Album table (since each song has an album)
SELECT * 
FROM Album;
--PostCondition:  Same as prec.

--PreCondition:  1 song in Album table (since each song has an album)
SELECT * 
FROM Favorites;
--PostCondition:  Same as prec.

--Pre:  3 song in Song
INSERT INTO Song VALUES('C:/Music/Song', 'Justin Bieber', '.mp3', 
	'I'm Not the Father, I Swear', 'Pop', 5, 'Biebertastic', 128, 
	2011, 'November');
--Post:  4 song in Song


--Pre:  4 Songs in Song, 0 in Duplicates
INSERT INTO Song VALUES ('C:/Music/Song/', 'Justin Bieber', '.mp3', 
	'Baby Isn't Mine, I Swear', 'Pop', 5, 'Biebertastic', 128, 
	2011, 'November');
--Post:  4 Songs in Song, 1 in Duplicates

	
--Pre:  0 songs in Playlist
INSERT INTO Contains VALUES('Pop and Hop', 'C:/Music/Song/', 'Justin 
Bieber', '.mp3', 'Baby Isn't Mine, I Swear');
--Post:  1 song in Playlist

--Pre:  1 song in Contains
SELECT * 
FROM Contains;
--Post:  1 song in Contains

--Pre:  1 Song in Playlist
INSERT INTO Playlist VALUES('Pop and Hop', 2, 1);
--Post:  1 song in Playlist

--Pre:  2 songs in Playlist
SELECT * 
FROM Playlist;
--Post:  2 Song in Playlist

--Pre:  Four songs in Song
INSERT INTO Song VALUES('C:/Music/', 'Dr. Dre', 
	'.wav', 'Still Dre', 'Hip Hop', 3, 'Dre 2000', 64, 2000, 
	'July');
--Post:  Five Songs in Song

--Pre:  2 Songs in Contains
INSERT INTO Contains VALUES('C:/Music/Contains', 'Dr. Dre', 
	'.wav', 'Still Dre', 'Hip Hop', 3, 'Dre 2000', 64, 2000, 
	'July');
--Post:  3 Songs in Contains

--See if 3 songs are in Contains, and 5 in Song
SELECT *
FROM Contains;

SELECT * 
FROM Song;

--Pre:  5 Songs in Song
INSERT INTO Song VALUES('C:/Music/MyMusic/', 'JLo', '.mp3', 
	'On the Floor', 'Pop', 8, 'JLo Blast', 32, 2011, 'June');
--Post:  6 Songs in Song

--Pre:  6 Songs in Song
INSERT INTO Song VALUES('C:/Music/hop/', 'Bob Dylan', '.mp3', 
	'All the Lonely Horses', 'Classic', 10, 'Dylanastic', 128, 
	1970, 'May');
--Post:  7 Songs in Song

--Pre:  7 Songs in Song
INSERT INTO Song VALUES('C:/Music/MyMusic/', 'Johnny Cash', '.org', 
	'I Killed a Man', 'Classic', 18, 'Cashastic', 64, 1965, 
	'January');
--Post:  8 Songs in Song

--Pre:  8 songs in Song
INSERT INTO Song VALUES('C:/Music/MyLocation/', 'Nelly', '.mp3', 
	'St. Loui', 'Rap', 12, 'South', 128, 1999, 
	'August');
--Post:  9 songs in Song

--Pre:  3 songs in Contains	
INSERT INTO Contains('C:/Music/MyLocation/', 'Nelly', '.mp3', 
	'St. Loui', 'Rap', 12, 'South', 128, 1999, 
	'August'); 
--Post:  4 songs in Contains

--Pre:  9 songs in Song
DELETE FROM Song VALUES('C:/Music/MyLocation/', 'Nelly', '.mp3', 
	'St. Loui', 'Rap', 12, 'South', 128, 1999, 
	'August');
--Post:  8 songs in song
	
--Pre:  4 songs in Contains
DELETE FROM Contains VALUES('C:/Music/MyLocation/', 'Nelly', '.mp3', 
	'St. Loui', 'Rap', 12, 'South', 128, 1999, 
	'August');
--Post:  3 songs in Contains	

--Should be 8 songs in song, and 3 in Contains

SELECT *
FROM Song;

SELECT * 
FROM Contains;

UPDATE Playlist SET bitrate =128 WHERE count.Playlist = ' 
AND	Artist.Song = '311' AND filetype.Song = '.mp3' AND title.Song = 
	'Come Original');







