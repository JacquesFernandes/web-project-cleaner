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
  parser.add_argument('start', help="Base directory to start searching from", nargs='?', default=os.getcwd())
  parser.add_argument('-v', '--verbose', help="Make execution more verbose", nargs='?', default=False)
  args = parser.parse_args()
  
  root_path = searcher.getFullQualifiedPath(args.start)
  print('Search root:', root_path)

  verbose = True if args.verbose is None else False
  print("verbose?", verbose)

  if root_path is None:
    print("Invalid path:", args.start)
    exit()

  paths = []
  curr_path = root_path

  if verbose:
    print("---")

  results = []

  for path in searcher.searchForTerms(root_path, check_for_names):
    if verbose:
      print(path)
    results.append(path)

  if verbose:
    print("---")

  print("number of results:", len(results))

  pass