arr = ["hello", "world", "python"]
encode = ""
for i in range(len((arr))):
    a = str(len(arr[i]))+"#"
    encode += a+arr[i]
print(encode)
i=0
decode = []
j = 0
while i<len(encode):
    j=i
    while encode[j] != "#":
        j+=1
    length = int(encode[i:j])
    start = j+1
    end = start + length
    decode.append(encode[start:end])
    i=end
print(decode)




# if j!= "#":
