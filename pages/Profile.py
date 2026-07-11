import streamlit as st

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="My Profile",
    page_icon="👤",
    layout="wide"
)

st.title("👤 My Profile")

# -----------------------------
# SESSION STATE
# -----------------------------
if "cart" not in st.session_state:
    st.session_state.cart = []

if "wishlist" not in st.session_state:
    st.session_state.wishlist = []

if "orders" not in st.session_state:
    st.session_state.orders = []

# -----------------------------
# USER DETAILS
# -----------------------------
st.subheader("Personal Information")

name = st.text_input("Full Name", "Anushka Aswale")
email = st.text_input("Email", "anushka@example.com")
phone = st.text_input("Phone Number", "9876543210")
city = st.text_input("City", "Pune")
address = st.text_area(
    "Delivery Address",
    "Enter your address..."
)

if st.button("💾 Save Profile"):
    st.success("Profile Updated Successfully!")

st.markdown("---")

# -----------------------------
# ACCOUNT SUMMARY
# -----------------------------
st.subheader("📊 Account Summary")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("🛒 Cart Items", len(st.session_state.cart))

with c2:
    st.metric("❤️ Wishlist", len(st.session_state.wishlist))

with c3:
    st.metric("📦 Orders", len(st.session_state.orders))

st.markdown("---")

# -----------------------------
# SHOPPING STATS
# -----------------------------
st.subheader("Shopping Statistics")

total_spent = 0

for order in st.session_state.orders:
    total_spent += order["Amount"]

c1, c2 = st.columns(2)

with c1:
    st.metric("💰 Total Spent", f"₹{total_spent:.2f}")

with c2:
    st.metric("⭐ Reward Points", int(total_spent // 100))

st.markdown("---")

# -----------------------------
# MEMBERSHIP
# -----------------------------
st.subheader("🏅 Membership")

if total_spent >= 10000:
    st.success("🌟 Gold Member")

elif total_spent >= 5000:
    st.info("🥈 Silver Member")

else:
    st.warning("🥉 Bronze Member")

st.markdown("---")

# -----------------------------
# SETTINGS
# -----------------------------
st.subheader("⚙️ Settings")

notification = st.checkbox(
    "Receive Notifications",
    value=True
)

newsletter = st.checkbox(
    "Subscribe to Newsletter",
    value=True
)

dark = st.checkbox(
    "Enable Dark Mode (Demo)"
)

if st.button("Save Settings"):
    st.success("Settings Saved!")

st.markdown("---")

# -----------------------------
# LOGOUT
# -----------------------------
if st.button("🚪 Logout"):
    st.success("Logged Out Successfully!")

st.markdown("---")

st.caption("© 2026 ShopNest | Developed by Anushka Aswale")