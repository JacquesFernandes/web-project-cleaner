#! /usr/bin/python3

import argparse
import os

import searcher

check_for_names = [
  'node_modules',
  'vendor'
]

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('start', help="base directory to start searching from", nargs='?', default=os.getcwd())
  # parser.add_argument('-d', '--depth', help="Max depth to check", type=int, nargs='?', default=None)
  args = parser.parse_args()
  
  print('Search root:', args.start)
  root_path = searcher.getFullQualifiedPath(args.start)

  # print('Max depth:', args.depth)
  # max_depth = args.depth

  if root_path is None:
    print("Invalid path:", args.start)
    exit()

  paths = []
  curr_path = root_path


  print("---")

  results = []

  for path in searcher.searchForTerms(root_path, check_for_names):
    print(path)
    results.append(path)

  print("---")

  print("number of results:", len(results))

  pass