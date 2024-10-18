import streamlit as st

from electionpages import HomePage, USSenatorPage, USRepPage, StateSenatorPage, StateAssemblyPage, SchoolDistrictPage, MayorPage, CityCouncilPage, MunicipalWaterPage, OCWaterPage

# Add navigation to the sidebar
st.sidebar.title("Elections")
page_selection = st.sidebar.radio("Go to", 
                                  ["Home Page",
                                   "United States Senator",
                                   "United States Representative",
                                   "State Senator", 
                                   "State Assembly Member",
                                   "School District Governing Board Member",
                                   "City of Costa Mesa Mayor", 
                                   "Costa Mesa City Council Member", 
                                   "Municipal Water District of OC Director", 
                                   "OC Water District Director"])

# Display the selected page
if page_selection == "Home Page":
    HomePage()
elif page_selection == "United States Senator":
    USSenatorPage()
elif page_selection == "United States Representative":
    USRepPage()
elif page_selection == "State Senator":
    StateSenatorPage()
elif page_selection == "State Assembly Member":
    StateAssemblyPage()
elif page_selection == "School District Governing Board Member":
    SchoolDistrictPage()
elif page_selection == "City of Costa Mesa Mayor":
    MayorPage()
elif page_selection == "Costa Mesa City Council Member":
    CityCouncilPage()
elif page_selection == "Municipal Water District of OC Director":
    MunicipalWaterPage()
elif page_selection == "OC Water District Director":
    OCWaterPage()
