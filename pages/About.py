import streamlit as st

# -----------------------------------
# PAGE CONFIG
# -----------------------------------
st.set_page_config(
    page_title="About ShopNest",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About ShopNest")

st.markdown("""
# 🛍️ ShopNest

**ShopNest** is an AI-powered Fashion E-Commerce Web Application developed using **Python** and **Streamlit**.

It allows users to browse fashion products, search items, add products to cart, save products to wishlist, place orders and receive smart product recommendations.

---
""")

# -----------------------------------
# PROJECT FEATURES
# -----------------------------------

st.header("✨ Features")

c1, c2 = st.columns(2)

with c1:
    st.success("✔ Product Search")
    st.success("✔ Category Filter")
    st.success("✔ Shopping Cart")
    st.success("✔ Wishlist")
    st.success("✔ Smart Recommendations")
    st.success("✔ Order Management")

with c2:
    st.success("✔ Product Images")
    st.success("✔ Checkout")
    st.success("✔ Coupon Discount")
    st.success("✔ GST Calculation")
    st.success("✔ Delivery Charges")
    st.success("✔ Responsive Interface")

st.markdown("---")

# -----------------------------------
# TECHNOLOGIES
# -----------------------------------

st.header("💻 Technologies Used")

tech = [
    "🐍 Python",
    "🎨 Streamlit",
    "🐼 Pandas",
    "📊 Excel Dataset",
    "🖼️ PIL / Images",
    "📁 VS Code"
]

for t in tech:
    st.write(t)

st.markdown("---")

# -----------------------------------
# PROJECT MODULES
# -----------------------------------

st.header("📂 Project Modules")

modules = [
    "🏠 Home",
    "🛍️ Products",
    "🛒 Shopping Cart",
    "❤️ Wishlist",
    "📦 Orders",
    "👤 Profile",
    "ℹ️ About"
]

for m in modules:
    st.write(m)

st.markdown("---")

# -----------------------------------
# PROJECT STATISTICS
# -----------------------------------

st.header("📈 Project Statistics")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Products", "500+")
c2.metric("Categories", "10+")
c3.metric("Brands", "25+")
c4.metric("Pages", "7")

st.markdown("---")

# -----------------------------------
# DEVELOPER
# -----------------------------------

st.header("👩‍💻 Developer")

st.info("""
**Name:** Anushka Aswale

**Course:** Diploma in Computer Engineering

**Project:** ShopNest - Fashion E-Commerce Website

**Technology:** Python + Streamlit
""")

st.markdown("---")

# -----------------------------------
# FUTURE ENHANCEMENTS
# -----------------------------------

st.header("🚀 Future Enhancements")

future = [
    "🔐 User Login & Registration",
    "💳 Online Payment Gateway",
    "🗄️ PostgreSQL Database",
    "🤖 AI Recommendation Engine",
    "⭐ Product Reviews & Ratings",
    "📦 Live Order Tracking",
    "📱 Mobile Responsive UI",
    "🔔 Email & SMS Notifications"
]

for item in future:
    st.write(item)

st.markdown("---")

st.success("Thank you for visiting ShopNest!")

st.caption("© 2026 ShopNest | Developed by Anushka Aswale")