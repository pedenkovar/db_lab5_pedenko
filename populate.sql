insert into author (id_author, name) values (1, 'J.K. Rowling');
insert into author (id_author, name) values (2, 'Mary GrandPré');
insert into author (id_author, name) values (3, 'W. Frederick Zimmerman');
insert into author (id_author, name) values (4, 'Madeleine L''Engle');
insert into author (id_author, name) values (5, 'Bill Bryson');
insert into author (id_author, name) values (6, 'John McPhee');
insert into author (id_author, name) values (7, 'J.R.R. Tolkien');

insert into book (isbn, title, data_publication, language) values (0439785960, 'Harry Potter and the Half-Blood Prince (Harry Potter #6)', TO_DATE('9/16/2006', 'MM/DD/YYYY'), 'eng');
insert into book (isbn, title, data_publication, language) values (0439358078, 'Harry Potter and the Order of the Phoenix (Harry Potter #5)', TO_DATE('9/1/2004', 'MM/DD/YYYY'), 'eng');
insert into book (isbn, title, data_publication, language) values (0439554896, 'Harry Potter and the Chamber of Secrets (Harry Potter #2)', TO_DATE('11/1/2003', 'MM/DD/YYYY'), 'eng');
insert into book (isbn, title, data_publication, language) values (0618346252, 'The Fellowship of the Ring (The Lord of the Rings #1)', TO_DATE('9/5/2003', 'MM/DD/YYYY'), 'eng');
insert into book (isbn, title, data_publication, language) values (0374519323, 'La Place de la Concorde Suisse', TO_DATE('4/1/1994', 'MM/DD/YYYY'), 'fre');
insert into book (isbn, title, data_publication, language) values (0374280398, 'Uncommon Carriers', TO_DATE('5/16/2006', 'MM/DD/YYYY'),'en-US');
insert into book (isbn, title, data_publication, language) values (0374522596, 'The Control of Nature', TO_DATE('9/1/1990', 'MM/DD/YYYY'),'en-US');
insert into book (isbn, title, data_publication, language) values (0606105263, 'Una arruga en el tiempo – A Wrinkle in Time', TO_DATE('6/1/1984', 'MM/DD/YYYY'),'spa');

insert into review (average_rating, text_reviews_count, ratings_count, isbn) values (4.57, 27591, 2095690, 0439785960);
insert into review (average_rating, text_reviews_count, ratings_count, isbn) values (4.49, 29221, 2153167, 0439358078);
insert into review (average_rating, text_reviews_count, ratings_count, isbn) values (4.42, 244, 6333, 0439554896);
insert into review (average_rating, text_reviews_count, ratings_count, isbn) values (4.36, 13670, 2128944, 0618346252);
insert into review (average_rating, text_reviews_count, ratings_count, isbn) values (3.92, 52, 698, 0374519323);
insert into review (average_rating, text_reviews_count, ratings_count, isbn) values (3.95, 203, 1630, 0374280398);
insert into review (average_rating, text_reviews_count, ratings_count, isbn) values (4.24, 305, 3498, 0374522596);
insert into review (average_rating, text_reviews_count, ratings_count, isbn) values (4.00, 1, 6, 0606105263);

insert into author_book (id_author, isbn) values (1, 0439785960);
insert into author_book (id_author, isbn) values (2, 0439785960);
insert into author_book (id_author, isbn) values (1, 0439358078);
insert into author_book (id_author, isbn) values (2, 0439358078);
insert into author_book (id_author, isbn) values (1, 0439554896);
insert into author_book (id_author, isbn) values (7, 0618346252);
insert into author_book (id_author, isbn) values (6, 0374519323);
insert into author_book (id_author, isbn) values (6, 0374280398);
insert into author_book (id_author, isbn) values (6, 0374522596);
insert into author_book (id_author, isbn) values (4, 0606105263);
