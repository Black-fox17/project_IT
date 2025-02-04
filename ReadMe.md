# Number Classification API - HNG Stage 1 Internship

## Author
**Ayeleru Abdulsalam Oluwaseun**

## Description
This is a FastAPI-based number classification API built for the HNG Stage 1 Internship. The API classifies numbers based on different mathematical properties and provides additional fun facts.

## Features
- Checks if a number is **prime**
- Determines if a number is **perfect**
- Identifies **Armstrong numbers**
- Classifies the number as **even or odd**
- Computes the **sum of its digits**
- Fetches a **fun fact** about the number from [numbersapi.com](http://numbersapi.com)

## Endpoints
### 1. Classify a Number
**Endpoint:** `GET /api/classify-number`

**Query Parameter:**
- `number` (int) - The number to classify

**Example Request:**
```
GET http://127.0.0.1:8000/api/classify-number?number=23
```

**Example Response:**
```json
{
    "number": 23,
    "is_prime": true,
    "is_perfect": false,
    "properties": ["odd"],
    "digit_sum": 5,
    "fun_fact": "23 is the number of chromosomes in a human gamete."
}
```

## Installation & Setup
### Prerequisites
Ensure you have Python 3.7+ installed.

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/Black-fox17/project_IT.git
   cd number-classification-api
   ```
2. Install dependencies:
   ```sh
   pip install fastapi uvicorn requests
   ```
3. Run the application:
   ```sh
   uvicorn main:app --reload
   ```

## CORS Setup
The API includes CORS middleware to allow requests from all origins:
```python
origins = ["*"]
```
Modify the list to allow additional domains.

## Thanks