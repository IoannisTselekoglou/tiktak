
def order(input_string):
  unique_order = []
  i = 0
  while i < len(input_string)-1:
    if input_string[i] != input_string[i+1]:
     unique_order.append(input_string[i])
    i += 1
  if input_string!= None and input_string[len(input_string)-1::] != unique_order[::-1]:
    unique_order.append(input_string[len(input_string)-1::])
  else:
    unique_order = input_string
  print(unique_order)
order("AAAABBBCCDAABBB")




#debuggen funktioniert noch nicht ganz wie erwartet diggah du musst das noch besser machen du nuttenkind
