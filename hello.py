def summarize_orders():
    orders = [
    {"customer_id": 1, "amount": 500, "status": "completed"},
    {"customer_id": 1, "amount": 300, "status": "cancelled"},
    {"customer_id": 1, "amount": 800, "status": "completed"},
    {"customer_id": 2, "amount": 200, "status": "completed"},
    {"customer_id": 2, "amount": 100, "status": "completed"},
]
    summary = {}

    for order in orders:

        if order["status"] != "cancelled":

            customer = order["customer_id"]
            amount = order["amount"]

            if customer not in summary:
                summary[customer] = {
                    "count": 0,
                    "total": 0,
                    "highest": 0
                }

            summary[customer]["count"] += 1
            summary[customer]["total"] += amount

            if amount > summary[customer]["highest"]:
                summary[customer]["highest"] = amount

    return summary

print(summarize_orders())