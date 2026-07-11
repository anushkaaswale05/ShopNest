import streamlit as st
import pandas as pd
import os

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="ShopNest",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_excel(
    "data/processed/cleaned_fashion_products.xlsx"
)

# -----------------------------
# SESSION STATE
# -----------------------------
if "cart" not in st.session_state:
    st.session_state.cart = []
    
    if "wishlist" not in st.session_state:
        st.session_state.wishlist = []
    
# -----------------------------
# CSS
# -----------------------------

st.markdown("""
<style>

.stApp{
    background:#F6F7FB;
}

header{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

.main .block-container{
    padding-top:20px;
    padding-left:40px;
    padding-right:40px;
}


/* Navbar */

.navbar{
    background:white;
    padding:20px;
    border-radius:18px;
    box-shadow:0px 5px 20px rgba(0,0,0,.08);
    margin-bottom:25px;
}


/* Logo Blue */

.logo{
    font-size:38px;
    font-weight:bold;
color:#4A90E2;}


.tagline{
    color:#555555;
    font-size:17px;
}


/* Headings */

h1,h2,h3,h4,h5,h6{
    color:#0057B8 !important;
}


p,label,span{
    color:#333333 !important;
}


/* Buttons Blue */

.stButton>button{

    width:100%;

background:#6FA8DC;
    color:white;

    border:none;

    border-radius:10px;

    padding:12px;

    font-weight:bold;

}


.stButton>button:hover{

background:#4A90E2;
}


/* Product Card */

.card{

    background:white;

    padding:18px;

    border-radius:18px;

    box-shadow:0px 3px 15px rgba(0,0,0,.08);

}


.category-card{

    background:white;

    padding:18px;

    border-radius:15px;

    text-align:center;

    box-shadow:0px 3px 12px rgba(0,0,0,.08);

}


/* ShopNest Main Title */

.shop-title {

    color:#0057B8 !important;

    font-size:45px;

    font-weight:bold;

    text-align:center;

}


/* Product Border Card */

div[data-testid="stVerticalBlockBorderWrapper"] {

    background-color:white;

    border-radius:15px;

    padding:10px;

border:1px solid #BFD9F2;
}


</style>
""", unsafe_allow_html=True)
# -----------------------------
# NAVBAR
# -----------------------------

st.markdown("""

<div class="navbar">

<div class="logo">
🛍️ ShopNest
</div>

<div class="tagline">
Fashion • Clothing • Shoes • Bags • Accessories
</div>

</div>

""", unsafe_allow_html=True)

# -----------------------------
# SEARCH
# -----------------------------

search = st.text_input(
    "",
    placeholder="🔍 Search for products..."
)

# -----------------------------
# CATEGORY BUTTONS
# -----------------------------

st.markdown("<h2>Shop by Category</h2>", unsafe_allow_html=True)

c1,c2,c3,c4,c5=st.columns(5)

with c1:
    st.button("👗 Women")

with c2:
    st.button("👔 Men")

with c3:
    st.button("👟 Shoes")

with c4:
    st.button("👜 Bags")

with c5:
    st.button("⌚ Accessories")

st.markdown("<br>",unsafe_allow_html=True)

# -----------------------------
# HERO SECTION
# -----------------------------

left,right=st.columns([2,1])

with left:

    st.markdown("""

<h1 style="color:#E91E63;">
Discover Your Perfect Style
</h1>

<p style="font-size:20px;">

Explore premium fashion collections with amazing prices,
smart recommendations and secure shopping.

</p>

""",unsafe_allow_html=True)

    col1,col2=st.columns(2)

    with col1:
        st.button("🛍️ Shop Now")

    with col2:
        st.button("❤️ New Collection")

