#!usr/bin/python2.6

from mrjob.job import MRJob

class MRWordCounter(MRJob):
    OUTPUT_PROTOCOL = JSONValueProtocol
    def mapper(self, _, url):
      r = requests.get(url)
      if r.status_code==200:
        response = 1
      else:
        response = 0
      yield url, {"url":url, "response":response, "content":r.content}

if __name__ == '__main__':
    MRWordCounter.run()