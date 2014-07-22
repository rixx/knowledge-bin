# Footnotes and Margin Notes

    \footnote{text}
    \marginpar{text}

## Margin notes for footnotes or stuff

    \usepackage{marginnote}
    \usepackage[top=Bcm, bottom=Hcm, outer=Ccm, inner=Acm, heightrounded, marginparwidth=Ecm, marginparsep=Dcm]{geometry}
    \marginnote{text}[Fcm]

## Resetting the footnote counter

Every chapter:

    \makeatletter
    \@addtoreset{footnote}{section}
    \makeatother

Every page:

    \usepackage{perpage}
    \MakePerPage{footnote}


