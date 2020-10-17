A collection of minimal radius lattice circles
----------------------------------------------

Lattice circles are circles drawn in the 2-dimensional cartesian
plane, whose circumference passes through a specific number of lattice
points (i.e. points whose x and y coordinates are both integers).

The centre of a lattice circle does not have to be on a lattice point.

Schinzel circles can be constructed that pass through any given exact
number of lattice points, but these circles are almost always much
larger than than a minimal radius circle.


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
code, and given in the alt_xy dict).


When run as a standalone program the lattice_circles.py program
produces the text summary of the list found in the file:
lattice_circles.txt

There is a circle listed for every n < 3805 (but most of these are not
verified minimal circles).


The list is composed from several methods:

  - Exhaustive search for circles with any number of points below a
    specific radius.

    The following searches have currently been completed:

      All minimal circles with n > 0 and r < 2660

  - Exhuastive search for circles with a minimum number of points
    below a specific radius.

    The following searches have currently been completed:

      All minimal circles with n >  48 and r <  3661
      All minimal circles with n >  80 and r <  7968
      All minimal circles with n > 192 and r < 12320
      All minimal circles with n > 496 and r < 24561

  - Taking lattice circles centred on the origin passing through a
    number of lattice points and scaling down the circles to find smaller
    lattice circles, not necessarily centred on the origin.

    Good numbers to try are products of Pythogorean primes (of the
    form 4k+1) possibly with an additional factor of 2.

    OEIS A018782 and A016032 are good sources of numbers.

  - A list of improvements for many circles with n > 196 contributed
    by Rei Igarshi. Contributions that I have not verified are listed
    in the file [ lattice_circles_unverified.py ].


See also:

[ https://enigmaticcode.wordpress.com/2013/10/15/enigma-136-twelve-point-square/ ]


I welcome any additions or improvements to the list (particularly for
circles with n < 2501, or circles with r < 25e+9 (or preferably,
both)).

If anyone has any use for these circles I would be interested to hear
about it.

Also any ideas on fast algorithms for finding minimal circles would be
appreciated.

Or if you want to donate some computer time to finding minimal circles.

-- Jim Randell <jim.randell@gmail.com>