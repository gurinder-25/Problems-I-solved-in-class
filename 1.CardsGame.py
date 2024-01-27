def card(piles):
  d, m = 0, 0
  d_turn = 0
  
  while piles:
    
    if d_turn:
    selected_pile = piles.pop(0) if piles[0]>piles[-1] else piles.pop()
    d+=selected_pile
    else:
      selected_pile = piles.pop(0) if piles[0]>piles[-1] else piles.pop()
      m+=selected_pile
      
    d_turn = not d_turn

  if d>m:
    return f"Dheeraj wins with {d-m} cards !"
  elif m>d:
    return f"Mansi wins with {m-d} cards !"
  else:
    return "Its a tie"


piles = list(map(int, input().split()))
result = card(piles)
print(result)

