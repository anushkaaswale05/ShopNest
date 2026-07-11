import streamlit as st

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Orders",
    page_icon="📦",
    layout="wide"
)

st.title("📦 My Orders")

# -----------------------------
# SESSION STATE
# -----------------------------
if "orders" not in st.session_state:
    st.session_state.orders = []

# -----------------------------
# EMPTY ORDERS
# -----------------------------
if len(st.session_state.orders) == 0:

    st.info("You haven't placed any orders yet.")

else:

    st.success(f"Total Orders : {len(st.session_state.orders)}")

    st.markdown("---")

    total_spent = 0

    for index, order in enumerate(st.session_state.orders):

        with st.container(border=True):

            col1, col2, col3 = st.columns([4,2,2])

            with col1:

                st.subheader(order["Product"])
                st.write(f"🆔 Order ID : {order['Order ID']}")

            with col2:

                st.write(f"💰 Amount : ₹{order['Amount']}")

            with col3:

                status = order.get("Status", "Processing")

                if status == "Processing":
                    st.warning("📦 Processing")

                elif status == "Shipped":
                    st.info("🚚 Shipped")

                elif status == "Delivered":
                    st.success("✅ Delivered")

                elif status == "Cancelled":
                    st.error("❌ Cancelled")

            total_spent += order["Amount"]

    st.markdown("---")

    c1, c2 = st.columns(2)

    with c1:
        st.metric("🛒 Total Orders", len(st.session_state.orders))

    with c2:
        st.metric("💰 Total Spent", f"₹{total_spent:.2f}")

    st.markdown("---")

    if st.button("🗑️ Clear Order History"):

        st.session_state.orders = []

        st.success("Order history cleared.")

        st.rerun()