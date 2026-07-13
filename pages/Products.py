import streamlit as st
import pandas as pd
import os
import math

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="ShopNest | Products",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# LOAD DATA
# =====================================================

df = pd.read_excel(
    "data/processed/cleaned_fashion_products.xlsx"
)

# Remove duplicate products
df = df.drop_duplicates(subset=["product_id"])

# =====================================================
# SESSION STATE
# =====================================================

if "cart" not in st.session_state:
    st.session_state.cart = []

if "wishlist" not in st.session_state:
    st.session_state.wishlist = []

# =====================================================
# CSS
# =====================================================

st.markdown("""
<style>

/* Background */

.stApp{
background:#F6F8FC;
}

/* Hide Streamlit Menu */

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

/* All text */

html,body,p,label,span,div,h1,h2,h3,h4,h5,h6{
color:#222222 !important;
}

/* Headings */

.main-title{
font-size:45px;
font-weight:700;
color:#1E3A8A!important;
}

.subtitle{
font-size:18px;
color:#666!important;
margin-bottom:30px;
}

/* Sidebar */

section[data-testid="stSidebar"]{
background:white;
border-right:1px solid #ECECEC;
}

/* Cards */

div[data-testid="stVerticalBlockBorderWrapper"]{

background:white;

border-radius:18px;

border:1px solid #ECECEC;

padding:15px;

box-shadow:0px 5px 18px rgba(0,0,0,.08);

transition:.3s;

}

div[data-testid="stVerticalBlockBorderWrapper"]:hover{

transform:translateY(-6px);

box-shadow:0px 10px 28px rgba(0,0,0,.15);

}

/* Buttons */

.stButton>button{

width:100%;

border:none;

border-radius:10px;

background:#2563EB;

color:white!important;

font-weight:bold;

padding:10px;

}

.stButton>button:hover{

background:#1D4ED8;

}

/* Metrics */

div[data-testid="metric-container"]{

background:white;

padding:15px;

border-radius:15px;

border:1px solid #ECECEC;

}

/* Expanders */

.streamlit-expanderHeader{

font-weight:600;

color:#222!important;

}

</style>
""", unsafe_allow_html=True)

# =====================================================
# HEADER
# =====================================================

st.markdown(
"""
<div class="main-title">
🛍️ ShopNest Fashion Store
</div>

<div class="subtitle">
Discover Premium Fashion Collections
</div>
""",
unsafe_allow_html=True
)

# =====================================================
# TOP METRICS
# =====================================================

m1,m2,m3,m4=st.columns(4)

m1.metric(
"Products",
len(df)
)

m2.metric(
"Brands",
df["brand"].nunique()
)

m3.metric(
"Categories",
df["category"].nunique()
)

m4.metric(
"Items in Cart",
sum(
item["Quantity"]
for item in st.session_state.cart
) if st.session_state.cart else 0
)

st.markdown("---")
# =====================================================
# SEARCH & FILTERS
# =====================================================

st.subheader("🔍 Find Your Perfect Outfit")

c1, c2, c3 = st.columns([2, 1, 1])

with c1:
    search = st.text_input(
        "Search Products",
        placeholder="Search by product name..."
    )

with c2:
    categories = ["All"] + sorted(df["category"].dropna().unique().tolist())
    selected_category = st.selectbox(
        "Category",
        categories
    )

with c3:
    brands = ["All"] + sorted(df["brand"].dropna().unique().tolist())
    selected_brand = st.selectbox(
        "Brand",
        brands
    )

# =====================================================
# PRICE FILTER
# =====================================================

min_price = float(df["price"].min())
max_price = float(df["price"].max())

price_range = st.slider(
    "Price Range (₹)",
    min_value=min_price,
    max_value=max_price,
    value=(min_price, max_price)
)

# =====================================================
# APPLY FILTERS
# =====================================================

filtered_df = df.copy()

# Search
if search.strip():
    filtered_df = filtered_df[
        filtered_df["product_name"]
        .astype(str)
        .str.contains(search, case=False, na=False)
    ]

# Category
if selected_category != "All":
    filtered_df = filtered_df[
        filtered_df["category"] == selected_category
    ]

# Brand
if selected_brand != "All":
    filtered_df = filtered_df[
        filtered_df["brand"] == selected_brand
    ]

