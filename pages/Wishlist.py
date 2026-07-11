import streamlit as st

# -----------------------------------
# PAGE CONFIG
# -----------------------------------
st.set_page_config(
    page_title="Wishlist",
    page_icon="❤️",
    layout="wide"
)

st.title("❤️ My Wishlist")

# -----------------------------------
# SESSION STATE
# -----------------------------------
if "wishlist" not in st.session_state:
    st.session_state.wishlist = []

if "cart" not in st.session_state:
    st.session_state.cart = []

# -----------------------------------
# EMPTY WISHLIST
# -----------------------------------
if len(st.session_state.wishlist) == 0:

    st.info("❤️ Your wishlist is empty.")

else:

    st.success(f"Total Wishlist Items : {len(st.session_state.wishlist)}")

    st.markdown("---")

    for index, item in enumerate(st.session_state.wishlist):

        with st.container(border=True):

            c1, c2, c3, c4 = st.columns([4,2,2,2])

            with c1:
                st.subheader(item["Product"])

            with c2:
                st.write(f"💰 ₹{item['Price']}")

            with c3:

                if st.button(
                    "🛒 Move to Cart",
                    key=f"move_{index}"
                ):

                    found = False

                    for cart_item in st.session_state.cart:

                        if cart_item["Product"] == item["Product"]:

                            cart_item["Quantity"] += 1
                            found = True
                            break

                    if not found:

                        st.session_state.cart.append({

                            "Product": item["Product"],
                            "Price": item["Price"],
                            "Quantity": 1

                        })

                    st.session_state.wishlist.pop(index)

                    st.success("Moved to Cart")

                    st.rerun()

            with c4:

                if st.button(
                    "❌ Remove",
                    key=f"remove_{index}"
                ):

                    st.session_state.wishlist.pop(index)

                    st.success("Removed from Wishlist")

                    st.rerun()

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        if st.button("🛍️ Move All to Cart"):

            for item in st.session_state.wishlist:

                found = False

                for cart_item in st.session_state.cart:

                    if cart_item["Product"] == item["Product"]:

                        cart_item["Quantity"] += 1
                        found = True
                        break

                if not found:

                    st.session_state.cart.append({

                        "Product": item["Product"],
                        "Price": item["Price"],
                        "Quantity": 1

                    })

            st.session_state.wishlist = []

            st.success("All products moved to Cart")

            st.rerun()

    with col2:

        if st.button("🗑️ Clear Wishlist"):

            st.session_state.wishlist = []

            st.success("Wishlist Cleared")

            st.rerun()