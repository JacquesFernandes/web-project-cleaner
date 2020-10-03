#! /usr/bin/python3

import argparse
import os

import searcher
from search_result import SearchResult

check_for_names = [
  'node_modules',
  'vendor'
]

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('start', help="Base directory to start searching from", nargs='?', default=os.getcwd())
  parser.add_argument('-v', '--verbose', help="Make execution more verbose", nargs='?', default=False)
  parser.add_argument('-o', '--output', help="Output paths to a file", nargs='?', default=None)
  args = parser.parse_args()
  
  root_path = searcher.getFullQualifiedPath(args.start)
  print('Search root:', root_path)

  verbose = True if args.verbose is None else False
  print("verbose?", verbose)

  output_file_name = args.output
  print("Output File:", output_file_name)

  if root_path is None:
    print("Invalid path:", args.start)
    exit()

  paths = []
  curr_path = root_path

  if verbose:
    print("---")

  results = []

  for path in searcher.searchForTerms(root_path, check_for_names, verbose=verbose):
    result = SearchResult(path, searcher.getSize(path))
    results.append(result)

  if output_file_name != None:
    with open(output_file_name, 'w+') as output_file:
      output_file.writelines([ result.path+'\n' for result in results ])

  if verbose:
    print("---")

  total= sum(result.size for result in results)

  print("number of results:", len(results))
  print("total size:", searcher.getOptimalHumanSize(total))

  delete = True if input("Delete? [y/n]: ").lower() == 'y' else False
  if delete:
    for result in results:
      searcher.systemForceDelete(result.path)

  print("Done!")

  pass