# Price
filtered_df = filtered_df[
    (filtered_df["price"] >= price_range[0]) &
    (filtered_df["price"] <= price_range[1])
]

st.markdown("")

st.info(f"Showing **{len(filtered_df)}** products")

st.markdown("---")
# =====================================================
# PRODUCT GRID
# =====================================================

st.subheader("🛍️ Products")

if filtered_df.empty:
    st.warning("No products found.")
else:

    products_per_row = 4

    total_products = len(filtered_df)

    total_rows = math.ceil(total_products / products_per_row)

    image_folder = "images"

    for row in range(total_rows):

        cols = st.columns(products_per_row)

        for col_num in range(products_per_row):

            index = row * products_per_row + col_num

            if index >= total_products:
                continue

            product = filtered_df.iloc[index]

            with cols[col_num]:

                with st.container(border=True):

                    image_path = os.path.join(
                        image_folder,
                        str(product["image_file"])
                    )

                    if os.path.exists(image_path):
                        st.image(image_path, use_container_width=True)
                    else:
                        st.image("https://via.placeholder.com/300x350?text=No+Image", use_container_width=True)

                    st.markdown(f"### {product['product_name']}")
                    st.caption(product["brand"])
                    st.write(f"**Category:** {product['category']}")
                    st.write(f"**Color:** {product['color']}")
                    st.write(f"**Size:** {product['size']}")
                    st.write(f"⭐ {product['rating']}")
                    st.write(f"### ₹ {product['price']:.2f}")

                    if product["stock"] > 0:
                        st.success(f"In Stock ({product['stock']})")
                    else:
                        st.error("Out of Stock")

                    with st.expander("Description"):
                        st.write(product["description"])

                    if st.button("🛒 Add to Cart", key=f"cart_{product['product_id']}"):
                        found=False
                        for item in st.session_state.cart:
                            if item["product_id"]==product["product_id"]:
                                item["Quantity"]+=1
                                found=True
                                break
                        if not found:
                            st.session_state.cart.append({
                                "product_id":product["product_id"],
                                "Product":product["product_name"],
                                "Price":float(product["price"]),
                                "Quantity":1
                            })
                        st.success("Added to cart!")

# =====================================================
# WISHLIST
# =====================================================

st.markdown("---")
st.subheader("❤️ Wishlist")

wishlist_col1, wishlist_col2 = st.columns([1, 4])

with wishlist_col1:
    if st.button("🗑️ Clear Wishlist"):
        st.session_state.wishlist = []
        st.success("Wishlist cleared!")

# =====================================================
# SIDEBAR CART
# =====================================================

with st.sidebar:

    st.title("🛒 Shopping Cart")

    if len(st.session_state.cart) == 0:

        st.info("Your cart is empty.")

    else:

        total = 0

        remove_index = None

        for i, item in enumerate(st.session_state.cart):

            subtotal = item["Price"] * item["Quantity"]

            total += subtotal

            with st.expander(item["Product"], expanded=False):

                st.write(f"Price : ₹{item['Price']:.2f}")

                st.write(f"Quantity : {item['Quantity']}")

                st.write(f"Subtotal : ₹{subtotal:.2f}")

                c1, c2 = st.columns(2)

                with c1:
                    if st.button("➕", key=f"plus_{i}"):
                        item["Quantity"] += 1
                        st.rerun()

                with c2:
                    if st.button("➖", key=f"minus_{i}"):

                        if item["Quantity"] > 1:
                            item["Quantity"] -= 1
                        else:
                            remove_index = i

                        st.rerun()

        if remove_index is not None:
            st.session_state.cart.pop(remove_index)
            st.rerun()

        st.markdown("---")

        st.subheader(f"💰 Total : ₹{total:.2f}")

        if st.button("🗑 Remove All Items"):

            st.session_state.cart = []

            st.success("Cart Cleared!")

            st.rerun()

        if st.button("✅ Proceed to Checkout"):

            st.success("Order placed successfully! 🎉")

        

            st.session_state.cart = []

            st.rerun()

# =====================================================
# FOOTER
# =====================================================

st.markdown("---")

st.markdown(
"""
<div style='text-align:center;
padding:20px;
font-size:15px;
color:#777;'

© 2026 <b>ShopNest Fashion Store</b><br>
Premium Fashion • Secure Shopping • Fast Delivery

</div>
""",
unsafe_allow_html=True
)