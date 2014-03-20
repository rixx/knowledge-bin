# IEEE Standard for Binary Floating-Point Arithmetic

## History

First defined 1985, updated 2008. Is the same as ISO/IEC/IEEE 60559:2011.

## Scope

 - arithmetic formats (binary and decimal floating-point data, two NaN, infinites
 - interchange formats (bit strings)
 - rounding rules
 - operations
 - exception handling
 - recommendations for further operations, expression evaluation and reproducability

## Formats

A format contains:
 - finite numbers, base 2 or 10, described by sign s (0 or 1), significand c (coefficient) and exponent q. The value of a number is `(-1)^s * c * b^q`
 - two infinites
 - two NaNs: quiet qNaN and signaling sNaN. May carry a payload for diagnostics.

Rules, p being the precision (number of digits in the significand), and emax the exponent parameter:
 - c must be an integer in the range of `[0, b^p - 1]`
 - q must be an integer such that `1 - emax <= q+p-1 <= emax`

Zero values are signed, so there is +0 and -0.
