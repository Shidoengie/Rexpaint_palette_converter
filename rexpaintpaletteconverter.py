from converter import *
filename = input("enter the name of your palette")
filename2 = filename + ".txt"
filename3 = filename + ".hex"
rex_palette = open(filename2, "w")
hex_conv = open(filename3, "r")
i = 0
for hexnum in hex_conv.readlines():
    val1 = convert(hexnum,0,0,0)
    val1.R = str(val1.R)
    val1.G = str(val1.G)
    val1.B = str(val1.B)
    while len(val1.R) < 3:
        val1.R = " " + val1.R
    while len(val1.G) < 3:
        val1.G = " " + val1.G
    while len(val1.B) < 3:
        val1.B = " " + val1.B
    A = "{" + val1.R + "," + val1.G + "," + val1.B + "}	"
    rex_palette.write(A)
    i += 1
    if i >= 192:
        break
    if i % 16 == 0:
        rex_palette.write("\n")
i2 = i
while i2 < 192:
    rex_palette.write("{  0,  0,  0}	")
    i2 += 1
    if i2 % 16 == 0:
        rex_palette.write("\n")
