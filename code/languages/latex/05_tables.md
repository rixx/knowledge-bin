#Tables

## Syntax

    \begin{tabular}[pos]{spec}

* *pos*: `b`ottom or `c`enter or `t`op on the page
* *spec*: 
    * `l`eft, `c`enter or `r`ight justified column
    * `|` or `||` vertical lines
    * >{format}: `\begin{tabular}{ >{\bfseries}l c >{\itshape}r }`
* *in the environment*:
    * `&` separates columns
    * `//` starts a new row (optionally specify space, `//[6pt]`)
    * `\hline` inserts a horizontal line
    * `\cline{i-j} inserts a partial horizontal line from column i to column j

## Text wrapping

Choose `p<5cm>` as descriptor instead of `l`, `c` or `r`

You can also use `parbox` to manually set your line breaks:

    boring cell content & \parbox[t]{5cm}{rather long par\\new par}

You might also have to use a descriptor like this to use other environments like `verbatim` inside a table.

## Spanning: Multicolumn, Multirow



## Infinitely more stuff and other packages:

look [here](https://en.wikibooks.org/wiki/LaTeX/Tables)


