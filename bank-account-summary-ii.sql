# Write your MySQL query statement below
SELECT name,
    sum(amount) as balance
FROM Users
JOIN Transactions
    ON Transactions.account = Users.account
GROUP BY Transactions.account
HAVING sum(amount) > 10000;