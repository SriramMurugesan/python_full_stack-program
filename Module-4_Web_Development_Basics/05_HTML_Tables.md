# 05 | HTML Tables: Structuring Data

Tables are used to display data in a grid (rows and columns), such as a product list, a schedule, or a leaderboard.

---

## 1. Table structure
Creating a table requires multiple nested tags.

- `<table>`: The container for the whole table.
- `<tr>`: **Table Row**. Every row starts here.
- `<th>`: **Table Header**. Used for the top row (bold and centered by default).
- `<td>`: **Table Data**. Used for the regular cells.

### 📊 A Simple Example
```html
<table border="1"> <!-- Border is just for visualization (Styling belongs in CSS!) -->
  <tr>
    <th>Course</th>
    <th>Duration</th>
    <th>Instructor</th>
  </tr>
  <tr>
    <td>Python Basics</td>
    <td>4 Weeks</td>
    <td>Sriram</td>
  </tr>
  <tr>
    <td>Web Fundamentals</td>
    <td>3 Weeks</td>
    <td>Antigravity</td>
  </tr>
</table>
```

---

## 2. Advanced: Spanning Rows and Columns
Sometimes you want a cell to take up more than one box.

### A. Column Span (`colspan`)
Makes a cell stretch across multiple columns.
```html
<tr>
  <td colspan="2">This cell covers two columns</td>
  <td>Normal cell</td>
</tr>
```

### B. Row Span (`rowspan`)
Makes a cell stretch down across multiple rows.
```html
<tr>
  <td rowspan="2">This cell covers two rows</td>
  <td>Row 1 Content</td>
</tr>
<tr>
  <td>Row 2 Content</td>
</tr>
```

---

## 3. Table Sections (Semantic)
For very large tables, we use these tags to help the browser:
- `<thead>`: Wraps the header row(s).
- `<tbody>`: Wraps the body content.
- `<tfoot>`: Wraps the summary or footer row.

---

### 📝 Exercise
1. Add a table to your `index.html` titled "My Skill Progress".
2. The table should have 3 columns: **Skill**, **Level**, and **Confidence**.
3. Add 3 rows of your skills (e.g., HTML, Python, Logic).
4. Use `colspan` to add a bottom row that says "Total Experience: 1 Year" stretching across all 3 columns.
