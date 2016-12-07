# pancake-slicer

Exploring 3D printer slicing software as applied to printer art.

##Input image, output GCode instructions in order:
- Dark image contours
- Dark color regions with infill
- Midlevel color regions with infill
- Light color regions with infill
- Total infill over the non-white area

## Run slicer

`python Slicer.py`

flag | action
------- | -------
--in | input file name
--out | output file name
--layer | # of perimeter layers
--l | # of levels
--th | layer thickness
--infill | % infill (1.0)
--r | blur radius
--t | tolerance darkest
--t2 | tolerance lighter
--flip | flag to flip the image
--w | white tolerance
--img | flag to show the images