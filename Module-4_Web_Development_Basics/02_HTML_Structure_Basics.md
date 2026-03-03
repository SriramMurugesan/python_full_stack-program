# 02 | HTML Basics: The Skeleton of the Web

Every website is like a house. **HTML** (HyperText Markup Language) provides the structure for that house—the walls, the roof, and the rooms.

---

## 1. What is HTML?
HTML is the standard language for creating web pages. It uses **"Tags"** to tell the browser what kind of content it's looking at (e.g., "This is a heading," "This is a paragraph").

### 🏗️ Anatomy of a Tag
Most tags have an opening tag and a closing tag:
```html
<p>This is a paragraph.</p>
 ^      ^            ^
 |      |            |
Open   Content     Close (with a /)
```

---

## 2. The HTML Boilerplate (Standard Structure)
Every HTML file MUST start with this standard boilerplate code. Copy-paste this into your editor to begin!

```html
<!DOCTYPE html> <!-- Tells the browser this is an HTML5 document -->
<html lang="en"> <!-- Root element of the page -->
<head>
    <!-- Meta info: Hidden from users, used by browsers/search engines -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My First Web Page</title> <!-- Tab name in your browser -->
</head>
<body>
    <!-- Visible Content: Everything here is shown on the screen -->
    <h1>Welcome to My Website!</h1>
    <p>This is my first time writing HTML.</p>
</body>
</html>
```

---

## 3. Core Tags to Know
### A. Headings (`<h1>` to `<h6>`)
Used for titles and subtitles. `<h1>` is the most important, and `<h6>` is the smallest.
```html
<h1>Main Title</h1>
<h2>Sub-heading</h2>
<h3>Smaller heading</h3>
```

### B. Paragraphs (`<p>`)
Used for blocks of regular text.
```html
<p>HTML is easy to learn once you understand tags!</p>
```

---

## 4. Semantic HTML (The Goal)
Don't just use `<div>` (generic container) for everything! Use **Semantic Tags** to give meaning to your structure. It helps search engines (SEO) and people using screen readers.

| Tag | Use Case |
| :--- | :--- |
| `<header>` | Site logo, navigation |
| `<nav>` | List of links |
| `<main>` | The primary content of the page |
| `<article>` | A self-contained piece (like a blog post) |
| `<section>` | A group of related content |
| `<footer>` | Copyright info, contact links |

---

### 📝 Exercise
1. Create a file named `index.html` on your desktop.
2. Paste the boilerplate code above.
3. Change the `<title>` to your name.
4. Add an `<h2>` tag inside the `<body>` that says "About Me".
5. Save and double-click the file to open it in your browser.
