# 07 | CSS Introduction: Styling the Web

If HTML is the skeleton (structure), then **CSS** (Cascading Style Sheets) is the skin and the clothes. It makes things look beautiful!

---

## 1. CSS Syntax (The Rules)
A CSS rule tells the browser: "Target *these* elements and apply *these* styles."

```css
h1 {
  color: blue;
  font-size: 24px;
}
```
- **Selector:** `h1` (Who am I styling?)
- **Property:** `color` (What am I changing?)
- **Value:** `blue` (What is the new value?)

> [!IMPORTANT]
> Always end every property-value pair with a **semicolon (`;`)** and wrap your styles in **curly braces (`{}`)**.

---

## 2. The Three Ways to Apply CSS
There are three ways to link CSS to your HTML.

### A. Inline CSS (Not Recommended)
Styles are written directly inside the HTML tag.
```html
<h1 style="color: red;">Hello World</h1>
```
- **Why avoid?** It's messy and hard to manage once your page grows.

### B. Internal CSS (Good for Single Pages)
Styles are written inside the `<style>` tag in the `<head>` of your HTML.
```html
<head>
  <style>
    p { color: green; }
  </style>
</head>
```

### C. External CSS (The Professional Way)
Styles are written in a separate `.css` file and linked in the `<head>`.
```html
<head>
  <link rel="stylesheet" href="style.css">
</head>
```
- **Why use?** You can style 100 pages using just one CSS file. Clean and efficient!

---

## 3. What does "Cascading" mean?
If two rules conflict, which one wins?
1. **The Order:** Later rules override earlier ones.
2. **Specificity:** More specific selectors override general ones (e.g., an ID beats a Tag).
3. **Importance:** Inline styles beat almost everything else.

---

### 📝 Exercise
1. Create a new file named `style.css` in your project folder.
2. Open your `index.html` and add the `<link>` tag inside the `<head>` section.
3. In `style.css`, write a rule to change the background of the whole page:
   ```css
   body { background-color: #f0f0f0; }
   ```
4. Save both files and refresh your browser. Did the color change?
