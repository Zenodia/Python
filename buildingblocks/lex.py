#get lexical diversity, but first one must summarize the text data to one record per row

def lexical_diversity(text):
  if len(text) == 0:
    diversity = 0
  else: 
   diversity = float(len(set(text))) / len(text)
  return diversity

# how to call the function
#diversity=groupedrecord.apply(lexical_diversity)
