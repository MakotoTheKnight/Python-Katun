INSERT INTO user values(NULL, 'feltzn', 'robin');
INSERT INTO user values(NULL, 'jblack32', '23kcalbj');

--PreCondition:  Vanilla Table

INSERT INTO Song VALUES('C:/music/Song', 'Radiohead', '.mp3', 'Faust Arp', 'New Age', 5, 'SomeAlbum', 128, 1995, 8);
--Post Condition:  Song should be inserted into table, with above values.

--PreCondition:  1 song in Song

--PostCondition:  Same

--PreCondition:  1 song in table

INSERT INTO Song VALUES('C:/music/Song', 'Philip Glass', 'wav', 'Violin Concerto #3', 'Orchestra', 7, 'Greatest of Philip Glass', 64, 2001, 5);
--PostCondition:  2 songs in Song

--pre:  2 songs in song

INSERT INTO Song VALUES('C:/music/MyMusic/Songs', 'Philip Glass', 'wav', 'Violin Concerto #3', 'Orchestra', 7, 'Greatest of Philip Glass', 64, 2001, 5);
--PostCondition:  2 songs in Song

INSERT INTO Song VALUES('C:/Music/Song', 'Justin Bieber', '.mp3', 'I''m Not the Father, I Swear', 'Pop', 5, 'Biebertastic', 128, 2011, 11);
INSERT INTO Song VALUES('C:/Mine/Song', 'Justin Bieber', '.mp3', 'I''m Not the Father, I Swear', 'Pop', 5, 'Biebertastic', 128, 2011, 11);

SELECT *
FROM Song;

SELECT *
FROM Duplicates;
