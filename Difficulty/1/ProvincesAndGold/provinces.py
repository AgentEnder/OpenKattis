gold, silver, copper = [int(x) for x in input().split()]
money = 3*gold+2*silver+copper
victory_cards = [ name for cost, name in {2:"Estate",5:"Duchy",8:"Province"}.items() if cost <= money ]
treasure_cards = [ name for cost, name in {0:"Copper",3:"Silver",6:"Gold"}.items() if cost <= money ]
if len(victory_cards) > 0:
	print(victory_cards[-1], "or", end=" ")
print(treasure_cards[-1])