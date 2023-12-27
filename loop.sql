DO $$ 
DECLARE
    languages TEXT[] := ARRAY['eng', 'spa', 'fre', 'en-US', 'en-GB'];
    
BEGIN
	FOR i in 1..20
    	LOOP
        	INSERT INTO book (ISBN, title, data_publication, language)
        	VALUES (100000000 + i, 'Test Book ' || i, CURRENT_DATE - INTERVAL '7 days' * i,
            languages[i % array_length(languages, 1) + 1]);

    	END LOOP;
END;
$$;

select * from book;




