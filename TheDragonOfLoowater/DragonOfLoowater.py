import sys

while True:
    line = sys.stdin.readline() #Get first line of each case
    line_split = line.split(" ") #split into array of heads,height
    num_heads = int(line_split[0]) #Get nums
    num_heights = int(line_split[1]) #Get nums
    if num_heights == 0 and num_heads == 0: #No more test cases
        break #Stop Algorithm
    heads = [] #Array for nums heads
    heights = [] #Array for nums heights
    for i in range(num_heads):
        heads.append(int(sys.stdin.readline())) #Get each head listed and add to list
    heads.sort() #Sort list of heads in ascending order
    for i in range(num_heights):
        heights.append(int(sys.stdin.readline())) #Get each height listed
    heights.sort()
    if len(heads) > len(heights): #less knights than heads, each night can only kill one dragon, loowater doomed
        print("Loowater is doomed!")
    else:
        heads_idx = 0 #Next dragon to slay
        heights_idx = 0 #Next possible night to slay dragon
        total_cost = 0 #Expenditure to loowater
        while heads_idx < len(heads) and heights_idx < len(heights): #Loop  until out of dragons or out of heads
            if heads[heads_idx] <= heights[heights_idx]: #Dragon killed
                total_cost += heights[heights_idx] #Add knight price
                heads_idx += 1 #Move to next dragon
            heights_idx += 1 #Move to next knight (Regardless of if dragon changes)
        if heads_idx >= len(heads): #Killed all dragons
            print(total_cost)
        else: #Doom
            print("Loowater is doomed!")
