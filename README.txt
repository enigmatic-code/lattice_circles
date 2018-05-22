A collection of minimal radius lattice circles
----------------------------------------------

Lattice circles are circles drawn in the 2-dimensional cartesian
plane, whose circumference passes through a specific number of lattice
points (i.e. points whose x and y coordinates are both integers).

The centre of a lattice circle does not have to be on a lattice point.

The list of lattice circles given in the Python source code:

  lattice_circles.py

which includes the following dictionaries

  minimal - which contains lattice circles for which exhaustive search
  has shown that there are no smaller radius lattice circles with the
  specified number of points on the circumference.

  best - other lattice circles that have been found during the
  search. These are not verified as minimal radius lattice circles,
  but only the smallest radius found so far for any given number of
  points on the circumference is given.

each of these dictionaries is of the form:

  n: ((r2a, r2b), ((xa, xb), (ya, yb)))

where n is the number of lattice points required on the circumference
of the circle.

which gives the following rational numbers:

  r2a/r2b = the square of the radius of the circle

  xa/xb = the x coordinate of the centre of the circle
  
  ya/yb = the y coordinate of the centre of the circle

the equation of the circle is thus:

  (x - xa/xb)^2 + (y - ya/yb)^2 = r2a/r2b

the centres are normalised to lie within the triangle with vertices:

  (0, 0), (1/2, 0), (1/2, 1/2)

where there are multiple possible centres in this triangle only one is
given (although others may be mentioned in the comments of the Python
code).

When run as a standalone program the lattice_circles.py program
produces the text summary of the list found in the file:
lattice_circles.txt


The list is composed from several methods:

  - Exhaustive search for circles with any number of points below a
    specific radius.

    The following searches have currently been completed:

      All minimal circles with n > 0 and r < 1840

  - Exhuastive search for circles with a minimum number of points
    below a specific radius.

    The following searches have currently been completed:

      All minimal circles with n >= 33 and r < 2245
      All minimal circles with n >= 49 and r < 3660
      All minimal circles with n >= 193 and r < 12320
      All minimal circles with n >= 495 and r < 13001

  - Taking lattice circles centred on the origin passing through a
    number of lattice points and scaling down the circles to find smaller
    lattice circles, not necessarily centred on the origin.

    Good numbers to try are products of Pythogorean primes (of the
    form 4k+1) possibly with an additional factor of 2.

    OEIS A018782 and A016032 are good sources of numbers.



See also:

https://enigmaticcode.wordpress.com/2013/10/15/enigma-136-twelve-point-square/

