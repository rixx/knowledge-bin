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

    \multicolumn{2}{|c|}{content}

    \usepackage{multirow}
    \multirow{2}{*}{content}   % second parameter is width, * is natural width

## Controlling the size
Use `graphicx` to resize the whole table:

    \usepackage{graphicx}

    \resizebox{8cm}{!} {
        \begin{tabular}
        …
        \end{tabular}
    }

You can also use `\scalebox{0.7}{…}` if you would rather use ratios.

## Changing the font size

    { \footnotesize
        \begin{tabular}
        …
        \end{tabular}
    }

## Change colors
### Alternating row colors

    \usepackage[table]{xcolor}

    \rowcolors{1}{green}{pink}
    \begin{tabular}
    …
    \end{tabular}

You can add `\hiderowcolors` to disable this feature until the end of the table, counter with `\showrowcolors`.

### Highlight cells

    \usepackage[table]{xcolor}

    \cellcolor[gray]{0.9}
    \cellcolor{red}

## Refs, captions and floating

If you want a `\listoftables` and refs and captions and even floating, you need to place your `tabular` environment (containing your content) inside a `table` environment:

    \begin{table}[position specifier]
        \centering

        \begin{tabular}{c|ll}
        …
        \end{tabular}

        \caption{olol \latex}
        \label{tab:olol}
    \end{table}

Position specifier being: *h*ere, *t*op, *b*ottom, *c*enter, *!* override float limitations.

## Infinitely more stuff and other packages:

look [here](https://en.wikibooks.org/wiki/LaTeX/Tables)


