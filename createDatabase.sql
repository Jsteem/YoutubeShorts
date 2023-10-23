

CREATE TABLE Quotes (
    QuoteID SERIAL PRIMARY KEY,
    QuoteText TEXT UNIQUE,
	QuoteHeading TEXT,
    BackgroundID INTEGER,
    MusicClipID INTEGER
);

CREATE TABLE Backgrounds (
    BackgroundID SERIAL PRIMARY KEY,
	BackgroundSiteId INT UNIQUE,
	BackgroundDuration INT,
	BackgroundMaker TEXT,
    BackgroundLink TEXT,
	BackgroundQuery TEXT,
	QuoteID INT,
    Width INT,
	Height INT,
    FOREIGN KEY (QuoteID) REFERENCES Quotes (QuoteID)
);


CREATE TABLE Music (
    MusicID SERIAL PRIMARY KEY,
	MusicPreviewLink TEXT,
    MusicSiteId TEXT UNIQUE,
	MusicTitle TEXT,
	MusicArtist TEXT,
	MusicQuery TEXT,
	QuoteID INT,
    FOREIGN KEY (QuoteID) REFERENCES Quotes (QuoteID)
);
