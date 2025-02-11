import sqlite3

# Establishing connection
conn = sqlite3.connect('northwind_small.sqlite3')

curs = conn.cursor()

# Queries Part 2 With Outputs
# Question 1:
"""What are the top ten most expensive items in the database?")"""
curs.execute("""
SELECT ProductName, UnitPrice 
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10
""").fetchall()
"""
[('Côte de Blaye', 263.5),
 ('Thüringer Rostbratwurst', 123.79),
 ('Mishi Kobe Niku', 97),
 ("Sir Rodney's Marmalade", 81),
 ('Carnarvon Tigers', 62.5),
 ('Raclette Courdavault', 55),
 ('Manjimup Dried Apples', 53),
 ('Tarte au sucre', 49.3),
 ('Ipoh Coffee', 46),
 ('Rössle Sauerkraut', 45.6)]
"""

# Question 2:
"""What is the average age of an employee at the time of their hiring?"""
curs.execute("""
SELECT AVG(HireDate - BirthDate) 
FROM Employee
""").fetchall()
"""[(37.22222222222222,)]"""

# Question 3: Stretch
"""How does the average age of employee at hire vary by city?"""
curs.execute("""
SELECT City, AVG(HireDate - BirthDate) 
FROM Employee
GROUP BY City
""").fetchall()
"""
[('Kirkland', 29.0),
 ('London', 32.5),
 ('Redmond', 56.0),
 ('Seattle', 40.0),
 ('Tacoma', 40.0)]
"""

# Queries Part 3 With Outputs
# Question 1:
"""What are the ten most expensive items in the database and their suppliers?"""
curs.execute("""
SELECT ProductName, UnitPrice, CompanyName 
FROM Product
LEFT JOIN Supplier
ON SupplierID
ORDER BY UnitPrice DESC
LIMIT 10
""").fetchall()
## Added Post Submission 
# Côte de Blaye  :  263.5  :  Aux joyeux ecclésiastiques
# Thüringer Rostbratwurst  :  123.79  :  Plutzer Lebensmittelgroßmärkte AG
# Mishi Kobe Niku  :  97  :  Tokyo Traders
# Sir Rodney's Marmalade  :  81  :  Specialty Biscuits, Ltd.
# Carnarvon Tigers  :  62.5  :  Pavlova, Ltd.
# Raclette Courdavault  :  55  :  Gai pâturage
# Manjimup Dried Apples  :  53  :  G'day, Mate
# Tarte au sucre  :  49.3  :  Forêts d'érables
# Ipoh Coffee  :  46  :  Leka Trading
# Rössle Sauerkraut  :  45.6  :  Plutzer Lebensmittelgroßmärkte AG
# Question 2:
"""What is the largest category (by number of unique products 
in it)?"""
curs.execute("""
SELECT CategoryName, COUNT(DISTINCT ProductName) as Count
FROM Product
LEFT JOIN Category
ON Product.CategoryID = Category.ID 
GROUP BY CategoryName
ORDER BY Count DESC
LIMIT 1
""").fetchall()
"""[('Confections', 13)]"""

# Question 3:
"""
Who's the employee with the most territories? Use TerritoryId (not name, region, 
or other fields) as the unique identifier for territories.)"""
curs.execute("""
SELECT FirstName, COUNT(TerritoryId) as Count
FROM Employee
LEFT JOIN EmployeeTerritory
ON Employee.ID = EmployeeTerritory.EmployeeID 
GROUP BY EmployeeID
ORDER BY Count DESC
LIMIT 1
""").fetchall()
"""[('Robert', 10)]"""

