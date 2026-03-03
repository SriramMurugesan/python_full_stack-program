# 11 | Responsive Web Design: The Mobile-First Approach

In today's world, more people browse the web on phones than on computers. Your website must look great on screens of all sizes.

---

## 1. The Viewport Meta Tag
Before you can make a site responsive, your HTML must tell the browser how to scale. This tag is always inside the `<head>`:
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

---

## 2. Media Queries (The If-Statement of CSS)
Media queries allow you to apply CSS only when a specific condition is met (e.g., the screen is narrow).

```css
/* Normal styles (for Desktop) */
.container { grid-template-columns: 1fr 1fr 1fr 1fr; }

/* Styles for Tablets (Max-Width 768px) */
@media (max-width: 768px) {
  .container { grid-template-columns: 1fr 1fr; }
}

/* Styles for Phones (Max-Width 480px) */
@media (max-width: 480px) {
  .container { grid-template-columns: 1fr; }
}
```

---

## 3. Designing Responsively

### A. Fluid Units
Avoid fixed pixels (`px`) for widths! Use percentages or flexible units.
- `width: 80%;`
- `width: 50vw;` (50% of the viewport width)
- `max-width: 1200px;` (Let it shrink, but don't let it grow too large).

### B. Flexible Images
Prevent images from "breaking" out of their boxes.
```css
img {
  max-width: 100%;
  height: auto;
}
```

### C. Flexbox Wrapping
Let items drop to the next line when there isn't enough space.
```css
.flex-container {
  display: flex;
  flex-wrap: wrap; /* Items will wrap automatically! */
}
```

---

## 4. Mobile-First (Pro Strategy)
Professional developers write CSS for the **smallest screen first**, then use media queries to add complexity for larger screens.

```css
/* Mobile styles (Default) */
.sidebar { display: none; }

/* Large Desktop styles */
@media (min-width: 1024px) {
  .sidebar { display: block; }
}
```

---

### 📝 Exercise
1. Add 4 simple boxes to your page inside a `container` div.
2. In `style.css`, make them sit in a row using Flexbox.
3. Use a **Media Query** so that when the screen width is less than `600px`, the boxes stack on top of each other (Change `flex-direction` to `column`).
4. Test this by making your browser window narrow—the boxes should shift!
