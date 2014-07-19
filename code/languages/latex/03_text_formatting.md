
# Text Formatting

## Macros

    \newcommand{\oops}
    [1]{\textit{#1}}

## Line Spaces

    \usepackage{setspace}
    \singlespacing
    \onehalfspacing
    \doublespacing
    \setstretch{1.1}

    \begin{doublespace}
    \end{doublespace}

    \begin{spacing}{2.5}
    \end{spacing}

## Word Spaces

    50~€                         % ~ is a nonbreaking space.
    
    \frenchspacing               % disables the additional second space after a period

    Date:\hfill\today            % horizontal filling

    \maketitle                   % vertical filling
    \vfill
    \tableofcontents
    \clearpage  

    \begin{sloppypar}            % do stuff you otherwise would not do
    \end{sloppypar}              % because you have loooong words close to the margin or stuff

    Dampf{}fahrzeug              % suppress ligature
    \usepackage[resetfonts]{cmap}% help make ligatures readable and searchable

## Hyphenation

    \hyphenation{FORTRAN Py-thon}% forbid hyphenation of FORTRAN, specify hyphenation of Python, not often needed
    su\-per\-ca                  % specify allowed hyphenation points

    \mbox{0176 64 63 65}         % keep words together on one line
    \fbox{0176 64 63 65}         % like mbox, but with a visible box

    \hyphenpenalty=100000        % no hyphens anywhere (do not. just not. no.)

 
## Sub- and superscript

    \usepackage{fixltx2e}
    \textsubscript{bla}
    \textsuperscript{keks}

or math mode:

    H$_2$O

Not as good, you need to specify `\mathroman{text}` for all text occurences. If you need chemistry subscripts, consider using [mhchem](http://www.ctan.org/tex-archive/macros/latex/contrib/mhchem/).

## Alignment

    \raggedright
    \raggedleft
    \centering

    \begin{flushleft}
    \begin{flushright}
    \begin{center}

## Indentation

    \usepackage{parskip}
    \setlength{\parindent}{1cm}  % set the parindent depth, default 15pt
    \setlength{\parskip}{1cm plus4mm minus3mm}
                                 % give-or-take in vertical space between paragraphs

    \indent
    \noindent                    % indenting paragraphs

    \hangindent=0.7cm            % hanging indentation

    \paragraph{Title} ~\\        % line break after paragraph title
    Text


## Quotes

    \quote                       % short quotation(s), separated by blank lines
    \quotation                   % longer quotations, >1 paragraph
    \verse                       % to quote lyric stuff


## Verbatim and Comments

    \usepackage{verbatim}
    \begin{verbatim}             % reproduces every character you write, including spaces
    \verb+my text+               % verbatim command, first character is delimiter
    \begin{listing}[step]{first line}
                                 % verbatim, but with line numbers

    \usepackage{alltt}           % like verbatim, but can emph text etc
    \begin{alltt}

    \begin{comment}              % multiline comments yay, belongs to verbatim
    \end{comment}

    \newcommand{\comment}[2]{#2} % alternative, but content is still parsed
    \command{blakeks hihihi}


## Miscellaneous

    \oldstylenums{42}            % pretty numbers
    
    \url{bla://keks.foo}         % links


