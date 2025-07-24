## 📗 README 3: Java


```markdown
# Java for Frontend (Uncommon but Possible)

Java is typically used on the backend, but with tools like JSP or applets (legacy), it has touched frontend contexts.

## ☕ Java and the Web
Although modern frontend development relies on HTML/CSS/JavaScript, Java can integrate via:

### 1. JSP (Java Server Pages)
Used in server-side rendering of HTML pages.

### 2. Java Applets (Deprecated)
Historically used to run small programs in the browser. Not recommended anymore.

## 💡 Java and Frontend Integration
- Java can serve dynamic content to HTML via servlets
- Libraries like Thymeleaf (in Spring Boot) render templates using Java code

### 🧪 Code Snippet: JSP Example
```jsp
<h2>Welcome, <%= request.getAttribute("username") %>!</h2>