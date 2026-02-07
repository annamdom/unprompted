Unprompted

Unprompted is a minimal, human-first writing platform built with Django.
It’s designed as a quiet space for short-form writing. No prompts, no algorithms, no AI assistance. Just people writing and reading each other.

Inspired by the simplicity of early blogging platforms, with light social features similar to Instagram or Facebook.


Authentication:

User signup, login, and logout

Session-based authentication using Django’s auth system

Feed:

Chronological feed of all posts

Clickable author names → user profile (Instagram-style)

Logged-in users can create posts directly from the feed

Posts:

Create posts

Edit your own posts

Delete your own posts

View post detail pages with comments

Comments:

Add comments to posts

Delete your own comments

Comment threads shown on post detail pages

User Profiles:

Automatic profile creation for every user

Profile includes:

Name

Username

Bio

Profile picture (avatar)

View your own profile and other users’ profiles

Profile pages show all posts by that user

Edit profile (name, bio, avatar)

Delete your account (with confirmation)

Users Page

Grid-style user directory

Profile cards with avatar, name, and bio

Click any user to view their profile

Search users by username

Search

Search posts by content

Search users by username

Navigation

Persistent “Unprompted” logo + typewriter icon on all pages

One-click return to feed from anywhere

Clean, minimal UI inspired by writing-first platforms

Project Structure 
personal_blog/
├── blog/
│   ├── models.py      # Post, Comment, Profile
│   ├── views.py       # Feed, profiles, posts, search, delete/edit logic
│   ├── urls.py
│   └── templates/
│       └── blog/
│           ├── base.html
│           ├── landing.html
│           ├── home.html
│           ├── profile.html
│           ├── users.html
│           ├── post_detail.html
│           └── edit_*.html
├── media/             # Uploaded avatars (ignored in git)
├── static/
├── db.sqlite3         # Ignored in git
└── manage.py



Design Philosophy

Writing over engagement

No likes, no counters, no ranking

Human expression without prompts




Built by Anna Dominic
As an exploration of writing-first social spaces and full-stack Django development.
