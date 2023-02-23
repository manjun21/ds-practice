
def find_substring(str1, pattern):
  # TODO: Write your code here
  win_start = 0
  pattern_char_freq = {}
  smallest_str = ""
  
        
  for win_end in range(len(str1)):
    
    for p in pattern:
        if p in pattern_char_freq:
          pattern_char_freq[p] = pattern_char_freq[p] +1
        else:
          pattern_char_freq[p] = 1

    if str1[win_end] in pattern_char_freq:
      k = win_end
      print('k'+str(k))
      while len(pattern_char_freq) > 0 and k < len(str1):    
        print(k)
        print(pattern_char_freq)
        if str1[k] in pattern_char_freq:
          pattern_char_freq[str1[k]] = pattern_char_freq[str1[k]] - 1
          if pattern_char_freq[str1[k]] == 0:
            del pattern_char_freq[str1[k]]
        k = k +1
      
      print('pattern_char_freq:'+str(pattern_char_freq))
      if len(pattern_char_freq) == 0:
        # match found
        print(str1[win_start:k])
        if smallest_str== "":
            smallest_str =  str1[win_start:k]
        elif len(str1[win_start:k]) < len(smallest_str):
            smallest_str = str1[win_start:k]

    print('smallest_str:'+smallest_str)      

    win_start = win_start +1

  print('----')

  return smallest_str

def main():
  #print(find_substring("aabdec", "abc"))
#   print(find_substring("aabdec", "abac"))
 print(find_substring("abdbca", "abc"))
#   print(find_substring("adcad", "abc"))

main()