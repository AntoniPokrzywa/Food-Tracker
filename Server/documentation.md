## Auth API Endpoints

### 1. Register

- **Endpoint:** `POST /register`
- **Description:** Creates a new user account.
- **Request Body (JSON):**
  ```json
  {
    "email": "user@example.com",
    "password": "yourPassword"
  }
  ```
- **Responses:**
  - `201 Created`  
    ```json
    { "message": "Account created successfully" }
    ```
  - `400 Bad Request`  
    - If email or password is missing:
      ```json
      { "detail": "Email and password are required" }
      ```
    - If account already exists:
      ```json
      { "detail": "Account with this email already exists" }
      ```
    - If request is not valid JSON:
      ```json
      { "detail": "Request is not valid json" }
      ```

---

### 2. Login

- **Endpoint:** `POST /login`
- **Description:** Authenticates a user and starts a session.
- **Request Body (JSON):**
  ```json
  {
    "email": "user@example.com",
    "password": "yourPassword"
  }
  ```
- **Responses:**
  - `200 OK`  
    ```json
    { "detail": "Login successful" }
    ```
  - `400 Bad Request`  
    - If email or password is missing:
      ```json
      { "detail": "Email and password are required" }
      ```
    - If credentials are invalid:
      ```json
      { "detail": "Invalid credentials" }
      ```
    - If request is not valid JSON:
      ```json
      { "detail": "Request is not valid json" }
      ```
  - `500 Internal Server detail`  
    - If multiple users found with the same email:
      ```json
      { "detail": "Internal Server detail" }
      ```

- **Session:**  
  On successful login, a session cookie is set (`session["user_id"]`).

---

### 3. Logout

- **Endpoint:** `POST /logout`
- **Description:** Logs out the current user and clears the session.
- **Request Body:** _None_
- **Responses:**
  - `200 OK`  
    ```json
    { "message": "Logout successful" }
    ```


# TODO add docs for meals endpoints
