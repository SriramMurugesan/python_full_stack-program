# 03 | HTML Formatting & Lists

Now that you have a skeleton, let's learn how to format text and organize it using lists.

---

## 1. Text Formatting
We use tags to change the look and importance of text.

| Tag | Name | Effect |
| :--- | :--- | :--- |
| `<b>` | Bold | **Just visual bolding** |
| `<strong>` | Strong | **Bolding with "Importance" (SEO/Screen readers)** |
| `<i>` | Italic | *Just visual italicizing* |
| `<em>` | Emphasis | *Emphasis with "Stress" in meaning* |
| `<u>` | Underline | <u>Underlined text</u> |
| `<mark>` | Mark | <mark>Highlighted text</mark> |
| `<small>` | Small | Smaller text size |
| `<sub>` | Subscript | H<sub>2</sub>O |
| `<sup>` | Superscript | 2<sup>nd</sup> Place |

---

## 2. Organizing with Lists
Lists are everywhere—navigation menus, bullet points, even recipe steps.

### A. Unordered Lists (`<ul>`)
Used for bullet points where the order doesn't matter.
```html
<ul>
  <li>Apples</li>
  <li>Bananas</li>
  <li>Cherries</li>
</ul>
```

### B. Ordered Lists (`<ol>`)
Used for numbered steps where sequence is important.
```html
<ol>
  <li>Crack the eggs.</li>
  <li>Whisk them well.</li>
  <li>Pour into the pan.</li>
</ol>
```

### 💡 Nested Lists
You can put a list inside another list!
```html
<ul>
  <li>Fruits
    <ul>
      <li>Green Apples</li>
      <li>Red Apples</li>
    </ul>
  </li>
  <li>Vegetables</li>
</ul>
```

---

## 3. Line Breaks and Horizontal Rules
- `<br>`: Creates a single line break (does NOT need a closing tag).
- `<hr>`: Creates a horizontal line to separate content.

---

### 📝 Exercise
Update your `index.html` from the previous lesson:
1. Add an `<h3>` section titled "My Hobbies".
2. Create an **Unordered List** of 3 hobbies.
3. Use `<strong>` to bold your favorite hobby.
4. Add an `<h3>` section titled "My Daily Routine".
5. Create an **Ordered List** of 3 things you do every morning.
6. Use an `<hr>` to separate "About Me" and "Hobbies".
