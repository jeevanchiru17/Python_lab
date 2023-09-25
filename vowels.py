vowels = 'aeiou'

ip_str = 'hello have you tried our tutorial section yet'
ip_str=ip_str.casefold()
count ={}.fromkeys(vowels,0)
for char in ip_str:
    if char in count:
        count[char]+=1
        print(count)