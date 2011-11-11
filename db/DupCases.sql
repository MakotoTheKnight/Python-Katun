INSERT INTO user values(NULL, 'feltzn', 'robin');

--PreCondition:  Vanilla Table

     INSERT INTO Song VALUES('C:/music/Song', 'Radiohead', '.mp3', 'Faust Arp', 
		'New Age', 5, 'SomeAlbum', 128, 1995, 'August');
--Post Condition:  Song should be inserted into table, with above values.

--PreCondition:  1 song in Song

--PostCondition:  Same

--PreCondition:  1 song in table

INSERT INTO Song VALUES('C:/music/Song', 'Philip Glass', 'wav', 'Violin Concerto #3', 
		'Orchestra', 7, 'Greatest of Philip Glass', 64, 2001, 'May');
--PostCondition:  2 songs in Song

--pre:  2 songs in song


INSERT INTO Song VALUES('C:/music/MyMusic/Songs', 'Philip Glass', 'wav', 'Violin Concerto #3', 
		'Orchestra', 7, 'Greatest of Philip Glass', 64, 2001, 'May');
--PostCondition:  2 songs in Song

INSERT INTO Song VALUES('C:/Music/Song', 'Justin Bieber', '.mp3', 
	'I''m Not the Father, I Swear', 'Pop', 5, 'Biebertastic', 128, 
	2011, 'November');
	
	INSERT INTO Song VALUES('C:/Mine/Song', 'Justin Bieber', '.mp3', 
	'I''m Not the Father, I Swear', 'Pop', 5, 'Biebertastic', 128, 
	2011, 'November');

SELECT *
FROM Song;

SELECT *
FROM Duplicates;






