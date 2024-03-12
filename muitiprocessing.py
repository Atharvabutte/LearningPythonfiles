import multiprocessing
import requests
import concurrent.futures


#  Code for getting download files
def downloadFile(url, name):
  print(f"Started Downloading {name}")
  response = requests.get(url)
  open(f"files/file{name}.jpg", "wb").write(response.content)
  print(f"Finished Downloading {name}")
 

if __name__ == '__main__':
 url = "https://picsum.photos/2000/3000"
    # pros = []
    # for i in range(1,11):
    # #    Multiprocssing Code
    #     p = multiprocessing.Process(target=downloadFile, args=[url, i])
    #     p.start()
    #     pros.append(p)

    # for p in pros:
    #   p.join()
 with concurrent.futures.ProcessPoolExecutor() as executor:
  l1 = [url for i in range(10)]
  l2 = [i for i in range(10)]
  results = executor.map(downloadFile, l1, l2)
  for r in results:
        print(r)
  