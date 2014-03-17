# Git Flow

Summarization of ["A successful git branching model"](http://nvie.com/posts/a-successful-git-branching-model/) by @nvie (Vincent Driessen) and explanation of the git-flow tool

## The branching model


### `origin/master`

Infinite lifetime. Main Branch. Reflects strictly *production ready* state, each time a commit is done on `master`, a hook could be used to roll out a release.


### `origin/develop`

Infinite lifetime. Integration branch, source for automatic nightly builds.

When the code reaches a stable point, it is to be merged back to the `master` branch and tagged.

### `feature/*` or just anything other than the other names

Limited lifetime. Doesn't exist on `origin`, just in developer repo(s). Branching off from `develop`. Merge to `develop` should be `--no-ff`, afterwards delete the feature branch and push `develop`.

    git checkout -b feature/newfeature develop
    git checkout develop
    git merge --no-ff feature/newfeature
    git branch -d feature/newfeature

### `release-*`

Release branches *prepare* a new release (last-minute-changes, prepare and fix release metadata such as version number and build date). 

Branches off of `develop` when exactly all features meant for the release, and these alone, are merged into `develop`. Assign new version numbers in the beginning of the release branch, no earlier.

Merge back to master and develop. Tag the new release. Delete the branch.

    git checkout -b release-1.2 develop
    <do something, change version number>
    git commit -m 'new version number: 1.2'
    git checkout master
    git merge --no-ff release-1.2
    git tag -a 1.2
    git checkout develop
    git merge --no-ff release-1.2
    git branch -d release-1.2

### `hotfix-*`

Merges off `master` and into `develop` and `master`, `--no-ff` as the others, can be deleted afterwards. Remember to bump the version number and tag the merge commit on `master`.

If a release branch exists, merge the hotfix branch into `master` and the release branch instead of `develop`.

## The tool

The [git-flow](https://github.com/nvie/gitflow) tool (actually a git extension, so it's doing things right) does fancy stuff for those who want to use the git flow branching model without having to give it a lot of thought. 

### Commands:

    git flow init [-d for defaults]
    git flow [feature | release | hotfix] start <name>
    git flow [feature | release | hotfix] finish <name>
    git flow feature [publish | pull <remote>] <name>

### Additional support:

There's an oh-my-zsh plugin for that (depends on the git plugin, just include `git` and `git-flow`).

