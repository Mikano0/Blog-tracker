Blog Tracker

A simple blog tracker web application built with Flask, Jinja2, and Python. This project displays blog posts fetched from an online JSON API and allows users to view each post individually.

Might scale this project up to add personal blogs and multiple pages to scroll through

Features

Display a list of blog posts on the homepage.

View individual blog posts by clicking on them.

Responsive and clean UI using HTML and CSS.

Easy to extend with new posts or features.

Tech Stack

Python – Backend logic

Flask – Web framework for routing and rendering

Jinja2 – Templating engine for HTML pages

HTML/CSS – Frontend design

Requests – Fetching blog posts from an external JSON API

Installation

Clone the repository

git clone <your-repo-url>
cd <repo-folder>

Open your browser

Go to http://127.0.0.1:5000/ to view the blog tracker.

Project Structure
blog-tracker/
│
├── app.py                  # Main Flask application
├── post.py                 # Post class
├── templates/
│   ├── index.html          # Homepage template
│   └── post.html           # Individual post template
├── static/
│   └── css/
│       └── styles.css      # Custom CSS styles
├── requirements.txt        # Python dependencies
└── README.md

Usage

Homepage shows all blog posts.

Click on a post to view the full content on a separate page.

The app fetches posts from a JSON API, so updating the API will automatically update the posts.
