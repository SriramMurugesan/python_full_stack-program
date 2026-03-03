# 08 | CSS Selectors & Properties

To style modern websites, you need more than just tag names. You need to target specific elements and control their visuals deeply.

---

## 1. CSS Selectors (Targeting)

### A. Tag Selector
Targets every instance of a tag.
```css
p { color: gray; } /* Styles all paragraphs */
```

### B. Class Selector (`.`)
Targets elements with a specific `class` attribute. You can use a class on multiple elements.
```css
.highlight { color: orange; font-weight: bold; }
```
`HTML: <p class="highlight">Important Text</p>`

### C. ID Selector (`#`)
Targets a single element with a specific `id`. Each ID must be unique per page.
```css
#main-title { font-size: 50px; text-align: center; }
```
`HTML: <h1 id="main-title">Welcome</h1>`

### D. Universal Selector (`*`)
Targets every single element on the page. Usually used for resetting margins.
```css
* { margin: 0; padding: 0; box-sizing: border-box; }
```

---

## 2. Core Visual Properties

### A. Colors
- **Names:** `red`, `blue`, `black`
- **Hex Codes:** `#ff0000` (Red), `#ffffff` (White)
- **RGB:** `rgb(255, 0, 0)`
- **Opacity:** `rgba(255, 0, 0, 0.5)` (The `0.5` makes it semi-transparent!)

### B. Typography
- `font-family`: Choose your font (e.g., Arial, 'Roboto', sans-serif).
- `font-size`: `16px`, `2rem`.
- `line-height`: Controls the space between lines.
- `text-align`: `left`, `center`, `right`, `justify`.

### C. Text Decoration
- `text-decoration: none;` (Removes the underline from links).
- `text-transform: uppercase;` (Converts all text to capital letters).

---

## 3. Backgrounds
You can add colors or images to the background of any element.
```css
.card {
  background-color: lightblue;
  background-image: url('pattern.png');
  background-size: cover;
}
```

---

### 📝 Exercise
1. Go to your `index.html`.
2. Give one of your paragraphs a class of `bio`.
3. Give your "My Skill Progress" table an ID of `skills-table`.
4. In `style.css`:
   - Style the `.bio` class with a specific font and color.
   - Style the `#skills-table` with a border and a background color.
   - Remove the underline from your LinkedIn link using `text-decoration: none;`.
   - Use the `*` selector to set `font-family: Arial, sans-serif;` for the whole page.
