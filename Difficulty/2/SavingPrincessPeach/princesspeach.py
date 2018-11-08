num_obstacles, num_counted = [int(x) for x in input().split()]
seen = set([int(input()) for i in range(num_counted)])
for i in range(num_obstacles):
	if i not in seen:
		print(i)
print("Mario got", len(seen), "of the dangerous obstacles.")
