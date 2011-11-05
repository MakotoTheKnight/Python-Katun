/* Specify foreign keys to be ON in order for them to work properly. */

PRAGMA foreign_keys=ON;
BEGIN TRANSACTION;

/* Schemas */
CREATE TABLE song(
	location TEXT,
	artist TEXT,
	filetype TEXT,
	title TEXT,
	genre TEXT,
	track INTEGER,
	album TEXT,
	bitrate INTEGER,
	year INTEGER,
	month INTEGER,
	PRIMARY KEY(
		location,
		artist,
		filetype,
		title
	)
);

CREATE TABLE user(
	uid INTEGER PRIMARY KEY ASC,
	uname TEXT
);

CREATE TABLE contains(
	pname TEXT,
	location TEXT,
	artist TEXT,
	filetype TEXT,
	title TEXT,
	FOREIGN KEY(pname) references playlist(pname),
	FOREIGN KEY(location, artist, filetype, title) references song(location, artist, filetype, title)
);

CREATE TABLE favorites(
	uid INTEGER PRIMARY KEY ASC,
	location TEXT,
	artist TEXT,
	filetype TEXT,
	title TEXT,
	FOREIGN KEY(location, artist, filetype, title) references song(location, artist, filetype, title)
);

CREATE TABLE duplicates(
	location TEXT,
	artist TEXT,
	filetype TEXT,
	title TEXT,
	duplicate_location TEXT PRIMARY KEY,
	FOREIGN KEY(location, artist, filetype, title) references song(location, artist, filetype, title)
);

CREATE TABLE playlist(
	pname TEXT PRIMARY KEY,
	uid INTEGER,
	count INTEGER,
	FOREIGN KEY(uid) references user(uid)
);

CREATE TABLE album(
	location TEXT,
	artist TEXT,
	filetype TEXT,
	title TEXT,
	album_art_filename TEXT PRIMARY KEY,
	track_count INTEGER,
	FOREIGN KEY(location, artist, filetype, title) references song(location, artist, filetype, title)
);

/* Triggers */

CREATE TRIGGER IF NOT EXISTS song.updateLocation AFTER UPDATE OF location on song FOR EACH ROW
BEGIN (
	UPDATE favorites SET location = song.location WHERE favorites.location = old.location;
	
	UPDATE album SET location = song.location WHERE album.location = old.location;
	
	UPDATE duplicates SET location = song.location WHERE duplicates.location = old.location;
	
	UPDATE contains SET location = song.location WHERE contains.location = old.location;
)
END; 

CREATE TRIGGER IF NOT EXISTS song.updateArtist AFTER UPDATE OF artist on song FOR EACH ROW
BEGIN (
	UPDATE favorites SET artist = song.artist WHERE favorites.artist = old.artist;
	
	UPDATE album SET artist = song.artist WHERE album.artist = old.artist;
	
	UPDATE duplicates SET artist = song.artist WHERE duplicates.artist = old.artist;
	
	UPDATE contains SET artist = song.artist WHERE contains.artist = old.artist;
)
END; 

CREATE TRIGGER IF NOT EXISTS song.updateTitle AFTER UPDATE OF title on song FOR EACH ROW
BEGIN (
	UPDATE favorites SET title = song.title WHERE favorites.title = old.title;
	
	UPDATE album SET title = song.title WHERE album.title = old.title;
	
	UPDATE duplicates SET title = song.title WHERE duplicates.title = old.title;
	
	UPDATE contains SET title = song.title WHERE contains.title = old.title;
)
END; 

CREATE TRIGGER IF NOT EXISTS song.updateFiletype AFTER UPDATE OF filetype on song FOR EACH ROW
BEGIN (
	UPDATE favorites SET filetype = song.filetype WHERE favorites.filetype = old.filetype;
	
	UPDATE album SET filetype = song.filetype WHERE album.filetype = old.filetype;
	
	UPDATE duplicates SET filetype = song.filetype WHERE duplicates.filetype = old.filetype;
	
	UPDATE contains SET filetype = song.filetype WHERE contains.filetype = old.filetype;
)
END;

CREATE TRIGGER IF NOT EXISTS song.deleteSong BEFORE DELETE ON song
BEGIN (
	DELETE FROM album
	WHERE song.location = album.location and song.artist = album.artist and song.filetype = album.filetype and song.title = album.title;
	
	DELETE FROM favorites
	WHERE song.location = favorites.location and song.artist = favorites.artist and song.filetype = favorites.filetype and song.title = favorites.title;
	
	DELETE FROM duplicates
	WHERE song.location = duplicates.location and song.artist = duplicates.artist and song.filetype = duplicates.filetype and song.title = duplicates.title;
	
	DELETE FROM contains
	WHERE song.location = contains.location and song.artist = contains.artist and song.filetype = contains.filetype and song.title = contains.title;
)
END;

CREATE TRIGGER IF NOT EXISTS song.checkDuplicates AFTER INSERT ON song
BEGIN
	(
		INSERT INTO duplicates (location, artist, filetype, title)
		VALUES (
			SELECT location, artist, filetype, title AS duplicate
			FROM song
			WHERE song.location = duplicate.location and song.artist = duplicate.artist and song.filetype = duplicate.filetype and song.title = duplicate.title;
		)
	)
END;


CREATE TRIGGER IF NOT EXISTS playlist.updateName AFTER UPDATE OF pname on playlist
BEGIN
	(
	UPDATE contains SET pname = playlist.pname WHERE contains.pname = old.pname;
)
END;

CREATE TRIGGER IF NOT EXISTS playlist.deleteName AFTER DELETE ON playlist
BEGIN
	(
	DELETE FROM contains WHERE contains.pname = old.pname;
)
END;

/* Indexes/Indices*/

CREATE INDEX IF NOT EXISTS KeyIndex ON song (location, artist, filetype, title);
CREATE INDEX IF NOT EXISTS KeyIndex ON user (uid);

COMMIT;
