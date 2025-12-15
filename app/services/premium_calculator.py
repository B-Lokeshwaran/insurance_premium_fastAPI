def calculate_premium(base_amount: float, age: int, risk_factor: float):
   age_factor = 1.2 if age > 45 else 1.0
   return base_amount * risk_factor * age_factor