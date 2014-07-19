# Basic Syntax

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

