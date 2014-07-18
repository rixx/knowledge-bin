# LaTeX

You know the drill. pdflatex is for pdfs, lualatex may include lua scripting, xelatex is especially good for unicode and fonts (though lualatex can do those too).

## Basic Syntax

   { }
   \begingroup
   \endgroup

Groups limits the range of commands inside them.

   \begin{name}
   \end{name}

Environments are somewhat similar to commands with a wider scope.

   \command[option,option2]{argument}{argument2}

A command. Most commands have a *switch* equivalent. Those do not take arguments, but apply on the rest of the scope:

   \emph{emphasized text}
   {\em emphasized text }

## Document Structure

   \documentclass{...}
   %here: preamble
   
   \begin{document}
   %stuff
   \end{document}


## Document classes

**Classes**:
* article
* report
* book
* letter
* beamer (see a separate, to-be-written 'LaTeX Beamer' guide)

**Options**: 
* [10pt,11pt,12pt]
* [a4paper,letterpaper,...],
* [fleqn]: formulas left-aligned; [leqno]: formula numbers on the left
* [titlepage, notitlepage]: whether to put a page break after the title page (article does not by default)
* [twocolumn]
* [landscape]
* [draft] -- mark problems with a small square next to the problem line, for better finding, suppresses inclusion of images and instead only shows a frame

## Packages

    \usepackage[options]{package}

## The Document Environment
###Beginning
    \title{Bla}
    \author{keks\\
    cookie monster academy}
    \date{november?}
    \date{\today}
    \maketitle


    \renewcommand{\abstractname}{Executive Summary}
    \begin{abstract}
    \end{abstract}

### Sections

**Order**:
* \part
* \chapter (only in books and reports)
* \section
* \subsection
* \subsubsection
* \paragraph
* \subparagraph

Example:
   \section[Short for TOC]{Name too long for the Table of Contents, I guess}

If you only want parts and sections numbered (not subsections) or want to limit the depth of the table of contents:

    \setcounter{secnumdepth}{1}
    \setcounter{tocdepth}{3}

Unnumbered sections which do not appear in the table of contents, or, are manually put there:

    \subsection*{Introduction}
    \addcontentsline{toc}{section}{Introduction}

You can also reset the counters and do more [fancy stuff](https://en.wikibooks.org/wiki/LaTeX/Counters)

### Other important special sections

    \tableofcontents %usually after the abstract, needs one re-run
    \listoffigures   %both normally after the table of contents
    \listoftables
    \thebibliography %bibliographies are hard
    \glossary        %ain`t quite easy, either





