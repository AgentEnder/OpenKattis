#Hissing Microphone, OpenKattis, https://open.kattis.com/problems/hissingmicrophone
#Sln by Craigory Coppola
in_str = input()
for chr_idx in range(len(in_str)-1):
	if in_str[chr_idx] == "s" and in_str[chr_idx+1] == "s":
		print("hiss")
		break
else:
	print("no hiss")