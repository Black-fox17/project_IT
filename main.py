from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests
import math as Math
app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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

@app.get("/api/classify-number")
async def classify(number: int):
    prime_check = is_prime(number)
    perfect_check = is_perfect(number)
    armstrong_check = is_armstrong(number)
    is_even = "even" if number % 2 == 0 else "odd"

    # Fetch fun fact with error handling
    try:
        fun_fact_response = requests.get(f'http://numbersapi.com/{number}')
        fun_fact = fun_fact_response.text
    except requests.RequestException:
        fun_fact = "No fun fact available."

    properties = ["armstrong"] if armstrong_check else []
    properties.append(is_even)

    return {
        "number": number,
        "is_prime": prime_check,
        "is_perfect": perfect_check,
        "properties": properties,
        "digit_sum": sum(int(digit) for digit in str(number)),
        "fun_fact": fun_fact
    }