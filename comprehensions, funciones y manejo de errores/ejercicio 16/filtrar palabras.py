def filter_by_length(words):
   new = list(filter(lambda w: len(w)>=4, words))
   return new

words = ['amor', 'sol', 'piedra', 'día']
response = filter_by_length(words)
print(response)