# 09 | The CSS Box Model: Spacing and Sizing

In CSS, **everything is a box**. To master layout, you must understand how these boxes are built.

---

## 1. The Four Layers of the Box
Imagine a picture in a frame.

1. **Content:** The actual image (text, images, video).
2. **Padding:** The space between the image and the frame (Inside).
3. **Border:** The frame itself.
4. **Margin:** The space between this picture frame and the one next to it (Outside).

---

## 2. Controlling the Spaces

### A. Padding (Inside)
Pushes the content away from the border.
```css
.card { padding: 20px; } /* All sides */
.card { padding-top: 10px; padding-left: 5px; } /* Individual sides */
.card { padding: 10px 20px; } /* Top/Bottom: 10, Left/Right: 20 */
```

### B. Margin (Outside)
Creates space between different elements.
```css
.button { margin: 15px; }
.centered { margin: 0 auto; } /* Centers a block element horizontally! */
```

### C. Border (The Edge)
```css
div { border: 2px solid black; } /* Style: solid, dotted, dashed, double */
div { border-radius: 10px; } /* Makes the corners rounded! */
```

---

## 3. The `box-sizing` Trick
By default, adding padding makes an element **wider** than you set (Width + Padding = Total).
To fix this, we use:
```css
* { box-sizing: border-box; }
```
Now, padding is included **inside** the width you set. It makes math much easier!

---

## 4. Block vs. Inline
- **Block:** Takes up the full width (e.g., `<div>`, `<h1>`, `<p>`).
- **Inline:** Only takes as much width as its content (e.g., `<span>`, `<a>`, `<strong>`).
- **Inline-Block:** Acts like inline but lets you set width, height, and margins.

---

### 📝 Exercise
1. Add a `<div>` with a class of `box` to your `index.html`.
2. Inside the div, write "Box Model Test".
3. In `style.css`:
   - Set the `width` to `300px`.
   - Add `padding: 30px;`.
   - Add a `border: 5px solid blue;`.
   - Set `margin: 50px auto;` to center it.
   - Use `border-radius: 15px;` for rounded corners.
4. Experiment by removing `box-sizing: border-box;` and see what happens to the size.
