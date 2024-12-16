import numpy as np

# Mock Data
users = [
    {"user_id": "user1", "session_duration": 120, "performance": [0.4, -0.1, 0.8, 0.1, 0.5]},
    {"user_id": "user2", "session_duration": 200, "performance": [0.3, -0.2, 1.0, 0.0, 0.6]},
    {"user_id": "user3", "session_duration": 150, "performance": [0.5, -0.3, 0.9, -0.2, 0.7]},
]
sp500_performance = [0.3, -0.1, 0.8, -0.2, 0.6]

# Function to calculate alpha and beta
def calculate_alpha_beta(user_performance, sp500_performance):
    user_excess = np.array(user_performance) - np.array(sp500_performance)
    beta = np.cov(user_performance, sp500_performance)[0, 1] / np.var(sp500_performance)
    alpha = np.mean(user_excess)
    return round(alpha, 3), round(beta, 3)

# Function to analyze user activity
def analyze_users(users, sp500_performance):
    top_user = max(users, key=lambda x: x['session_duration'])
    print(f"Top user by activity: {top_user['user_id']} with session duration {top_user['session_duration']} minutes.")
    
    for user in users:
        alpha, beta = calculate_alpha_beta(user['performance'], sp500_performance)
        print(f"User: {user['user_id']} - Alpha: {alpha}, Beta: {beta}")

# Demo
analyze_users(users, sp500_performance)
