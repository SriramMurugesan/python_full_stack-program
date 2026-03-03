# 01 | Web Architecture: How the Web Works

Before we write a single line of code, we must understand the environment where our code lives: the **World Wide Web**.

## 1. The Client-Server Model
The entire web operates on a simple relationship: **Someone asks, someone provides.**

- **The Client:** This is your web browser (Chrome, Firefox, Safari). It acts like a customer in a restaurant. It "orders" information.
- **The Server:** This is a powerful computer located somewhere in the world that stores the website's files. It acts like the kitchen. It "serves" the requested information.

### 🔄 The Cycle (Request-Response)
1. **Request:** You type `www.google.com` and press Enter. Your browser sends a message (HTTP Request) asking for Google's homepage.
2. **Transfer:** This request travels through wires and satellites.
3. **Processing:** Google's server receives the request and finds the `index.html` file.
4. **Response:** The server sends the file back (HTTP Response) to your browser.
5. **Rendering:** Your browser reads the code and builds the beautiful page you see.

---

## 2. IP Addresses and DNS (The Phonebook of the Web)
Every computer on the internet has a unique address called an **IP Address** (e.g., `142.250.190.46`).

Since humans are bad at remembering numbers, we use names like `google.com`.
- **DNS (Domain Name System):** Think of this as the internet's contacts list. When you type a URL, the DNS looks up the corresponding IP address so your browser knows which server to talk to.

---

## 3. HTTP vs. HTTPS
- **HTTP (HyperText Transfer Protocol):** The language used for the Request-Response cycle.
- **HTTPS (HyperText Transfer Protocol Secure):** The "S" stands for **Secure**. It encrypts the data sent between client and server, meaning hackers can't read your passwords or credit card info during transit.

---

## 4. Front-End vs. Back-End
- **Front-End (The Client Side):** Everything you see and interact with. Built using **HTML, CSS, and JavaScript**.
- **Back-End (The Server Side):** The "brain" behind the scenes. It handles databases, user accounts, and logic. Built using **Python (Django), Node.js, PHP, etc.**

> [!TIP]
> **Analogy Time:** A car's dashboard and steering wheel are the Front-End. The engine under the hood is the Back-End.

---

## Summary Table
| Component | Function | Analogy |
| :--- | :--- | :--- |
| **Browser** | Displays the web page | The Customer |
| **Server** | Stores website files | The Kitchen |
| **IP Address** | Unique ID of a computer | Home Address |
| **DNS** | Matches names to IP addresses | Phonebook |
| **HTTP(S)** | Protocol for communication | The Language |

---

### 📝 Exercise
Open your browser, right-click anywhere on a page, and select **"Inspect"**. You are now looking at the "Front-End" code that the server "Responded" with!
