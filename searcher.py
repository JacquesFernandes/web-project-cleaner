import os
import subprocess
from typing import List

from search_result import SearchResult

def kb2mb(kb:int)->float:
  return kb/(1024 ** 1)

def kb2gb(kb:int)->float:
  return kb/(1024 ** 2)

def getFullQualifiedPath(given_path:str) -> str:
  given_path = os.path.normpath(given_path)
  if os.path.exists(given_path) is False:
    return None
  return os.path.realpath(given_path)

def getSize(path:str)->int:
  res = subprocess.run(['du', '-d 0', path], stdout=subprocess.PIPE)
  converted_res = res.stdout.decode('utf-8')
  size = int(converted_res.split()[0])
  return size

def systemForceDelete(path:str):
  subprocess.run(['rm', '-r', '-d', '-f', '-v', path])
  return

def searchForTerms(path:str, search_terms:List[str], verbose=False):
  num_results=0
  for path, directories, files in os.walk(path):
    for search_term in search_terms:
      if search_term in directories or search_term in files:
        new_path = os.path.join(path, search_term)
        if new_path.count(search_term) == 1:
          num_results += 1
          if verbose:
            print("found %d results" % (num_results), end='\r', flush=True)
          yield new_path
  print("") # force a new line


def getOptimalHumanSize(kb:int) -> str:
  gb = kb2gb(kb)
  if gb >= 0:
    return '{:.2f} GB'.format(gb)

  mb = kb2mb(kb)
  if mb >= 0:
    return '{:.2f} MB'.format(mb)
    
  return '{} KB'.format(kb)
