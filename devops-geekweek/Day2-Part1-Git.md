# Source Code Management

^ Open this presentation with [Deckset](http://www.decksetapp.com/)

---

# What You'll Learn

* Why use version control
* How to use Git
* How to use GitHub
* What a pull request is
* Branches and why they're really smart

---

# Day 2 Agenda

* Daily Standup
* Understand Git / Source Code Management
* Do work via collaborative methods
* Write some code, deploy containers locally

---

# Why use version control

 - Version control records changes that are made so you can recall specific version later
 - Makes it possible for you to work on a feature/bug fix/release without changing production code
 - No more "file-version3.py" or "config-020315.conf"!
 - Since everything is pure text it's easy to "merge" new code into existing

---

# Git

A distributed version control system, where every user has a complete and full copy of the source code.  

If you can't check it in, you can't keep track of it, so you can't version it, so you can't automate it.

*Everything* belongs in source code control, and git is the standard in 3rd platform.

Other possible options: subversion (svn), mercurial (hg), Perforce (p4), ClearCase (cc).

---

# GitHub

A freemium service to host Git repositories (repos). Public repos are free, private ones are still cheap.

Most open source projects are hosted and collaborated on here.

> If you're not on GitHub you don't exists.
-- Friendly developer

---


# How does it work?

1. Initialize a central repository
2. Clone the repo
3. Make changes
4. Commit changes
5. Push those changes to the central repo
6. ...
7. Profit!

---

# Create a new repo

![inline, 100%](https://help.github.com/assets/images/help/repository/repo-create.png)

---

# Clone the repo

```git clone https://github.com/virtualswede/training-repo.git```

---

# Make changes

```cd training-repo```
```echo "Hello World" > yourname.txt```

---

# Commit changes

```git add yourname.txt```
```git commit -m "added yourname.txt to the repo"```

---

# Push changes

```git push```

---

# What happened?

---

# DENIED!

You're not allowed to push to this repo

So how can we collaborate?

Fork it!

---

# Fork a repo

![inline, 100%](https://help.github.com/assets/images/help/repository/fork_button.jpg)

---

# Clone _that_ repo instead of the original one

```git clone https://github.com/yourname/training-repo```

Repeat your changes, and try to push

What happens?

---

# Compare to the original

![inline, 100%](images/github_compare.png)

---

![inline, 100%](images/github_compare2.png)

---

# Create a pull request

![inline](images/github_create_pr.png)

---

![inline](images/github_pr.png)

---

# If a Pull Request is alright, it can then be merged

---

![inline](images/github_merge.png)

---

![inline](images/github_merge_successful.png)

---

# Branches

---

```git branch new-feature```

![inline](images/github_new_branch.png)

---

# Switch to your branch

```git check new-feature```

---

# Make changes, commit, then push

```echo "Hello World again" > yourname.txt```

```git diff```

```git add yourname.txt```

```git commit -m "made some changes"```

```git push```

What happens?

---

# You need to set the upstream

 - This is where we should push the new changes to

 - It might be a totally different repo than the original

```git push --set-upstream origin new-feature```

Now go look at that branch up on GitHub

---

# You can now create a pull request from that branch!
