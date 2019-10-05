# painting.py
import settings
import functions

# Paint semaphores
def paint_semaphore( semID, color, passenger = False ):
    R  = settings.R
    Y  = settings.Y
    G  = settings.G
    RY = settings.RY
    switcher = {
        R: "red",
        G: "green",
        Y: "yellow",
       -1: "none"
    }
    # Reset all colors on semaphore
    if passenger:
        functions.paintobj( semID, R, True ).setStyleSheet("background: none")
        functions.paintobj( semID, G, True ).setStyleSheet("background: none")
    else :
        functions.paintobj( semID, R ).setStyleSheet("background: none")
        functions.paintobj( semID, Y ).setStyleSheet("background: none")
        functions.paintobj( semID, G ).setStyleSheet("background: none")

    if ( color == -1 ):
        return
    elif ( color == RY ):
        functions.paintobj( semID, R ).setStyleSheet("background: red")
        functions.paintobj( semID, Y ).setStyleSheet("background: yellow")
        return
    sem = functions.paintobj( semID, color, passenger )
    sem.setStyleSheet("background: " + switcher[color])

# Paint direction of the semaphores
def paint_direction( dir, color, passenger = False ):
    if ( not(passenger) ):
        if ( dir == 1 ):
            paint_semaphore(1, color)
            paint_semaphore(3, color)
        else:
            paint_semaphore(2, color)
            paint_semaphore(4, color)
    else:
        if ( dir == 3 ):
            paint_semaphore(2, color, True)
            paint_semaphore(3, color, True)
            paint_semaphore(6, color, True)
            paint_semaphore(7, color, True)
        else:
            paint_semaphore(1, color, True)
            paint_semaphore(4, color, True)
            paint_semaphore(5, color, True)
            paint_semaphore(8, color, True)

# Clear all lights on the semaphores
def clear_all_lights():
    color = -1
    paint_semaphore(1, color)
    paint_semaphore(3, color)
    paint_semaphore(2, color)
    paint_semaphore(4, color)
    paint_semaphore(2, color, True)
    paint_semaphore(3, color, True)
    paint_semaphore(6, color, True)
    paint_semaphore(7, color, True)
    paint_semaphore(1, color, True)
    paint_semaphore(4, color, True)
    paint_semaphore(5, color, True)
    paint_semaphore(8, color, True)

# Paint GUI semaphores with colors
def paint_gui( opf, ops ):
    R  = settings.R
    Y  = settings.Y
    G  = settings.G
    RY = settings.RY
    colormap = {
        0: RY,
        1: G,
        2: Y,
        3: R
    }
    passcolormap = {
        0: R,
        1: G
    }
    # First direction semaphore
    e = (opf >> 6) & 1
    clr = opf & 3
    if e:
        paint_direction( 1, colormap[clr] )
    else:
        paint_direction( 1, -1 )
    # Second direction semaphore
    e = (opf >> 7) & 1
    clr = (opf >> 2) & 3
    if e:
        paint_direction( 2, colormap[clr] )
    else:
        paint_direction( 2, -1 )

    # First direction passengers semaphore
    e = ops & 1
    clr = (opf >> 4) & 1
    if e:
        paint_direction( 3, passcolormap[clr], True )
    else:
        paint_direction( 3, -1, True )
    # Second direction passengers semaphore
    e = (ops >> 1) & 1
    clr = (opf >> 5) & 1
    if e:
        paint_direction( 4, passcolormap[clr], True )
    else:
        paint_direction( 4, -1, True )
