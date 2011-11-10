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
	uid INTEGER PRIMARY KEY AUTOINCREMENT,
	uname TEXT,
	password TEXT
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
	uid INTEGER,
	location TEXT,
	artist TEXT,
	filetype TEXT,
	title TEXT,
	FOREIGN KEY(location, artist, filetype, title) references song(location, artist, filetype, title),
	FOREIGN KEY(uid) references user(uid)
);

CREATE TABLE duplicates(
	location TEXT,
	artist TEXT,
	filetype TEXT,
	title TEXT,
	--duplicate_location TEXT PRIMARY KEY,
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

CREATE TRIGGER updateLocation AFTER UPDATE OF location on song FOR EACH ROW
BEGIN
	UPDATE favorites SET location = new.location WHERE favorites.location = old.location;
	UPDATE album SET location = new.location WHERE album.location = old.location;
	UPDATE duplicates SET location = new.location WHERE duplicates.location = old.location;
	UPDATE contains SET location = new.location WHERE contains.location = old.location;
END; 

CREATE TRIGGER updateArtist AFTER UPDATE OF artist on song FOR EACH ROW
BEGIN
	UPDATE favorites SET artist = new.artist WHERE favorites.artist = old.artist;
	UPDATE album SET artist = new.artist WHERE album.artist = old.artist;
	UPDATE duplicates SET artist = new.artist WHERE duplicates.artist = old.artist;
	UPDATE contains SET artist = new.artist WHERE contains.artist = old.artist;
END; 

CREATE TRIGGER updateTitle AFTER UPDATE OF title on song FOR EACH ROW
BEGIN
	UPDATE favorites SET title = new.title WHERE favorites.title = old.title;
	UPDATE album SET title = new.title WHERE album.title = old.title;
	UPDATE duplicates SET title = new.title WHERE duplicates.title = old.title;
	UPDATE contains SET title = new.title WHERE contains.title = old.title;
END; 

CREATE TRIGGER updateFiletype AFTER UPDATE OF filetype on song FOR EACH ROW
BEGIN
	UPDATE favorites SET filetype = new.filetype WHERE favorites.filetype = old.filetype;
	UPDATE album SET filetype = new.filetype WHERE album.filetype = old.filetype;
	UPDATE duplicates SET filetype = new.filetype WHERE duplicates.filetype = old.filetype;
	UPDATE contains SET filetype = new.filetype WHERE contains.filetype = old.filetype;
END;

CREATE TRIGGER deleteSong BEFORE DELETE ON song FOR EACH ROW
BEGIN
	DELETE FROM album
	WHERE new.location = album.location and new.artist = album.artist and new.filetype = album.filetype and new.title = album.title;
	DELETE FROM favorites
	WHERE new.location = favorites.location and new.artist = favorites.artist and new.filetype = favorites.filetype and new.title = favorites.title;
	DELETE FROM duplicates
	WHERE new.location = duplicates.location and new.artist = duplicates.artist and new.filetype = duplicates.filetype and new.title = duplicates.title;
	DELETE FROM contains
	WHERE new.location = contains.location and new.artist = contains.artist and new.filetype = contains.filetype and new.title = contains.title;
END;

CREATE TRIGGER checkDuplicates AFTER INSERT ON song FOR EACH ROW
BEGIN
	INSERT INTO duplicates (location, artist, filetype, title)
		SELECT location, artist, filetype, title
		FROM song
		WHERE artist = new.artist
			and filetype = new.filetype
			and title = new.title
			and location <> new.location;
END;


CREATE TRIGGER updateName AFTER UPDATE OF pname on playlist FOR EACH ROW
BEGIN
	UPDATE contains SET pname = playlist.pname WHERE contains.pname = old.pname;
END;

CREATE TRIGGER deleteName AFTER DELETE ON playlist FOR EACH ROW
BEGIN
	DELETE FROM contains WHERE contains.pname = old.pname;
END;

/* Indexes/Indices*/

CREATE INDEX KeyIndex ON song (location, artist, filetype, title);
CREATE INDEX UserIndex ON user (uid);
CREATE INDEX SongIndex on song(genre, track, album,	bitrate);

COMMIT;
