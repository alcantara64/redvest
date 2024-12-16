# Mock Data
user_performance = [0.5, -0.2, 1.0, -0.3, 0.7]  # User's daily returns (%)
sp500_performance = [0.3, -0.1, 0.8, -0.2, 0.6]  # S&P 500 returns (%)

def calculate_alpha_beta(user_performance, sp500_performance):
    user_excess = [u - s for u, s in zip(user_performance, sp500_performance)]
    beta = sum(u * s for u, s in zip(user_performance, sp500_performance)) / sum(s ** 2 for s in sp500_performance)
    alpha = sum(user_excess) / len(user_performance)
    return round(alpha, 3), round(beta, 3)

def ask_gpt(question, user_performance, sp500_performance):
    # Calculate metrics
    alpha, beta = calculate_alpha_beta(user_performance, sp500_performance)
    
    # Construct a response for the GPT prompt
    response = f"""
    User performance data: {user_performance}
    S&P 500 performance data: {sp500_performance}
    Alpha: {alpha}, Beta: {beta}.
    Your Question: {question}
    """
    return f"Mock GPT Answer: Based on the data, {response}"

# Demo
print(ask_gpt("What was my alpha last week?", user_performance, sp500_performance))
print(ask_gpt("How volatile was my trading?", user_performance, sp500_performance))
