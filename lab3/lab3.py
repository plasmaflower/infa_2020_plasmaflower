from graph import *
windowSize(900, 600)


def evil_smile():
    xc = 200
    yc = xc
    R = 150
    brushColor('yellow')
    penColor('black')
    penSize(1)
    circle(xc, yc, R)

    r = 20
    brushColor('red')
    circle(xc - R / 2, yc + r, r * 1.2)
    circle(xc + R / 2, yc + r, r)

    brushColor('black')
    circle(xc - R / 2, yc + r, r / 2)
    circle(xc + R / 2, yc + r, r / 2)
    rectangle(xc - R / 4, yc + 4 * r, xc + R / 4, yc + 4.5 * r)
    rectangle(xc - R / 6, yc + 3 * r, xc + R / 6, yc + 4 * r)
    run()

def python_amazing():
    brushColor('black')
    penColor('black')
    penSize('1')
#    rectangle(1,1,800,600)

#    brushColor(255,220,220)
    circle(400,300,150)
    run()

#evil_smile()
python_amazing()

#penColor(255,0,255)
#penSize(5)
#brushColor("blue")
#rectangle(100, 100, 300, 200)
#polygon([(100,100), (200,50),(300,100), (100,100)])
#circle(200, 150, 50)
