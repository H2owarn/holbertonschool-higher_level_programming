
## Differences Between HTTP and HTTPS



| Feature | HTTP     | HTTPS                |
| :-------- | :------- | :------------------------- |
| **Security** | No encryption | Encrypts data using SSL/TLS |
| **Data Protection** | Vulnerable to interception | Protects against eavesdropping |
| **Port Used**| Port 80 | Port 443 |
| **SEO & Trust** | Not preferred by search engines |  Your API keyGoogle ranks HTTPS sites higher |
| **Usage** | non-sensitive data | sensitive data |

## Structure of an HTTP Request and Response

When a browser requests a webpage, it sends an HTTP request, and the server responds with an HTTP response.
- Example HTTP Request Structure

```bash
GET /index.html HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
Accept: text/html
```

- Method: `GET` (requests a resource)
- Path: `/index.html` (specific file being requested)
- Protocol: `HTTP/1.1` (version of HTTP)
- Headers: Additional information like `User-Agent` (browser type) and `Accept` (expected response format)


- Example HTTP Response Structure

```bash
GET /index.html HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
Accept: text/html
```

- Status Code: `200 OK` (successful request)
- Headers: `Content-Type` (format of response), `Content-Length` (size of response), `Server` (server type)
- Body: Contains the actual webpage content

