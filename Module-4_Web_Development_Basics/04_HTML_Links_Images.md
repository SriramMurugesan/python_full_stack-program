# 04 | HTML Links & Images

The web wouldn't be "The Web" without **Hyperlinks** (connections between pages) and **Media**.

---

## 1. Hyperlinks (The `<a>` Tag)
The `<a>` (Anchor) tag allows users to navigate from one page to another.

### A. External Links
Links to another website.
```html
<a href="https://www.google.com" target="_blank">Visit Google</a>
```
- `href`: The destination URL.
- `target="_blank"`: Opens the link in a **new tab** (Very important for UX!).

### B. Internal Links
Links to another file in your own project folder.
```html
<a href="contact.html">Contact Me</a>
```

---

## 2. Embedding Images (The `<img>` Tag)
The `<img>` tag is used to display pictures. It is a **Self-Closing** tag (no `</img>` needed).

```html
<img src="mountain.jpg" alt="A snowy mountain peak" width="500">
```
- `src`: The Source (where the image file is).
- `alt`: Alternative Text (What to show if the image fails to load. Vital for accessibility!).
- `width`/`height`: Optional attributes to set size.

---

## 3. Linking an Image
You can turn an image into a button by wrapping it in an `<a>` tag!
```html
<a href="https://www.wikipedia.org">
  <img src="wiki-logo.png" alt="Wikipedia Logo">
</a>
```

---

## 4. Attributes (A Recap)
Attributes provide extra information about an element. They always sit inside the opening tag.
- `class`: For styling later with CSS.
- `id`: Unique identifier.
- `title`: Shows a "tooltip" when you hover over the element.

---

### 📝 Exercise
1. Go to your `index.html`.
2. Find a small image online (or use a placeholder like `https://via.placeholder.com/150`).
3. Add the image to your page with a proper `alt` description.
4. Below the image, add a link that says "Follow me on LinkedIn" and make it open in a new tab.
5. Create a second file named `projects.html` in the same folder.
6. In `index.html`, add a link that says "View My Projects" that leads to `projects.html`.
7. Reload your browser and click the links to test them!
