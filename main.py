from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import requests
import math as Math

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def is_prime(num: int) -> bool:
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(Math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def is_perfect(num: int) -> bool:
    """Check if a number is a perfect number."""
    if num < 1:  # Negative numbers cannot be perfect numbers
        return False
    return num == sum(i for i in range(1, num) if num % i == 0)

def is_armstrong(num: int) -> bool:
    """Check if a number is an Armstrong number."""
    if num < 0:
        return False  # Negative numbers cannot be Armstrong numbers
    digits = [int(digit) for digit in str(num)]
    power = len(digits)
    return num == sum(d ** power for d in digits)

@app.get("/api/classify-number")
async def classify(number: str):
    # Check for invalid numbers
    try:
        number = int(number)
    except ValueError:
        return JSONResponse(
            status_code=400,
            content={
                "number": "alphabet",
                "error": True
            }
        )

    prime_check = is_prime(number)
    perfect_check = is_perfect(number)
    armstrong_check = is_armstrong(number)
    is_even = "even" if number % 2 == 0 else "odd"

    # Fetch fun fact only if the number is valid
    fun_fact = "No fun fact available."
    try:
        response = requests.get(f"http://numbersapi.com/{number}/math")
        if response.status_code == 200:
                fun_fact = response.text
    except requests.RequestException:
        pass  # Handle failure gracefully

    # Determine properties
    properties = []
    if armstrong_check:
        properties.append("armstrong")
    properties.append(is_even)

    response_data = {
        "number": number,
        "is_prime": prime_check,
        "is_perfect": perfect_check,
        "properties": properties,
        "digit_sum": sum(int(digit) for digit in str((number if number > 0 else -number))),
        "fun_fact": fun_fact
    }

    return JSONResponse(content=response_data)
