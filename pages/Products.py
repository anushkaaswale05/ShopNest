import streamlit as st
import pandas as pd
import os

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Products",
    page_icon="🛍️",
    layout="wide"
)

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_excel("data/processed/cleaned_fashion_products.xlsx")

# -----------------------------
# SESSION STATE
# -----------------------------
if "cart" not in st.session_state:
    st.session_state.cart = []

if "wishlist" not in st.session_state:
    st.session_state.wishlist = []

# -----------------------------
# TITLE
# -----------------------------
st.title("🛍️ All Products")
st.write("Browse our latest fashion collection.")

# -----------------------------
# SEARCH & FILTER
# -----------------------------
col1, col2 = st.columns([2, 1])

with col1:
    search = st.text_input("🔍 Search Products")

with col2:
    categories = ["All"] + sorted(df["category"].unique().tolist())
    selected_category = st.selectbox("Category", categories)

filtered_df = df.copy()

if search:
    filtered_df = filtered_df[
        filtered_df["product_name"].str.contains(
            search,
            case=False,
            na=False
        )
    ]

if selected_category != "All":
    filtered_df = filtered_df[
        filtered_df["category"] == selected_category
    ]

st.write(f"### {len(filtered_df)} Products Found")

sort = st.selectbox(
    "Sort By",
    [
        "Default",
        "Price: Low to High",
        "Price: High to Low",
        "Highest Rating"
    ]
)

if sort == "Price: Low to High":
    filtered_df = filtered_df.sort_values("price")

elif sort == "Price: High to Low":
    filtered_df = filtered_df.sort_values("price", ascending=False)

elif sort == "Highest Rating":
    filtered_df = filtered_df.sort_values("rating", ascending=False)

# -----------------------------
# DISPLAY PRODUCTS
# -----------------------------
cols = st.columns(3)

for index, (_, row) in enumerate(filtered_df.iterrows()):

    with cols[index % 3]:

        with st.container(border=True):

            image_path = os.path.join(
                "images",
                str(row["image_file"])
            )

            if os.path.exists(image_path):
                st.image(
                    image_path,
                    use_container_width=True
                )
            else:
                st.image(
                    "https://via.placeholder.com/300x300?text=No+Image",
                    use_container_width=True
                )

            st.subheader(row["product_name"])

            st.write(f"🏷️ Brand: **{row['brand']}**")
            st.write(f"📂 Category: **{row['category']}**")
            st.write(f"🎨 Color: **{row['color']}**")
            st.write(f"📏 Size: **{row['size']}**")
            st.write(f"⭐ Rating: **{row['rating']}**")
            st.write(f"### 💰 ₹{row['price']}")
            if row["stock"] < 10:

             st.error("⚠️ Only Few Left!")
else:
    st.success("✅ In Stock")

            # -----------------------------
            # ADD TO CART
            # -----------------------------
    if st.button(
                "🛒 Add to Cart",
                key=f"cart_{row['product_id']}"
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

            # -----------------------------
            # ADD TO WISHLIST
            # -----------------------------
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