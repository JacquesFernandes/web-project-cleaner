import os
from typing import List

from search_result import SearchResult

def getFullQualifiedPath(given_path:str) -> str:
  given_path = os.path.normpath(given_path)
  if os.path.exists(given_path) is False:
    return None
  return os.path.realpath(given_path)

def searchForTerms(path:str, search_terms:List[str]):
  for path, directories, files in os.walk(path):
    for search_term in search_terms:
      if search_term in directories or search_term in files:
        new_path = os.path.join(path, search_term)
        if new_path.count(search_term) == 1:
          yield new_path
