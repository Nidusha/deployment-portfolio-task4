import os
from flask import Flask, render_template_string

app = Flask(__name__)

@app.get("/")
def home():
    title = os.getenv("APP_TITLE", "Study Task Tracker")
    tasks = [
        ("Complete Docker lab", "In progress"),
        ("Capture deployment screenshots", "To do"),
        ("Submit PDF report", "To do"),
    ]
    return render_template_string("""
    <!doctype html>
    <html lang="en">
    <head>
      <meta charset="utf-8">
      <title>{{ title }}</title>
      <style>
        body { font-family: Arial, sans-serif; background: #f2f5fa;
               max-width: 700px; margin: 60px auto; color: #1e293b; }
        main { background: white; padding: 32px; border-radius: 14px;
               box-shadow: 0 4px 20px #0001; }
        h1 { color: #2563eb; }
        li { padding: 14px; border-bottom: 1px solid #e5e7eb; }
        span { float: right; color: #475569; }
      </style>
    </head>
    <body><main>
      <h1>{{ title }}</h1>
      <p>Deployment Portfolio — Task 4.3</p>
      <ul>{% for name, status in tasks %}
        <li>{{ name }} <span>{{ status }}</span></li>
      {% endfor %}</ul>
    </main></body>
    </html>
    """, title=title, tasks=tasks)