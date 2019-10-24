import redis

r = redis.Redis()
regiset = "tasks"

while True:
    task = input("Please enter a task (enter if you want to stop) : ").lower()
    if not task:
        break
    r.sadd(regiset, task)
tasks = r.smembers(regiset)

print("Your current tasks are:")
for task in tasks:
    print(task.decode())

while True:
    task = input("Please enter a task that you have completed(enter if you want to stop) : ").lower()
    if not task:
        print("Your tasks have been saved. Thank you for using our todo list. Keep working!")
        break
    for t in tasks:
        r.srem(regiset, task)
