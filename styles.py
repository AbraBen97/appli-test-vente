import streamlit as st

def load_styles():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
        
        .main {
            font-family: 'Poppins', sans-serif;
        }
        
        .main-header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 2rem;
            border-radius: 20px;
            text-align: center;
            color: white;
            margin-bottom: 1.5rem;
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            position: relative;
            overflow: hidden;
        }
        
        .main-header::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: linear-gradient(45deg, transparent, rgba(255,255,255,0.1), transparent);
            animation: shine 3s infinite;
        }
        
        @keyframes shine {
            0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
            100% { transform: translateX(100%) translateY(100%) rotate(45deg); }
        }
        
        .floating-badge {
            position: absolute;
            top: 15px;
            right: 15px;
            background: #ff4757;
            color: white;
            padding: 0.4rem 0.8rem;
            border-radius: 15px;
            font-size: 0.7rem;
            font-weight: bold;
            animation: bounce 2s infinite;
        }
        
        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
            40% { transform: translateY(-8px); }
            60% { transform: translateY(-4px); }
        }
        
        .product-card {
            background: white;
            border-radius: 15px;
            padding: 1rem;
            box-shadow: 0 6px 20px rgba(0,0,0,0.1);
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            border: 1px solid #f0f0f0;
            height: 100%;
            display: flex;
            flex-direction: column;
            position: relative;
            overflow: hidden;
        }
        
        .product-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
            transition: left 0.5s;
        }
        
        .product-card:hover::before {
            left: 100%;
        }
        
        .product-card:hover {
            transform: translateY(-8px) scale(1.02);
            box-shadow: 0 15px 30px rgba(0,0,0,0.2);
        }
        
        .product-image {
            width: 100%;
            height: 200px;
            object-fit: cover;
            border-radius: 10px;
            margin-bottom: 0.8rem;
            transition: transform 0.3s ease;
        }
        
        .product-card:hover .product-image {
            transform: scale(1.05);
        }
        
        .product-title {
            font-size: 1.1rem;
            font-weight: 600;
            color: #333;
            margin-bottom: 0.6rem;
            text-align: center;
        }
        
        .product-price {
            font-size: 1.4rem;
            font-weight: 700;
            background: linear-gradient(45deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-top: auto;
            text-align: center;
        }
        
        .new-badge {
            position: absolute;
            top: 10px;
            left: 10px;
            background: linear-gradient(45deg, #ff6b6b, #ee5a52);
            color: white;
            padding: 0.3rem 0.6rem;
            border-radius: 10px;
            font-size: 0.6rem;
            font-weight: bold;
            z-index: 2;
        }
        
        .sale-badge {
            position: absolute;
            top: 10px;
            right: 10px;
            background: linear-gradient(45deg, #feca57, #ff9ff3);
            color: white;
            padding: 0.3rem 0.6rem;
            border-radius: 10px;
            font-size: 0.6rem;
            font-weight: bold;
            z-index: 2;
        }
        
        .category-filter {
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            padding: 1.5rem;
            border-radius: 15px;
            margin-bottom: 1.5rem;
            text-align: center;
            box-shadow: 0 8px 20px rgba(0,0,0,0.1);
        }
        
        .stats-section {
            background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
            padding: 1.5rem;
            border-radius: 15px;
            margin: 1.5rem 0;
            text-align: center;
            box-shadow: 0 8px 20px rgba(0,0,0,0.1);
        }
        
        .stat-item {
            display: inline-block;
            margin: 0.8rem;
            text-align: center;
        }
        
        .stat-number {
            font-size: 2rem;
            font-weight: 700;
            color: #333;
            display: block;
        }
        
        .stat-label {
            font-size: 0.9rem;
            color: #666;
            font-weight: 500;
        }
        
        .promo-banner {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 0.8rem;
            text-align: center;
            border-radius: 8px;
            margin: 0.8rem 0;
            animation: pulse 2s infinite;
            cursor: pointer;
        }
        
        @keyframes pulse {
            0% { box-shadow: 0 0 0 0 rgba(102, 126, 234, 0.7); }
            70% { box-shadow: 0 0 0 8px rgba(102, 126, 234, 0); }
            100% { box-shadow: 0 0 0 0 rgba(102, 126, 234, 0); }
        }
        
        .testimonial-card {
            background: white;
            padding: 1.5rem;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            margin: 0.8rem;
            text-align: center;
            border-left: 3px solid #667eea;
        }
        
        .filter-button {
            background: white;
            border: 2px solid transparent;
            padding: 0.8rem 1rem;
            border-radius: 25px;
            margin: 0.2rem;
            cursor: pointer;
            transition: all 0.3s ease;
            font-weight: 600;
            color: #333;
        }
        
        .filter-button:hover {
            background: white;
            border-color: white;
            transform: translateY(-2px);
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
        }
        
        .detail-modal {
            background: white;
            border-radius: 20px;
            padding: 1.5rem;
            box-shadow: 0 20px 60px rgba(0,0,0,0.15);
        }
        
        .gallery-image {
            width: 100%;
            height: 180px;
            object-fit: cover;
            border-radius: 10px;
            margin-bottom: 0.8rem;
            cursor: pointer;
            transition: all 0.3s ease;
            border: 2px solid transparent;
        }
        
        .gallery-image:hover {
            transform: scale(1.05);
            border-color: #667eea;
            box-shadow: 0 8px 20px rgba(0,0,0,0.2);
        }
        
        .size-badge {
            display: inline-block;
            background: linear-gradient(45deg, #667eea, #764ba2);
            color: white;
            padding: 0.4rem 0.8rem;
            border-radius: 15px;
            margin: 0.2rem;
            font-size: 0.8rem;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.2s ease;
        }
        
        .size-badge:hover {
            transform: scale(1.1);
        }
        
        .back-button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 0.8rem 2rem;
            border-radius: 25px;
            cursor: pointer;
            font-weight: bold;
            margin-bottom: 0.8rem;
            transition: all 0.3s ease;
        }
        
        .back-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(0,0,0,0.2);
        }
        
        .contact-section {
            background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
            padding: 2rem;
            border-radius: 20px;
            margin-top: 2rem;
            color: white;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }
        
        .contact-item {
            background: rgba(255,255,255,0.2);
            padding: 1rem;
            border-radius: 10px;
            margin: 0.8rem 0;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.3);
        }
        
        .whatsapp-button {
            background: #25D366;
            color: white;
            padding: 1rem 2rem;
            border-radius: 25px;
            text-decoration: none;
            font-weight: bold;
            display: inline-block;
            margin: 0.8rem;
            transition: all 0.3s ease;
            box-shadow: 0 4px 10px rgba(37, 211, 102, 0.4);
        }
        
        .whatsapp-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(37, 211, 102, 0.6);
            text-decoration: none;
            color: white;
        }
        
        .order-section {
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            padding: 1.5rem;
            border-radius: 15px;
            margin: 1rem 0;
            text-align: center;
            color: white;
            box-shadow: 0 8px 20px rgba(0,0,0,0.1);
        }
        
        .cart-section {
            background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
            padding: 1.5rem;
            border-radius: 15px;
            margin: 1rem 0;
            text-align: center;
            box-shadow: 0 8px 20px rgba(0,0,0,0.1);
        }
        
        .loading-spinner {
            border: 2px solid #f3f3f3;
            border-top: 2px solid #667eea;
            border-radius: 50%;
            width: 30px;
            height: 30px;
            animation: spin 1s linear infinite;
            margin: 15px auto;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        .search-container {
            background: white;
            padding: 0.8rem;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            margin-bottom: 1.5rem;
        }
        
        .feature-highlight {
            background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
            padding: 1.5rem;
            border-radius: 15px;
            margin: 1.5rem 0;
            text-align: center;
            box-shadow: 0 6px 20px rgba(0,0,0,0.1);
        }
                

        .old-price {
            color: #e63946;
            font-size: 1.2rem;
            font-weight: 500;
            text-decoration: line-through;
            text-align: center;
            margin-bottom: 0.2rem;
        }
        
        .new-price {
            color: #333;
            font-size: 1.4rem;
            font-weight: 700;
            text-align: center;
        }
        
        /* Responsive Design */
        @media (max-width: 768px) {
            .product-card {
                margin: 0.5rem;
                padding: 0.8rem;
            }
            .product-image {
                height: 150px;
            }
            .product-title {
                font-size: 1rem;
            }
            .product-price {
                font-size: 1.2rem;
            }
            .stat-number {
                font-size: 1.5rem;
            }
            .stat-label {
                font-size: 0.8rem;
            }
            .gallery-image {
                height: 120px;
            }
            .main-header {
                padding: 1.5rem;
            }
            .main-header h1 {
                font-size: 1.5rem;
            }
            .category-filter {
                padding: 1rem;
            }
            .filter-button {
                padding: 0.6rem 0.8rem;
                font-size: 0.8rem;
            }
            .size-badge {
                padding: 0.3rem 0.6rem;
                font-size: 0.7rem;
            }
        }
        
        @media (max-width: 480px) {
            .product-image {
                height: 120px;
            }
            .product-title {
                font-size: 0.9rem;
            }
            .product-price {
                font-size: 1rem;
            }
            .gallery-image {
                height: 100px;
            }
            .main-header {
                padding: 1rem;
            }
            .main-header h1 {
                font-size: 1.2rem;
            }
            .filter-button {
                padding: 0.5rem 0.6rem;
                font-size: 0.7rem;
            }
        }
    </style>
    """, unsafe_allow_html=True)