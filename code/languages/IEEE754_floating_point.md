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

### Basic formats

A conforming implementation must fully implement at least one of the five basic formats. Precision is typically one bit more than the width of the significant (because the leading 1 is implied).

| Name       | aka                 | base | digits | exponent range | decimal digits | maximum exponent (decimal) |
|------------|---------------------|------|--------|:--------------:|----------------|----------------------------|
| Binary16   | half precision      | 2    | 10+1   | -14,15         | 3.31           | 4.51                       |
| Binary32   | single precision    | 2    | 23+1   | -126,127       | 7.22           | 38.23                      |
| Binary64   | double precision    | 2    | 52+1   | -1022,1023     | 15.95          | 307.95                     |
| Binary128  | quadruple precision | 2    | 112+1  | -16382,16383   | 34.02          | 4931.77                    |
| Decimal32  |                     | 10   | 7      | -95,96         |                |                            |
| Decimal64  |                     | 10   | 16     | -383,384       |                |                            |
| Decimal128 |                     | 10   | 34     | -6143,6144     |                |                            |

### Extended and extendable Formats

Basic formats can be extended by using more precision and a greater exponent range. b, p and emax need to be re-defined. Implementations of this standard need not support extendable formats. 

### Interchange formats

For the exchange of binary numbers: 16 bit, 32 bit, 64 bit, and 128 + n*32 bit interchange formats. 

`k` bit format: Sign bit, `w = round(4* log_2(k)) -13)` exponent bits (describe exponent, offset by the bias), `p-1` significand bits.

## Rounding Rules

Recommended: round to the nearest, ties to next even number.

Alternatives: ties away from zero, always towards 0, always towards +∞, always towards -∞.
