#!/usr/bin/python
import time
import sys
import ueberzug.lib.v0 as ueberzug

def main(x, y, width, height, path):
    with ueberzug.Canvas() as c:
        demo = c.create_placement(
                'img',
                x=x,
                y=y,
                width=width,
                height=height,
                path=path,
                scaler=ueberzug.ScalerOption.CONTAIN.value
            )
        demo.visibility = ueberzug.Visibility.VISIBLE
        input()

if __name__ == '__main__':
    if (len(sys.argv) != 6):
        print(" usage:\n     %s x y width height path"%sys.argv[0])
    main(*sys.argv[1:])
