PRAGMA foreign_keys=ON;
BEGIN TRANSACTION;

CREATE TABLE song(location TEXT, artist TEXT, filetype TEXT, title TEXT, genre TEXT, track INTEGER, album TEXT, bitrate INTEGER, year INTEGER, month INTEGER, PRIMARY KEY(location, artist, filetype, title));

CREATE TABLE user(uid INTEGER PRIMARY KEY ASC, uname TEXT);

CREATE TABLE contains(pname TEXT, location TEXT, artist TEXT, filetype TEXT, title TEXT, FOREIGN KEY(pname) references playlist(pname), FOREIGN KEY(location, artist, filetype, title) references song(location, artist, filetype, title));

CREATE TABLE favorites(uid INTEGER PRIMARY KEY ASC, location TEXT, artist TEXT, filetype TEXT, title TEXT, FOREIGN KEY(location, artist, filetype, title) references song(location, artist, filetype, title));

CREATE TABLE duplicates(location TEXT, artist TEXT, filetype TEXT, title TEXT, duplicate_location TEXT PRIMARY KEY, FOREIGN KEY(location, artist, filetype, title) references song(location, artist, filetype, title));

CREATE TABLE playlist(pname TEXT PRIMARY KEY, uid INTEGER, count INTEGER, FOREIGN KEY(uid) references user(uid));

CREATE TABLE album(location TEXT, artist TEXT, filetype TEXT, title TEXT, album_art_filename TEXT PRIMARY KEY, track_count INTEGER, FOREIGN KEY(location, artist, filetype, title) references song(location, artist, filetype, title));

COMMIT;
