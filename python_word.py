#!/usr/bin/python

from optparse import OptionParser

def parse_cli():
    ''' CLI parser using OptionParser'''

    parser = OptionParser()
    parser.add_option('-d', '--debug',
                      dest='debug',
                      default=False,
                      help='Enable debug output',
                      action='store_true')
    parser.add_option('-F', '--filename',
                      dest='FILE',
                      default="word10k.txt",
                      help='File to use as dictionary file',
                      type='string',
                      action='store')
    parser.add_option('-P', '--pattern',
                      dest='pattern',
                      default="",
                      help='Pattern of word characters',
                      type='string',
                      action='store')

    return parser.parse_args()

(options, args) = parse_cli()
def check_word_length(word,pattern):
  if len(word) == int(len(pattern)):
    return True

def check_repeating_chars(word,pattern):
  #repeats = False (default) then skip any words with repeating chars
  #pattern = true and repeats = True, then look for only words which match the repetition pattern
  match_score = 0
  for i in range(len(word)):
     for j in range(len(word)): 
       if i != j :
         if word[i] == word[j]:
           if pattern[i] == pattern[j]:
             match_score = match_score
           else:
             match_score = match_score + 1
  if match_score == 0:
    return True 
  else:
    return False

with open(options.FILE) as f:
  for line in f:
    WORD = line.rstrip('\n').strip()
    if check_word_length(WORD,options.pattern) == True :
      if check_repeating_chars(WORD,options.pattern):
        print(WORD)
