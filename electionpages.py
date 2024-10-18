import streamlit as st

from electionsurveys import USSenator, USRep, StateSenator, StateAssembly, SchoolDistrict, Mayor, CityCouncil, MunicipalWater, OCWater, results, results3

# Function to handle the OC Water District Election page
def HomePage():
    st.header("**:rainbow[Hello Katie]** :unicorn_face:")
    st.subheader("**:rainbow[Welcome to Your Custom 2024 Election Discision Tool]** :us:", divider="rainbow")
    st.subheader("How To Use")
    st.markdown("""
                - Navigate to the election you want to learn more about in the side pannel.
                - Complete the survey to decide your prefered candidate.
                """)
    st.subheader("Notes")
    st.markdown("""
                - Information sourced mainly from candidates webpages, some info from pages about their work or other offices held, and occaisional instagram stalking.
                - Candidates for non-party elections were randonly assigned a green/orange/purple colour pallet where the colours don't mean anything.
                - Info in brackets is my personal contribution.
                - Some of the formatting is questionable because I couldn't be bothered to learn any HTML.
                """)

# Function to handle the US Senator page
def USSenatorPage():
    st.header("**:rainbow[Katie Decices Who to Vote For As...]**", divider="rainbow")
    st.header("United States Senator")
    st.subheader("Note there are sections to vote for a partial term and a full term but the same candidates are running for both.")
    
    # Get results on election survey
    adam, steve, adam_agree, steve_agree = USSenator()

    # Candidates
    names = ["Adam Schiff", "Steve Garvey"]
    
    # State Assembly is a party electon
    party = True

    # Call the OCWater survey function and display results
    results(adam, steve, adam_agree, steve_agree, names, party)

# Function to handle the US Representative page
def USRepPage():
    st.header("**:rainbow[Katie Decices Who to Vote For As...]**", divider="rainbow")
    st.header("United States Representative for 47th District")
    
    # Get results on election survey
    dave, scott, dave_agree, scott_agree = USRep()

    # Candidates
    names = ["Dave Min", "Scott Baugh"]
    
    # State Assembly is a party electon
    party = True

    # Call the OCWater survey function and display results
    results(dave, scott, dave_agree, scott_agree, names, party)

# Function to handle the State Senator page
def StateSenatorPage():
    st.header("**:rainbow[Katie Decices Who to Vote For As...]**", divider="rainbow")
    st.header("State Senator for 37th District")
    
    # Get results on election survey
    josh, steven, josh_agree, steven_agree = StateSenator()

    # Candidates
    names = ["Josh Newman", "Steven 'Steve' Choi"]
    
    # State Assembly is a party electon
    party = True

    # Call the OCWater survey function and display results
    results(josh, steven, josh_agree, steven_agree, names, party)

# Function to handle the State Assembly Member page
def StateAssemblyPage():
    st.header("**:rainbow[Katie Decices Who to Vote For As...]**", divider="rainbow")
    st.header("Member of State Assembly for 73rd District")
    
    # Get results on election survey
    cottie, scotty, cottie_agree, scotty_agree = StateAssembly()

    # Candidates
    names = ["Cottie Petrie-Norris", "Scotty Peotter"]
    
    # State Assembly is a party electon
    party = True

    # Call the OCWater survey function and display results
    results(cottie, scotty, cottie_agree, scotty_agree, names, party)

# Function to handle the CM School District page
def SchoolDistrictPage():
    st.header("**:rainbow[Katie Decices Who to Vote For As...]**", divider="rainbow")
    st.header("Newport-Mesa Unified School District Governing Board Member, Trustee Area 6")
    
    # Get results on election survey
    amy, chris, krita, amy_agree, chris_agree, krita_agree = SchoolDistrict()
    
    names = ["Amy Peters", "Chris Kretzu", "Krita Weigand"]
    
    # Call the OCWater survey function and display results
    results3(amy, chris, krita, amy_agree, chris_agree, krita_agree, names)

# Function to handle the CM Mayor page
def MayorPage():
    st.header("**:rainbow[Katie Decices Who to Vote For As...]**", divider="rainbow")
    st.header("City of Costa Mesa Mayor")
    
    # Get results on election survey
    james, john, james_agree, john_agree = Mayor()

    # Candidates
    names = ["James Peters", "John Stephens"]
    
    # Mayor not a party electon
    party = False

    # Call the OCWater survey function and display results
    results(james, john, james_agree, john_agree, names, party)

# Function to handle the CM City Council Member page
def CityCouncilPage():
    st.header("**:rainbow[Katie Decices Who to Vote For As...]**", divider="rainbow")
    st.header("City of Costa Mesa Member, City Council, District 6")
    
    # Get results on election survey
    jeffH, jeffP, jeffH_agree, jeffP_agree = CityCouncil()
    
    # Candidates
    names = ["Jeffrey Harlan", "Jeff Pettis"]
    
    # City Council not a party electon
    party = False

    # Call the OCWater survey function and display results
    results(jeffH, jeffP, jeffH_agree, jeffP_agree, names, party)

# Function to handle the Municipal Water District Election page
def MunicipalWaterPage():
    st.header("**:rainbow[Katie Decices Who to Vote For As...]**", divider="rainbow")
    st.header("Municipal Water District of Orange County Director, Division 4")
    
    # Get results on election survey
    pano, karl, pano_agree, karl_agree = MunicipalWater()

    # Candidates
    names = ["Pano Frousakis", "Karl W. Seckel"]
    
    # Municipal Water District not a party electon
    party = False

    # Call the OCWater survey function and display results
    results(pano, karl, pano_agree, karl_agree, names, party)

# Function to handle the OC Water District Election page
def OCWaterPage():
    st.header("**:rainbow[Katie Decices Who to Vote For As...]**", divider="rainbow")
    st.header("Orange County Water District Director, Division 7, Short Term")
    
    # Get results on election survey
    bob, erik, bob_agree, erik_agree = OCWater()

    # Candidates
    names = ["Bob Ooten", "Erik Weigand"]
    
    # OC Water District not a party electon
    party = False

    # Call the OCWater survey function and display results
    results(bob, erik, bob_agree, erik_agree, names, party)