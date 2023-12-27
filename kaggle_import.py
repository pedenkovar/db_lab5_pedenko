import csv
import psycopg2
from datetime import datetime

username = 'Pedenko_Varvara'
password = '123'
database = 'db_lab3'

INPUT_CSV_FILE = 'books.csv'

query_drop_table = '''
    DROP TABLE IF EXISTS book CASCADE;
    DROP TABLE IF EXISTS author CASCADE;
    DROP TABLE IF EXISTS review CASCADE;
    DROP TABLE IF EXISTS author_book;
'''
query_create_table = '''
CREATE TABLE book
(
  ISBN CHAR(12) NOT NULL,
  title VARCHAR(10000) NOT NULL,
  data_publication DATE NOT NULL,
  language CHAR(10) NOT NULL,
  PRIMARY KEY (ISBN)
);

CREATE TABLE author
(
  id_author SERIAL PRIMARY KEY,
  name VARCHAR(10000) UNIQUE NOT NULL
);

CREATE TABLE review
(
  average_rating FLOAT NOT NULL,
  text_reviews_count INT NOT NULL,
  ratings_count INT NOT NULL,
  ISBN CHAR(12) NOT NULL,
  FOREIGN KEY (ISBN) REFERENCES book(ISBN)
);

CREATE TABLE author_book
(
  id_author INT NOT NULL,
  ISBN CHAR(12) NOT NULL,
  PRIMARY KEY (id_author, ISBN),
  FOREIGN KEY (id_author) REFERENCES author(id_author),
  FOREIGN KEY (ISBN) REFERENCES book(ISBN)
);
'''


query_1 = '''
INSERT INTO book (isbn, title, data_publication, language) VALUES (%s, %s, %s, %s)
'''
query_2 = '''
INSERT INTO author (name) VALUES (%s) RETURNING id_author
'''
query_3 = '''
INSERT INTO review (average_rating, text_reviews_count, ratings_count, isbn) VALUES (%s, %s, %s, %s)
'''
query_4 = '''
INSERT INTO author_book (id_author, isbn) VALUES (%s, %s)
'''

conn = psycopg2.connect(user=username, password=password, dbname=database)

with conn:
    cur = conn.cursor()
    cur.execute(query_drop_table)
    cur.execute(query_create_table)


    authors_id = {}

    with open(INPUT_CSV_FILE, 'r', encoding='utf-8') as inf:
        reader = csv.DictReader(inf)
        for idx, row in enumerate(reader):

            try:
                values_book = (
                row['isbn'],
                row['title'],
                datetime.strptime(row['publication_date'], '%m/%d/%Y'),
                row['language_code']
            ) 
            except ValueError:
                continue

            cur.execute(query_1, values_book)
            
            book_id = row['isbn']

            authors = set(row['authors'].split('/'))
            author_ids = []
            for author_name in authors:
                id_author = authors_id.get(author_name)
                if id_author is None:
                    cur.execute(query_2, (author_name,))
                    id_author = cur.fetchone()[0]
                    authors_id[author_name] = id_author
                cur.execute(query_4, (id_author, book_id))

            
            values_reviews = (row['average_rating'], row['text_reviews_count'], row['ratings_count'], row['isbn'])
            cur.execute(query_3, values_reviews)
            

    conn.commit()
