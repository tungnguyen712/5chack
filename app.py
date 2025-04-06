import streamlit as st
from datetime import datetime, timedelta 
from calendar import monthrange
import json
import os


with open("hoch_menus.json", "r") as f:
    data = json.load(f)
    
st.markdown(
    """
    <style>
    body {
        background-color: #F8F4EF !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f'<style>{open(os.path.join(".streamlit", "styles.css")).read()}</style>',
    unsafe_allow_html=True
)

# st.title(":red[5C Dining Healthy Menu Search] :knife_fork_plate: :wine_glass:")
st.markdown(
    '<h1 style="color:#b68958;">5C Dining Healthy Menu Search 🍴 🍷</h1>',
    unsafe_allow_html=True
)

st.sidebar.header("5C Campus Dining")
st.sidebar.subheader("Select a dining hall")
hall_select = st.sidebar.selectbox(
   "",
   ("Frank (Pomona College)",
   "Frary (Pomona College)",
   "Oldenborg (Pomona College)",
   "Collins (Claremont McKenna College)",
   "McConell (Pitzer College)",
   "Mallot (Scripps College)",
   "Hoch (Harvey Mudd College)"),
   )


meal_stations = {"frank": ["Expo Station", "Desserts", "Mainline", "Pizza", "Grill Station", "Salad Bar", "Soup Station"],
                "frary": ["Expo Station", "Desserts", "Grill Station ", "Mainline", "Pizza", "Salad Bar", "Soup Station"],
                "oldenborg": ["Panini Station", "Mainline", "Pizza", "Salad Bar", "Soup Station"],
                "collins": ["@home", "Options", "Grill Station", "Stock Pot", "Ovens", "Expo Station", "PLant Forward"],
                "mcconell_breakfast": ["Global", "Hot Cereal"],
                "mcconell": ["Comfort", "Herbivore", "Stocks"],
                "mallot_breakfast": ["Herbivore", "Global", "Salad", "Soup", "Sweets"],
                "mallot": ["Grill", "Herbivore", "Global", "Oasis", "Salad", "Ovens", "Soup", "Sweets"],
                "hoch_breakfast": ["Bakery", "Exhibition", "Grill", "HMC Special Salad", "Salad Bar Yogurt"],
                "hoch": ["Bakery", "Chef Corner", "Creations", "Deli Bar HMC", "Exhibition", 
                         "Grill", "Grown Plant", "HMC Special Salad", "Oven", "Salad Bar Yogurt", 
                         "Simple Servings", "Soup Bar", "Special Bar Salad-S", "Special Hot Salad-N"]
                }
  


if "show_chat" not in st.session_state:
    if st.button("Talk to Bot :robot_face:"):  # Single button to activate
        st.session_state.show_chat = True
if st.session_state.get("show_chat"):
    # PASTE YOUR EXISTING CHATBOT CODE HERE
    # Example:
    if "messages" not in st.session_state:
        st.session_state.messages = []
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
    
    if prompt := st.chat_input("Your message..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Add your chatbot's response logic here
        response = f"Echo: {prompt}"  # Replace with real responses
        st.session_state.messages.append({"role": "assistant", "content": response})
   
                   
def meal_station_caption(s):
   for i in range(len(meal_stations[s])):
       st.markdown(
            f'<div style="color:#b68958; font-size:1.25rem; font-weight:bold; font-family:serif;">{meal_stations[s][i]}</div>',
            unsafe_allow_html=True
        )
   st.divider()


if hall_select == "Frank (Pomona College)":
   st.markdown(
    '<h2 style="color:#b68958;">Frank Dining Hall (Pomona College)</h2>',
    unsafe_allow_html=True
    )
   # date_buttons()
   with st.container():
        st.divider()
        with st.expander("Breakfast 7:30 AM - 9:30 AM", expanded=False):
            st.markdown(
            '<div style="color:#b68958; font-size:1.5rem; font-weight:bold;">Breakfast 7:30 AM - 9:30 AM</div>',
            unsafe_allow_html=True
            )
            meal_station_caption("frank")
        with st.expander("Lunch 10:30 AM - 1:30 PM"):
            meal_station_caption("frank")
        with st.expander("Dinner 5:00 PM - 7:30 PM"):
            meal_station_caption("frank")


if hall_select == "Frary (Pomona College)":
    st.markdown(
    '<h2 style="color:#b68958;">Frary Dining Hall (Pomona College)</h2>',
    unsafe_allow_html=True
    )
    # date_buttons()
    with st.container():
        st.divider()
        with st.expander("Breakfast 7:30 AM - 10:00 AM"):
            meal_station_caption("frary")
        with st.expander("Lunch 11:00 AM - 1:30 PM"):
            meal_station_caption("frary")
        with st.expander("Dinner 5:00 PM - 7:30 PM"):
            meal_station_caption("frary")

if hall_select == "Oldenborg (Pomona College)":
    st.markdown(
    '<h2 style="color:#b68958;">Oldenborg Dining Hall (Pomona College)</h2>',
    unsafe_allow_html=True
    )
    # date_buttons()
    with st.container():
        st.divider()
        with st.expander("Lunch 12:00 PM - 1:00 PM"):
            meal_station_caption("oldenborg")

if hall_select == "Collins (Claremont McKenna College)":
    st.markdown(
    '<h2 style="color:#b68958;">Frank Dining Hall (Pomona College)</h2>',
    unsafe_allow_html=True
    )
    # date_buttons()
    with st.container():
        st.divider()
        with st.expander("Breakfast 7:30 AM - 9:30 AM"):
            meal_station_caption("collins")
        with st.expander("Lunch 11:00 AM - 1:00 PM"):
            meal_station_caption("collins")
        with st.expander("Dinner 5:00 PM - 7:00 PM"):
            meal_station_caption("collins")

if hall_select == "McConell (Pitzer College)":
    st.markdown(
    '<h2 style="color:#b68958;">McConell (Pitzer College)</h2>',
    unsafe_allow_html=True
    )
    # date_buttons()
    with st.container():
        st.divider()
        with st.expander("Breakfast 7:45 AM - 10:00 AM"):
            meal_station_caption("mcconell_breakfast")
        with st.expander("Lunch 11:00 AM - 1:30 PM"):
            meal_station_caption("mcconell")
        with st.expander("Dinner 5:00 PM - 7:30 PM"):
            meal_station_caption("mcconell")
    
if hall_select == "Mallot (Scripps College)":
    st.markdown(
    '<h2 style="color:#b68958;">Mallot (Scripps College)</h2>',
    unsafe_allow_html=True
    )
    # date_buttons()
    with st.container():
        st.divider()
        with st.expander("Breakfast 7:30 AM - 10:00 AM"):
            meal_station_caption("mallot_breakfast")
        with st.expander("Lunch 11:00 AM - 2:00 PM"):
            meal_station_caption("mallot")
        with st.expander("Dinner 5:00 PM - 7:15 PM"):
            meal_station_caption("mallot")

if hall_select == "Hoch (Harvey Mudd College)":
    st.markdown(
    '<h2 style="color:#b68958;">Hoch (Harvey Mudd College)</h2>',
    unsafe_allow_html=True
    )
    # date_buttons()
    with st.container():
        st.divider()
        with st.expander("Breakfast 7:30 AM - 9:30 AM"):
            meal_station_caption("hoch_breakfast")
        with st.expander("Lunch 11:15 AM - 1:00 PM"):
            meal_station_caption("hoch")
        with st.expander("Dinner 5:00 PM - 7:00 PM"):
            meal_station_caption("hoch")


        



