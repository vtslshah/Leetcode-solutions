Select month, revenue,
    lag(revenue) over (order by month) as previous_month_revenue,
    ( ((revenue - lag(revenue) over (order by month)) / (lag(revenue) over (order by month))) * 100) as growth_percentage
from 