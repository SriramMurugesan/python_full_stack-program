# 06 | HTML Forms: User Interaction

Forms are how we collect data from users—logging in, signing up for a newsletter, or searching for products.

---

## 1. The `<form>` Container
The `<form>` tag wraps all input elements. It has two specific attributes you must know:
- `action`: Where to send the data (e.g., a URL of a server).
- `method`: How to send it (`GET` or `POST`).

```html
<form action="/submit-data" method="POST">
  <!-- Inputs go here -->
</form>
```

---

## 2. Common Input Types (`<input>`)
The `<input>` tag changes its behavior based on the `type` attribute.

| Type | Use Case | Result |
| :--- | :--- | :--- |
| `text` | Names, addresses | Single-line text box |
| `password` | Passwords | Hides characters as dots |
| `email` | Email addresses | Validates if format is correct |
| `number` | Ages, counts | Only allows numeric input |
| `date` | Birthdays | Shows a calendar picker |
| `checkbox` | Multiple choices | Square boxes to tick |
| `radio` | Single choice | Circle buttons (only one can be selected) |
| `file` | Profile pictures | File upload button |
| `submit` | Sending the form | A button that sends the data |

---

## 3. Labels and Placeholders
- **Labels (`<label>`):** Makes forms accessible and clickable. Clicking a label focuses the input.
- **Placeholder:** Ghost text that tells the user what to type.

```html
<label for="username">Username:</label>
<input type="text" id="username" name="user" placeholder="Enter your handle">
```

---

## 4. Other Form Elements
- **`<textarea>`:** For long text (messages, comments).
- **`<select>` & `<option>`:** For dropdown menus.
```html
<select name="cars">
  <option value="volvo">Volvo</option>
  <option value="tesla">Tesla</option>
</select>
```

---

## 5. Basic Validation
- `required`: Prevents form submission if empty.
- `minlength`/`maxlength`: Limits character count.

---

### 📝 Exercise
Create a new file named `contact.html` and build a contact form with:
1. A **Name** input (Text, Required).
2. An **Email** input (Email).
3. A **Reason for Contact** dropdown (Options: Job, Bug, Just Hello).
4. A **Message** area (Textarea).
5. A **Checkbox** that says "I agree to the terms".
6. A **Submit Button** that says "Send Message".
