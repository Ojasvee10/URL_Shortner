# 🔗 URL Shortener Microservice

A lightweight, self-hosted URL shortening service built with Python and Flask. It provides a simple REST API to shorten long URLs, track clicks, and view analytics—perfect for developers who need a private, customizable alternative to services like Bitly.

## ✨ Features

-   **Shorten URLs**: Generate unique, alphanumeric short codes for long URLs.
-   **Automatic Redirects**: Seamlessly redirect users from the short URL to the original destination.
-   **Click Analytics**: Track the number of times each short link has been clicked.
-   **RESTful API**: Clean and simple JSON API for easy integration with other applications.
-   **Input Validation**: Robust validation to ensure only proper URLs are shortened.
-   **Concurrency Safe**: Built to handle multiple requests simultaneously.

## 🛠️ Tech Stack

-   **Backend Framework**: Flask (Python)
-   **Testing**: Pytest
-   **Data Storage**: In-memory storage (Easily extendable to a database)

## 🚀 Quick Start

### Prerequisites

-   Python 3.8 or higher
-   `pip` (Python package manager)

### Installation & Setup

1.  **Clone the repository**
    ```bash
    git clone https://github.com/Ojasvee10/URL_Shortner.git
    cd URL_Shortner
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the application**
    ```bash
    python -m flask --app app.main run --reload
    ```
    The API will now be running at `http://localhost:5000`.

### Running Tests

To ensure everything is working correctly, run the test suite with Pytest:

pytest -v 

### 📖 API Documentation
1. Shorten a URL
Endpoint: POST /api/shorten

Request Body:

{
  "url": "https://www.example.com/very/long/path/that/you/want/to/shorten"
}

Response:

{
  "short_code": "abc123",
  "short_url": "http://localhost:5000/abc123"
}

2. Redirect to Original URL
Simply visit the generated short URL in your browser or use curl:

bash
curl -L http://localhost:5000/abc123
This will automatically redirect you to the original long URL.

3. Get Link Analytics
Endpoint: GET /api/stats/<short_code>

Example: GET /api/stats/abc123

Response:

json
{
  "url": "https://www.example.com/very/long/path/that/you/want/to/shorten",
  "clicks": 42,
  "created_at": "2024-01-01T10:00:00"
}
🧠 How It Works
Short Code Generation: The service generates a random 6-character alphanumeric string for each new URL.

In-Memory Storage: The mapping between the short code and the original URL is stored in a thread-safe Python dictionary.

Click Tracking: Each access to a short link increments a counter, which is visible via the analytics endpoint.

Validation: The API checks that provided URLs are well-formed before creating a short link.

🔧 Implementation Details
Concurrency Handling: Uses thread-safe data structures to handle multiple simultaneous requests.

Error Handling: Returns appropriate HTTP status codes (404 for not found, 400 for bad requests).

Scalable Design: The architecture is designed to easily swap the in-memory storage for a persistent database like Redis or SQLite.

### 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.
To ensure everything is working correctly, run the test suite with Pytest:
```bash
pytest -v
