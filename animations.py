# These are commonly used tuple values for RBG colors
b = (0,0,255)
w = (255,255, 255)
y = (255, 255, 0)
g = (0, 255, 0)
lb = (173, 216, 230)
bk = (0, 0, 0)
gr = (134, 136, 138)

# Lines 11-163 are different frames for the animations
rain = [
  bk, bk, bk, bk, bk, y, y, y,
  bk, bk, w, w, w, w, y, y,
  bk, w, w, w, w, w, w, y,
  w, w, w, w, w, w, w, w,
  lb, bk, lb, bk, lb, bk, lb, bk,
  bk, lb, bk, lb, bk, lb, bk, lb,
  lb, bk, lb, bk, lb, bk, lb, bk,
  g, g, g, g, g, g, g, g,
]

rain2 = [
  bk, bk, bk, bk, bk, y, y, y,
  bk, bk, w, w, w, w, y, y,
  bk, w, w, w, w, w, w, y,
  w, w, w, w, w, w, w, w,
  bk, lb, bk, lb, bk, lb, bk, lb,
  lb, bk, lb, bk, lb, bk, lb, bk,
  bk, lb, bk, lb, bk, lb, bk, lb,
  g, g, g, g, g, g, g, g,
]

clear_skies = [
  b, b, b, b, b, y, y, y,
  b, b, b, b, b, y, y, y,
  b, b, b, b, b, y, y, y,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  g, g, g, g, g, g, g, g
]

clear_skies2 = [
  b, b, b, b, b, y, y, y,
  w, w, b, b, b, y, y, y,
  w, w, b, b, b, y, y, y,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  g, g, g, g, g, g, g, g
]

clear_skies3 = [
  b, b, b, b, b, y, y, y,
  b, b, w, w, b, y, y, y,
  b, b, w, w, b, y, y, y,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  g, g, g, g, g, g, g, g
]

clear_skies4 = [
  b, b, b, b, b, y, y, y,
  b, b, b, b, w, w, y, y,
  b, b, b, b, w, w, y, y,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  g, g, g, g, g, g, g, g
]

blizzard = [
  gr, gr, gr, gr, gr, gr, gr, gr,
  w, b, w, b, w, b, w, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  b, b, b, b, b, b, b, b,
  g, g, g, g, g, g, g, g
]

blizzard2 = [
  gr, gr, gr, gr, gr, gr, gr, gr,
  b, w, b, w, b, w, b, w,
  w, b, w, b, w, b, w, b,
  b, w, b, w, b, w, b, w,
  w, b, w, b, w, b, w, b,
  b, w, b, w, b, w, b, w,
  b, b, b, b, b, b, b, b,
  w, g, g, w, g, g, w, w
]

blizzard3 =[
  gr, gr, gr, gr, gr, gr, gr, gr,
  w, b, w, b, w, b, w, b,
  b, w, b, w, b, w, b, w,
  w, b, w, b, w, b, w, b,
  b, w, b, w, b, w, b, w,
  w, b, w, b, w, b, w, b,
  w, w, w, w, w, w, w, w,
  w, w, w, w, w, w, w, w
]

cloud = [
  bk, w, w, bk, bk, bk, bk, bk,
  w, w, w, w, bk, bk, bk, bk,
  bk, bk, bk, bk, bk, bk, bk, bk,
  bk, bk, w, w, bk, bk, bk, bk,
  bk, w, w, w, w, bk, bk, bk,
  bk, bk, bk, bk, bk, bk, bk, bk,
  bk, w, w, bk, bk, bk, bk, bk,
  w, w, w, w, bk, bk, bk, bk
]

cloud2 = [
  bk, bk, w, w, bk, bk, bk, bk,
  bk, w, w, w, w, bk, bk, bk,
  bk, bk, bk, bk, bk, bk, bk, bk,
  bk, bk, bk, bk, w, w, bk, bk,
  bk, bk, bk, w, w, w, w, bk,
  bk, bk, bk, bk, bk, bk, bk, bk,
  bk, bk, w, w, bk, bk, bk, bk,
  bk, w, w, w, w, bk, bk, bk
]

cloud3 = [
  bk, bk, bk, bk, bk, w, w, bk,
  bk, bk, bk, bk, w, w, w, w,
  bk, bk, bk, bk, bk, bk, bk, bk,
  bk, bk, bk, bk, bk, bk, w, w,
  bk, bk, bk, bk, bk, w, w, w,
  bk, bk, bk, bk, bk, bk, bk, bk,
  bk, bk, bk, w, w, w, bk, bk,
  bk, bk, w, w, w, w, w, bk
]

mist1 = [
  bk, bk, bk, bk, bk, bk, bk, bk,
  bk, bk, bk, gr, gr, bk, bk, bk,
  bk, bk, gr, gr, gr, gr, bk, bk,
  bk, gr, gr, gr, gr, gr, gr, bk,
  bk, bk, bk, bk, bk, bk, bk, bk,
  bk, w, bk, w, bk, w, bk, w,
  w, bk, w, bk, w, bk, w, bk,
  bk, bk, bk, bk, bk, bk, bk, bk
]

mist2 = [
  bk, bk, bk, bk, bk, bk, bk, bk,
  bk, bk, bk, gr, gr, bk, bk, bk,
  bk, bk, gr, gr, gr, gr, bk, bk,
  bk, gr, gr, gr, gr, gr, gr, bk,
  bk, bk, bk, bk, bk, bk, bk, bk,
  w, bk, w, bk, w, bk, w ,bk,
  bk, w, bk, w, bk, w, bk, w,
  bk, bk, bk, bk, bk, bk, bk, bk
]