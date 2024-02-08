import psutil
#print(psutil.cpu_times())
#blocking
#print(psutil.cpu_percent(interval=1))
# non-blocking (процент с момента последнего звонка)
#print(psutil.cpu_percent(interval=None))
#блокировка, pet-cpu
#print(psutil.cpu_percent(interval=1, percpu=True))

#print(psutil.cpu_times_percent(interval=None, percpu=False))

print(psutil.cpu_count())
print(psutil.cpu_count(logical=True))
print(psutil.cpu_count(logical=False))