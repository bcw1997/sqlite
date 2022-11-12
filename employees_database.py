import sqlite3

connection = sqlite3.connect("employee.db")
cursor = connection.cursor()

# cursor.execute("""
#                CREATE TABLE employee_record(
#                     Id INTEGER PRIMARY KEY,
#                     first_name TEXT, 
#                     last_name TEXT, 
#                     date_started TEXT, 
#                     date_left TEXT, 
#                     dob TEXT)"""
#                 )

# cursor.execute("""
#                 CREATE TABLE hr_data_table (
#                     Id INTEGER PRIMARY KEY,
#                     Salary TEXT
#                 )    """)

employee_records = [
    (100, "John", "Smith", "01/01/1998", " ", "04/05/1978"),
    (101, "Jason", "State", "10/05/1998", "02/05/1999", "04/05/1978"),
    (102, "Brad", "Smith", "01/01/1998", "02/05/1999", "04/05/1978"),
    (103, "Peter", "Hudson", "01/01/2020", "10/25/2000 ", "04/05/1978"),
    (104, "Carrie", "East", "09/10/2000", " ", "04/05/1978"),
    (105, "Britney", "Code", "02/27/2001", " ", "04/05/1978"),
    (106, "Lisa", "Simpson", "07/05/2003", " ", "04/05/1978"),
    (107, "Adam", "Scott", "07/07/2003", " ", "04/05/1978"),
    (108, "Todd", "Howard", "08/05/2003", "11/11/2011 ", "04/05/1978"),   
]

hr_data = [
    (100,"320000"),
    (101,"0"),
    (102,"0"),
    (103,"0"),
    (104,"190000"),
    (105,"125000"),
    (106,"89000"),
    (107,"175000"),
    (108,"0")
]

cursor.executemany("INSERT INTO employee_record VALUES (?,?,?,?,?,?)", employee_records)
cursor.executemany("INSERT INTO hr_data_table VALUES (?,?)", hr_data)

for _ in cursor.execute("SELECT * FROM employee_record"):
    print(_)
    
for _ in cursor.execute("SELECT * FROM hr_data_table"):
    print(_)


inner_join = """
                SELECT er.Id, er.first_name, er.last_name, hr.salary 
                FROM employee_record as er
                INNER JOIN hr_data_table as hr
                ON er.Id = hr.ID
            """

cursor.execute(inner_join)

result = cursor.fetchall()
print('ID,\tFirst,\tLast,\tSalary')
for _ in result:
    print(_)
    
query = connection.execute("""
          SELECT er.Id, er.first_name, er.last_name, hr.salary 
                FROM employee_record as er
                INNER JOIN hr_data_table as hr
                ON er.Id = hr.ID
                WHERE first_name like 'L%'
          """)
for _ in query:
    print(_)


connection.close()