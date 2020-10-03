import os
from typing import List

class SearchResult:
  def __init__(self, path:str, size:int):
    self.path=path
    self.size=size

  def __str__(self) -> str:
    return 'path: {} \n size: {}'.format(self.path, self.size)