import matplotlib.pyplot as plt
import psycopg2

username = 'Pedenko_Varvara'
password = '123'
database = 'db_lab3'
host = 'localhost'
port = '5432'


query_2a = """
        create or replace view number_average_rating as    
	        select trunc(average_rating) as rating_interval, count(*) as rating_count
	        from review
	        group by trunc(average_rating)
	        order by rating_interval;
    """

query_2b = """
        create or replace view top_5_language as
	        select 
		        case
			        when language in ('eng', 'spa', 'fre', 'en-US', 'en-GB') then language
			        else 'Other'
		        end as language_category,
		        count(*) as book_count from book
		        group by language_category;
    """

query_2c = """
        create or replace view number_book_year_publication as
	        select extract(year from data_publication) as publication_year, count(*) as book_count
	            from book
	            group by publication_year
	            order by publication_year;
    """


conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn, conn.cursor() as cursor:
    cursor.execute(query_2a)
    cursor.execute(query_2b)
    cursor.execute(query_2c)

    cursor.execute("SELECT * FROM number_average_rating;")
    data_2a = cursor.fetchall()

    cursor.execute("SELECT * FROM top_5_language;")
    data_2b = cursor.fetchall()

    cursor.execute("SELECT * FROM number_book_year_publication;")
    data_2c = cursor.fetchall()

# Plot 1: 
rating_intervals = [row[0] for row in data_2a]
rating_counts = [row[1] for row in data_2a]

plt.figure(figsize=(18, 6))  

plt.subplot(1, 3, 1)
bars = plt.bar(rating_intervals, rating_counts, width=0.8, align='center', color='skyblue')
plt.xlabel('Оцінковий інтервал')
plt.ylabel('Кількість оцінок')
plt.title('Гістограма оцінок')
plt.xticks(range(6))

for bar, value in zip(bars, rating_counts):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.05, f'{value}',
             ha='center', va='bottom')



# Plot 2:
languages = [row[0] for row in data_2b]
book_counts = [row[1] for row in data_2b]

plt.subplot(1, 3, 2)
plt.pie(book_counts, labels=languages, autopct='%1.1f%%', startangle=140)
plt.title('Частка книг для кожної мови (Топ-5 та інші)')

# Plot 3: 
years = [row[0] for row in data_2c]
book_counts = [row[1] for row in data_2c]

plt.subplot(1, 3, 3)
plt.plot(years, book_counts, marker='o')
plt.xlabel('Рік публікації')
plt.ylabel('Кількість книг')
plt.title('Залежність кількості книг від року публікації')
plt.grid(True)


plt.tight_layout() 
plt.show()
