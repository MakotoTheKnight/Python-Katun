//PreCondition:  Vanilla Table

     INSERT INTO Song VALUES('C:/music/', 'Radiohead', '.mp3', 'Faust Arp', 
		'New Age', 5, 'SomeAlbum', '128', '1995', 'August');
//Post Condition:  Song should be inserted into table, with above values.


//PreCondition:  1 song in table

INSERT INTO Song VALUES('C:/music/', 'Philip Glass', '.wav', 'Violin Concerto #3', 
		'Orchestra', 7, 'Greatest of Philip Glass', '64', '2001', 'May');
		
//PreCondition:  2 songs in table
INSERT INTO Song VALUES('C:/music/mymusic', '311', '.mp3', 'Come Original', 
		'Punk', 12, 'Transition', '64', '1999', 'October');
//PostCondition:  3 songs now in table

//Precondition:  0 songs in favorites table
INSERT INTO Favorites VALUES (INSERT INTO Song VALUES(2, 'C:/music/mymusic', 
	'311', '.mp3', 'Come Original');
//Postcondition:  1 song in favorites table

//PreCondition:  3 songs in Song table (since each song has an album)
SELECT * 
FROM Song
//PostCondition:  Same as prec.

//PreCondition:  3 songs in Album table (since each song has an album)
SELECT * 
FROM Album
//PostCondition:  Same as prec.

//PreCondition:  3 songs in Favorites table (since each song has an album)
SELECT * 
FROM Favorites
//PostCondition:  Same as prec.

//PreCondition:  3 songs in table
UPDATE Song SET bitrate ='128' WHERE location.song = 'C:/music/mymusic' AND
	Artist.Song = '311' AND filetype.Song = '.mp3' AND title.Song = 
	'Come Original');
//PostCondition:  3 songs in table, song 'Come Original" is updated with new 
//bitrate

//PreCondition:  3 songs in Album table (since each song has an album)
SELECT * 
FROM Song
//PostCondition:  Same as prec.

//PreCondition:  3 songs in Album table (since each song has an album)
SELECT * 
FROM Album
//PostCondition:  Same as prec.

//PreCondition:  3 songs in Album table (since each song has an album)
SELECT * 
FROM Favorites
//PostCondition:  Same as prec.








