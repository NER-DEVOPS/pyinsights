from datetime import timedelta
from datetime import datetime

q = ""
with open("queries/all.yml") as r:
    q = r.read()
print(q)

delta = timedelta(days=-7)

now = datetime.now()

for x in range(1,10):
    end_date = now.date()
    now = now + delta
    start_date = now.date()
    with open("queries/all_{end_date}.yml".format(end_date=end_date),"w") as w:
        w.write(q.format(start_date=start_date, end_date=end_date))
