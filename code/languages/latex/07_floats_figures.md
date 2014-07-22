# Floats

There are `table` and `figure` floats, though you could make your own. Floats are numbered and have a caption.

    \listoffigures
    \listoftables

To adjust the appearing name, you can also do

    \caption[short name]{because the real description is rather long}

## Figures

### Placement

    \begin{figure}[placement]

Placement specifiers are:
    
* *h*ere: approximately here
* *t*op
* *b*ottom
* *p*age: on a special page for floats
* *!*: Override internal parameters
* *H*ere: only with `usepackage{float}`: nearly the same as `h!`

### Side captions

    \usepackage{sidecap}

    \begin{SCfigure}
    \includegraphics{keks}
    \caption{will appear to the side of your graphic}
    \end{SCfigure}

### Wrapping text around

This sucks. Look up the `wrapfig` package if you really need to do this.

## Tables

    \begin{table}
    \begin{tabular}
    \end{tabular}
    \caption{bla}
    \label{keks}
    \end{table}

## Borders

    \usepackage{float}
    \floatstyle{boxed}
    \restylefloat{figure}


