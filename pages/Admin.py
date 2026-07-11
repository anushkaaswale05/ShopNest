import streamlit as st
import pandas as pd

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Admin Panel",
    page_icon="🛠️",
    layout="wide"
)

st.title("🛠️ ShopNest Admin Dashboard")

# =====================================================
# LOAD DATA
# =====================================================

df = pd.read_excel("data/processed/cleaned_fashion_products.xlsx")

# =====================================================
# SESSION STATE
# =====================================================

if "cart" not in st.session_state:
    st.session_state.cart = []

if "wishlist" not in st.session_state:
    st.session_state.wishlist = []

if "orders" not in st.session_state:
    st.session_state.orders = []

# =====================================================
# DASHBOARD
# =====================================================

total_revenue = 0

for order in st.session_state.orders:
    total_revenue += order["Amount"]

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("🛍️ Products", len(df))

with c2:
    st.metric("📦 Orders", len(st.session_state.orders))

with c3:
    st.metric("❤️ Wishlist", len(st.session_state.wishlist))

with c4:
    st.metric("💰 Revenue", f"₹{total_revenue}")

st.markdown("---")

# =====================================================
# PRODUCT INVENTORY
# =====================================================

st.header("📦 Product Inventory")

st.dataframe(df, use_container_width=True)

st.markdown("---")

# =====================================================
# SEARCH PRODUCT
# =====================================================

st.header("🔍 Search Product")

search = st.text_input("Enter Product Name")

if search:

    result = df[
        df["product_name"].str.contains(
            search,
            case=False,
            na=False
        )
    ]

    st.write(f"Found {len(result)} Product(s)")

    st.dataframe(result, use_container_width=True)

st.markdown("---")

# =====================================================
# ADD PRODUCT (DEMO)
# =====================================================

st.header("➕ Add New Product")

col1, col2 = st.columns(2)

with col1:

    pname = st.text_input("Product Name")

    brand = st.text_input("Brand")

    category = st.text_input("Category")

with col2:

    color = st.text_input("Color")

    size = st.text_input("Size")

    price = st.number_input("Price", min_value=0.0)

rating = st.slider(
    "Rating",
    1.0,
    5.0,
    4.0
)

stock = st.number_input(
    "Stock",
    min_value=0
)

description = st.text_area(
    "Description"
)

if st.button("✅ Add Product"):

    st.success("Product Added Successfully! (Demo Version)")

st.markdown("---")

# =====================================================
# CATEGORY STATISTICS
# =====================================================

st.header("📊 Category Statistics")

category_count = df["category"].value_counts()

st.bar_chart(category_count)

st.markdown("---")

# =====================================================
# BRAND STATISTICS
# =====================================================

st.header("🏷️ Brand Statistics")

brand_count = df["brand"].value_counts()

st.bar_chart(brand_count)

st.markdown("---")

# =====================================================
# LOW STOCK PRODUCTS
# =====================================================

st.header("⚠️ Low Stock Products")

low_stock = df[df["stock"] < 10]

if len(low_stock) == 0:

    st.success("No Low Stock Products")

else:

    st.dataframe(
        low_stock,
        use_container_width=True
    )

st.markdown("---")

# =====================================================
# PROJECT SUMMARY
# =====================================================

st.header("📈 Project Summary")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Categories",
        df["category"].nunique()
    )

with c2:
    st.metric(
        "Brands",
        df["brand"].nunique()
    )

with c3:
    st.metric(
        "Average Rating",
        round(df["rating"].mean(), 2)
    )

st.markdown("---")

# =====================================================
# DOWNLOAD DATASET
# =====================================================

st.header("📥 Download Dataset")

csv = df.to_csv(index=False)

st.download_button(
    label="Download Products CSV",
    data=csv,
    file_name="shopnest_products.csv",
    mime="text/csv"
)

st.markdown("---")

# =====================================================
# FOOTER
# =====================================================

st.success("Admin Panel Loaded Successfully!")

st.caption("© 2026 ShopNest Admin Panel | Developed by Anushka Aswale")