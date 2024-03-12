import threading
import time
from concurrent.futures import ThreadPoolExecutor

def City_name(name):
    print(f"You live in this city {name}")
    time.sleep(5)
    print(f"this is threading")
    return 10
    

# time1 = time.perf_counter()
# t1 = threading.Thread(target=City_name,args=["Mumbai"])
# t2 = threading.Thread(target=City_name,args=["Pune"])
# t3 = threading.Thread(target=City_name,args=["Ghatkopar"])

# t1.start()
# t2.start()
# t3.start()


# # t1.join()
# # t2.join()
# # t3.join()

# time2 = time.perf_counter()
# print( time2 - time1)

def polling_executer():
    with ThreadPoolExecutor() as executor:
        l = ["Mumbai","Pune","Dehli","Panjab"]
        results = executor.map(City_name, l)
        for result in results:
            print(result)

polling_executer()