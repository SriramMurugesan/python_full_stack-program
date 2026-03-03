# 10 | CSS Layout: Flexbox & Grid

In the old days, arranging boxes was painful. Today, we have two superpowers: **Flexbox** (for rows OR columns) and **Grid** (for rows AND columns).

---

## 1. Flexbox (One Dimension)
Flexbox is perfect for navigation bars, centering items, or a single row of cards.

### A. The Setup
You apply Flexbox to the **Parent Container**.
```css
.container {
  display: flex;
}
```

### B. Aligning Items
- `justify-content`: Horizontal alignment (`flex-start`, `center`, `flex-end`, `space-between`).
- `align-items`: Vertical alignment (`flex-start`, `center`, `flex-end`, `stretch`).
- `flex-direction`: `row` (default) or `column`.
- `gap`: Space between items (e.g., `20px`).

```css
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
}
```

---

## 2. CSS Grid (Two Dimensions)
Grid is for complex layouts like magazine covers or a whole website structure.

```css
.grid-container {
  display: grid;
  grid-template-columns: 200px 1fr 1fr; /* Fixed, then two flexible columns */
  grid-template-rows: auto;
  gap: 15px;
}
```
- `1fr` means "one fraction"—it takes up the remaining space.

---

## 3. Positioning
Sometimes you want an element to "float" above others or stay fixed.
- `position: relative`: The element stays in its normal spot.
- `position: absolute`: Moves relative to its nearest "relative" parent.
- `position: fixed`: Stays in one spot even when you scroll (like a persistent navbar).
- `z-index`: Controls layers (Which item is on top?).

---

### 📝 Exercise
1. Create a `<div>` with class `nav` at the top of your page.
2. Put 3 links inside it.
3. Use **Flexbox** to:
   - Make the links sit in a row.
   - Space them out using `justify-content: space-around;`.
   - Give them a `gap: 20px;`.
4. Create a `<div>` with class `features`.
5. Put 4 `<div>` boxes inside it.
6. Use **Grid** to display them in a 2x2 layout:
   ```css
   .features {
     display: grid;
     grid-template-columns: 1fr 1fr;
     gap: 10px;
   }
   ```
