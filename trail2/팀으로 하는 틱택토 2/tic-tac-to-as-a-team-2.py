from collections import Counter

inp = [input() for _ in range(3)]

# Please write your code here.

def find_win_team(case):
    return sorted(list(Counter(case).keys()))

search_list = []

for row in range(3):
    line_x = []
    line_y = []
    for col in range(3):

        line_x.append(inp[row][col])
        line_y.append(inp[col][row])
    
    if line_x not in search_list:
        search_list.append(line_x)
        
    if line_y not in search_list:
        search_list.append(line_y)
    

if [inp[0][0], inp[1][1], inp[2][2]] not in search_list:
    search_list.append([inp[0][0], inp[1][1], inp[2][2]]) 

if [inp[0][2], inp[1][1], inp[2][0]] not in search_list:
    search_list.append([inp[0][2], inp[1][1], inp[2][0]])

result = 0

team_list = []

for item in search_list:

    win_team = find_win_team(item)

    if  win_team not in team_list and len(win_team) == 2:
        team_list.append(win_team)
        
        

print(len(team_list))
