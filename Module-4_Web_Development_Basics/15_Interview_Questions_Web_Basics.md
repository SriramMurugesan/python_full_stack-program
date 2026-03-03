# 15 | Interview Questions: Web Basics

Preparing for a technical interview? Here are the most common questions you'll face regarding HTML and CSS architecture.

---

### 1. What is the difference between a `<div>` and a `<span>`?
- **Answer:** A `<div>` is a **block-level** element (takes up full width, starts on a new line). A `<span>` is an **inline** element (only takes up as much width as its content, stays on the same line).

### 2. Can you explain the CSS Box Model?
- **Answer:** The Box Model consists of four layers: **Content** (text/image), **Padding** (inner space), **Border** (the edge), and **Margin** (outer space). It determines how much space an element occupies and how it interacts with neighbors.

### 3. What is the purpose of the `alt` attribute in an `<img>` tag?
- **Answer:** It provides **alternative text** if the image fails to load. It is critical for **Accessibility** (screen readers for the visually impaired) and **SEO** (Search Engine Optimization).

### 4. What are 'Semantic Tags' and why should we use them?
- **Answer:** Semantic tags like `<header>`, `<main>`, and `<footer>` describe their content's meaning to the browser. They improve SEO, make code more readable, and enhance accessibility.

### 5. What is the difference between `display: none` and `visibility: hidden`?
- **Answer:** `display: none` removes the element entirely from the layout (the page acts as if it's not there). `visibility: hidden` hides the element, but the empty space it occupied remains.

### 6. Explain the difference between `px`, `em`, and `rem`.
- **Answer:** 
  - `px`: Fixed pixels (static).
  - `em`: Relative to the font-size of its **parent** element.
  - `rem`: Relative to the font-size of the **root** (`<html>`) element.

### 7. How do you center a `<div>` horizontally and vertically?
- **Answer:** The modern way is using **Flexbox**:
  ```css
  .parent {
    display: flex;
    justify-content: center; /* Horizontal */
    align-items: center;     /* Vertical */
    height: 100vh;           /* Parent must have height */
  }
  ```

### 8. What is a CSS Media Query?
- **Answer:** A media query is a CSS technique used to apply styles based on device characteristics, usually screen width. It's the foundation of **Responsive Web Design**.

### 9. What is the `DOCTYPE` declaration for?
- **Answer:** It tells the browser which version of HTML the page is written in (e.g., `<!DOCTYPE html>` for HTML5). It prevents the browser from entering "quirks mode."

### 10. In a form, what is the difference between `GET` and `POST` methods?
- **Answer:** 
  - `GET`: Appends data to the URL (visible, limited size). Best for searches.
  - `POST`: Sends data in the request body (hidden, unlimited size). Best for sensitive info like passwords.
