CREATE TABLE "Anime" (
	"AnimeID"	INTEGER NOT NULL UNIQUE,
	"Name"	TEXT NOT NULL,
	"Start"	TEXT,
	"End"	TEXT,
	"Episodes"	INTEGER NOT NULL,
	"Synopsis"	TEXT,
	PRIMARY KEY("AnimeID" AUTOINCREMENT)
);

CREATE TABLE "AnimeGenre" (
	"AnimeID"	INTEGER NOT NULL,
	"Genre"	TEXT NOT NULL,
	FOREIGN KEY("AnimeID") REFERENCES "Anime"("AnimeID"),
	PRIMARY KEY("AnimeID","Genre")
);

CREATE TABLE "User" (
	"UserID"	INTEGER NOT NULL UNIQUE,
	"Username"	TEXT NOT NULL UNIQUE,
	"Gender"	TEXT NOT NULL CHECK("Gender" = "M" OR "Gender" = "F"),
	PRIMARY KEY("UserID" AUTOINCREMENT)
);

CREATE TABLE "Recommendation" (
	"UserID"	INTEGER NOT NULL,
	"AnimeID"	INTEGER NOT NULL,
	"Date"	TEXT NOT NULL,
	"Rating"	INTEGER NOT NULL,
	"Comment"	TEXT NOT NULL,
	"SimilarAnime"	INTEGER NOT NULL,
	FOREIGN KEY("UserID") REFERENCES "User"("UserID"),
	FOREIGN KEY("AnimeID") REFERENCES "Anime"("AnimeID"),
	FOREIGN KEY("SimilarAnime") REFERENCES "Anime"("AnimeID"),
	PRIMARY KEY("UserID","AnimeID")
)