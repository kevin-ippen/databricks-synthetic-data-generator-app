# templates.py - Enhanced B2C synthetic data templates with advanced Faker capabilities

TEMPLATES = {
    "Custom": {"description": "Build your own schema", "columns": []},
    
    "Customer Records": {
        "description": "Complete customer database with demographics and realistic business correlations",
        "columns": [
            {"name": "customer_id", "type": "realistic_id", "prefix": "CUST", "length": 8, "format": "alphanumeric", "null_rate": 0},
            {"name": "first_name", "type": "first_name", "null_rate": 0},
            {"name": "last_name", "type": "last_name", "null_rate": 0},
            {"name": "email", "type": "company_email", "null_rate": 0.02},
            {"name": "personal_email", "type": "email", "null_rate": 0.15},
            {"name": "phone", "type": "business_phone", "null_rate": 0.1},
            {"name": "date_of_birth", "type": "date", "start_date": "1950-01-01", "end_date": "2005-12-31", "null_rate": 0.05},
            {"name": "gender", "type": "weighted_choice", "choices": ["Male", "Female", "Non-binary", "Prefer not to say"], "weights": [45, 45, 5, 5], "null_rate": 0.03},
            {"name": "address", "type": "localized_address", "locale": "en_US", "null_rate": 0.08},
            {"name": "city", "type": "city", "null_rate": 0.02},
            {"name": "state", "type": "state", "null_rate": 0.02},
            {"name": "zip_code", "type": "zipcode", "null_rate": 0.05},
            {"name": "coordinates", "type": "coordinates", "null_rate": 0.3},
            {"name": "job_title", "type": "job_title", "null_rate": 0.1},
            {"name": "company", "type": "company_name", "null_rate": 0.2},
            {"name": "registration_date", "type": "business_date", "start_date": "2020-01-01", "end_date": "2024-12-31", "null_rate": 0},
            {"name": "customer_tier", "type": "weighted_choice", "choices": ["Bronze", "Silver", "Gold", "Platinum"], "weights": [40, 30, 20, 10], "null_rate": 0},
            {"name": "lifetime_value", "type": "currency_amount", "min_val": 0, "max_val": 50000, "decimals": 2, "null_rate": 0},
            {"name": "credit_card", "type": "credit_card", "card_type": "visa", "null_rate": 0.6}
        ]
    },
    
    "Restaurant POS Data": {
        "description": "Point of sale transactions for restaurant business with realistic timing and patterns",
        "columns": [
            {"name": "transaction_id", "type": "realistic_id", "prefix": "TXN", "length": 8, "format": "alphanumeric", "null_rate": 0},
            {"name": "order_number", "type": "integer", "min_val": 1, "max_val": 99999, "null_rate": 0},
            {"name": "timestamp", "type": "business_hours_timestamp", "start_date": "2024-01-01", "end_date": "2024-12-31", "null_rate": 0},
            {"name": "table_number", "type": "integer", "min_val": 1, "max_val": 50, "null_rate": 0.1},
            {"name": "server_id", "type": "weighted_choice", "choices": ["SRV001", "SRV002", "SRV003", "SRV004", "SRV005", "SRV006"], "weights": [20, 20, 20, 15, 15, 10], "null_rate": 0},
            {"name": "item_name", "type": "weighted_choice", "choices": ["Burger", "Pizza", "Salad", "Pasta", "Steak", "Fish", "Chicken", "Soup", "Sandwich", "Dessert"], "weights": [15, 20, 8, 12, 10, 8, 12, 5, 7, 3], "null_rate": 0},
            {"name": "category", "type": "weighted_choice", "choices": ["Appetizer", "Main Course", "Dessert", "Beverage", "Side"], "weights": [15, 50, 15, 15, 5], "null_rate": 0},
            {"name": "quantity", "type": "integer", "min_val": 1, "max_val": 5, "null_rate": 0},
            {"name": "unit_price", "type": "currency_amount", "min_val": 5.99, "max_val": 49.99, "decimals": 2, "null_rate": 0},
            {"name": "total_amount", "type": "currency_amount", "min_val": 5.99, "max_val": 200.00, "decimals": 2, "null_rate": 0},
            {"name": "payment_method", "type": "weighted_choice", "choices": ["Credit Card", "Debit Card", "Cash", "Mobile Pay"], "weights": [45, 25, 20, 10], "null_rate": 0},
            {"name": "tip_amount", "type": "currency_amount", "min_val": 0, "max_val": 50.00, "decimals": 2, "null_rate": 0.1},
            {"name": "customer_satisfaction", "type": "weighted_choice", "choices": [1, 2, 3, 4, 5], "weights": [5, 10, 20, 35, 30], "null_rate": 0.2},
            {"name": "special_requests", "type": "review_text", "min_sentences": 1, "max_sentences": 2, "null_rate": 0.7}
        ]
    },
    
    "Retail POS Data": {
        "description": "Point of sale transactions for retail business with seasonal patterns",
        "columns": [
            {"name": "transaction_id", "type": "realistic_id", "prefix": "RTL", "length": 8, "format": "alphanumeric", "null_rate": 0},
            {"name": "store_id", "type": "weighted_choice", "choices": ["ST001", "ST002", "ST003", "ST004", "ST005"], "weights": [25, 20, 20, 20, 15], "null_rate": 0},
            {"name": "cashier_id", "type": "weighted_choice", "choices": ["CSH001", "CSH002", "CSH003", "CSH004", "CSH005", "CSH006"], "weights": [18, 17, 17, 17, 16, 15], "null_rate": 0},
            {"name": "timestamp", "type": "business_hours_timestamp", "start_date": "2024-01-01", "end_date": "2024-12-31", "null_rate": 0},
            {"name": "product_sku", "type": "realistic_id", "prefix": "SKU", "length": 8, "format": "alphanumeric", "null_rate": 0},
            {"name": "product_name", "type": "product_name", "null_rate": 0},
            {"name": "category", "type": "weighted_choice", "choices": ["Clothing", "Footwear", "Accessories", "Electronics", "Home"], "weights": [40, 25, 15, 15, 5], "null_rate": 0},
            {"name": "brand", "type": "weighted_choice", "choices": ["Nike", "Adidas", "Levi's", "Zara", "H&M", "Gap", "Uniqlo", "Target"], "weights": [15, 15, 12, 12, 12, 12, 12, 10], "null_rate": 0},
            {"name": "size", "type": "weighted_choice", "choices": ["XS", "S", "M", "L", "XL", "XXL"], "weights": [5, 20, 30, 25, 15, 5], "null_rate": 0.3},
            {"name": "color", "type": "weighted_choice", "choices": ["Black", "White", "Blue", "Red", "Green", "Gray", "Brown", "Pink"], "weights": [20, 18, 15, 12, 10, 10, 10, 5], "null_rate": 0.1},
            {"name": "quantity", "type": "integer", "min_val": 1, "max_val": 10, "null_rate": 0},
            {"name": "unit_price", "type": "currency_amount", "min_val": 9.99, "max_val": 299.99, "decimals": 2, "null_rate": 0},
            {"name": "discount_percent", "type": "float", "min_val": 0, "max_val": 50, "decimals": 1, "null_rate": 0.6},
            {"name": "total_amount", "type": "currency_amount", "min_val": 9.99, "max_val": 1500.00, "decimals": 2, "null_rate": 0},
            {"name": "payment_method", "type": "weighted_choice", "choices": ["Credit Card", "Debit Card", "Cash", "Gift Card", "Mobile Pay"], "weights": [40, 25, 15, 10, 10], "null_rate": 0},
            {"name": "loyalty_card", "type": "realistic_id", "prefix": "LOY", "length": 10, "format": "numeric", "null_rate": 0.4}
        ]
    },
    
    "Product Reviews": {
        "description": "Customer product reviews with realistic sentiment and engagement patterns",
        "columns": [
            {"name": "review_id", "type": "realistic_id", "prefix": "REV", "length": 8, "format": "alphanumeric", "null_rate": 0},
            {"name": "product_id", "type": "realistic_id", "prefix": "PROD", "length": 8, "format": "alphanumeric", "null_rate": 0},
            {"name": "customer_id", "type": "realistic_id", "prefix": "CUST", "length": 8, "format": "alphanumeric", "null_rate": 0},
            {"name": "rating", "type": "weighted_choice", "choices": [1, 2, 3, 4, 5], "weights": [8, 7, 15, 35, 35], "null_rate": 0},
            {"name": "review_title", "type": "sentence", "min_words": 3, "max_words": 8, "null_rate": 0.1},
            {"name": "review_text", "type": "review_text", "min_sentences": 1, "max_sentences": 5, "null_rate": 0.05},
            {"name": "verified_purchase", "type": "boolean", "true_rate": 0.85, "null_rate": 0},
            {"name": "helpful_votes", "type": "weighted_choice", "choices": [0, 1, 2, 3, 4, 5, 10, 20, 50, 100], "weights": [30, 20, 15, 10, 8, 7, 5, 3, 1, 1], "null_rate": 0},
            {"name": "review_date", "type": "business_date", "start_date": "2023-01-01", "end_date": "2024-12-31", "null_rate": 0},
            {"name": "reviewer_location", "type": "city", "null_rate": 0.2},
            {"name": "product_category", "type": "weighted_choice", "choices": ["Electronics", "Clothing", "Home", "Books", "Sports", "Beauty", "Toys"], "weights": [25, 20, 15, 10, 10, 10, 10], "null_rate": 0},
            {"name": "review_sentiment", "type": "weighted_choice", "choices": ["Positive", "Neutral", "Negative"], "weights": [60, 25, 15], "null_rate": 0},
            {"name": "reviewer_level", "type": "weighted_choice", "choices": ["Beginner", "Intermediate", "Expert", "Professional"], "weights": [40, 35, 20, 5], "null_rate": 0.3}
        ]
    },
    
    "E-commerce Transactions": {
        "description": "Online shopping transaction data with realistic customer behavior",
        "columns": [
            {"name": "order_id", "type": "realistic_id", "prefix": "ORD", "length": 8, "format": "alphanumeric", "null_rate": 0},
            {"name": "customer_id", "type": "realistic_id", "prefix": "CUST", "length": 8, "format": "alphanumeric", "null_rate": 0},
            {"name": "order_date", "type": "business_hours_timestamp", "start_date": "2024-01-01", "end_date": "2024-12-31", "null_rate": 0},
            {"name": "product_id", "type": "realistic_id", "prefix": "PROD", "length": 8, "format": "alphanumeric", "null_rate": 0},
            {"name": "product_name", "type": "product_name", "null_rate": 0},
            {"name": "quantity", "type": "weighted_choice", "choices": [1, 2, 3, 4, 5], "weights": [60, 25, 10, 3, 2], "null_rate": 0},
            {"name": "unit_price", "type": "currency_amount", "min_val": 19.99, "max_val": 1999.99, "decimals": 2, "null_rate": 0},
            {"name": "shipping_cost", "type": "currency_amount", "min_val": 0, "max_val": 25.99, "decimals": 2, "null_rate": 0},
            {"name": "tax_amount", "type": "currency_amount", "min_val": 0, "max_val": 200.00, "decimals": 2, "null_rate": 0},
            {"name": "total_amount", "type": "currency_amount", "min_val": 19.99, "max_val": 5000.00, "decimals": 2, "null_rate": 0},
            {"name": "payment_method", "type": "weighted_choice", "choices": ["Credit Card", "PayPal", "Apple Pay", "Google Pay", "Bank Transfer"], "weights": [50, 25, 10, 10, 5], "null_rate": 0},
            {"name": "shipping_address", "type": "localized_address", "locale": "en_US", "null_rate": 0},
            {"name": "order_status", "type": "weighted_choice", "choices": ["Pending", "Processing", "Shipped", "Delivered", "Cancelled"], "weights": [5, 10, 20, 60, 5], "null_rate": 0},
            {"name": "delivery_date", "type": "business_date", "start_date": "2024-01-01", "end_date": "2024-12-31", "null_rate": 0.1},
            {"name": "customer_ip", "type": "coordinates", "null_rate": 0.1},
            {"name": "referral_source", "type": "weighted_choice", "choices": ["Direct", "Google", "Facebook", "Email", "Affiliate"], "weights": [35, 30, 15, 15, 5], "null_rate": 0.1}
        ]
    },
    
    "Voice of Customer (VOC)": {
        "description": "Customer feedback with realistic sentiment patterns and response quality",
        "columns": [
            {"name": "feedback_id", "type": "realistic_id", "prefix": "VOC", "length": 8, "format": "alphanumeric", "null_rate": 0},
            {"name": "customer_id", "type": "realistic_id", "prefix": "CUST", "length": 8, "format": "alphanumeric", "null_rate": 0},
            {"name": "survey_id", "type": "realistic_id", "prefix": "SURV", "length": 6, "format": "alphanumeric", "null_rate": 0},
            {"name": "feedback_date", "type": "business_hours_timestamp", "start_date": "2024-01-01", "end_date": "2024-12-31", "null_rate": 0},
            {"name": "touchpoint", "type": "weighted_choice", "choices": ["Website", "Mobile App", "Call Center", "Email", "In-Store", "Social Media"], "weights": [25, 20, 15, 15, 20, 5], "null_rate": 0},
            {"name": "sentiment_score", "type": "float", "min_val": -1.0, "max_val": 1.0, "decimals": 3, "null_rate": 0},
            {"name": "nps_score", "type": "weighted_choice", "choices": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "weights": [5, 3, 3, 4, 4, 5, 6, 8, 12, 20, 30], "null_rate": 0.1},
            {"name": "csat_score", "type": "weighted_choice", "choices": [1, 2, 3, 4, 5], "weights": [8, 12, 20, 35, 25], "null_rate": 0.05},
            {"name": "feedback_text", "type": "review_text", "min_sentences": 1, "max_sentences": 4, "null_rate": 0.02},
            {"name": "category", "type": "weighted_choice", "choices": ["Product Quality", "Customer Service", "Pricing", "Delivery", "Website", "General"], "weights": [25, 30, 10, 15, 10, 10], "null_rate": 0},
            {"name": "priority", "type": "weighted_choice", "choices": ["Low", "Medium", "High", "Critical"], "weights": [40, 35, 20, 5], "null_rate": 0},
            {"name": "resolved", "type": "boolean", "true_rate": 0.75, "null_rate": 0},
            {"name": "resolution_notes", "type": "review_text", "min_sentences": 1, "max_sentences": 3, "null_rate": 0.4}
        ]
    },
    
    "Marketing Campaign Data": {
        "description": "Marketing campaign performance with realistic engagement rates",
        "columns": [
            {"name": "campaign_id", "type": "realistic_id", "prefix": "CAMP", "length": 8, "format": "alphanumeric", "null_rate": 0},
            {"name": "customer_id", "type": "realistic_id", "prefix": "CUST", "length": 8, "format": "alphanumeric", "null_rate": 0},
            {"name": "campaign_name", "type": "weighted_choice", "choices": ["Summer Sale", "Black Friday", "Holiday Special", "New Product Launch", "Back to School", "Spring Collection"], "weights": [15, 25, 20, 15, 15, 10], "null_rate": 0},
            {"name": "channel", "type": "weighted_choice", "choices": ["Email", "Social Media", "Display Ads", "Search Ads", "Direct Mail", "SMS"], "weights": [30, 25, 20, 15, 5, 5], "null_rate": 0},
            {"name": "send_date", "type": "business_hours_timestamp", "start_date": "2024-01-01", "end_date": "2024-12-31", "null_rate": 0},
            {"name": "opened", "type": "boolean", "true_rate": 0.22, "null_rate": 0},
            {"name": "clicked", "type": "boolean", "true_rate": 0.03, "null_rate": 0},
            {"name": "converted", "type": "boolean", "true_rate": 0.015, "null_rate": 0},
            {"name": "revenue_generated", "type": "currency_amount", "min_val": 0, "max_val": 500.00, "decimals": 2, "null_rate": 0.8},
            {"name": "cost_per_send", "type": "currency_amount", "min_val": 0.01, "max_val": 5.00, "decimals": 3, "null_rate": 0},
            {"name": "audience_segment", "type": "weighted_choice", "choices": ["High Value", "Frequent Buyers", "New Customers", "Lapsed", "VIP", "General"], "weights": [15, 25, 20, 15, 10, 15], "null_rate": 0},
            {"name": "creative_type", "type": "weighted_choice", "choices": ["Image", "Video", "Text", "Carousel", "Interactive"], "weights": [40, 25, 15, 15, 5], "null_rate": 0},
            {"name": "ab_test_variant", "type": "weighted_choice", "choices": ["A", "B", "Control"], "weights": [40, 40, 20], "null_rate": 0.3}
        ]
    },
    
    "User Behavior/Clickstream": {
        "description": "Website and app user behavior with realistic session patterns",
        "columns": [
            {"name": "session_id", "type": "realistic_id", "prefix": "SESS", "length": 12, "format": "alphanumeric", "null_rate": 0},
            {"name": "user_id", "type": "realistic_id", "prefix": "USER", "length": 8, "format": "alphanumeric", "null_rate": 0.1},
            {"name": "timestamp", "type": "business_hours_timestamp", "start_date": "2024-01-01", "end_date": "2024-12-31", "null_rate": 0},
            {"name": "page_url", "type": "weighted_choice", "choices": ["/home", "/products", "/cart", "/checkout", "/account", "/search", "/category/electronics", "/category/clothing"], "weights": [20, 25, 10, 5, 8, 12, 10, 10], "null_rate": 0},
            {"name": "action", "type": "weighted_choice", "choices": ["page_view", "click", "scroll", "form_submit", "search", "add_to_cart", "purchase"], "weights": [40, 25, 15, 5, 8, 5, 2], "null_rate": 0},
            {"name": "device_type", "type": "weighted_choice", "choices": ["Desktop", "Mobile", "Tablet"], "weights": [35, 55, 10], "null_rate": 0},
            {"name": "browser", "type": "weighted_choice", "choices": ["Chrome", "Safari", "Firefox", "Edge", "Other"], "weights": [50, 25, 15, 8, 2], "null_rate": 0},
            {"name": "referrer", "type": "weighted_choice", "choices": ["Direct", "Google", "Facebook", "Email", "Other"], "weights": [35, 30, 15, 15, 5], "null_rate": 0.2},
            {"name": "session_duration", "type": "weighted_choice", "choices": [30, 60, 120, 300, 600, 1800, 3600], "weights": [20, 25, 20, 15, 10, 7, 3], "null_rate": 0.1},
            {"name": "pages_viewed", "type": "weighted_choice", "choices": [1, 2, 3, 4, 5, 10, 20], "weights": [25, 20, 18, 15, 12, 7, 3], "null_rate": 0},
            {"name": "location", "type": "city", "null_rate": 0.3},
            {"name": "utm_source", "type": "weighted_choice", "choices": ["google", "facebook", "email", "direct", "affiliate"], "weights": [35, 20, 20, 20, 5], "null_rate": 0.5}
        ]
    },
    
    "Social Media Engagement": {
        "description": "Social media posts with realistic engagement distributions",
        "columns": [
            {"name": "post_id", "type": "realistic_id", "prefix": "POST", "length": 8, "format": "alphanumeric", "null_rate": 0},
            {"name": "user_id", "type": "realistic_id", "prefix": "USER", "length": 8, "format": "alphanumeric", "null_rate": 0},
            {"name": "platform", "type": "weighted_choice", "choices": ["Instagram", "Facebook", "Twitter", "TikTok", "LinkedIn"], "weights": [30, 25, 20, 15, 10], "null_rate": 0},
            {"name": "post_type", "type": "weighted_choice", "choices": ["Photo", "Video", "Story", "Reel", "Text"], "weights": [30, 25, 20, 15, 10], "null_rate": 0},
            {"name": "post_date", "type": "business_hours_timestamp", "start_date": "2024-01-01", "end_date": "2024-12-31", "null_rate": 0},
            {"name": "content_category", "type": "weighted_choice", "choices": ["Product", "Lifestyle", "Behind-the-scenes", "User-generated", "Educational", "Promotional"], "weights": [25, 20, 15, 15, 15, 10], "null_rate": 0},
            {"name": "likes", "type": "weighted_choice", "choices": [0, 5, 10, 25, 50, 100, 500, 1000, 5000, 10000], "weights": [10, 15, 20, 20, 15, 10, 5, 3, 1, 1], "null_rate": 0},
            {"name": "comments", "type": "weighted_choice", "choices": [0, 1, 2, 5, 10, 25, 50, 100, 500], "weights": [20, 25, 20, 15, 10, 5, 3, 1, 1], "null_rate": 0},
            {"name": "shares", "type": "weighted_choice", "choices": [0, 1, 2, 5, 10, 25, 50, 100, 1000], "weights": [30, 25, 20, 15, 5, 3, 1, 0.5, 0.5], "null_rate": 0},
            {"name": "reach", "type": "weighted_choice", "choices": [100, 500, 1000, 5000, 10000, 25000, 50000], "weights": [20, 25, 25, 15, 10, 3, 2], "null_rate": 0},
            {"name": "engagement_rate", "type": "float", "min_val": 0.001, "max_val": 0.15, "decimals": 4, "null_rate": 0},
            {"name": "hashtags_used", "type": "weighted_choice", "choices": [0, 1, 3, 5, 10, 15, 30], "weights": [5, 10, 20, 25, 25, 10, 5], "null_rate": 0},
            {"name": "primary_hashtag", "type": "hashtag", "null_rate": 0.3}
        ]
    },
    
    "Subscription Data": {
        "description": "Subscription service data with realistic churn patterns",
        "columns": [
            {"name": "subscription_id", "type": "realistic_id", "prefix": "SUB", "length": 8, "format": "alphanumeric", "null_rate": 0},
            {"name": "customer_id", "type": "realistic_id", "prefix": "CUST", "length": 8, "format": "alphanumeric", "null_rate": 0},
            {"name": "plan_type", "type": "weighted_choice", "choices": ["Basic", "Premium", "Pro", "Enterprise"], "weights": [40, 35, 20, 5], "null_rate": 0},
            {"name": "start_date", "type": "business_date", "start_date": "2020-01-01", "end_date": "2024-12-31", "null_rate": 0},
            {"name": "end_date", "type": "business_date", "start_date": "2024-01-01", "end_date": "2025-12-31", "null_rate": 0.3},
            {"name": "monthly_price", "type": "currency_amount", "min_val": 9.99, "max_val": 199.99, "decimals": 2, "null_rate": 0},
            {"name": "billing_cycle", "type": "weighted_choice", "choices": ["Monthly", "Quarterly", "Annual"], "weights": [60, 20, 20], "null_rate": 0},
            {"name": "payment_method", "type": "weighted_choice", "choices": ["Credit Card", "PayPal", "Bank Transfer", "Apple Pay"], "weights": [70, 20, 5, 5], "null_rate": 0},
            {"name": "auto_renew", "type": "boolean", "true_rate": 0.85, "null_rate": 0},
            {"name": "cancellation_reason", "type": "weighted_choice", "choices": ["Price", "Not using", "Found alternative", "Technical issues", "Other"], "weights": [30, 25, 20, 15, 10], "null_rate": 0.7},
            {"name": "churn_risk_score", "type": "float", "min_val": 0.0, "max_val": 1.0, "decimals": 3, "null_rate": 0},
            {"name": "usage_frequency", "type": "weighted_choice", "choices": ["Daily", "Weekly", "Monthly", "Rarely"], "weights": [30, 40, 20, 10], "null_rate": 0},
            {"name": "customer_support_tickets", "type": "weighted_choice", "choices": [0, 1, 2, 3, 5, 10], "weights": [40, 30, 15, 10, 3, 2], "null_rate": 0}
        ]
    },
    
    "Support Tickets": {
        "description": "Customer support tickets with realistic resolution patterns",
        "columns": [
            {"name": "ticket_id", "type": "realistic_id", "prefix": "TKT", "length": 8, "format": "alphanumeric", "null_rate": 0},
            {"name": "customer_id", "type": "realistic_id", "prefix": "CUST", "length": 8, "format": "alphanumeric", "null_rate": 0},
            {"name": "created_date", "type": "business_hours_timestamp", "start_date": "2024-01-01", "end_date": "2024-12-31", "null_rate": 0},
            {"name": "category", "type": "weighted_choice", "choices": ["Technical", "Billing", "Product", "Account", "General"], "weights": [35, 25, 20, 15, 5], "null_rate": 0},
            {"name": "priority", "type": "weighted_choice", "choices": ["Low", "Medium", "High", "Critical"], "weights": [30, 45, 20, 5], "null_rate": 0},
            {"name": "status", "type": "weighted_choice", "choices": ["Open", "In Progress", "Pending Customer", "Resolved", "Closed"], "weights": [10, 20, 15, 30, 25], "null_rate": 0},
            {"name": "assigned_agent", "type": "weighted_choice", "choices": ["Agent001", "Agent002", "Agent003", "Agent004", "Agent005"], "weights": [22, 21, 20, 19, 18], "null_rate": 0.1},
            {"name": "subject", "type": "sentence", "min_words": 4, "max_words": 10, "null_rate": 0},
            {"name": "description", "type": "review_text", "min_sentences": 2, "max_sentences": 5, "null_rate": 0},
            {"name": "resolution_time_hours", "type": "weighted_choice", "choices": [0.5, 1, 2, 4, 8, 24, 48, 168], "weights": [5, 15, 20, 25, 20, 10, 3, 2], "null_rate": 0.3},
            {"name": "customer_satisfaction", "type": "weighted_choice", "choices": [1, 2, 3, 4, 5], "weights": [5, 10, 20, 35, 30], "null_rate": 0.4},
            {"name": "first_response_time_hours", "type": "weighted_choice", "choices": [0.1, 0.5, 1, 2, 4, 8, 24, 48], "weights": [15, 25, 25, 20, 10, 3, 1, 1], "null_rate": 0.1},
            {"name": "escalated", "type": "boolean", "true_rate": 0.15, "null_rate": 0}
        ]
    },
    
    "Loyalty Program": {
        "description": "Customer loyalty program with realistic engagement patterns",
        "columns": [
            {"name": "member_id", "type": "realistic_id", "prefix": "MEM", "length": 8, "format": "alphanumeric", "null_rate": 0},
            {"name": "customer_id", "type": "realistic_id", "prefix": "CUST", "length": 8, "format": "alphanumeric", "null_rate": 0},
            {"name": "join_date", "type": "business_date", "start_date": "2020-01-01", "end_date": "2024-12-31", "null_rate": 0},
            {"name": "tier_level", "type": "weighted_choice", "choices": ["Bronze", "Silver", "Gold", "Platinum", "Diamond"], "weights": [35, 30, 20, 10, 5], "null_rate": 0},
            {"name": "points_balance", "type": "weighted_choice", "choices": [0, 100, 500, 1000, 5000, 10000, 25000, 50000], "weights": [10, 20, 25, 20, 15, 5, 3, 2], "null_rate": 0},
            {"name": "points_earned_ytd", "type": "weighted_choice", "choices": [0, 100, 500, 1000, 5000, 10000, 25000], "weights": [5, 15, 25, 25, 20, 8, 2], "null_rate": 0},
            {"name": "points_redeemed_ytd", "type": "weighted_choice", "choices": [0, 100, 500, 1000, 5000, 10000, 20000], "weights": [20, 25, 25, 15, 10, 3, 2], "null_rate": 0},
            {"name": "last_activity_date", "type": "business_date", "start_date": "2024-01-01", "end_date": "2024-12-31", "null_rate": 0.1},
            {"name": "preferred_reward_type", "type": "weighted_choice", "choices": ["Discount", "Free Product", "Experience", "Cashback"], "weights": [40, 30, 15, 15], "null_rate": 0.2},
            {"name": "referrals_made", "type": "weighted_choice", "choices": [0, 1, 2, 3, 5, 10, 25, 50], "weights": [40, 25, 15, 10, 5, 3, 1, 1], "null_rate": 0},
            {"name": "active_status", "type": "boolean", "true_rate": 0.85, "null_rate": 0},
            {"name": "communication_preference", "type": "weighted_choice", "choices": ["Email", "SMS", "Push", "Mail", "None"], "weights": [45, 25, 15, 10, 5], "null_rate": 0}
        ]
    },

    "Email Marketing": {
        "description": "Email campaign performance with realistic deliverability patterns",
        "columns": [
            {"name": "email_id", "type": "realistic_id", "prefix": "EMAIL", "length": 10, "format": "alphanumeric", "null_rate": 0},
            {"name": "subscriber_id", "type": "realistic_id", "prefix": "SUB", "length": 8, "format": "alphanumeric", "null_rate": 0},
            {"name": "campaign_name", "type": "weighted_choice", "choices": ["Weekly Newsletter", "Product Launch", "Holiday Sale", "Welcome Series", "Re-engagement"], "weights": [30, 20, 25, 15, 10], "null_rate": 0},
            {"name": "send_date", "type": "business_hours_timestamp", "start_date": "2024-01-01", "end_date": "2024-12-31", "null_rate": 0},
            {"name": "subject_line", "type": "sentence", "min_words": 4, "max_words": 8, "null_rate": 0},
            {"name": "delivered", "type": "boolean", "true_rate": 0.98, "null_rate": 0},
            {"name": "opened", "type": "boolean", "true_rate": 0.23, "null_rate": 0},
            {"name": "clicked", "type": "boolean", "true_rate": 0.035, "null_rate": 0},
            {"name": "unsubscribed", "type": "boolean", "true_rate": 0.002, "null_rate": 0},
            {"name": "bounce_type", "type": "weighted_choice", "choices": ["None", "Soft", "Hard"], "weights": [95, 3, 2], "null_rate": 0},
            {"name": "time_to_open_hours", "type": "weighted_choice", "choices": [0.1, 0.5, 1, 2, 6, 24, 72, 168], "weights": [15, 20, 25, 20, 10, 7, 2, 1], "null_rate": 0.7},
            {"name": "device_type", "type": "weighted_choice", "choices": ["Desktop", "Mobile", "Tablet"], "weights": [35, 55, 10], "null_rate": 0.2},
            {"name": "email_client", "type": "weighted_choice", "choices": ["Gmail", "Outlook", "Apple Mail", "Yahoo", "Other"], "weights": [45, 25, 15, 10, 5], "null_rate": 0.1}
        ]
    },

    "App Usage Analytics": {
        "description": "Mobile app engagement with realistic usage distributions",
        "columns": [
            {"name": "session_id", "type": "realistic_id", "prefix": "APP", "length": 12, "format": "alphanumeric", "null_rate": 0},
            {"name": "user_id", "type": "realistic_id", "prefix": "USER", "length": 8, "format": "alphanumeric", "null_rate": 0},
            {"name": "app_version", "type": "weighted_choice", "choices": ["2.1.0", "2.1.1", "2.2.0", "2.2.1", "2.3.0"], "weights": [5, 10, 25, 35, 25], "null_rate": 0},
            {"name": "session_start", "type": "timestamp", "start_date": "2024-01-01", "end_date": "2024-12-31", "null_rate": 0},
            {"name": "session_duration_seconds", "type": "weighted_choice", "choices": [10, 30, 60, 120, 300, 600, 1800, 3600], "weights": [15, 20, 25, 20, 10, 5, 3, 2], "null_rate": 0},
            {"name": "screens_viewed", "type": "weighted_choice", "choices": [1, 2, 3, 5, 10, 20, 50], "weights": [25, 25, 20, 15, 10, 3, 2], "null_rate": 0},
            {"name": "actions_taken", "type": "weighted_choice", "choices": [0, 1, 3, 5, 10, 25, 50, 100], "weights": [10, 20, 25, 20, 15, 7, 2, 1], "null_rate": 0},
            {"name": "device_model", "type": "weighted_choice", "choices": ["iPhone 14", "iPhone 15", "Samsung Galaxy S23", "Google Pixel 7", "Other"], "weights": [25, 30, 20, 15, 10], "null_rate": 0},
            {"name": "os_version", "type": "weighted_choice", "choices": ["iOS 17.0", "iOS 17.1", "iOS 17.2", "Android 13", "Android 14"], "weights": [15, 25, 30, 20, 10], "null_rate": 0},
            {"name": "crash_occurred", "type": "boolean", "true_rate": 0.005, "null_rate": 0},
            {"name": "push_notifications_enabled", "type": "boolean", "true_rate": 0.65, "null_rate": 0},
            {"name": "location_permission", "type": "weighted_choice", "choices": ["Always", "When in Use", "Never"], "weights": [15, 60, 25], "null_rate": 0},
            {"name": "first_time_user", "type": "boolean", "true_rate": 0.15, "null_rate": 0}
        ]
    },

    "Survey Responses": {
        "description": "Customer survey data with realistic completion and quality patterns",
        "columns": [
            {"name": "response_id", "type": "realistic_id", "prefix": "RESP", "length": 8, "format": "alphanumeric", "null_rate": 0},
            {"name": "survey_id", "type": "realistic_id", "prefix": "SURV", "length": 6, "format": "alphanumeric", "null_rate": 0},
            {"name": "respondent_id", "type": "realistic_id", "prefix": "USER", "length": 8, "format": "alphanumeric", "null_rate": 0.1},
            {"name": "completion_date", "type": "business_hours_timestamp", "start_date": "2024-01-01", "end_date": "2024-12-31", "null_rate": 0},
            {"name": "survey_type", "type": "weighted_choice", "choices": ["Customer Satisfaction", "Product Feedback", "Brand Awareness", "Market Research", "Post-Purchase"], "weights": [30, 25, 15, 15, 15], "null_rate": 0},
            {"name": "completion_rate", "type": "weighted_choice", "choices": [0.1, 0.3, 0.5, 0.7, 0.9, 1.0], "weights": [5, 10, 15, 25, 25, 20], "null_rate": 0},
            {"name": "overall_satisfaction", "type": "weighted_choice", "choices": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "weights": [3, 5, 8, 10, 12, 15, 18, 15, 10, 4], "null_rate": 0.05},
            {"name": "recommend_score", "type": "weighted_choice", "choices": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "weights": [5, 3, 4, 5, 6, 8, 10, 12, 15, 17, 15], "null_rate": 0.1},
            {"name": "time_to_complete_minutes", "type": "weighted_choice", "choices": [0.5, 1, 2, 5, 10, 15, 30], "weights": [5, 15, 25, 30, 15, 7, 3], "null_rate": 0},
            {"name": "response_quality", "type": "weighted_choice", "choices": ["High", "Medium", "Low"], "weights": [40, 45, 15], "null_rate": 0},
            {"name": "demographic_age_group", "type": "weighted_choice", "choices": ["18-24", "25-34", "35-44", "45-54", "55-64", "65+"], "weights": [15, 25, 25, 20, 10, 5], "null_rate": 0.2},
            {"name": "open_text_provided", "type": "boolean", "true_rate": 0.35, "null_rate": 0},
            {"name": "incentive_received", "type": "weighted_choice", "choices": ["None", "Discount", "Gift Card", "Points"], "weights": [40, 30, 20, 10], "null_rate": 0}
        ]
    },

    "Product Catalog": {
        "description": "Product catalog with realistic pricing and inventory patterns",
        "columns": [
            {"name": "product_id", "type": "realistic_id", "prefix": "PROD", "length": 8, "format": "alphanumeric", "null_rate": 0},
            {"name": "sku", "type": "realistic_id", "prefix": "SKU", "length": 10, "format": "alphanumeric", "null_rate": 0},
            {"name": "product_name", "type": "product_name", "null_rate": 0},
            {"name": "category", "type": "weighted_choice", "choices": ["Electronics", "Clothing", "Home & Garden", "Sports", "Books", "Beauty", "Toys"], "weights": [25, 20, 15, 12, 10, 10, 8], "null_rate": 0},
            {"name": "subcategory", "type": "weighted_choice", "choices": ["Audio", "Computers", "Mobile", "Wearables", "Gaming", "Photography"], "weights": [20, 18, 17, 15, 15, 15], "null_rate": 0.1},
            {"name": "brand", "type": "weighted_choice", "choices": ["Apple", "Samsung", "Sony", "Nike", "Adidas", "Generic"], "weights": [20, 18, 15, 12, 10, 25], "null_rate": 0},
            {"name": "price", "type": "currency_amount", "min_val": 9.99, "max_val": 2999.99, "decimals": 2, "null_rate": 0},
            {"name": "cost", "type": "currency_amount", "min_val": 5.00, "max_val": 1500.00, "decimals": 2, "null_rate": 0},
            {"name": "in_stock", "type": "boolean", "true_rate": 0.85, "null_rate": 0},
            {"name": "stock_quantity", "type": "weighted_choice", "choices": [0, 1, 5, 10, 25, 50, 100, 500, 1000], "weights": [5, 5, 10, 15, 20, 20, 15, 7, 3], "null_rate": 0},
            {"name": "avg_rating", "type": "weighted_choice", "choices": [1.0, 2.0, 3.0, 4.0, 4.5, 5.0], "weights": [2, 5, 15, 35, 25, 18], "null_rate": 0.1},
            {"name": "review_count", "type": "weighted_choice", "choices": [0, 1, 5, 10, 25, 100, 500, 1000, 5000], "weights": [10, 15, 20, 20, 15, 10, 7, 2, 1], "null_rate": 0},
            {"name": "created_date", "type": "business_date", "start_date": "2020-01-01", "end_date": "2024-12-31", "null_rate": 0},
            {"name": "last_updated", "type": "business_hours_timestamp", "start_date": "2024-01-01", "end_date": "2024-12-31", "null_rate": 0},
            {"name": "manufacturer_url", "type": "website_url", "null_rate": 0.3}
        ]
    },

    "Shipping & Logistics": {
        "description": "Shipping data with realistic delivery patterns and geographic correlations",
        "columns": [
            {"name": "shipment_id", "type": "realistic_id", "prefix": "SHIP", "length": 10, "format": "alphanumeric", "null_rate": 0},
            {"name": "order_id", "type": "realistic_id", "prefix": "ORD", "length": 8, "format": "alphanumeric", "null_rate": 0},
            {"name": "tracking_number", "type": "realistic_id", "prefix": "TRK", "length": 12, "format": "alphanumeric", "null_rate": 0},
            {"name": "carrier", "type": "weighted_choice", "choices": ["UPS", "FedEx", "USPS", "DHL", "Amazon"], "weights": [30, 25, 20, 15, 10], "null_rate": 0},
            {"name": "service_type", "type": "weighted_choice", "choices": ["Standard", "Express", "Overnight", "Same Day"], "weights": [60, 25, 10, 5], "null_rate": 0},
            {"name": "ship_date", "type": "business_hours_timestamp", "start_date": "2024-01-01", "end_date": "2024-12-31", "null_rate": 0},
            {"name": "estimated_delivery", "type": "business_date", "start_date": "2024-01-01", "end_date": "2024-12-31", "null_rate": 0},
            {"name": "actual_delivery", "type": "business_hours_timestamp", "start_date": "2024-01-01", "end_date": "2024-12-31", "null_rate": 0.1},
            {"name": "origin_address", "type": "localized_address", "locale": "en_US", "null_rate": 0},
            {"name": "destination_address", "type": "localized_address", "locale": "en_US", "null_rate": 0},
            {"name": "origin_coordinates", "type": "coordinates", "null_rate": 0.1},
            {"name": "destination_coordinates", "type": "coordinates", "null_rate": 0.1},
            {"name": "weight_lbs", "type": "weighted_choice", "choices": [0.1, 0.5, 1, 2, 5, 10, 25, 50], "weights": [15, 20, 25, 20, 12, 5, 2, 1], "null_rate": 0},
            {"name": "shipping_cost", "type": "currency_amount", "min_val": 0.99, "max_val": 49.99, "decimals": 2, "null_rate": 0},
            {"name": "delivery_status", "type": "weighted_choice", "choices": ["In Transit", "Out for Delivery", "Delivered", "Failed Delivery", "Returned"], "weights": [20, 10, 60, 5, 5], "null_rate": 0},
            {"name": "delivery_attempts", "type": "weighted_choice", "choices": [1, 2, 3], "weights": [80, 15, 5], "null_rate": 0}
        ]
    },

    "Financial Transactions": {
        "description": "Financial transactions with realistic patterns and fraud indicators",
        "columns": [
            {"name": "transaction_id", "type": "realistic_id", "prefix": "TXN", "length": 12, "format": "alphanumeric", "null_rate": 0},
            {"name": "customer_id", "type": "realistic_id", "prefix": "CUST", "length": 8, "format": "alphanumeric", "null_rate": 0},
            {"name": "account_id", "type": "realistic_id", "prefix": "ACC", "length": 10, "format": "alphanumeric", "null_rate": 0},
            {"name": "transaction_date", "type": "business_hours_timestamp", "start_date": "2024-01-01", "end_date": "2024-12-31", "null_rate": 0},
            {"name": "transaction_type", "type": "weighted_choice", "choices": ["Purchase", "Refund", "Transfer", "Fee", "Interest"], "weights": [70, 10, 10, 7, 3], "null_rate": 0},
            {"name": "amount", "type": "currency_amount", "min_val": 0.01, "max_val": 10000.00, "decimals": 2, "null_rate": 0},
            {"name": "currency", "type": "weighted_choice", "choices": ["USD", "EUR", "GBP", "CAD"], "weights": [70, 15, 10, 5], "null_rate": 0},
            {"name": "payment_method", "type": "weighted_choice", "choices": ["Credit Card", "Debit Card", "ACH", "Wire", "Digital Wallet"], "weights": [40, 25, 20, 10, 5], "null_rate": 0},
            {"name": "merchant_category", "type": "weighted_choice", "choices": ["Retail", "Restaurant", "Gas Station", "Online", "Grocery"], "weights": [30, 20, 15, 25, 10], "null_rate": 0},
            {"name": "status", "type": "weighted_choice", "choices": ["Completed", "Pending", "Failed", "Cancelled"], "weights": [85, 8, 5, 2], "null_rate": 0},
            {"name": "fee_amount", "type": "currency_amount", "min_val": 0.00, "max_val": 50.00, "decimals": 2, "null_rate": 0.7},
            {"name": "balance_after", "type": "currency_amount", "min_val": 0.00, "max_val": 50000.00, "decimals": 2, "null_rate": 0.1},
            {"name": "location", "type": "city", "null_rate": 0.2},
            {"name": "fraud_score", "type": "float", "min_val": 0.0, "max_val": 1.0, "decimals": 4, "null_rate": 0}
        ]
    },

    "Inventory Management": {
        "description": "Product inventory with realistic stock patterns and warehouse operations",
        "columns": [
            {"name": "inventory_id", "type": "realistic_id", "prefix": "INV", "length": 8, "format": "alphanumeric", "null_rate": 0},
            {"name": "product_id", "type": "realistic_id", "prefix": "PROD", "length": 8, "format": "alphanumeric", "null_rate": 0},
            {"name": "warehouse_id", "type": "weighted_choice", "choices": ["WH001", "WH002", "WH003", "WH004", "WH005"], "weights": [25, 20, 20, 20, 15], "null_rate": 0},
            {"name": "location_code", "type": "realistic_id", "prefix": "LOC", "length": 6, "format": "alphanumeric", "null_rate": 0},
            {"name": "current_stock", "type": "weighted_choice", "choices": [0, 5, 10, 25, 50, 100, 500, 1000], "weights": [5, 10, 15, 20, 25, 15, 7, 3], "null_rate": 0},
            {"name": "reserved_stock", "type": "weighted_choice", "choices": [0, 1, 5, 10, 25, 50, 100], "weights": [20, 25, 25, 15, 10, 3, 2], "null_rate": 0},
            {"name": "available_stock", "type": "weighted_choice", "choices": [0, 5, 10, 25, 50, 100, 500, 900], "weights": [5, 10, 15, 20, 25, 15, 7, 3], "null_rate": 0},
            {"name": "reorder_point", "type": "weighted_choice", "choices": [5, 10, 25, 50, 100], "weights": [10, 25, 35, 25, 5], "null_rate": 0},
            {"name": "max_stock_level", "type": "weighted_choice", "choices": [100, 250, 500, 1000, 2000], "weights": [15, 25, 30, 25, 5], "null_rate": 0},
            {"name": "last_received_date", "type": "business_date", "start_date": "2024-01-01", "end_date": "2024-12-31", "null_rate": 0.1},
            {"name": "last_sold_date", "type": "business_date", "start_date": "2024-01-01", "end_date": "2024-12-31", "null_rate": 0.2},
            {"name": "unit_cost", "type": "currency_amount", "min_val": 1.00, "max_val": 500.00, "decimals": 2, "null_rate": 0},
            {"name": "total_value", "type": "currency_amount", "min_val": 0.00, "max_val": 50000.00, "decimals": 2, "null_rate": 0},
            {"name": "turnover_rate", "type": "weighted_choice", "choices": [0.1, 0.5, 1.0, 2.0, 4.0, 8.0, 12.0], "weights": [5, 10, 15, 25, 25, 15, 5], "null_rate": 0},
            {"name": "supplier", "type": "company_name", "null_rate": 0.1}
        ]
    },

    "Sales Leads": {
        "description": "Sales pipeline with realistic lead scoring and progression patterns",
        "columns": [
            {"name": "lead_id", "type": "realistic_id", "prefix": "LEAD", "length": 8, "format": "alphanumeric", "null_rate": 0},
            {"name": "first_name", "type": "first_name", "null_rate": 0},
            {"name": "last_name", "type": "last_name", "null_rate": 0},
            {"name": "email", "type": "company_email", "null_rate": 0},
            {"name": "phone", "type": "business_phone", "null_rate": 0.1},
            {"name": "company", "type": "company_name", "null_rate": 0.2},
            {"name": "job_title", "type": "job_title", "null_rate": 0.15},
            {"name": "company_website", "type": "website_url", "null_rate": 0.4},
            {"name": "lead_source", "type": "weighted_choice", "choices": ["Website", "Referral", "Cold Call", "Trade Show", "Social Media", "Paid Ads"], "weights": [30, 25, 15, 10, 10, 10], "null_rate": 0},
            {"name": "lead_status", "type": "weighted_choice", "choices": ["New", "Qualified", "Contacted", "Opportunity", "Closed Won", "Closed Lost"], "weights": [20, 25, 20, 15, 10, 10], "null_rate": 0},
            {"name": "lead_score", "type": "weighted_choice", "choices": [0, 10, 25, 50, 75, 90, 100], "weights": [10, 15, 20, 25, 20, 7, 3], "null_rate": 0},
            {"name": "estimated_value", "type": "currency_amount", "min_val": 1000.00, "max_val": 100000.00, "decimals": 2, "null_rate": 0.3},
            {"name": "probability", "type": "weighted_choice", "choices": [0.05, 0.15, 0.25, 0.5, 0.75, 0.9, 0.95], "weights": [15, 20, 25, 20, 15, 3, 2], "null_rate": 0.2},
            {"name": "created_date", "type": "business_date", "start_date": "2024-01-01", "end_date": "2024-12-31", "null_rate": 0},
            {"name": "last_contact_date", "type": "business_date", "start_date": "2024-01-01", "end_date": "2024-12-31", "null_rate": 0.1},
            {"name": "assigned_rep", "type": "weighted_choice", "choices": ["Rep001", "Rep002", "Rep003", "Rep004", "Rep005"], "weights": [22, 21, 20, 19, 18], "null_rate": 0.05},
            {"name": "industry", "type": "weighted_choice", "choices": ["Technology", "Healthcare", "Finance", "Manufacturing", "Retail", "Other"], "weights": [25, 20, 15, 15, 15, 10], "null_rate": 0.2}
        ]
    }
}