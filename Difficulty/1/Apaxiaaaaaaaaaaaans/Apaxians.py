in_stream = input()
print("".join([x for idx,x in enumerate(list(in_stream)) if idx == 0 or in_stream[idx-1] != x]))