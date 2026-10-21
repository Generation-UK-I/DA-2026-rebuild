# SQL CASE Statements

The SQL CASE statement is your conditional logic tool inside a query; Essentially SQL’s version of an if-then-else statement.

It allows you to evaluate data row-by-row and return custom values, categorise information, or alter results dynamically without modifying the underlying database.

There are two ways to write a CASE statement depending on your needs:

- **Simple CASE** format compares a single expression or column against a list of specific static values.

- **Searched CASE** format evaluates a series of boolean expressions. It can handle ranges, multiple columns, and complex conditions (`>`, `<`, `AND`, `OR`).

```sql
/*Simple CASE*/

CASE column_name
    WHEN value1 THEN result1
    WHEN value2 THEN result2
    ELSE default_result
END

/*Searched CASE*/

CASE 
    WHEN condition1 THEN result1
    WHEN condition2 THEN result2
    ELSE default_result
END
```

We can use our `Products` table in the `sales_db` database to build a `CASE` statement from scratch.

The Original Table Data:

|ProductName|Price|
|---|---|
|Widget A|20.00|
|Widget B|30.00|
|Widget C|40.00|
|Widget D|50.00|

**Challenge**: We want to categorize each product into a Price Tier based on its price

- Under $35.00 --> "Budget"
- Between $35.00 and $45.00 --> "Standard"
- Anything else --> "Premium"

**Step 1**: Select the columns you want to display - We want to see the product name and its price alongside our new calculated category.

```sql
SELECT ProductName, Price
FROM Products
```

**Step 2**: Write the `CASE` logic block - We evaluate the Price column using `WHEN` conditions. SQL reads these top-to-bottom and stops at the first condition that matches.

```sql
CASE 
    WHEN Price < 35.00 THEN 'Budget'
    WHEN Price BETWEEN 35.00 AND 45.00 THEN 'Standard'
    ELSE 'Premium'
END
```

**Step 3**: Give the new column an alias - Just like using `AS` to alias math calculations or aggregate functions, we give our conditional column a clean name using `AS PriceCategory`.

**The Final Query**: Putting it all together, the complete query looks like this

```sql
SELECT 
    ProductName, 
    Price,
    CASE 
        WHEN Price < 35.00 THEN 'Budget'
        WHEN Price BETWEEN 35.00 AND 45.00 THEN 'Standard'
        ELSE 'Premium'
    END AS PriceCategory
FROM Products;
```

Expected Output:

|ProductName|Price|PriceCategory|
|---|---|---|
|Widget A|20.00|Budget|
|Widget B|30.00|Budget|
|Widget C|40.00|Standard|
|Widget D|50.00|Premium|

**Advanced**: Using CASE Inside Aggregate Functions - You can place a CASE statement inside functions like `SUM()` or `COUNT()` to count specific subsets of data in a single query without writing multiple `WHERE` clauses.

For example, counting how many products fall into each tier at once:

```sql
SELECT 
    SUM(CASE WHEN Price < 35.00 THEN 1 ELSE 0 END) AS BudgetCount,
    SUM(CASE WHEN Price >= 35.00 THEN 1 ELSE 0 END) AS NonBudgetCount
FROM Products;
```

## Learner Challenge

Setup:

- Use or re-create the `social_media_db` database from Lab1
- Create tables and populate them with data
- Review the user_data table.

Try to remember how to do this before reviewing the reminder below...

<details><summary>SQL code:</summary>

```sql
1. CREATE DATABASE social_media_db;
2. USE social_media_db;
3. SELECT DATABASES();
4. source C:\[LOCAL PATH TO FILES]\SQL-05 Lab 1\SQL-05 - SQL Lab 1 Files\table_creation.sql
5. SHOW TABLES;
5. SELECT * FROM user_data;
```

</details>

### Scenario

This scenario uses conditional logic in MySQL with the CASE statement, based on the `user_data` table.

We want to create a report that categorises users based on their follower count and post activity. Specifically, we want to:

- Label users as '**Influencer**' if they have more than 300 followers.
- Label users as '**Active User**' if they have more than 100 posts but are not influencers.
- Label users as '**Regular User**' if they don't meet either of the above conditions.

<details><summary>Hint:</summary>

Remember: Think of it like a loop - Although SQL doesn’t use visible loops, internally it behaves like one, for example, in Python we might write it like this...

```py
for each row in user_data:
    if Followers > 300:
        User_Category = 'Influencer'
    elif Posts > 100:
        User_Category = 'Active User'
    else:
        User_Category = 'Regular User'
```

</details>

<details><summary>Solution:</summary>

```sql
SELECT 
    User_ID,
    Account_Name,
    User_Name,
    Followers,
    Posts,
    CASE
        WHEN Followers > 300 THEN 'Influencer'
        WHEN Posts > 100 THEN 'Active User'
        ELSE 'Regular User'
    END AS User_Category
FROM user_data;
```

</details>

---

**Stretch and Challenge**: How would you modify the query to add a '**Special Influencer**' category for users with 400 or more followers, and where should this condition be placed?

Try to adapt your previous code to meet the challenge requirement before reviewing the solution below.

<details><summary>Solution:</summary>

```sql
SELECT 
    User_ID,
    Account_Name,
    User_Name,
    Followers,
    Posts,
    CASE
        WHEN Followers >= 400 THEN 'Special Influencer'  -- Check first for Special Influencer (400+ followers)
        WHEN Followers > 300 THEN 'Influencer'           -- Check next for Influencer (301-399 followers)
        WHEN Posts > 100 THEN 'Active User'              -- Check for Active Users based on posts
        ELSE 'Regular User'                              -- Default to Regular User
    END AS User_Category
FROM user_data;
```

</details>
