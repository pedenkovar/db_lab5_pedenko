CREATE TABLE book
(
  ISBN INT NOT NULL,
  title VARCHAR(100) NOT NULL,
  data_publication DATE NOT NULL,
  language CHAR(10) NOT NULL,
  PRIMARY KEY (ISBN)
);

CREATE TABLE author
(
  id_author INT NOT NULL,
  name VARCHAR(50) NOT NULL,
  PRIMARY KEY (id_author)
);

CREATE TABLE review
(
  average_rating FLOAT NOT NULL,
  text_reviews_count INT NOT NULL,
  ratings_count INT NOT NULL,
  ISBN INT NOT NULL,
  FOREIGN KEY (ISBN) REFERENCES book(ISBN)
);

CREATE TABLE author_book
(
  id_author INT NOT NULL,
  ISBN INT NOT NULL,
  PRIMARY KEY (id_author, ISBN),
  FOREIGN KEY (id_author) REFERENCES Author(id_author),
  FOREIGN KEY (ISBN) REFERENCES book(ISBN)
);