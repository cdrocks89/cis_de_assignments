# calculate the capital gain/loss


SELECT
    stock_name,
    SUM(
        CASE
            WHEN operation = 'Sell' THEN price - prev_buy_price
            WHEN operation = 'Buy' THEN 0
        END
    ) AS capital_gain_loss
FROM (
    SELECT
        stock_name,
        operation,
        price,
        LAG(price, 1, 0) OVER (PARTITION BY stock_name ORDER BY operation_day) AS prev_buy_price
    FROM Stocks
) AS subquery
WHERE operation = 'Sell'
GROUP BY stock_name;
