from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests
import math as Math
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    # Add other origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(Math.sqrt(num)) + 1):  # Corrected range
        if num % i == 0:
            return False
    return True

def is_perfect(num):
    total = sum(i for i in range(1, num) if num % i == 0)
    return total == num

def is_armstrong(number):
    digits = [int(digit) for digit in str(number)]
    power = len(digits)
    return number == sum(d ** power for d in digits)

@app.get("/api/classify-number/{num}")
async def classify(num: int):
    prime_check = is_prime(num)
    perfect_check = is_perfect(num)
    armstrong_check = is_armstrong(num)
    is_even = "even" if num % 2 == 0 else "odd"

    # Fetch fun fact with error handling
    try:
        fun_fact_response = requests.get(f'http://numbersapi.com/{num}')
        fun_fact = fun_fact_response.text
    except requests.RequestException:
        fun_fact = "No fun fact available."

    properties = ["armstrong"] if armstrong_check else []
    properties.append(is_even)

    return {
        "number": num,
        "is_prime": prime_check,
        "is_perfect": perfect_check,
        "properties": properties,
        "digit_sum": sum(int(digit) for digit in str(num)),
        "fun_fact": fun_fact
    }