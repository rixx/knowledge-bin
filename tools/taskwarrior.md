# Taskwarrior

`pacman -S task`

[Taskwarrior](http://taskwarrior.org/) is a command-line task manager with **all** the features.

## Adding and modifying Tasks

    task add <description> [priority:<H|M|L>] [project:<name>] [+<tag>] [due:<date>] [depends:<id>]
    task <id> done
    task <id> start

The `modify <id>` command can use all of the above properties and more. The `next` tag boosts the urgency of a task. 


## Reports

    task list
    task next
    task info
    task summary
    task burndown.<daily|monthly|weekly>
    task all
    task active
    task oldest
    task overdue

Also configurable. The default report is the `next` report.
