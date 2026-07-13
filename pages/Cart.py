import streamlit as st

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Shopping Cart",
    page_icon="🛒",
    layout="wide"
)

st.title("🛒 Shopping Cart")

# -----------------------------
# SESSION STATE
# -----------------------------
if "cart" not in st.session_state:
    st.session_state.cart = []

if "orders" not in st.session_state:
    st.session_state.orders = []

# -----------------------------
# EMPTY CART
# -----------------------------
if len(st.session_state.cart) == 0:

    st.info("🛍️ Your cart is empty.")

else:

    subtotal = 0

    st.subheader("Items in Cart")

    for index, item in enumerate(st.session_state.cart):

        with st.container(border=True):

            col1, col2, col3, col4, col5 = st.columns([4,1,1,2,1])

            with col1:
                st.write(f"### {item['Product']}")

            with col2:
                if st.button("➖", key=f"minus_{index}"):

                    if item["Quantity"] > 1:
                        item["Quantity"] -= 1

                    st.rerun()

            with col3:

                st.write(f"**{item['Quantity']}**")

                if st.button("➕", key=f"plus_{index}"):

                    item["Quantity"] += 1

                    st.rerun()

            with col4:

                amount = item["Price"] * item["Quantity"]

                subtotal += amount

                st.write(f"₹ {amount:.2f}")

            with col5:

                if st.button("❌", key=f"remove_{index}"):

                    st.session_state.cart.pop(index)

                    st.rerun()

    st.markdown("---")

    # -----------------------------
    # BILL SUMMARY
    # -----------------------------

    if subtotal >= 999:
        delivery = 0
        st.success("🎉 Congratulations! You got FREE Delivery.")
    else:
        delivery = 99
        st.warning(f"Add ₹{999-subtotal:.0f} more for FREE Delivery 🚚")

    gst = subtotal * 0.18

    coupon = st.text_input("🎟️ Enter Coupon Code")

    discount = 0

    if coupon.upper() == "SHOP10":
        discount = subtotal * 0.10
        st.success("Coupon Applied Successfully!")
    elif coupon != "":
        st.error("Invalid Coupon Code")

    grand_total = subtotal + delivery + gst - discount

    st.subheader("💰 Bill Summary")

    st.write(f"Subtotal : ₹ {subtotal:.2f}")
    st.write(f"Delivery Charges : ₹ {delivery:.2f}")
    st.write(f"GST (18%) : ₹ {gst:.2f}")
    st.write(f"Discount : -₹ {discount:.2f}")

    st.markdown("---")

    st.success(f"Grand Total : ₹ {grand_total:.2f}")

    st.markdown("---")

    # -----------------------------
    # DELIVERY DETAILS
    # -----------------------------

    st.subheader("📍 Delivery Details")

    name = st.text_input("Full Name")

    phone = st.text_input("Phone Number")

    address = st.text_area("Delivery Address")

    payment = st.radio(
        "Payment Method",
        [
            "Cash on Delivery",
            "Online Payment"
        ]
    )

    if payment == "Online Payment":
        st.info("💳 Online Payment is available in the future version.")

    st.markdown("---")

    # -----------------------------
    # PLACE ORDER
    # -----------------------------

    if st.button("✅ Place Order"):

        if name == "" or phone == "" or address == "":

            st.error("Please fill all delivery details.")

        else:

            for item in st.session_state.cart:

                st.session_state.orders.append({

                    "Order ID": f"SN{1000 + len(st.session_state.orders)+1}",

                    "Product": item["Product"],

                    "Amount": item["Price"] * item["Quantity"],

                    "Status": "Processing"

                })

            st.session_state.cart = []

            st.success("🎉 Order Placed Successfully!")

            st.balloons()

            

st.markdown("---")

st.caption("© 2026 ShopNest | Shopping Cart")