# 13 | Capstone Project: Build Your Personal Portfolio

It's time to put everything together! You will build a one-page responsive portfolio website.

---

## 🎯 The Goal
A website that includes:
1. **Header:** Your name and a navigation menu (Flexbox).
2. **Hero Section:** An image of you (or a placeholder) and a "Hire Me" button.
3. **About Me:** A clean section with text and maybe a list of your top 3 values.
4. **Skills:** A grid of your skills (CSS Grid).
5. **Contact:** A functional-looking contact form (Forms).
6. **Footer:** Copyright info and social media links.

---

## 🏗️ Step-by-Step Instructions

### Step 1: Structure (HTML)
- Use semantic tags: `<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`.
- Link your `style.css`.

### Step 2: Styling (CSS)
- Set a global font in `*`.
- Give your sections some padding so they don't touch the screen edges.
- Use `display: flex` to align your navigation items.

### Step 3: Layout (Grid)
- Create a 3-column grid for your skills on Desktop.
- Ensure the background colors are harmonious (e.g., Dark Mode: `#1a1a1a` background with `#ffffff` text).

### Step 4: Responsiveness
- Add a media query for `< 768px`.
- Change the skills grid to only 1 column so it's readable on phones.
- Make your image smaller for mobile users.

---

## 💡 Pro Tip: Hover Effects
Make your site feel "alive" by adding hover effects to buttons:
```css
button:hover {
  background-color: darkblue;
  transform: translateY(-5px); /* Moves it up slightly! */
  transition: 0.3s; /* Makes the movement smooth */
}
```

---

### 📝 Review Checklist
- [ ] Does it have a boilerplate?
- [ ] Are all images visible?
- [ ] Do the links work?
- [ ] Is it readable on a phone?
- [ ] Is there a contact form?

**Congratulations! You are now a Front-End Beginner-Expert!**
