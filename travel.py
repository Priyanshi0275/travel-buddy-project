import streamlit as st
import pandas as pd
from datetime import datetime, date, timedelta
import hashlib

# Page configuration - must be first Streamlit command
st.set_page_config(
    page_title="TravelMatch - Find Your Perfect Travel Companions",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced custom CSS for modern black and purple theme
def load_css():
    st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    .stApp {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a0a1a 25%, #2a1a3a 50%, #1a0a1a 75%, #0a0a0a 100%);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
        font-family: 'Inter', sans-serif;
        color: #ffffff;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Sidebar Styling */
    .css-1d391kg, [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1a2e 0%, #16213e 50%, #0f0f23 100%);
        border-right: 2px solid rgba(139, 92, 246, 0.3);
        backdrop-filter: blur(15px);
    }
    
    .css-1d391kg::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(45deg, rgba(139, 92, 246, 0.05) 0%, rgba(168, 85, 247, 0.05) 100%);
        border-radius: 20px;
        margin: 10px;
    }
    
    /* Main content area */
    .main .block-container {
        padding: 1rem 2rem;
        background: rgba(255, 255, 255, 0.02);
        border-radius: 25px;
        backdrop-filter: blur(20px);
        border: 1px solid rgba(139, 92, 246, 0.2);
        margin: 1rem;
        box-shadow: 0 20px 60px rgba(139, 92, 246, 0.1);
        animation: fadeInUp 0.8s ease-out;
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Enhanced Typography */
    h1 {
        color: #ffffff;
        font-family: 'Poppins', sans-serif;
        font-weight: 800;
        font-size: 4rem;
        text-align: center;
        margin-bottom: 0.5rem;
        background: linear-gradient(45deg, #8b5cf6, #a855f7, #c084fc, #e879f9);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: gradientText 3s ease-in-out infinite;
        text-shadow: 0 0 40px rgba(139, 92, 246, 0.3);
    }
    
    @keyframes gradientText {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    h2 {
        color: #e5e7eb;
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        font-size: 2.5rem;
        margin-bottom: 1.5rem;
        position: relative;
        padding-bottom: 0.5rem;
    }
    
    h2::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        width: 60px;
        height: 3px;
        background: linear-gradient(90deg, #8b5cf6, #a855f7);
        border-radius: 2px;
    }
    
    h3 {
        color: #d1d5db;
        font-family: 'Poppins', sans-serif;
        font-weight: 500;
        font-size: 1.8rem;
        margin-bottom: 1rem;
    }
    
    /* Enhanced Cards */
    .glass-card {
        background: linear-gradient(135deg, rgba(139, 92, 246, 0.1) 0%, rgba(168, 85, 247, 0.05) 100%);
        border: 1px solid rgba(139, 92, 246, 0.2);
        border-radius: 20px;
        padding: 2rem;
        margin: 1.5rem 0;
        backdrop-filter: blur(20px);
        box-shadow: 0 15px 35px rgba(139, 92, 246, 0.1);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .glass-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
        transition: left 0.7s;
    }
    
    .glass-card:hover::before {
        left: 100%;
    }
    
    .glass-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 25px 50px rgba(139, 92, 246, 0.2);
        border-color: rgba(139, 92, 246, 0.4);
    }
    
    /* Hero Section */
    .hero-container {
        text-align: center;
        padding: 3rem 0;
        background: linear-gradient(135deg, rgba(139, 92, 246, 0.05) 0%, rgba(168, 85, 247, 0.05) 100%);
        border-radius: 25px;
        margin-bottom: 2rem;
        position: relative;
        overflow: hidden;
    }
    
    .hero-container::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(139, 92, 246, 0.1) 0%, transparent 70%);
        animation: rotate 20s linear infinite;
    }
    
    @keyframes rotate {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    
    .hero-title {
        font-family: 'Poppins', sans-serif;
        font-size: 5rem;
        font-weight: 800;
        background: linear-gradient(45deg, #8b5cf6, #a855f7, #c084fc, #e879f9);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: gradientText 3s ease-in-out infinite;
        margin-bottom: 1rem;
        position: relative;
        z-index: 1;
    }
    
    .hero-subtitle {
        font-size: 1.5rem;
        color: #d1d5db;
        font-weight: 300;
        font-style: italic;
        margin-bottom: 2rem;
        position: relative;
        z-index: 1;
    }
    
    /* Enhanced Buttons */
    .stButton > button {
        background: linear-gradient(45deg, #8b5cf6, #a855f7);
        color: white;
        border: none;
        border-radius: 15px;
        padding: 1rem 2.5rem;
        font-weight: 600;
        font-size: 1.1rem;
        font-family: 'Poppins', sans-serif;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 8px 25px rgba(139, 92, 246, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
        transition: left 0.5s;
    }
    
    .stButton > button:hover::before {
        left: 100%;
    }
    
    .stButton > button:hover {
        background: linear-gradient(45deg, #7c3aed, #9333ea);
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 15px 35px rgba(139, 92, 246, 0.4);
    }
    
    /* Enhanced Form Elements */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div > select,
    .stNumberInput > div > div > input,
    .stDateInput > div > div > input {
        background: rgba(255, 255, 255, 0.05);
        border: 2px solid rgba(139, 92, 246, 0.2);
        border-radius: 12px;
        color: #ffffff;
        padding: 1rem;
        font-size: 1rem;
        font-family: 'Inter', sans-serif;
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus,
    .stSelectbox > div > div > select:focus,
    .stNumberInput > div > div > input:focus,
    .stDateInput > div > div > input:focus {
        border-color: #8b5cf6;
        box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.2);
        background: rgba(255, 255, 255, 0.08);
    }
    
    /* Enhanced Labels */
    .stTextInput > label,
    .stTextArea > label,
    .stSelectbox > label,
    .stNumberInput > label,
    .stDateInput > label {
        color: #e5e7eb;
        font-weight: 500;
        font-size: 1.1rem;
        font-family: 'Poppins', sans-serif;
        margin-bottom: 0.5rem;
    }
    
    /* Enhanced Metrics */
    [data-testid="metric-container"] {
        background: linear-gradient(135deg, rgba(139, 92, 246, 0.15) 0%, rgba(168, 85, 247, 0.1) 100%);
        border: 1px solid rgba(139, 92, 246, 0.3);
        border-radius: 15px;
        padding: 1.5rem;
        backdrop-filter: blur(15px);
        transition: all 0.3s ease;
        text-align: center;
    }
    
    [data-testid="metric-container"]:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(139, 92, 246, 0.2);
    }
    
    [data-testid="metric-container"] > div {
        color: #ffffff;
        font-family: 'Poppins', sans-serif;
    }
    
    [data-testid="metric-container"] [data-testid="metric-value"] {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(45deg, #8b5cf6, #a855f7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    /* Match Cards */
    .match-card {
        background: linear-gradient(135deg, rgba(139, 92, 246, 0.1) 0%, rgba(168, 85, 247, 0.05) 100%);
        border: 1px solid rgba(139, 92, 246, 0.3);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        backdrop-filter: blur(20px);
        box-shadow: 0 10px 30px rgba(139, 92, 246, 0.1);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .match-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #8b5cf6, #a855f7, #c084fc);
        border-radius: 20px 20px 0 0;
    }
    
    .match-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 20px 40px rgba(139, 92, 246, 0.2);
        border-color: rgba(139, 92, 246, 0.5);
    }
    
    /* Match Score Badge */
    .match-score {
        background: linear-gradient(45deg, #8b5cf6, #a855f7);
        color: white;
        padding: 0.5rem 1.2rem;
        border-radius: 25px;
        font-weight: 600;
        font-family: 'Poppins', sans-serif;
        display: inline-block;
        margin: 0.5rem 0;
        box-shadow: 0 4px 15px rgba(139, 92, 246, 0.3);
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    
    /* Enhanced Expander */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, rgba(139, 92, 246, 0.2) 0%, rgba(168, 85, 247, 0.15) 100%);
        border: 1px solid rgba(139, 92, 246, 0.3);
        border-radius: 15px;
        color: #ffffff;
        font-weight: 600;
        font-family: 'Poppins', sans-serif;
        padding: 1rem;
        transition: all 0.3s ease;
    }
    
    .streamlit-expanderHeader:hover {
        background: linear-gradient(135deg, rgba(139, 92, 246, 0.3) 0%, rgba(168, 85, 247, 0.25) 100%);
        transform: translateY(-2px);
    }
    
    /* Success/Error/Info messages */
    .stSuccess {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.15) 0%, rgba(5, 150, 105, 0.1) 100%);
        border: 1px solid rgba(16, 185, 129, 0.3);
        border-radius: 15px;
        color: #86efac;
        backdrop-filter: blur(10px);
    }
    
    .stError {
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.15) 0%, rgba(220, 38, 38, 0.1) 100%);
        border: 1px solid rgba(239, 68, 68, 0.3);
        border-radius: 15px;
        color: #fca5a5;
        backdrop-filter: blur(10px);
    }
    
    .stInfo {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.15) 0%, rgba(37, 99, 235, 0.1) 100%);
        border: 1px solid rgba(59, 130, 246, 0.3);
        border-radius: 15px;
        color: #93c5fd;
        backdrop-filter: blur(10px);
    }
    
    .stWarning {
        background: linear-gradient(135deg, rgba(245, 158, 11, 0.15) 0%, rgba(217, 119, 6, 0.1) 100%);
        border: 1px solid rgba(245, 158, 11, 0.3);
        border-radius: 15px;
        color: #fbbf24;
        backdrop-filter: blur(10px);
    }
    
    /* Feature Icons */
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        display: block;
        text-align: center;
        filter: drop-shadow(0 0 10px rgba(139, 92, 246, 0.5));
    }
    
    /* Stats Container */
    .stats-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
    }
    
    /* Floating Elements */
    .floating {
        animation: floating 3s ease-in-out infinite;
    }
    
    @keyframes floating {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    /* Glassmorphism effect for sidebar elements */
    .css-1d391kg .stSelectbox > div > div,
    .css-1d391kg .stButton > button {
        background: rgba(139, 92, 246, 0.1);
        border: 1px solid rgba(139, 92, 246, 0.3);
        backdrop-filter: blur(10px);
        border-radius: 12px;
    }
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(0, 0, 0, 0.2);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(45deg, #8b5cf6, #a855f7);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(45deg, #7c3aed, #9333ea);
    }
    
    /* Loading animation */
    .loading {
        display: inline-block;
        width: 20px;
        height: 20px;
        border: 3px solid rgba(139, 92, 246, 0.3);
        border-radius: 50%;
        border-top-color: #8b5cf6;
        animation: spin 1s ease-in-out infinite;
    }
    
    @keyframes spin {
        to { transform: rotate(360deg); }
    }
    
    /* Mobile responsiveness */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 3rem;
        }
        
        h1 {
            font-size: 3rem;
        }
        
        .glass-card {
            padding: 1.5rem;
            margin: 1rem 0;
        }
        
        .main .block-container {
            padding: 1rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state for data storage
def init_session_state():
    if 'users' not in st.session_state:
        st.session_state.users = {}
    if 'trips' not in st.session_state:
        st.session_state.trips = {}
    if 'current_user' not in st.session_state:
        st.session_state.current_user = None

def generate_id(text):
    """Generate a simple ID from text"""
    return hashlib.md5(text.encode()).hexdigest()[:8]

def register_user(name, email, age, bio):
    """Register a new user and return their ID"""
    user_id = generate_id(email + str(datetime.now()))
    st.session_state.users[user_id] = {
        'id': user_id,
        'name': name,
        'email': email,
        'age': age,
        'bio': bio,
        'created_at': datetime.now()
    }
    return user_id

def create_trip(user_id, destination, start_date, end_date, budget, itinerary, group_size, travel_style):
    """Create a new trip and return trip ID"""
    trip_id = generate_id(user_id + destination + str(datetime.now()))
    st.session_state.trips[trip_id] = {
        'id': trip_id,
        'user_id': user_id,
        'destination': destination,
        'start_date': start_date,
        'end_date': end_date,
        'budget': budget,
        'itinerary': itinerary,
        'group_size': group_size,
        'travel_style': travel_style,
        'created_at': datetime.now()
    }
    return trip_id

def calculate_match_score(trip1, trip2):
    """Calculate compatibility score between two trips"""
    if trip1['user_id'] == trip2['user_id']:
        return 0
    
    score = 0
    max_score = 100
    
    # Destination match (30 points)
    if trip1['destination'].lower() == trip2['destination'].lower():
        score += 30
    elif any(word in trip2['destination'].lower() for word in trip1['destination'].lower().split()):
        score += 15
    
    # Date overlap (25 points)
    start1, end1 = trip1['start_date'], trip1['end_date']
    start2, end2 = trip2['start_date'], trip2['end_date']
    
    if start1 <= end2 and start2 <= end1:
        overlap_days = (min(end1, end2) - max(start1, start2)).days + 1
        total_days = max((end1 - start1).days + 1, (end2 - start2).days + 1)
        score += (overlap_days / total_days) * 25
    
    # Budget compatibility (20 points)
    budget_diff = abs(trip1['budget'] - trip2['budget'])
    max_budget = max(trip1['budget'], trip2['budget'])
    if max_budget > 0:
        budget_score = max(0, 20 - (budget_diff / max_budget) * 20)
        score += budget_score
    
    # Group size compatibility (15 points)
    size_diff = abs(trip1['group_size'] - trip2['group_size'])
    group_score = max(0, 15 - size_diff * 3)
    score += group_score
    
    # Travel style match (10 points)
    if trip1['travel_style'] == trip2['travel_style']:
        score += 10
    
    return score

def find_matches(user_trip_id, min_score=20):
    """Find matching trips for a given trip"""
    if user_trip_id not in st.session_state.trips:
        return []
    
    user_trip = st.session_state.trips[user_trip_id]
    matches = []
    
    for trip_id, trip in st.session_state.trips.items():
        if trip_id != user_trip_id:
            score = calculate_match_score(user_trip, trip)
            if score >= min_score:
                trip_with_score = trip.copy()
                trip_with_score['match_score'] = score
                trip_with_score['user_info'] = st.session_state.users.get(trip['user_id'], {})
                matches.append(trip_with_score)
    
    return sorted(matches, key=lambda x: x['match_score'], reverse=True)

def show_home_page():
    # Hero Section
    st.markdown("""
    <div class="hero-container">
        <div class="hero-title floating">✈️ TravelMatch</div>
        <div class="hero-subtitle">Connect with like-minded travelers and create unforgettable journeys together</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Main content in columns
    col1, col2 = st.columns([2, 1], gap="large")
    
    with col1:
        st.markdown("""
        <div class="glass-card">
            <div class="feature-icon">🌟</div>
            <h2>Welcome to the Future of Travel</h2>
            <p style="font-size: 1.2rem; line-height: 1.8; color: #d1d5db;">
                Transform your solo adventures into epic group journeys. Our AI-powered matching system connects you with travelers who share your wanderlust, budget, and timeline.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Feature cards
        features = [
            {"icon": "🎯", "title": "Smart Matching", "desc": "Advanced algorithm matches you with compatible travelers based on destination, dates, budget, and travel style"},
            {"icon": "💰", "title": "Cost Splitting", "desc": "Share expenses on accommodation, transportation, and activities to travel more for less"},
            {"icon": "🛡️", "title": "Safe & Secure", "desc": "Travel with vetted companions and enjoy the safety and confidence of group travel"},
            {"icon": "🌍", "title": "Global Network", "desc": "Connect with travelers worldwide and discover hidden gems through local insights"}
        ]
        
        for i, feature in enumerate(features):
            st.markdown(f"""
            <div class="glass-card" style="animation-delay: {i * 0.2}s;">
                <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                    <span style="font-size: 2.5rem; margin-right: 1rem;">{feature['icon']}</span>
                    <h3 style="margin: 0; color: #ffffff;">{feature['title']}</h3>
                </div>
                <p style="color: #d1d5db; font-size: 1.1rem; line-height: 1.6;">{feature['desc']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="glass-card">
            <div class="feature-icon">📊</div>
            <h3 style="text-align: center; margin-bottom: 2rem;">Live Statistics</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Enhanced metrics
        total_users = len(st.session_state.users)
        total_trips = len(st.session_state.trips)
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.metric("👥 Travelers", total_users, delta=f"+{min(total_users, 12)} this week")
        with col_b:
            st.metric("✈️ Active Trips", total_trips, delta=f"+{min(total_trips, 8)} today")
        
        if st.session_state.trips:
            destinations = [trip['destination'] for trip in st.session_state.trips.values()]
            if destinations:
                popular_dest = max(set(destinations), key=destinations.count)
                st.metric("🏆 Trending Destination", popular_dest)
        
        # Quick stats
        if total_trips > 0:
            avg_budget = sum(trip['budget'] for trip in st.session_state.trips.values()) / total_trips
            st.metric("💵 Average Budget", f"${avg_budget:,.0f}")
        
        # Call to action
        st.markdown("""
        <div class="glass-card" style="text-align: center; margin-top: 2rem;">
            <h3>Ready to Start Your Journey?</h3>
            <p style="color: #d1d5db;">Join thousands of travelers finding their perfect companions</p>
        </div>
        """, unsafe_allow_html=True)

def show_register_page():
    st.markdown('<h1>👤 Join TravelMatch</h1>', unsafe_allow_html=True)
    
    if st.session_state.current_user:
        user = st.session_state.users[st.session_state.current_user]
        st.markdown(f"""
        <div class="glass-card" style="text-align: center;">
            <div class="feature-icon">👋</div>
            <h2>Welcome back, {user['name']}!</h2>
            <p style="color: #d1d5db;">Ready to explore the world together?</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🚪 Logout", type="secondary"):
            st.session_state.current_user = None
            st.rerun()
        return
    
    st.markdown("""
    <div class="glass-card">
        <div class="feature-icon">🌟</div>
        <h2 style="text-align: center;">Create Your Travel Profile</h2>
        <p style="text-align: center; color: #d1d5db; font-size: 1.2rem;">Join our community of passionate travelers and discover your next adventure companions</p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.form("registration_form", clear_on_submit=False):
        col1, col2 = st.columns(2, gap="large")
        
        with col1:
            name = st.text_input("👤 Full Name", placeholder="Enter your full name", key="reg_name")
            email = st.text_input("📧 Email Address", placeholder="your.email@example.com", key="reg_email")
        
        with col2:
            age = st.number_input("🎂 Age", min_value=18, max_value=100, value=25, key="reg_age")
        
        bio = st.text_area("📝 Tell us about yourself", 
                          placeholder="Share your travel style, favorite destinations, what you're looking for in travel companions...",
                          height=120, key="reg_bio")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        col_submit, col_spacer = st.columns([1, 2])
        with col_submit:
            submitted = st.form_submit_button("🚀 Join TravelMatch", type="primary", use_container_width=True)
        
        if submitted:
            if name and email:
                existing_user = None
                for uid, user in st.session_state.users.items():
                    if user['email'] == email:
                        existing_user = uid
                        break
                
                if existing_user:
                    st.session_state.current_user = existing_user
                    st.success("🎉 Welcome back! You're now logged in.")
                    st.rerun()
                else:
                    user_id = register_user(name, email, age, bio)
                    st.session_state.current_user = user_id
                    st.success("🎊 Welcome to TravelMatch! Your profile has been created successfully.")
                    st.rerun()
            else:
                st.error("❗ Please fill in your name and email address to continue.")

def show_create_trip_page():
    st.markdown('<h1>✈️ Plan Your Adventure</h1>', unsafe_allow_html=True)
    
    if not st.session_state.current_user:
        st.markdown("""
        <div class="glass-card" style="text-align: center;">
            <div class="feature-icon">⚠️</div>
            <h3>Authentication Required</h3>
            <p style="color: #d1d5db;">Please register or log in to create your travel plans</p>
        </div>
        """, unsafe_allow_html=True)
        return
    
    st.markdown("""
    <div class="glass-card">
        <div class="feature-icon">🗺️</div>
        <h2 style="text-align: center;">Create Your Dream Trip</h2>
        <p style="text-align: center; color: #d1d5db; font-size: 1.2rem;">Share your travel plans and let our AI find your perfect companions</p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.form("trip_form", clear_on_submit=False):
        col1, col2 = st.columns(2, gap="large")
        
        with col1:
            destination = st.text_input("🌍 Destination", 
                                      placeholder="e.g., Bali, Indonesia or Europe Backpacking", 
                                      key="trip_dest")
            
            start_date = st.date_input("📅 Departure Date", 
                                     min_value=date.today(),
                                     value=date.today() + timedelta(days=30),
                                     key="trip_start")
            
            budget = st.number_input("💰 Budget per Person (USD)", 
                                   min_value=100, max_value=50000, value=2000, step=100,
                                   key="trip_budget")
            
            travel_style = st.selectbox("🎯 Travel Style", [
                "🎒 Backpacking Adventure", "💎 Luxury Experience", "🏨 Comfortable Mid-range", 
                "💵 Budget Explorer", "🏔️ Adventure Sports", "🏛️ Cultural Immersion", 
                "🏖️ Beach & Relaxation", "🎉 Nightlife & Party"
            ], key="trip_style")
        
        with col2:
            end_date = st.date_input("📅 Return Date", 
                                   min_value=start_date if 'start_date' in locals() else date.today(),
                                   value=(start_date if 'start_date' in locals() else date.today()) + timedelta(days=7),
                                   key="trip_end")
            
            group_size = st.number_input("👥 Ideal Group Size", 
                                       min_value=2, max_value=20, value=4,
                                       key="trip_group")
        
        itinerary = st.text_area("📋 Trip Details & Preferences", 
                                placeholder="Describe your planned activities, must-see places, accommodation style, special interests...",
                                height=150, key="trip_itinerary")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        col_submit, col_spacer = st.columns([1, 2])
        with col_submit:
            submitted = st.form_submit_button("🚀 Create Trip", type="primary", use_container_width=True)
        
        if submitted:
            if destination and start_date and end_date and budget:
                if end_date < start_date:
                    st.error("❗ Your return date must be after your departure date.")
                else:
                    trip_id = create_trip(
                        st.session_state.current_user, destination, start_date, 
                        end_date, budget, itinerary, group_size, travel_style
                    )
                    st.success("🎉 Your trip has been created successfully!")
                    st.info("💡 Head over to 'Find Matches' to discover your potential travel companions!")
            else:
                st.error("❗ Please fill in all the required fields to create your trip.")

def show_matches_page():
    st.markdown('<h1>🔍 Discover Your Travel Matches</h1>', unsafe_allow_html=True)
    
    if not st.session_state.current_user:
        st.markdown("""
        <div class="glass-card" style="text-align: center;">
            <div class="feature-icon">⚠️</div>
            <h3>Get Started</h3>
            <p style="color: #d1d5db;">Please register and create a trip to find your matches</p>
        </div>
        """, unsafe_allow_html=True)
        return
    
    user_trips = {}
    for tid, trip in st.session_state.trips.items():
        if trip['user_id'] == st.session_state.current_user:
            user_trips[tid] = trip
    
    if not user_trips:
        st.markdown("""
        <div class="glass-card" style="text-align: center;">
            <div class="feature-icon">✈️</div>
            <h3>No Trips Found</h3>
            <p style="color: #d1d5db;">Create your first trip to start finding amazing travel companions!</p>
        </div>
        """, unsafe_allow_html=True)
        return
    
    st.markdown("""
    <div class="glass-card">
        <div class="feature-icon">🎯</div>
        <h2 style="text-align: center;">AI-Powered Travel Matching</h2>
        <p style="text-align: center; color: #d1d5db; font-size: 1.2rem;">Our smart algorithm analyzes destinations, dates, budgets, and travel styles to find your perfect companions</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Trip selection
    trip_options = {}
    for tid, trip in user_trips.items():
        display_name = f"🌍 {trip['destination']} • {trip['start_date'].strftime('%b %d')} - {trip['end_date'].strftime('%b %d, %Y')}"
        trip_options[display_name] = tid
    
    selected_trip_display = st.selectbox("🎯 Select your trip to find matches:", list(trip_options.keys()))
    selected_trip_id = trip_options[selected_trip_display]
    
    col1, col2 = st.columns([2, 1])
    with col1:
        min_score = st.slider("🎚️ Minimum compatibility score:", 0, 100, 20, 5)
    
    matches = find_matches(selected_trip_id, min_score)
    
    if matches:
        st.markdown(f"""
        <div class="glass-card" style="text-align: center;">
            <div class="feature-icon">🎊</div>
            <h3>Found {len(matches)} Compatible Matches!</h3>
            <p style="color: #d1d5db;">Sorted by compatibility score</p>
        </div>
        """, unsafe_allow_html=True)
        
        for i, match in enumerate(matches):
            # Determine score color and emoji
            if match['match_score'] >= 80:
                score_emoji = "🔥"
                score_color = "#10b981"
            elif match['match_score'] >= 60:
                score_emoji = "⭐"
                score_color = "#8b5cf6"
            elif match['match_score'] >= 40:
                score_emoji = "✨"
                score_color = "#f59e0b"
            else:
                score_emoji = "💫"
                score_color = "#6b7280"
            
            with st.expander(f"{score_emoji} Match #{i+1} • {match['match_score']:.0f}% Compatibility", expanded=i==0):
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, rgba(139, 92, 246, 0.1) 0%, rgba(168, 85, 247, 0.05) 100%); 
                            border: 1px solid rgba(139, 92, 246, 0.2); border-radius: 15px; padding: 1.5rem; margin: 1rem 0;">
                """, unsafe_allow_html=True)
                
                col_left, col_right = st.columns([2, 1])
                
                with col_left:
                    st.markdown(f"### 📍 {match['destination']}")
                    
                    col_a, col_b = st.columns(2)
                    with col_a:
                        st.markdown(f"**📅 Dates:** {match['start_date']} → {match['end_date']}")
                        st.markdown(f"**💰 Budget:** ${match['budget']:,} per person")
                    with col_b:
                        st.markdown(f"**👥 Group Size:** {match['group_size']} travelers")
                        st.markdown(f"**🎯 Style:** {match['travel_style']}")
                    
                    if match['itinerary']:
                        st.markdown("**📋 Trip Details:**")
                        st.markdown(f"_{match['itinerary']}_")
                
                with col_right:
                    st.markdown(f"""
                    <div style="text-align: center; padding: 1rem; background: rgba(139, 92, 246, 0.1); border-radius: 12px;">
                        <div style="font-size: 2.5rem; color: {score_color}; font-weight: bold; margin-bottom: 0.5rem;">
                            {match['match_score']:.0f}%
                        </div>
                        <div style="color: #d1d5db; font-size: 0.9rem;">Compatibility</div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown("### 👤 Traveler Profile")
                    st.markdown(f"**Name:** {match['user_info'].get('name', 'Anonymous')}")
                    st.markdown(f"**Age:** {match['user_info'].get('age', 'N/A')}")
                    
                    if match['user_info'].get('bio'):
                        st.markdown("**About:**")
                        st.markdown(f"_{match['user_info']['bio']}_")
                    
                    if st.button(f"💬 Connect with {match['user_info'].get('name', 'Traveler')}", 
                               key=f"connect_{match['id']}", type="primary", use_container_width=True):
                        st.success("🎉 Connection request sent!")
                        st.info(f"📧 Contact: {match['user_info'].get('email', 'N/A')}")
                
                st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="glass-card" style="text-align: center;">
            <div class="feature-icon">🔍</div>
            <h3>No Matches Found</h3>
            <p style="color: #d1d5db;">Try lowering your compatibility threshold or create more trips to increase your chances!</p>
        </div>
        """, unsafe_allow_html=True)

def show_my_trips_page():
    st.markdown('<h1>📋 My Travel Plans</h1>', unsafe_allow_html=True)
    
    if not st.session_state.current_user:
        st.markdown("""
        <div class="glass-card" style="text-align: center;">
            <div class="feature-icon">⚠️</div>
            <h3>Please Sign In</h3>
            <p style="color: #d1d5db;">Register or log in to view your travel plans</p>
        </div>
        """, unsafe_allow_html=True)
        return
    
    user_trips = {}
    for tid, trip in st.session_state.trips.items():
        if trip['user_id'] == st.session_state.current_user:
            user_trips[tid] = trip
    
    if not user_trips:
        st.markdown("""
        <div class="glass-card" style="text-align: center;">
            <div class="feature-icon">✈️</div>
            <h3>No Trips Yet</h3>
            <p style="color: #d1d5db;">Ready to plan your next adventure? Create your first trip to get started!</p>
        </div>
        """, unsafe_allow_html=True)
        return
    
    user = st.session_state.users[st.session_state.current_user]
    st.markdown(f"""
    <div class="glass-card" style="text-align: center;">
        <div class="feature-icon">👋</div>
        <h2>Welcome, {user['name']}!</h2>
        <p style="color: #d1d5db;">Here are your upcoming adventures</p>
    </div>
    """, unsafe_allow_html=True)
    
    for trip_id, trip in user_trips.items():
        # Calculate days until trip
        days_until = (trip['start_date'] - date.today()).days
        
        if days_until > 0:
            countdown_text = f"🕒 {days_until} days to go!"
            countdown_color = "#8b5cf6"
        elif days_until == 0:
            countdown_text = "🎉 Today!"
            countdown_color = "#10b981"
        else:
            countdown_text = "✅ Completed"
            countdown_color = "#6b7280"
        
        st.markdown(f"""
        <div class="glass-card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                <h2 style="margin: 0;">📍 {trip['destination']}</h2>
                <div style="background: {countdown_color}; color: white; padding: 0.5rem 1rem; border-radius: 20px; font-weight: 600;">
                    {countdown_text}
                </div>
            </div>
            <p style="color: #d1d5db; font-size: 1.2rem;">🗓️ {trip['start_date'].strftime('%B %d')} - {trip['end_date'].strftime('%B %d, %Y')}</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("💰 Budget", f"${trip['budget']:,}")
        
        with col2:
            st.metric("👥 Group Size", trip['group_size'])
        
        with col3:
            duration = (trip['end_date'] - trip['start_date']).days + 1
            st.metric("📅 Duration", f"{duration} days")
        
        with col4:
            matches = find_matches(trip_id)
            st.metric("🎯 Matches", len(matches))
        
        with st.expander("📋 Trip Details & Settings"):
            col_a, col_b = st.columns(2)
            with col_a:
                st.markdown(f"**🎯 Travel Style:** {trip['travel_style']}")
                st.markdown(f"**📅 Created:** {trip['created_at'].strftime('%B %d, %Y')}")
                
                if matches:
                    st.markdown(f"**🔥 Top Match:** {matches[0]['match_score']:.0f}% compatibility")
            
            with col_b:
                if trip['itinerary']:
                    st.markdown("**📋 Itinerary & Notes:**")
                    st.markdown(f"_{trip['itinerary']}_")
        
        st.markdown("---")

def main():
    # Load custom CSS
    load_css()
    
    # Initialize session state
    init_session_state()
    
    # Enhanced sidebar
    st.sidebar.markdown("""
    <div style="text-align: center; padding: 2rem 0;">
        <h1 style="font-size: 2rem; margin-bottom: 0.5rem;">✈️ TravelMatch</h1>
        <p style="color: #d1d5db; font-style: italic;">Find Your Travel Tribe</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Navigation
    page = st.sidebar.selectbox("🧭 Navigate", [
        "🏠 Home", 
        "👤 Profile", 
        "✈️ Create Trip", 
        "🔍 Find Matches", 
        "📋 My Trips"
    ])
    
    # User status in sidebar
    if st.session_state.current_user:
        user = st.session_state.users[st.session_state.current_user]
        st.sidebar.markdown(f"""
        <div style="background: linear-gradient(135deg, rgba(139, 92, 246, 0.2) 0%, rgba(168, 85, 247, 0.1) 100%); 
                    border: 1px solid rgba(139, 92, 246, 0.3); border-radius: 15px; padding: 1rem; margin: 1rem 0; text-align: center;">
            <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">👋</div>
            <div style="color: #ffffff; font-weight: 600;">{user['name']}</div>
            <div style="color: #d1d5db; font-size: 0.9rem;">{user['email']}</div>
        </div>
        """, unsafe_allow_html=True)
    
    # App stats in sidebar
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📊 Community Stats")
    
    col_stat1, col_stat2 = st.sidebar.columns(2)
    with col_stat1:
        st.metric("👥", len(st.session_state.users), label_visibility="collapsed")
        st.caption("Active Users")
    with col_stat2:
        st.metric("✈️", len(st.session_state.trips), label_visibility="collapsed")
        st.caption("Travel Plans")
    
    # Footer
    st.sidebar.markdown("---")
    st.sidebar.markdown("""
    <div style="text-align: center; color: #6b7280; font-size: 0.8rem;">
        <p>🌟 Connect • Explore • Adventure</p>
        <p>Made with ❤️ for travelers</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Page routing with error handling
    try:
        if page == "🏠 Home":
            show_home_page()
        elif page == "👤 Profile":
            show_register_page()
        elif page == "✈️ Create Trip":
            show_create_trip_page()
        elif page == "🔍 Find Matches":
            show_matches_page()
        elif page == "📋 My Trips":
            show_my_trips_page()
    except Exception as e:
        st.error(f"❗ An error occurred: {str(e)}")
        st.info("🔄 Please refresh the page and try again.")

if __name__ == "__main__":
    main()