SELECT c.login, COUNT(o.id)
FROM "Orders" AS o
    JOIN "Couriers" AS c ON o."courierId" = c.id
WHERE o."inDelivery" = True
GROUP BY c.login;