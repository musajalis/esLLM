### Expanding Scope LLM ###

import statistics
import numpy as np

input = "And now, I said, let me show in a figure \
how far our nature is enlightened or unenlightened: \
Behold! human beings living in an underground den, \
which has a mouth open towards the light and reaching \
all along the den; here they have been from their \
childhood, and have their legs and necks chained so \
that they cannot move, and can only see before them, \
being prevented by the chains from turning round their \
heads. Above and behind them a fire is blazing at a \
distance, and between the fire and the prisoners there \
is a raised way; and you will see, if you look, a low \
wall built along the way, like the screen which marionette \
players have in front of them, over which they show the \
puppets."

def prevWordSelect(input, wordcount):
  charTime = -1
  char = input[charTime]
  while wordcount > 0:
    while char != " ":
      if char == "." or char == "," or char == "!" or char == "?":
        charTime -= 1
        if abs(charTime) >= len(input):
          return input
        char = input[charTime]
        continue
      else:
        if abs(charTime) >= len(input):
          return input
        charTime -= 1
        char = input[charTime]
    wordcount -= 1
    if abs(charTime) >= len(input):
      return input
    charTime -= 1
    char = input[charTime]
  return input[charTime+2:]

def prevSet(input, wordScope):
  output = []
  output.append(input[-1])
  limit = len(input.split())
  for i in wordScope:
    if i == 0:
      continue
    if i > limit:
      break
    selection = prevWordSelect(input, i)
    output.append(selection)
  return output

def asciiSet(wordSet):
  asciiValueSet = []
  for word in wordSet:
    asciiValueSet.append(sum(ord(char) for char in word))
  return asciiValueSet

def expVal(arr):
  if len(arr) == len(set(arr)):
    return statistics.median_low(arr)
  else:
    return statistics.mode(arr)

def esllm(input, wordScope, probMatrix):
  wordSet = prevSet(input, wordScope)
  wordSet = asciiSet(wordSet)
  outputPredSet = []
  for i in range(len(probMatrix)):
    pred = np.matmul(wordSet[i], probMatrix[i])
    outputPredSet.append(chr(pred))
  return expVal(outputPredSet)

wordScope = [0, 1, 2, 3, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]


