# templates.py - All B2C synthetic data templates

TEMPLATES = {
    "Custom": {"description": "Build your own schema", "columns": []},
    
    "Customer Records": {
        "description": "Complete customer database with demographics and preferences",
        "columns": [
            {"name": "customer_id", "type": "string", "pattern": "CUST-{random_int:10000:99999}", "null_rate": 0},
            {"name": "first_name", "type": "first_name", "null_rate": 0},
            {"name": "last_name", "type": "last_name", "null_rate": 0},
            {"name": "email", "type": "email", "null_rate": 0.02},
            {"name": "phone", "type": "phone", "null_rate": 0.1},
            {"name": "date_of_birth", "type": "date", "start_date": "1950-01-01", "end_date": "2005-12-31", "null_rate": 0.05},
            {"name": "gender", "type": "choice", "choices": ["Male", "Female", "Non-binary", "Prefer not to say"], "weights": [45, 45, 5, 5], "null_rate": 0.03},
            {"name": "address", "type": "address", "null_rate": 0.08},
            {"name": "city", "type": "city", "null_rate": 0.02},
            {"name": "state", "type": "state", "null_rate": 0.02},
            {"name": "zip_code", "type": "zipcode", "null_rate": 0.05},
            {"name": "registration_date", "type": "date", "start_date": "2020-01-01", "end_date": "2024-12-31", "null_rate": 0},
            {"name": "customer_tier", "type": "choice", "choices": ["Bronze", "Silver", "Gold", "Platinum"], "weights": [40, 30, 20, 10], "null_rate": 0},
            {"name": "lifetime_value", "type": "float", "min_val": 0, "max_val": 50000, "decimals": 2, "null_rate": 0}
        ]
    },
    
    "Restaurant POS Data": {
        "description": "Point of sale transactions for restaurant business",
        "columns": [
            {"name": "transaction_id", "type": "string", "pattern": "TXN-{random_int:100000:999999}", "null_rate": 0},
            {"name": "order_number", "type": "integer", "min_val": 1, "max_val": 99999, "null_rate": 0},
            {"name": "timestamp", "type": "timestamp", "start_date": "2024-01-01", "end_date": "2024-12-31", "null_rate": 0},
            {"name": "table_number", "type": "integer", "min_val": 1, "max_val": 50, "null_rate": 0.1},
            {"name": "server_id", "type": "choice", "choices": ["SRV001", "SRV002", "SRV003", "SRV004", "SRV005", "SRV006"], "null_rate": 0},
            {"name": "item_name", "type": "choice", "choices": ["Burger", "Pizza", "Salad", "Pasta", "Steak", "Fish", "Chicken", "Soup", "Sandwich", "Dessert"], "null_rate": 0},
            {"name": "category", "type": "choice", "choices": ["Appetizer", "Main Course", "Dessert", "Beverage", "Side"], "weights": [15, 50, 15, 15, 5], "null_rate": 0},
            {"name": "quantity", "type": "integer", "min_val": 1, "max_val": 5, "null_rate": 0},
            {"name": "unit_price", "type": "float", "min_val": 5.99, "max_val": 49.99, "decimals": 2, "null_rate": 0},
            {"name": "total_amount", "type": "float", "min_val": 5.99, "max_val": 200.00, "decimals": 2, "null_rate": 0},
            {"name": "payment_method", "type": "choice", "choices": ["Credit Card", "Debit Card", "Cash", "Mobile Pay"], "weights": [45, 25, 20, 10], "null_rate": 0},
            {"name": "tip_amount", "type": "float", "min_val": 0, "max_val": 50.00, "decimals": 2, "null_rate": 0.1},
            {"name": "customer_satisfaction", "type": "integer", "min_val": 1, "max_val": 5, "null_rate": 0.2}
        ]
    },
    
    "Retail POS Data": {
        "description": "Point of sale transactions for retail business",
        "columns": [
            {"name": "transaction_id", "type": "string", "pattern": "RTL-{random_int:100000:999999}", "null_rate": 0},
            {"name": "store_id", "type": "choice", "choices": ["ST001", "ST002", "ST003", "ST004", "ST005"], "null_rate": 0},
            {"name": "cashier_id", "type": "choice", "choices": ["CSH001", "CSH002", "CSH003", "CSH004", "CSH005", "CSH006"], "null_rate": 0},
            {"name": "timestamp", "type": "timestamp", "start_date": "2024-01-01", "end_date": "2024-12-31", "null_rate": 0},
            {"name": "product_sku", "type": "string", "pattern": "SKU-{random_int:10000:99999}", "null_rate": 0},
            {"name": "product_name", "type": "choice", "choices": ["T-Shirt", "Jeans", "Sneakers", "Jacket", "Dress", "Shorts", "Sweater", "Hat", "Belt", "Socks"], "null_rate": 0},
            {"name": "category", "type": "choice", "choices": ["Clothing", "Footwear", "Accessories", "Electronics", "Home"], "weights": [40, 25, 15, 15, 5], "null_rate": 0},
            {"name": "brand", "type": "choice", "choices": ["Nike", "Adidas", "Levi's", "Zara", "H&M", "Gap", "Uniqlo", "Target"], "null_rate": 0},
            {"name": "size", "type": "choice", "choices": ["XS", "S", "M", "L", "XL", "XXL"], "weights": [5, 20, 30, 25, 15, 5], "null_rate": 0.3},
            {"name": "color", "type": "choice", "choices": ["Black", "White", "Blue", "Red", "Green", "Gray", "Brown", "Pink"], "null_rate": 0.1},
            {"name": "quantity", "type": "integer", "min_val": 1, "max_val": 10, "null_rate": 0},
            {"name": "unit_price", "type": "float", "min_val": 9.99, "max_val": 299.99, "decimals": 2, "null_rate": 0},
            {"name": "discount_percent", "type": "float", "min_val": 0, "max_val": 50, "decimals": 1, "null_rate": 0.6},
            {"name": "total_amount", "type": "float", "min_val": 9.99, "max_val": 1500.00, "decimals": 2, "null_rate": 0},
            {"name": "payment_method", "type": "choice", "choices": ["Credit Card", "Debit Card", "Cash", "Gift Card", "Mobile Pay"], "weights": [40, 25, 15, 10, 10], "null_rate": 0}
        ]
    },
    
    "Product Reviews": {
        "description": "Customer product reviews and ratings",
        "columns": [
            {"name": "review_id", "type": "string", "pattern": "REV-{random_int:100000:999999}", "null_rate": 0},
            {"name": "product_id", "type": "string", "pattern": "PROD-{random_int:10000:99999}", "null_rate": 0},
            {"name": "customer_id", "type": "string", "pattern": "CUST-{random_int:10000:99999}", "null_rate": 0},
            {"name": "rating", "type": "integer", "min_val": 1, "max_val": 5, "null_rate": 0},
            {"name": "review_title", "type": "sentence", "min_words": 3, "max_words": 8, "null_rate": 0.1},
            {"name": "review_text", "type": "text", "min_sentences": 1, "max_sentences": 5, "null_rate": 0.05},
            {"name": "verified_purchase", "type": "boolean", "true_rate": 0.85, "null_rate": 0},
            {"name": "helpful_votes", "type": "integer", "min_val": 0, "max_val": 100, "null_rate": 0},
            {"name": "review_date", "type": "date", "start_date": "2023-01-01", "end_date": "2024-12-31", "null_rate": 0},
            {"name": "reviewer_location", "type": "city", "null_rate": 0.2},
            {"name": "product_category", "type": "choice", "choices": ["Electronics", "Clothing", "Home", "Books", "Sports", "Beauty", "Toys"], "null_rate": 0},
            {"name": "review_sentiment", "type": "choice", "choices": ["Positive", "Neutral", "Negative"], "weights": [60, 25, 15], "null_rate": 0}
        ]
    },
    
    "E-commerce Transactions": {
        "description": "Online shopping transaction data",
        "columns": [
            {"name": "order_id", "type": "string", "pattern": "ORD-{random_int:100000:999999}", "null_rate": 0},
            {"name": "customer_id", "type": "string", "pattern": "CUST-{random_int:10000:99999}", "null_rate": 0},
            {"name": "order_date", "type": "timestamp", "start_date": "2024-01-01", "end_date": "2024-12-31", "null_rate": 0},
            {"name": "product_id", "type": "string", "pattern": "PROD-{random_int:10000:99999}", "null_rate": 0},
            {"name": "product_name", "type": "choice", "choices": ["Laptop", "Phone", "Headphones", "Watch", "Tablet", "Camera", "Speaker", "Monitor"], "null_rate": 0},
            {"name": "quantity", "type": "integer", "min_val": 1, "max_val": 5, "null_rate": 0},
            {"name": "unit_price", "type": "float", "min_val": 19.99, "max_val": 1999.99, "decimals": 2, "null_rate": 0},
            {"name": "shipping_cost", "type": "float", "min_val": 0, "max_val": 25.99, "decimals": 2, "null_rate": 0},
            {"name": "tax_amount", "type": "float", "min_val": 0, "max_val": 200.00, "decimals": 2, "null_rate": 0},
            {"name": "total_amount", "type": "float", "min_val": 19.99, "max_val": 5000.00, "decimals": 2, "null_rate": 0},
            {"name": "payment_method", "type": "choice", "choices": ["Credit Card", "PayPal", "Apple Pay", "Google Pay", "Bank Transfer"], "weights": [50, 25, 10, 10, 5], "null_rate": 0},
            {"name": "shipping_address", "type": "address", "null_rate": 0},
            {"name": "order_status", "type": "choice", "choices": ["Pending", "Processing", "Shipped", "Delivered", "Cancelled"], "weights": [5, 10, 20, 60, 5], "null_rate": 0},
            {"name": "delivery_date", "type": "date", "start_date": "2024-01-01", "end_date": "2024-12-31", "null_rate": 0.1}
        ]
    },
    
    "Voice of Customer (VOC)": {
        "description": "Customer feedback and voice of customer data",
        "columns": [
            {"name": "feedback_id", "type": "string", "pattern": "VOC-{random_int:100000:999999}", "null_rate": 0},
            {"name": "customer_id", "type": "string", "pattern": "CUST-{random_int:10000:99999}", "null_rate": 0},
            {"name": "survey_id", "type": "string", "pattern": "SURV-{random_int:1000:9999}", "null_rate": 0},
            {"name": "feedback_date", "type": "timestamp", "start_date": "2024-01-01", "end_date": "2024-12-31", "null_rate": 0},
            {"name": "touchpoint", "type": "choice", "choices": ["Website", "Mobile App", "Call Center", "Email", "In-Store", "Social Media"], "weights": [25, 20, 15, 15, 20, 5], "null_rate": 0},
            {"name": "sentiment_score", "type": "float", "min_val": -1.0, "max_val": 1.0, "decimals": 3, "null_rate": 0},
            {"name": "nps_score", "type": "integer", "min_val": 0, "max_val": 10, "null_rate": 0.1},
            {"name": "csat_score", "type": "integer", "min_val": 1, "max_val": 5, "null_rate": 0.05},
            {"name": "feedback_text", "type": "text", "min_sentences": 1, "max_sentences": 4, "null_rate": 0.02},
            {"name": "category", "type": "choice", "choices": ["Product Quality", "Customer Service", "Pricing", "Delivery", "Website", "General"], "weights": [25, 30, 10, 15, 10, 10], "null_rate": 0},
            {"name": "priority", "type": "choice", "choices": ["Low", "Medium", "High", "Critical"], "weights": [40, 35, 20, 5], "null_rate": 0},
            {"name": "resolved", "type": "boolean", "true_rate": 0.75, "null_rate": 0}
        ]
    },
    
    "Marketing Campaign Data": {
        "description": "Marketing campaign performance and engagement metrics",
        "columns": [
            {"name": "campaign_id", "type": "string", "pattern": "CAMP-{random_int:10000:99999}", "null_rate": 0},
            {"name": "customer_id", "type": "string", "pattern": "CUST-{random_int:10000:99999}", "null_rate": 0},
            {"name": "campaign_name", "type": "choice", "choices": ["Summer Sale", "Black Friday", "Holiday Special", "New Product Launch", "Back to School", "Spring Collection"], "null_rate": 0},
            {"name": "channel", "type": "choice", "choices": ["Email", "Social Media", "Display Ads", "Search Ads", "Direct Mail", "SMS"], "weights": [30, 25, 20, 15, 5, 5], "null_rate": 0},
            {"name": "send_date", "type": "timestamp", "start_date": "2024-01-01", "end_date": "2024-12-31", "null_rate": 0},
            {"name": "opened", "type": "boolean", "true_rate": 0.22, "null_rate": 0},
            {"name": "clicked", "type": "boolean", "true_rate": 0.03, "null_rate": 0},
            {"name": "converted", "type": "boolean", "true_rate": 0.015, "null_rate": 0},
            {"name": "revenue_generated", "type": "float", "min_val": 0, "max_val": 500.00, "decimals": 2, "null_rate": 0.8},
            {"name": "cost_per_send", "type": "float", "min_val": 0.01, "max_val": 5.00, "decimals": 3, "null_rate": 0},
            {"name": "audience_segment", "type": "choice", "choices": ["High Value", "Frequent Buyers", "New Customers", "Lapsed", "VIP", "General"], "weights": [15, 25, 20, 15, 10, 15], "null_rate": 0}
        ]
    },
    
    "User Behavior/Clickstream": {
        "description": "Website and app user behavior tracking",
        "columns": [
            {"name": "session_id", "type": "string", "pattern": "SESS-{random_int:1000000:9999999}", "null_rate": 0},
            {"name": "user_id", "type": "string", "pattern": "USER-{random_int:10000:99999}", "null_rate": 0.1},
            {"name": "timestamp", "type": "timestamp", "start_date": "2024-01-01", "end_date": "2024-12-31", "null_rate": 0},
            {"name": "page_url", "type": "choice", "choices": ["/home", "/products", "/cart", "/checkout", "/account", "/search", "/category/electronics", "/category/clothing"], "weights": [20, 25, 10, 5, 8, 12, 10, 10], "null_rate": 0},
            {"name": "action", "type": "choice", "choices": ["page_view", "click", "scroll", "form_submit", "search", "add_to_cart", "purchase"], "weights": [40, 25, 15, 5, 8, 5, 2], "null_rate": 0},
            {"name": "device_type", "type": "choice", "choices": ["Desktop", "Mobile", "Tablet"], "weights": [45, 45, 10], "null_rate": 0},
            {"name": "browser", "type": "choice", "choices": ["Chrome", "Safari", "Firefox", "Edge", "Other"], "weights": [50, 25, 15, 8, 2], "null_rate": 0},
            {"name": "referrer", "type": "choice", "choices": ["Direct", "Google", "Facebook", "Email", "Other"], "weights": [35, 30, 15, 15, 5], "null_rate": 0.2},
            {"name": "session_duration", "type": "integer", "min_val": 30, "max_val": 3600, "null_rate": 0.1},
            {"name": "pages_viewed", "type": "integer", "min_val": 1, "max_val": 20, "null_rate": 0},
            {"name": "location", "type": "city", "null_rate": 0.3}
        ]
    },
    
    "Social Media Engagement": {
        "description": "Social media posts and engagement metrics",
        "columns": [
            {"name": "post_id", "type": "string", "pattern": "POST-{random_int:100000:999999}", "null_rate": 0},
            {"name": "user_id", "type": "string", "pattern": "USER-{random_int:10000:99999}", "null_rate": 0},
            {"name": "platform", "type": "choice", "choices": ["Instagram", "Facebook", "Twitter", "TikTok", "LinkedIn"], "weights": [30, 25, 20, 15, 10], "null_rate": 0},
            {"name": "post_type", "type": "choice", "choices": ["Photo", "Video", "Story", "Reel", "Text"], "weights": [30, 25, 20, 15, 10], "null_rate": 0},
            {"name": "post_date", "type": "timestamp", "start_date": "2024-01-01", "end_date": "2024-12-31", "null_rate": 0},
            {"name": "content_category", "type": "choice", "choices": ["Product", "Lifestyle", "Behind-the-scenes", "User-generated", "Educational", "Promotional"], "weights": [25, 20, 15, 15, 15, 10], "null_rate": 0},
            {"name": "likes", "type": "integer", "min_val": 0, "max_val": 10000, "null_rate": 0},
            {"name": "comments", "type": "integer", "min_val": 0, "max_val": 500, "null_rate": 0},
            {"name": "shares", "type": "integer", "min_val": 0, "max_val": 1000, "null_rate": 0},
            {"name": "reach", "type": "integer", "min_val": 100, "max_val": 50000, "null_rate": 0},
            {"name": "engagement_rate", "type": "float", "min_val": 0.001, "max_val": 0.15, "decimals": 4, "null_rate": 0},
            {"name": "hashtags_used", "type": "integer", "min_val": 0, "max_val": 30, "null_rate": 0}
        ]
    },
    
    "Subscription Data": {
        "description": "Subscription service customer data",
        "columns": [
            {"name": "subscription_id", "type": "string", "pattern": "SUB-{random_int:100000:999999}", "null_rate": 0},
            {"name": "customer_id", "type": "string", "pattern": "CUST-{random_int:10000:99999}", "null_rate": 0},
            {"name": "plan_type", "type": "choice", "choices": ["Basic", "Premium", "Pro", "Enterprise"], "weights": [40, 35, 20, 5], "null_rate": 0},
            {"name": "start_date", "type": "date", "start_date": "2020-01-01", "end_date": "2024-12-31", "null_rate": 0},
            {"name": "end_date", "type": "date", "start_date": "2024-01-01", "end_date": "2025-12-31", "null_rate": 0.3},
            {"name": "monthly_price", "type": "float", "min_val": 9.99, "max_val": 199.99, "decimals": 2, "null_rate": 0},
            {"name": "billing_cycle", "type": "choice", "choices": ["Monthly", "Quarterly", "Annual"], "weights": [60, 20, 20], "null_rate": 0},
            {"name": "payment_method", "type": "choice", "choices": ["Credit Card", "PayPal", "Bank Transfer", "Apple Pay"], "weights": [70, 20, 5, 5], "null_rate": 0},
            {"name": "auto_renew", "type": "boolean", "true_rate": 0.85, "null_rate": 0},
            {"name": "cancellation_reason", "type": "choice", "choices": ["Price", "Not using", "Found alternative", "Technical issues", "Other"], "weights": [30, 25, 20, 15, 10], "null_rate": 0.7},
            {"name": "churn_risk_score", "type": "float", "min_val": 0.0, "max_val": 1.0, "decimals": 3, "null_rate": 0},
            {"name": "usage_frequency", "type": "choice", "choices": ["Daily", "Weekly", "Monthly", "Rarely"], "weights": [30, 40, 20, 10], "null_rate": 0}
        ]
    },
    
    "Support Tickets": {
        "description": "Customer support ticket system data",
        "columns": [
            {"name": "ticket_id", "type": "string", "pattern": "TKT-{random_int:100000:999999}", "null_rate": 0},
            {"name": "customer_id", "type": "string", "pattern": "CUST-{random_int:10000:99999}", "null_rate": 0},
            {"name": "created_date", "type": "timestamp", "start_date": "2024-01-01", "end_date": "2024-12-31", "null_rate": 0},
            {"name": "category", "type": "choice", "choices": ["Technical", "Billing", "Product", "Account", "General"], "weights": [35, 25, 20, 15, 5], "null_rate": 0},
            {"name": "priority", "type": "choice", "choices": ["Low", "Medium", "High", "Critical"], "weights": [30, 45, 20, 5], "null_rate": 0},
            {"name": "status", "type": "choice", "choices": ["Open", "In Progress", "Pending Customer", "Resolved", "Closed"], "weights": [10, 20, 15, 30, 25], "null_rate": 0},
            {"name": "assigned_agent", "type": "choice", "choices": ["Agent001", "Agent002", "Agent003", "Agent004", "Agent005"], "null_rate": 0.1},
            {"name": "subject", "type": "sentence", "min_words": 4, "max_words": 10, "null_rate": 0},
            {"name": "description", "type": "text", "min_sentences": 2, "max_sentences": 5, "null_rate": 0},
            {"name": "resolution_time_hours", "type": "float", "min_val": 0.5, "max_val": 168.0, "decimals": 1, "null_rate": 0.3},
            {"name": "customer_satisfaction", "type": "integer", "min_val": 1, "max_val": 5, "null_rate": 0.4},
            {"name": "first_response_time_hours", "type": "float", "min_val": 0.1, "max_val": 48.0, "decimals": 1, "null_rate": 0.1}
        ]
    },
    
    "Loyalty Program": {
        "description": "Customer loyalty program data and points",
        "columns": [
            {"name": "member_id", "type": "string", "pattern": "MEM-{random_int:100000:999999}", "null_rate": 0},
            {"name": "customer_id", "type": "string", "pattern": "CUST-{random_int:10000:99999}", "null_rate": 0},
            {"name": "join_date", "type": "date", "start_date": "2020-01-01", "end_date": "2024-12-31", "null_rate": 0},
            {"name": "tier_level", "type": "choice", "choices": ["Bronze", "Silver", "Gold", "Platinum", "Diamond"], "weights": [35, 30, 20, 10, 5], "null_rate": 0},
            {"name": "points_balance", "type": "integer", "min_val": 0, "max_val": 50000, "null_rate": 0},
            {"name": "points_earned_ytd", "type": "integer", "min_val": 0, "max_val": 25000, "null_rate": 0},
            {"name": "points_redeemed_ytd", "type": "integer", "min_val": 0, "max_val": 20000, "null_rate": 0},
            {"name": "last_activity_date", "type": "date", "start_date": "2024-01-01", "end_date": "2024-12-31", "null_rate": 0.1},
            {"name": "preferred_reward_type", "type": "choice", "choices": ["Discount", "Free Product", "Experience", "Cashback"], "weights": [40, 30, 15, 15], "null_rate": 0.2},
            {"name": "referrals_made", "type": "integer", "min_val": 0, "max_val": 50, "null_rate": 0},
            {"name": "active_status", "type": "boolean", "true_rate": 0.85, "null_rate": 0}
        ]
    },

    "Email Marketing": {
        "description": "Email campaign performance and subscriber data",
        "columns": [
            {"name": "email_id", "type": "string", "pattern": "EMAIL-{random_int:1000000:9999999}", "null_rate": 0},
            {"name": "subscriber_id", "type": "string", "pattern": "SUB-{random_int:10000:99999}", "null_rate": 0},
            {"name": "campaign_name", "type": "choice", "choices": ["Weekly Newsletter", "Product Launch", "Holiday Sale", "Welcome Series", "Re-engagement"], "null_rate": 0},
            {"name": "send_date", "type": "timestamp", "start_date": "2024-01-01", "end_date": "2024-12-31", "null_rate": 0},
            {"name": "subject_line", "type": "sentence", "min_words": 4, "max_words": 8, "null_rate": 0},
            {"name": "delivered", "type": "boolean", "true_rate": 0.98, "null_rate": 0},
            {"name": "opened", "type": "boolean", "true_rate": 0.23, "null_rate": 0},
            {"name": "clicked", "type": "boolean", "true_rate": 0.035, "null_rate": 0},
            {"name": "unsubscribed", "type": "boolean", "true_rate": 0.002, "null_rate": 0},
            {"name": "bounce_type", "type": "choice", "choices": ["None", "Soft", "Hard"], "weights": [95, 3, 2], "null_rate": 0},
            {"name": "time_to_open_hours", "type": "float", "min_val": 0.1, "max_val": 168.0, "decimals": 1, "null_rate": 0.7},
            {"name": "device_type", "type": "choice", "choices": ["Desktop", "Mobile", "Tablet"], "weights": [35, 55, 10], "null_rate": 0.2}
        ]
    },

    "App Usage Analytics": {
        "description": "Mobile app usage and engagement metrics",
        "columns": [
            {"name": "session_id", "type": "string", "pattern": "APP-{random_int:1000000:9999999}", "null_rate": 0},
            {"name": "user_id", "type": "string", "pattern": "USER-{random_int:10000:99999}", "null_rate": 0},
            {"name": "app_version", "type": "choice", "choices": ["2.1.0", "2.1.1", "2.2.0", "2.2.1", "2.3.0"], "weights": [5, 10, 25, 35, 25], "null_rate": 0},
            {"name": "session_start", "type": "timestamp", "start_date": "2024-01-01", "end_date": "2024-12-31", "null_rate": 0},
            {"name": "session_duration_seconds", "type": "integer", "min_val": 10, "max_val": 3600, "null_rate": 0},
            {"name": "screens_viewed", "type": "integer", "min_val": 1, "max_val": 50, "null_rate": 0},
            {"name": "actions_taken", "type": "integer", "min_val": 0, "max_val": 100, "null_rate": 0},
            {"name": "device_model", "type": "choice", "choices": ["iPhone 14", "iPhone 15", "Samsung Galaxy S23", "Google Pixel 7", "Other"], "weights": [25, 30, 20, 15, 10], "null_rate": 0},
            {"name": "os_version", "type": "choice", "choices": ["iOS 17.0", "iOS 17.1", "iOS 17.2", "Android 13", "Android 14"], "weights": [15, 25, 30, 20, 10], "null_rate": 0},
            {"name": "crash_occurred", "type": "boolean", "true_rate": 0.005, "null_rate": 0},
            {"name": "push_notifications_enabled", "type": "boolean", "true_rate": 0.65, "null_rate": 0},
            {"name": "location_permission", "type": "choice", "choices": ["Always", "When in Use", "Never"], "weights": [15, 60, 25], "null_rate": 0}
        ]
    },

    "Survey Responses": {
        "description": "Customer survey responses and feedback",
        "columns": [
            {"name": "response_id", "type": "string", "pattern": "RESP-{random_int:100000:999999}", "null_rate": 0},
            {"name": "survey_id", "type": "string", "pattern": "SURV-{random_int:1000:9999}", "null_rate": 0},
            {"name": "respondent_id", "type": "string", "pattern": "USER-{random_int:10000:99999}", "null_rate": 0.1},
            {"name": "completion_date", "type": "timestamp", "start_date": "2024-01-01", "end_date": "2024-12-31", "null_rate": 0},
            {"name": "survey_type", "type": "choice", "choices": ["Customer Satisfaction", "Product Feedback", "Brand Awareness", "Market Research", "Post-Purchase"], "null_rate": 0},
            {"name": "completion_rate", "type": "float", "min_val": 0.1, "max_val": 1.0, "decimals": 2, "null_rate": 0},
            {"name": "overall_satisfaction", "type": "integer", "min_val": 1, "max_val": 10, "null_rate": 0.05},
            {"name": "recommend_score", "type": "integer", "min_val": 0, "max_val": 10, "null_rate": 0.1},
            {"name": "time_to_complete_minutes", "type": "float", "min_val": 0.5, "max_val": 30.0, "decimals": 1, "null_rate": 0},
            {"name": "response_quality", "type": "choice", "choices": ["High", "Medium", "Low"], "weights": [40, 45, 15], "null_rate": 0},
            {"name": "demographic_age_group", "type": "choice", "choices": ["18-24", "25-34", "35-44", "45-54", "55-64", "65+"], "weights": [15, 25, 25, 20, 10, 5], "null_rate": 0.2},
            {"name": "open_text_provided", "type": "boolean", "true_rate": 0.35, "null_rate": 0}
        ]
    },

    "Product Catalog": {
        "description": "Product information and catalog data",
        "columns": [
            {"name": "product_id", "type": "string", "pattern": "PROD-{random_int:10000:99999}", "null_rate": 0},
            {"name": "sku", "type": "string", "pattern": "SKU-{random_int:100000:999999}", "null_rate": 0},
            {"name": "product_name", "type": "choice", "choices": ["Wireless Headphones", "Smartphone", "Laptop", "Tablet", "Smart Watch", "Gaming Console", "Camera", "Speaker"], "null_rate": 0},
            {"name": "category", "type": "choice", "choices": ["Electronics", "Clothing", "Home & Garden", "Sports", "Books", "Beauty", "Toys"], "null_rate": 0},
            {"name": "subcategory", "type": "choice", "choices": ["Audio", "Computers", "Mobile", "Wearables", "Gaming", "Photography"], "null_rate": 0.1},
            {"name": "brand", "type": "choice", "choices": ["Apple", "Samsung", "Sony", "Nike", "Adidas", "Generic"], "weights": [20, 18, 15, 12, 10, 25], "null_rate": 0},
            {"name": "price", "type": "float", "min_val": 9.99, "max_val": 2999.99, "decimals": 2, "null_rate": 0},
            {"name": "cost", "type": "float", "min_val": 5.00, "max_val": 1500.00, "decimals": 2, "null_rate": 0},
            {"name": "in_stock", "type": "boolean", "true_rate": 0.85, "null_rate": 0},
            {"name": "stock_quantity", "type": "integer", "min_val": 0, "max_val": 1000, "null_rate": 0},
            {"name": "avg_rating", "type": "float", "min_val": 1.0, "max_val": 5.0, "decimals": 1, "null_rate": 0.1},
            {"name": "review_count", "type": "integer", "min_val": 0, "max_val": 5000, "null_rate": 0},
            {"name": "created_date", "type": "date", "start_date": "2020-01-01", "end_date": "2024-12-31", "null_rate": 0},
            {"name": "last_updated", "type": "timestamp", "start_date": "2024-01-01", "end_date": "2024-12-31", "null_rate": 0}
        ]
    },

    "Shipping & Logistics": {
        "description": "Order fulfillment and shipping data",
        "columns": [
            {"name": "shipment_id", "type": "string", "pattern": "SHIP-{random_int:1000000:9999999}", "null_rate": 0},
            {"name": "order_id", "type": "string", "pattern": "ORD-{random_int:100000:999999}", "null_rate": 0},
            {"name": "tracking_number", "type": "string", "pattern": "TRK-{random_int:1000000000:9999999999}", "null_rate": 0},
            {"name": "carrier", "type": "choice", "choices": ["UPS", "FedEx", "USPS", "DHL", "Amazon"], "weights": [30, 25, 20, 15, 10], "null_rate": 0},
            {"name": "service_type", "type": "choice", "choices": ["Standard", "Express", "Overnight", "Same Day"], "weights": [60, 25, 10, 5], "null_rate": 0},
            {"name": "ship_date", "type": "timestamp", "start_date": "2024-01-01", "end_date": "2024-12-31", "null_rate": 0},
            {"name": "estimated_delivery", "type": "date", "start_date": "2024-01-01", "end_date": "2024-12-31", "null_rate": 0},
            {"name": "actual_delivery", "type": "timestamp", "start_date": "2024-01-01", "end_date": "2024-12-31", "null_rate": 0.1},
            {"name": "origin_zip", "type": "zipcode", "null_rate": 0},
            {"name": "destination_zip", "type": "zipcode", "null_rate": 0},
            {"name": "weight_lbs", "type": "float", "min_val": 0.1, "max_val": 50.0, "decimals": 1, "null_rate": 0},
            {"name": "shipping_cost", "type": "float", "min_val": 0.99, "max_val": 49.99, "decimals": 2, "null_rate": 0},
            {"name": "delivery_status", "type": "choice", "choices": ["In Transit", "Out for Delivery", "Delivered", "Failed Delivery", "Returned"], "weights": [20, 10, 60, 5, 5], "null_rate": 0},
            {"name": "delivery_attempts", "type": "integer", "min_val": 1, "max_val": 3, "null_rate": 0}
        ]
    },

    "Financial Transactions": {
        "description": "Customer payment and financial transaction data",
        "columns": [
            {"name": "transaction_id", "type": "string", "pattern": "TXN-{random_int:10000000:99999999}", "null_rate": 0},
            {"name": "customer_id", "type": "string", "pattern": "CUST-{random_int:10000:99999}", "null_rate": 0},
            {"name": "account_id", "type": "string", "pattern": "ACC-{random_int:100000:999999}", "null_rate": 0},
            {"name": "transaction_date", "type": "timestamp", "start_date": "2024-01-01", "end_date": "2024-12-31", "null_rate": 0},
            {"name": "transaction_type", "type": "choice", "choices": ["Purchase", "Refund", "Transfer", "Fee", "Interest"], "weights": [70, 10, 10, 7, 3], "null_rate": 0},
            {"name": "amount", "type": "float", "min_val": 0.01, "max_val": 10000.00, "decimals": 2, "null_rate": 0},
            {"name": "currency", "type": "choice", "choices": ["USD", "EUR", "GBP", "CAD"], "weights": [70, 15, 10, 5], "null_rate": 0},
            {"name": "payment_method", "type": "choice", "choices": ["Credit Card", "Debit Card", "ACH", "Wire", "Digital Wallet"], "weights": [40, 25, 20, 10, 5], "null_rate": 0},
            {"name": "merchant_category", "type": "choice", "choices": ["Retail", "Restaurant", "Gas Station", "Online", "Grocery"], "weights": [30, 20, 15, 25, 10], "null_rate": 0},
            {"name": "status", "type": "choice", "choices": ["Completed", "Pending", "Failed", "Cancelled"], "weights": [85, 8, 5, 2], "null_rate": 0},
            {"name": "fee_amount", "type": "float", "min_val": 0.00, "max_val": 50.00, "decimals": 2, "null_rate": 0.7},
            {"name": "balance_after", "type": "float", "min_val": 0.00, "max_val": 50000.00, "decimals": 2, "null_rate": 0.1}
        ]
    },

    "Inventory Management": {
        "description": "Product inventory and stock management",
        "columns": [
            {"name": "inventory_id", "type": "string", "pattern": "INV-{random_int:100000:999999}", "null_rate": 0},
            {"name": "product_id", "type": "string", "pattern": "PROD-{random_int:10000:99999}", "null_rate": 0},
            {"name": "warehouse_id", "type": "choice", "choices": ["WH001", "WH002", "WH003", "WH004", "WH005"], "null_rate": 0},
            {"name": "location_code", "type": "string", "pattern": "LOC-{random_int:1000:9999}", "null_rate": 0},
            {"name": "current_stock", "type": "integer", "min_val": 0, "max_val": 1000, "null_rate": 0},
            {"name": "reserved_stock", "type": "integer", "min_val": 0, "max_val": 100, "null_rate": 0},
            {"name": "available_stock", "type": "integer", "min_val": 0, "max_val": 900, "null_rate": 0},
            {"name": "reorder_point", "type": "integer", "min_val": 5, "max_val": 100, "null_rate": 0},
            {"name": "max_stock_level", "type": "integer", "min_val": 100, "max_val": 2000, "null_rate": 0},
            {"name": "last_received_date", "type": "date", "start_date": "2024-01-01", "end_date": "2024-12-31", "null_rate": 0.1},
            {"name": "last_sold_date", "type": "date", "start_date": "2024-01-01", "end_date": "2024-12-31", "null_rate": 0.2},
            {"name": "unit_cost", "type": "float", "min_val": 1.00, "max_val": 500.00, "decimals": 2, "null_rate": 0},
            {"name": "total_value", "type": "float", "min_val": 0.00, "max_val": 50000.00, "decimals": 2, "null_rate": 0},
            {"name": "turnover_rate", "type": "float", "min_val": 0.1, "max_val": 12.0, "decimals": 1, "null_rate": 0}
        ]
    },

    "Sales Leads": {
        "description": "Sales pipeline and lead management data",
        "columns": [
            {"name": "lead_id", "type": "string", "pattern": "LEAD-{random_int:100000:999999}", "null_rate": 0},
            {"name": "first_name", "type": "first_name", "null_rate": 0},
            {"name": "last_name", "type": "last_name", "null_rate": 0},
            {"name": "company", "type": "choice", "choices": ["Acme Corp", "Tech Solutions Inc", "Global Industries", "Startup LLC", "Enterprise Co"], "null_rate": 0.2},
            {"name": "email", "type": "email", "null_rate": 0},
            {"name": "phone", "type": "phone", "null_rate": 0.1},
            {"name": "lead_source", "type": "choice", "choices": ["Website", "Referral", "Cold Call", "Trade Show", "Social Media", "Paid Ads"], "weights": [30, 25, 15, 10, 10, 10], "null_rate": 0},
            {"name": "lead_status", "type": "choice", "choices": ["New", "Qualified", "Contacted", "Opportunity", "Closed Won", "Closed Lost"], "weights": [20, 25, 20, 15, 10, 10], "null_rate": 0},
            {"name": "lead_score", "type": "integer", "min_val": 0, "max_val": 100, "null_rate": 0},
            {"name": "estimated_value", "type": "float", "min_val": 1000.00, "max_val": 100000.00, "decimals": 2, "null_rate": 0.3},
            {"name": "probability", "type": "float", "min_val": 0.05, "max_val": 0.95, "decimals": 2, "null_rate": 0.2},
            {"name": "created_date", "type": "date", "start_date": "2024-01-01", "end_date": "2024-12-31", "null_rate": 0},
            {"name": "last_contact_date", "type": "date", "start_date": "2024-01-01", "end_date": "2024-12-31", "null_rate": 0.1},
            {"name": "assigned_rep", "type": "choice", "choices": ["Rep001", "Rep002", "Rep003", "Rep004", "Rep005"], "null_rate": 0.05}
        ]
    }
}
