OSU CS261 Data Structures projec

Part 1: Hash Map

First, complete the hash map implementation by using the skeleton code provided below. This hash map uses a hash table of buckets, each containing a linked list of hash links. Each hash link stores the key-value pair (string and integer in this case) and a pointer to the next link in the list. See the Programming Assignment 5 GuidelinesPreview the document for additional method descriptions. Use the provided unit tests to help debug any failing test cases on GradeScope. You are encouraged to write additional unit tests, however, you are not permitted to share any additional tests with other students.   

    Class Student
        clear() (5pts)
        get(key) (5pts)
        resize_table(capacity) (15 pts)
        put(key, value) (10 pts)
        remove(key) (8pts)
        contains_key(key) (6 pts)
        empty_buckets() (6 pts)
        table_load() (5pts)

Part 2: Concordance

Once you have your hash map working properly, you can start to build your concordance program. Word_count.py takes an input document, computes the number of times each word was used in the document, and returns the top X words and associated counts. We have provided you with the code to take an input document and read in each word. From there, you must store each word in a hash table and keep track of how many times the word appears.

Top_words() should return a list of tuples: [(top word, count), (next top word, count)]. See the skeleton code and  input document below to get started. 

Use the provided unit tests to help debug any failing test cases on GradeScope. Again, you are encouraged to write additional unit tests, however, you are not permitted to share any additional tests with other students.   
