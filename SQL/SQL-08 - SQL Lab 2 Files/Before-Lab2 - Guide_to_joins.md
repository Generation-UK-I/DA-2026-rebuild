# Provide to learners before Lab 2

# SQL joins

SQL joins are the core mechanism for combining related data spread across multiple normalized tables. Mastering them transforms you from someone who queries single tables into someone who can extract complex insights from an entire relational database.

## The Core Join Types Explained

**INNER JOIN**:

- **The Logic**: Returns only the rows where there is a match in both tables. If a record exists in one table but has no matching partner in the other, it is completely excluded.
- **Analogy**: An exclusive club where you need a ticket (match in Table A) and a reservation (match in Table B) to enter.

**LEFT JOIN**:

- **The Logic**: Returns all rows from the left table, and the matched rows from the right table. If there is no match in the right table, the result returns NULL for the right table's columns.
- **Analogy**: A master guest list (Left Table). Everyone on the list is printed, and if they brought a plus-one (Right Table), their name is listed too; otherwise, the plus-one column is left blank.

**RIGHT JOIN**:

- **The Logic**: The exact mirror image of a Left Join. It returns all rows from the right table, and the matched rows from the left table (with NULLs where matches don't exist).
- **Usage Note**: Most developers prefer writing LEFT JOIN and swapping the table order because it feels more natural to read from left to right.

**FULL OUTER JOIN**:

- **The Logic**: Returns all records when there is a match in either the left or the right table. Rows that don't match on either side will show NULL values for the missing side.
- **Analogy**: Combining two different contact lists: you keep everyone from List A, everyone from List B, and merge the ones that overlap.

When writing a query involving two tables, ask yourself these three logical questions to pick the correct join:

1. Do I only care about records that have a direct relationship in both tables?

    Use: `INNER JOIN`

2. Do I want to keep every record from my primary (left) table, even if it has no related data in the secondary table?

    Use: `LEFT (OR RIGHT) JOIN`

3. Do I need to see everything from both sides simultaneously, capturing orphaned records on both ends?

    Use: `FULL OUTER JOIN`

## Working Through an Example

Imagine we have two tables...

**Product Table**:

|Product_ID|Product_Name|Price|
|---|---|---|
|1|Keyboard|35.00|
|2|Mouse|15.00|
|3|Monitor|180.00|
|4|Webcam|45.00|

**Orders Table**:

|Order_ID|Product_ID|Quantity|
|---|---|---|
|101|1|2|
|102|3|1|
|103|2|3|
|104|1|1|
|105|5|2|

A few important details:

- `products.product_id` uniquely identifies each product.
- `orders.order_id` uniquely identifies each order line in this example.
- `orders.product_id` tells us which product was purchased.
- Product_ID `1` appears twice in `orders`, because the keyboard was purchased in two separate orders.
- Product ID `5` appears in `orders`, but not in `products`. This is deliberately included to demonstrate how joins handle unmatched records.
- The webcam (product ID `4`) exists in `products` but has never been ordered.

In a real database, `products.product_id` would normally be a **primary key** and `orders.product_id` a **foreign key**. The unmatched ID `5` would typically be prevented by a foreign-key **constraint**, but it helps illustrate the join behaviour.

The business question - Suppose a manager asks:

"*Show me the name of every product that has been ordered, together with the order ID, quantity ordered, and price of the product.*"

Break the question down.

|Requirement|Where the data lives|
|---|---|
|Product name|products|
|Order ID|orders|
|Quantity ordered|orders|
|Product price|products|

**Step one**: Before choosing a join type, find the column that connects the two tables.

In our example, that is product_id.

`Product.Product_ID` **=** `Orders.Product_ID`

**Step two**: Decide which type of JOIN we need...

The manager asks for *every product* that has been ordered.

That means:

- Include products with matching order records.
- Exclude products that have never been ordered.
- Exclude orders that do not have a matching product record.

Therefore, the correct choice is an INNER JOIN.

**Step three**: Build the query incrementally

Rather than writing the entire query immediately, build it in small steps.

1. **Choose the columns**: We need the **product name**, **order ID**, **quantity**, and **product price**.

```sql
SELECT
    products.product_name,
    orders.order_id,
    orders.quantity,
    products.price
```

2. **Choose the starting table**: Since the question is about products that have been ordered, start with products.

```sql
SELECT
    products.product_name,
    orders.order_id,
    orders.quantity,
    products.price
FROM products
```

However, the `orders` table has not yet been brought into the query.

3. **Add the JOIN**: We now specify the second table and the type of join.

```sql
SELECT
    products.product_name,
    orders.order_id,
    orders.quantity,
    products.price
FROM products
INNER JOIN orders
```

SQL knows which tables we want to combine, but it still needs to know how to match their records.

4. **Add the matching condition**: We use `ON` to tell SQL which columns define a match.

```sql
SELECT
    products.product_name,
    orders.order_id,
    orders.quantity,
    products.price
FROM products
INNER JOIN orders
    ON products.product_id = orders.product_id;
```

That's the complete query.

**Result**:

|product_name|order_id|quantity|price|
|---|---|---|---|
|Keyboard|101|2|35.00|
|Monitor|102|1|180.00|
|Mouse|103|3|15.00|
|Keyboard|104|1|35.00|

The actual order may be different unless you add an `ORDER BY` clause.

If the manager instead asked: "*Show me every product and matching order details, include those products that have never been ordered.*"

In this case we must retain the webcam even though it has no orders. That means using a `LEFT JOIN`, with `products` on the left.

```sql
SELECT
    products.product_name,
    orders.order_id,
    orders.quantity,
    products.price
FROM products
LEFT JOIN orders
    ON products.product_id = orders.product_id;
```
