#Graphics
Prefer vector graphics, pdf and eds > jpg and png.

    \usepackage{graphicx}

## Basic graphic import

    \includegraphics[attr1=bla,attr2=keks]{path/to/image-without-extension}

Options include:

    width=
    height=
    keepaspectratio=true|false
    scale=
    angle=
    trim=l b r t     % eg trim=0mm 0mm 10mm 0mm, negative values allowed, too
    clip             % needed for trim
    page=
    resolution=

Length can also be given as `\linewidth`, `\textwidth` or `\textheight`

##Figures

    \begin{figure}[p]
        \centering
        \includegraphics{bla}
        \caption{keks}
        \label{img:keks}
    \end{figure}

##Storage

Use `\graphicspath{{/path/to/whatever/}{/note/trailing/slash/}{./relative/works/too/}}

If you reeeally want to have recursive search in your image directories, you can run `export TEXINPUTS=./images//:./Snapshots//` before running LaTeX.


##Borders

    \setlength\fboxsep{0pt}     %defines distance from image
    \setlength\fboxrule{0.5pt}  %defines width
    \fbox{\includegraphics{bla}}