with right:

 st.image(
    "assets/banner.jpg",
    use_container_width=True
)    # =====================================================
# FEATURED PRODUCTS
# =====================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<h2 style="color:#222222;">
🔥 Featured Products
</h2>
""", unsafe_allow_html=True)

# Search Filter
filtered_df = df.copy()

if search:
    filtered_df = filtered_df[
        filtered_df["product_name"].str.contains(
            search,
            case=False,
            na=False
        )
    ]

# Show only first 6 products (1.jpg to 6.jpg)
featured = filtered_df.head(6)

cols = st.columns(3)

for index, (_, row) in enumerate(featured.iterrows()):

    with cols[index % 3]:

        with st.container(border=True):

            # Product Image
            image_path = os.path.join(
                "images",
                str(row["image_file"])
            )

            if os.path.exists(image_path):
                st.image(
                    image_path,
                    width=220
                )
            else:
                st.image(
                    "https://via.placeholder.com/300x300?text=No+Image",
                    use_container_width=True
                )

                st.markdown(
    f"""
    <div style="height:55px;font-size:20px;font-weight:bold;">
        {product['product_name']}
    </div>
    """,
    unsafe_allow_html=True
)

            st.write(f"🏷️ **Brand:** {row['brand']}")
            st.write(f"📂 **Category:** {row['category']}")
            st.write(f"⭐ {row['rating']}")
            st.write(f"## ₹{row['price']}")

            if st.button(
                "🛒 Add to Cart",
                key=f"home_cart_{row['product_id']}"
            ):
                

                found = False

                for item in st.session_state.cart:
                    if item["Product"] == row["product_name"]:
                        item["Quantity"] += 1
                        found = True
                        break

                if not found:
                    st.session_state.cart.append({
                        "Product": row["product_name"],
                        "Price": row["price"],
                        "Quantity": 1
                    })

                st.success("Added to Cart!")

if st.button(
    "❤️ Add to Wishlist",
    key=f"wish_{row['product_id']}"
):

    found = False

    for item in st.session_state.wishlist:
        if item["Product"] == row["product_name"]:
            found = True
            break

    if not found:
        st.session_state.wishlist.append({
            "Product": row["product_name"],
            "Price": row["price"]
        })
        st.success("Added to Wishlist ❤️")
    else:
        st.warning("Already in Wishlist")
# =====================================================
# WHY SHOPNEST
# =====================================================

st.markdown("""
<h2 style="color:#222222;">
🌟 Why ShopNest?
</h2>
""", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.info("🚚 Fast Delivery")

with c2:
    st.info("💳 Secure Payment")

with c3:
    st.info("🎁 Great Offers")

with c4:
    st.info("🤖 Smart Recommendations")
    # =====================================================
# SHOPPING CART
# =====================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<h2 style="color:#222222;">
🛒 Your Cart
</h2>
""", unsafe_allow_html=True)


if len(st.session_state.cart) == 0:

    st.info("Your cart is empty. Add some products!")

else:

    total = 0

    for item in st.session_state.cart:

        col1, col2, col3 = st.columns([3, 2, 1])

        with col1:
            st.write(f"**{item['Product']}**")

        with col2:
            st.write(
                f"₹{item['Price']} × {item['Quantity']}"
            )

        with col3:

            if st.button(
                "❌ Remove",
                key=f"remove_{item['Product']}"
            ):

                st.session_state.cart.remove(item)
                st.rerun()


        total += item["Price"] * item["Quantity"]


    st.markdown("---")

    st.success(
        f"💰 Total Amount: ₹{total}"
    )


    if st.button("🛍️ Proceed to Checkout"):

        st.success("Order placed successfully! 🎉")

        st.session_state.cart = []
        # =====================================================
# SMART RECOMMENDATIONS
# =====================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<h2 style="color:#222222;">
🤖 Smart Recommendations
</h2>
""", unsafe_allow_html=True)


if len(st.session_state.cart) > 0:

    last_product = st.session_state.cart[-1]["Product"]

    product_category = df[
        df["product_name"] == last_product
    ]["category"].iloc[0]


    recommended = df[
        (df["category"] == product_category) &
        (df["product_name"] != last_product)
    ].head(3)


    cols = st.columns(3)


    for index, (_, row) in enumerate(recommended.iterrows()):

        with cols[index % 3]:

            with st.container(border=True):

                st.markdown(
                    f"### {row['product_name']}"
                )

                st.write(
                    f"📂 Category: {row['category']}"
                )

                st.write(
                    f"⭐ Rating: {row['rating']}"
                )

                st.write(
                    f"💰 Price: ₹{row['price']}"
                )


                if st.button(
                    "🛒 Add",
                    key=f"recommend_{row['product_id']}"
                ):

                    st.session_state.cart.append({

                        "Product": row["product_name"],
                        "Price": row["price"],
                        "Quantity": 1

                    })

                    st.success("Added to Cart!")

                    # =====================================================
# TODAY'S OFFERS
# =====================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<h2 style="color:#222222;">
🎁 Today's Offers
</h2>
""", unsafe_allow_html=True)

offer1, offer2, offer3 = st.columns(3)

with offer1:
    st.success("👟 Flat 30% OFF on Shoes")

with offer2:
    st.info("👜 Buy 2 Bags & Get 1 Free")

with offer3:
    st.warning("🚚 Free Delivery on Orders Above ₹999")

    # =====================================================
# NEWSLETTER
# =====================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<h2 style="color:#222222;">
📩 Subscribe to Our Newsletter
</h2>
""", unsafe_allow_html=True)

email = st.text_input(
    "Enter your Email Address"
)

if st.button("Subscribe"):

    if email:
        st.success("🎉 Thank you for subscribing!")
    else:
        st.warning("Please enter your email.")

        # =====================================================
# FOOTER
# =====================================================

st.markdown("---")

st.markdown(
    """
    <div style="text-align:center; color:gray; padding:15px;">
        <h4 style="color:#4A90E2;">🛍️ ShopNest</h4>
        <p>Your Smart Fashion Shopping Destination</p>
        <p>Developed by <b>Anushka Aswale</b></p>
        <p>© 2026 ShopNest. All Rights Reserved.</p>
    </div>
    """,
    unsafe_allow_html=True
)
