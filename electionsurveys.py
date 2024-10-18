import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

from candidates import candidatetable

# Function to make survey question button
def survey_question(question, candidateA_response, candidateB_response):
    response = st.radio(question, [candidateA_response, candidateB_response], horizontal=True)
    return response == candidateA_response



# Function to check image exists and display image
def display_image(path, width=250):
    if path.exists():
        st.image(str(path), width=width)



# Function to run the survey and calculate results for the US Senator race
def USSenator():
    
    # Get candidate info
    df = candidatetable()
    
    # Initial candidate scores
    adam = 0
    steve = 0
    
    adam_agree = []
    steve_agree = []

    # Survey question: Background
    st.text("")
    st.text("")
    st.subheader("Background", divider="rainbow")
    adam_bg = df.loc[df['Name'] == 'Adam Schiff', 'Background'].values[0]
    steve_bg = df.loc[df['Name'] == 'Steve Garvey', 'Background'].values[0]

    colA, colB = st.columns([1,5])
    with colA:
        st.markdown("**Candidate A**")
    with colB:
        st.markdown(adam_bg)
    
    st.divider()
    
    colA, colB = st.columns([1,5])
    with colA:
        st.markdown("**Candidate B**")
    with colB:
        st.markdown(steve_bg)
    
    st.text("")
    st.text("")
    
    if survey_question("Which candidate's background do you think makes them a better fit for this role?", "Candidate A", "Candidate B"):
        adam += 1
        adam_agree.append("Background")
    else:
        steve += 1
        steve_agree.append("Background")

    # Survey question: Policy - Jobs and Economy
    st.text("")
    st.text("")
    st.subheader("Policy - Jobs and Economy", divider="rainbow")
    adam_Econ = df.loc[df['Name'] == 'Adam Schiff', 'Policy - Economy'].values[0]
    steve_Econ = df.loc[df['Name'] == 'Steve Garvey', 'Policy - Economy'].values[0]
    
    colA, colB = st.columns([1,5])
    with colA:
        st.markdown("**Candidate A**")
    with colB:
        st.markdown(adam_Econ)
    
    st.divider()
    
    colA, colB = st.columns([1,5])
    with colA:
        st.markdown("**Candidate B**")
    with colB:
        st.markdown(steve_Econ)
        
    st.text("")
    st.text("")

    if survey_question("Which candidate's proposed policy on jobs and the economy do you agree with most?", "Candidate A", "Candidate B"):
        adam += 1
        adam_agree.append("Policy - Jobs and Economy")
    else:
        steve += 1
        steve_agree.append("Policy - Jobs and Economy")

    # Survey question: Policy - Healthcare
    st.text("")
    st.text("")
    st.subheader("Policy - Healthcare", divider="rainbow")
    adam_Health = df.loc[df['Name'] == 'Adam Schiff', 'Policy - Healthcare'].values[0]
    steve_Health = df.loc[df['Name'] == 'Steve Garvey', 'Policy - Healthcare'].values[0]

    colA, colB = st.columns([1,5])
    with colA:
        st.markdown("**Candidate A**")
    with colB:
        st.markdown(adam_Health)
    
    st.divider()
    
    colA, colB = st.columns([1,5])
    with colA:
        st.markdown("**Candidate B**")
    with colB:
        st.markdown(steve_Health)
        
    st.text("")
    st.text("")

    if survey_question("Which candidate's proposed policy on healthcare do you agree with most?", "Candidate A", "Candidate B"):
        adam += 1
        adam_agree.append("Policy - Healthcare")
    else:
        steve += 1
        steve_agree.append("Policy - Healthcare")

    # Survey question: Policy - Climate, Energy, and Water
    st.text("")
    st.text("")
    st.subheader("Policy - Climate, Energy, and Water", divider="rainbow")
    adam_Climate = df.loc[df['Name'] == 'Adam Schiff', 'Policy - Climate'].values[0]
    steve_Climate = df.loc[df['Name'] == 'Steve Garvey', 'Policy - Climate'].values[0]

    colA, colB = st.columns([1,5])
    with colA:
        st.markdown("**Candidate A**")
    with colB:
        st.markdown(adam_Climate)
    
    st.divider()
    
    colA, colB = st.columns([1,5])
    with colA:
        st.markdown("**Candidate B**")
    with colB:
        st.markdown(steve_Climate)
    
    st.text("")
    st.text("")
    
    if survey_question("Which candidate's proposed policy on climate, energy, and water do you agree with most?", "Candidate A", "Candidate B"):
        adam += 1
        adam_agree.append("Policy - Climate, Energy, and Water")
    else:
        steve += 1
        steve_agree.append("Policy - Climate, Energy, and Water")

    # Survey question: Policy - Education
    st.text("")
    st.text("")
    st.subheader("Policy - Education", divider="rainbow")
    adam_Edu = df.loc[df['Name'] == 'Adam Schiff', 'Policy - Education'].values[0]
    steve_Edu = df.loc[df['Name'] == 'Steve Garvey', 'Policy - Education'].values[0]

    colA, colB = st.columns([1,5])
    with colA:
        st.markdown("**Candidate A**")
    with colB:
        st.markdown(adam_Edu)
    
    st.divider()
    
    colA, colB = st.columns([1,5])
    with colA:
        st.markdown("**Candidate B**")
    with colB:
        st.markdown(steve_Edu)
        
    st.text("")
    st.text("")
    
    if survey_question("Which candidate's proposed policy on education do you agree with most?", "Candidate A", "Candidate B"):
        adam += 1
        adam_agree.append("Policy - Education")
    else:
        steve += 1
        steve_agree.append("Policy - Education")

    # Survey question: Policy - Safety, Security and Justice Reform
    st.text("")
    st.text("")
    st.subheader("Policy - Safety, Security, and Justice Reform", divider="rainbow")
    adam_Safety = df.loc[df['Name'] == 'Adam Schiff', 'Policy - Public Safety'].values[0]
    steve_Safety = df.loc[df['Name'] == 'Steve Garvey', 'Policy - Public Safety'].values[0]

    colA, colB = st.columns([1,5])
    with colA:
        st.markdown("**Candidate A**")
    with colB:
        st.markdown(adam_Safety)
    
    st.divider()
    
    colA, colB = st.columns([1,5])
    with colA:
        st.markdown("**Candidate B**")
    with colB:
        st.markdown(steve_Safety)
        
    st.text("")
    st.text("")
    
    if survey_question("Which candidate's proposed policy on safety, security, and justice reform do you agree with most?", "Candidate A", "Candidate B"):
        adam += 1
        adam_agree.append("Policy - Safety, Security, and Justice Reform")
    else:
        steve += 1
        steve_agree.append("Policy - Safety, Security, and Justice Reform")

    # Survey question: Policy - Taxes
    st.text("")
    st.text("")
    st.subheader("Policy - Taxes", divider="rainbow")
    adam_Tax = df.loc[df['Name'] == 'Adam Schiff', 'Policy - Taxes'].values[0]
    steve_Tax = df.loc[df['Name'] == 'Steve Garvey', 'Policy - Taxes'].values[0]

    colA, colB = st.columns([1,5])
    with colA:
        st.markdown("**Candidate A**")
    with colB:
        st.markdown(adam_Tax)
    
    st.divider()
    
    colA, colB = st.columns([1,5])
    with colA:
        st.markdown("**Candidate B**")
    with colB:
        st.markdown(steve_Tax)
        
    st.text("")
    st.text("")
    
    if survey_question("Which candidate's proposed policy on taxes do you agree with most?", "Candidate A", "Candidate B"):
        adam += 1
        adam_agree.append("Policy - Taxes")
    else:
        steve += 1
        steve_agree.append("Policy - Taxes")

    # Survey question: Policy - Housing
    st.text("")
    st.text("")
    st.subheader("Policy - Housing", divider="rainbow")
    adam_House = df.loc[df['Name'] == 'Adam Schiff', 'Policy - Housing'].values[0]
    steve_House = df.loc[df['Name'] == 'Steve Garvey', 'Policy - Housing'].values[0]

    colA, colB = st.columns([1,5])
    with colA:
        st.markdown("**Candidate A**")
    with colB:
        st.markdown(adam_House)
    
    st.divider()
    
    colA, colB = st.columns([1,5])
    with colA:
        st.markdown("**Candidate B**")
    with colB:
        st.markdown(steve_House)
        
    st.text("")
    st.text("")
    
    if survey_question("Which candidate's proposed policy on housing do you agree with most?", "Candidate A", "Candidate B"):
        adam += 1
        adam_agree.append("Policy - Housing")
    else:
        steve += 1
        steve_agree.append("Policy - Housing")

    # Survey question: Policy - Homelessness
    st.subheader("Policy - Homelessness", divider="rainbow")
    adam_Homeless = df.loc[df['Name'] == 'Adam Schiff', 'Policy - Homelessness'].values[0]
    steve_Homeless = df.loc[df['Name'] == 'Steve Garvey', 'Policy - Homelessness'].values[0]

    colA, colB = st.columns([1,5])
    with colA:
        st.markdown("**Candidate A**")
    with colB:
        st.markdown(adam_Homeless)
    
    st.divider()
    
    colA, colB = st.columns([1,5])
    with colA:
        st.markdown("**Candidate B**")
    with colB:
        st.markdown(steve_Homeless)
        
    st.text("")
    st.text("")
    
    if survey_question("Which candidate's proposed policy on homelessness do you agree with most?", "Candidate A", "Candidate B"):
        adam += 1
        adam_agree.append("Policy - Homelessness")
    else:
        steve += 1
        steve_agree.append("Policy - Homelessness")

    # Survey question: Policy - Other
    st.text("")
    st.text("")
    st.subheader("Policy - Other", divider="rainbow")
    adam_Other = df.loc[df['Name'] == 'Adam Schiff', 'Policy - Other'].values[0]
    steve_Other = df.loc[df['Name'] == 'Steve Garvey', 'Policy - Other'].values[0]

    colA, colB = st.columns([1,5])
    with colA:
        st.markdown("**Candidate A**")
    with colB:
        st.markdown(adam_Other)
    
    st.divider()
    
    colA, colB = st.columns([1,5])
    with colA:
        st.markdown("**Candidate B**")
    with colB:
        st.markdown(steve_Other)
        
    st.text("")
    st.text("")
    
    if survey_question("Which candidate's other proposed policies do you agree with most?", "Candidate A", "Candidate B"):
        adam += 1
        adam_agree.append("Policy - Other")
    else:
        steve += 1
        steve_agree.append("Policy - Other")

    # Survey question: Hotness factor
    st.text("")
    st.text("")
    st.subheader("Candidate Hotness", divider="rainbow")
    image_adam = Path(df.loc[df['Name'] == 'Adam Schiff', 'Image'].values[0])
    image_steve = Path(df.loc[df['Name'] == 'Steve Garvey', 'Image'].values[0])

    colA, colB = st.columns(2)
    with colA:
        st.markdown("**Candidate A**")
        display_image(image_adam)

    with colB:
        st.markdown("**Candidate B**")
        display_image(image_steve)

    if survey_question("Who is hotter?", "Candidate A", "Candidate B"):
        adam += 1
        adam_agree.append("Hotness")
    else:
        steve += 1
        steve_agree.append("Hotness")

    return adam, steve, adam_agree, steve_agree



# Function to run the survey and calculate results for the US Representative race
def USRep():

    # Get candidate info
    df = candidatetable()
    
    # Initial candidate scores
    dave = 0
    scott = 0

    dave_agree = []
    scott_agree = []

    # Survey question: Background
    st.text("")
    st.text("")
    st.subheader("Background", divider="rainbow")
    dave_bg = df.loc[df['Name'] == 'Dave Min', 'Background'].values[0]
    scott_bg = df.loc[df['Name'] == 'Scott Baugh', 'Background'].values[0]
    
    colA, colB = st.columns([1,5])
    with colA:
        st.markdown("**Candidate A**")
    with colB:
        st.markdown(dave_bg)
    
    st.divider()
    
    colA, colB = st.columns([1,5])
    with colA:
        st.markdown("**Candidate B**")
    with colB:
        st.markdown(scott_bg)
        
    st.text("")
    st.text("")
    
    if survey_question("Which candidate's background do you think makes them a better fit for this role?", "Candidate A", "Candidate B"):
        dave += 1
        dave_agree.append("Background")
    else:
        scott += 1
        scott_agree.append("Background")

    # Survey question: Policy - Crime and Safety
    st.text("")
    st.text("")
    st.subheader("Policy - Crime and Safety", divider="rainbow")
    dave_polS = df.loc[df['Name'] == 'Dave Min', 'Policy - Public Safety'].values[0]
    scott_polS = df.loc[df['Name'] == 'Scott Baugh', 'Policy - Public Safety'].values[0]

    colA, colB = st.columns([1,5])
    with colA:
        st.markdown("**Candidate A**")
    with colB:
        st.markdown(dave_polS)
    
    st.divider()
    
    colA, colB = st.columns([1,5])
    with colA:
        st.markdown("**Candidate B**")
    with colB:
        st.markdown(scott_polS)
        
    st.text("")
    st.text("")

    if survey_question("Which candidate's proposed policy on crime and safety do you agree with most?", "Candidate A", "Candidate B"):
        dave += 1
        dave_agree.append("Policy - Crime and Safety")
    else:
        scott += 1
        scott_agree.append("Policy - Crime and Safety") 

    # Survey question: Policy - Climate
    st.text("")
    st.text("")
    st.subheader("Policy - Climate", divider="rainbow")
    dave_polCl = df.loc[df['Name'] == 'Dave Min', 'Policy - Climate'].values[0]
    scott_polCl = df.loc[df['Name'] == 'Scott Baugh', 'Policy - Climate'].values[0]

    colA, colB = st.columns(2)
    with colA:
        st.markdown("**Candidate A**")
        st.markdown(dave_polCl)

    with colB:
        st.markdown("**Candidate B**")
        st.markdown(scott_polCl)
            
    st.text("")
    st.text("")

    if survey_question("Which candidate's proposed policy on the climate do you agree with most?", "Candidate A", "Candidate B"):
        dave += 1
        dave_agree.append("Policy - Climate")
    else:
        scott += 1
        scott_agree.append("Policy - Climate")     

    # Survey question: Policy - Economy
    st.text("")
    st.text("")
    st.subheader("Policy - Economy", divider="rainbow")
    dave_polE = df.loc[df['Name'] == 'Dave Min', 'Policy - Economy'].values[0]
    scott_polE = df.loc[df['Name'] == 'Scott Baugh', 'Policy - Economy'].values[0]

    colA, colB = st.columns(2)
    with colA:
        st.markdown("**Candidate A**")
        st.markdown(dave_polE)

    with colB:
        st.markdown("**Candidate B**")
        st.markdown(scott_polE)
            
    st.text("")
    st.text("")

    if survey_question("Which candidate's proposed economic policy do you agree with most?", "Candidate A", "Candidate B"):
        dave += 1
        dave_agree.append("Policy - Economy")
    else:
        scott += 1
        scott_agree.append("Policy - Economy")

    # Survey question: Policy - Other
    st.text("")
    st.text("")
    st.subheader("Policy - Other", divider="rainbow")
    dave_polO = df.loc[df['Name'] == 'Dave Min', 'Policy - Other'].values[0]
    scott_polO = df.loc[df['Name'] == 'Scott Baugh', 'Policy - Other'].values[0]

    colA, colB = st.columns([1,5])
    with colA:
        st.markdown("**Candidate A**")
    with colB:
        st.markdown(dave_polO)
    
    st.divider()
    
    colA, colB = st.columns([1,5])
    with colA:
        st.markdown("**Candidate B**")
    with colB:
        st.markdown(scott_polO)
        
    st.text("")
    st.text("")

    if survey_question("Which candidate's proposed other policies do you agree with most?", "Candidate A", "Candidate B"):
        dave += 1
        dave_agree.append("Policy - Other")
    else:
        scott += 1
        scott_agree.append("Policy - Other")

    # Survey question: Hotness factor
    st.text("")
    st.text("")
    st.subheader("Candidate Hotness", divider="rainbow")
    image_dave = Path(df.loc[df['Name'] == 'Dave Min', 'Image'].values[0])
    image_scott = Path(df.loc[df['Name'] == 'Scott Baugh', 'Image'].values[0])

    colA, colB = st.columns(2)
    with colA:
        st.markdown("**Candidate A**")
        display_image(image_dave)

    with colB:
        st.markdown("**Candidate B**")
        display_image(image_scott)

    if survey_question("Who is hotter?", "Candidate A", "Candidate B"):
        dave += 1
        dave_agree.append("Hotness")
    else:
        scott += 1
        scott_agree.append("Hotness")

    return dave, scott, dave_agree, scott_agree



# Function to run the survey and calculate results for the State Senator race
def StateSenator():

    # Get candidate info
    df = candidatetable()
    
    # Initial candidate scores
    josh = 0
    steven = 0
    
    josh_agree = []
    steven_agree = []

    # Survey question: Background
    st.text("")
    st.text("")
    st.subheader("Background", divider="rainbow")
    josh_bg = df.loc[df['Name'] == 'Josh Newman', 'Background'].values[0]
    steven_bg = df.loc[df['Name'] == "Steven 'Steve' Choi", 'Background'].values[0]

    colA, colB = st.columns(2)
    with colA:
        st.markdown("**Candidate A**")
        st.markdown(josh_bg)

    with colB:
        st.markdown("**Candidate B**")
        st.markdown(steven_bg)
            
    st.text("")
    st.text("")
    
    if survey_question("Which candidate's background do you think makes them a better fit for this role?", "Candidate A", "Candidate B"):
        josh += 1
        josh_agree.append("Background")
    else:
        steven += 1
        steven_agree.append("Background")

    # Survey question: Policy - All
    st.text("")
    st.text("")
    st.subheader("Policy", divider="rainbow")
    josh_polS = df.loc[df['Name'] == 'Josh Newman', 'Policy - All'].values[0]
    steven_polS = df.loc[df['Name'] == "Steven 'Steve' Choi", 'Policy - All'].values[0]

    colA, colB = st.columns(2)
    with colA:
        st.markdown("**Candidate A**")
        st.markdown(josh_polS)

    with colB:
        st.markdown("**Candidate B**")
        st.markdown(steven_polS)
            
    st.text("")
    st.text("")

    if survey_question("Which candidate's proposed policy do you agree with most?", "Candidate A", "Candidate B"):
        josh += 1
        josh_agree.append("Policy")
    else:
        steven += 1
        steven_agree.append("Policy")

    # Survey question: Hotness factor
    st.text("")
    st.text("")
    st.subheader("Candidate Hotness", divider="rainbow")
    image_josh = Path(df.loc[df['Name'] == 'Josh Newman', 'Image'].values[0])
    image_steven = Path(df.loc[df['Name'] == "Steven 'Steve' Choi", 'Image'].values[0])

    colA, colB = st.columns(2)
    with colA:
        st.markdown("**Candidate A**")
        display_image(image_josh)

    with colB:
        st.markdown("**Candidate B**")
        display_image(image_steven)

    if survey_question("Who is hotter?", "Candidate A", "Candidate B"):
        josh += 1
        josh_agree.append("Hotness")
    else:
        steven += 1
        steven_agree.append("Hotness")

    return josh, steven, josh_agree, steven_agree



# Function to run the survey and calculate results for the State Assembly race
def StateAssembly():

    # Get candidate info
    df = candidatetable()
    
    # Initial candidate scores
    cottie = 0
    scotty = 0
    
    cottie_agree = []
    scotty_agree = []

    # Survey question: Background
    st.text("")
    st.text("")
    st.subheader("Background", divider="rainbow")
    cottie_bg = df.loc[df['Name'] == 'Cottie Petrie-Norris', 'Background'].values[0]
    scotty_bg = df.loc[df['Name'] == 'Scotty Peotter', 'Background'].values[0]
    
    colA, colB = st.columns([1,5])
    with colA:
        st.markdown("**Candidate A**")
    with colB:
        st.markdown(cottie_bg)
    
    st.divider()
    
    colA, colB = st.columns([1,5])
    with colA:
        st.markdown("**Candidate B**")
    with colB:
        st.markdown(scotty_bg)
            
    st.text("")
    st.text("")
    
    if survey_question("Which candidate's background do you think makes them a better fit for this role?", "Candidate A", "Candidate B"):
        cottie += 1
        cottie_agree.append("Background")
    else:
        scotty += 1
        scotty_agree.append("Background")

    # Survey question: Policy - Reproductive Rights
    st.text("")
    st.text("")
    st.subheader("Policy - Reproductive Rights", divider="rainbow")
    cottie_polA = df.loc[df['Name'] == 'Cottie Petrie-Norris', 'Policy - Healthcare'].values[0]
    scotty_polA = df.loc[df['Name'] == 'Scotty Peotter', 'Policy - Healthcare'].values[0]

    colA, colB = st.columns(2)
    with colA:
        st.markdown("**Candidate A**")
        st.markdown(cottie_polA)

    with colB:
        st.markdown("**Candidate B**")
        st.markdown(scotty_polA)
            
    st.text("")
    st.text("")

    if survey_question("Which candidate's proposed policy on reproductive rights do you agree with most?", "Candidate A", "Candidate B"):
        cottie += 1
        cottie_agree.append("Policy - Reproductive Rights")
    else:
        scotty += 1
        scotty_agree.append("Policy - Reproductive Rights") 

    # Survey question: Policy - Education
    st.text("")
    st.text("")
    st.subheader("Policy - Education", divider="rainbow")
    cottie_polE = df.loc[df['Name'] == 'Cottie Petrie-Norris', 'Policy - Education'].values[0]
    scotty_polE = df.loc[df['Name'] == 'Scotty Peotter', 'Policy - Education'].values[0]

    colA, colB = st.columns(2)
    with colA:
        st.markdown("**Candidate A**")
        st.markdown(cottie_polE)

    with colB:
        st.markdown("**Candidate B**")
        st.markdown(scotty_polE)
            
    st.text("")
    st.text("")

    if survey_question("Which candidate's proposed policy on education do you agree with most?", "Candidate A", "Candidate B"):
        cottie += 1
        cottie_agree.append("Policy - Education")
    else:
        scotty += 1
        scotty_agree.append("Policy - Education")     

    # Survey question: Policy - Homelessness
    st.text("")
    st.text("")
    st.subheader("Policy - Homelessness", divider="rainbow")
    cottie_polH = df.loc[df['Name'] == 'Cottie Petrie-Norris', 'Policy - Homelessness'].values[0]
    scotty_polH = df.loc[df['Name'] == 'Scotty Peotter', 'Policy - Homelessness'].values[0]

    colA, colB = st.columns(2)
    with colA:
        st.markdown("**Candidate A**")
        st.markdown(cottie_polH)

    with colB:
        st.markdown("**Candidate B**")
        st.markdown(scotty_polH)
            
    st.text("")
    st.text("")

    if survey_question("Which candidate's proposed policy on homelessness do you agree with most?", "Candidate A", "Candidate B"):
        cottie += 1
        cottie_agree.append("Policy - Homelessness")
    else:
        scotty += 1
        scotty_agree.append("Policy - Homelessness")

    # Survey question: Policy - Fiscal Responsability
    st.text("")
    st.text("")
    st.subheader("Policy - Fiscal Responsibility", divider="rainbow")
    cottie_polFR = df.loc[df['Name'] == 'Cottie Petrie-Norris', 'Policy - Economy'].values[0]
    scotty_polFR = df.loc[df['Name'] == 'Scotty Peotter', 'Policy - Economy'].values[0]

    colA, colB = st.columns(2)
    with colA:
        st.markdown("**Candidate A**")
        st.markdown(cottie_polFR)

    with colB:
        st.markdown("**Candidate B**")
        st.markdown(scotty_polFR)
            
    st.text("")
    st.text("")

    if survey_question("Which candidate's proposed policy on fiscal responsibility do you agree with most?", "Candidate A", "Candidate B"):
        cottie += 1
        cottie_agree.append("Policy - Fiscal Responsibility")
    else:
        scotty += 1
        scotty_agree.append("Policy - Fiscal Responsibility")

    # Survey question: Policy - Public Safety
    st.text("")
    st.text("")
    st.subheader("Policy - Public Safety", divider="rainbow")
    cottie_polS = df.loc[df['Name'] == 'Cottie Petrie-Norris', 'Policy - Public Safety'].values[0]
    scotty_polS = df.loc[df['Name'] == 'Scotty Peotter', 'Policy - Public Safety'].values[0]

    colA, colB = st.columns(2)
    with colA:
        st.markdown("**Candidate A**")
        st.markdown(cottie_polS)

    with colB:
        st.markdown("**Candidate B**")
        st.markdown(scotty_polS)
            
    st.text("")
    st.text("")

    if survey_question("Which candidate's proposed policy on public safety do you agree with most?", "Candidate A", "Candidate B"):
        cottie += 1
        cottie_agree.append("Policy - Public Safety")
    else:
        scotty += 1
        scotty_agree.append("Policy - Public Safety")

    # Survey question: Policy - Guns
    st.text("")
    st.text("")
    st.subheader("Policy - Guns", divider="rainbow")
    cottie_polG = df.loc[df['Name'] == 'Cottie Petrie-Norris', 'Policy - Guns'].values[0]
    scotty_polG = df.loc[df['Name'] == 'Scotty Peotter', 'Policy - Guns'].values[0]

    colA, colB = st.columns(2)
    with colA:
        st.markdown("**Candidate A**")
        st.markdown(cottie_polG)

    with colB:
        st.markdown("**Candidate B**")
        st.markdown(scotty_polG)
            
    st.text("")
    st.text("")

    if survey_question("Which candidate's proposed policy on guns do you agree with most?", "Candidate A", "Candidate B"):
        cottie += 1
        cottie_agree.append("Policy - Guns")
    else:
        scotty += 1
        scotty_agree.append("Policy - Guns")

    # Survey question: Policy - Other
    st.text("")
    st.text("")
    st.subheader("Policy - Other", divider="rainbow")
    cottie_polO = df.loc[df['Name'] == 'Cottie Petrie-Norris', 'Policy - Other'].values[0]
    scotty_polO = df.loc[df['Name'] == 'Scotty Peotter', 'Policy - Other'].values[0]

    colA, colB = st.columns(2)
    with colA:
        st.markdown("**Candidate A**")
        st.markdown(cottie_polO)

    with colB:
        st.markdown("**Candidate B**")
        st.markdown(scotty_polO)
            
    st.text("")
    st.text("")

    if survey_question("Which candidate's proposed other policies do you agree with most?", "Candidate A", "Candidate B"):
        cottie += 1
        cottie_agree.append("Policy - Other")
    else:
        scotty += 1
        scotty_agree.append("Policy - Other")

    # Survey question: Endorsements
    st.text("")
    st.text("")
    st.subheader("Endorsements", divider="rainbow")
    cottie_end = df.loc[df['Name'] == 'Cottie Petrie-Norris', 'Endorsements'].values[0]
    scotty_end = df.loc[df['Name'] == 'Scotty Peotter', 'Endorsements'].values[0]

    if survey_question("Which endorsements do you think would indicate a better candidate?", cottie_end, scotty_end):
        cottie += 1
        cottie_agree.append("Endorsements")
    else:
        scotty += 1
        scotty_agree.append("Endorsements")

    # Survey question: Website Oddities
    st.text("")
    st.text("")
    st.subheader("Website Oddities", divider="rainbow")
    cottie_WO = df.loc[df['Name'] == 'Cottie Petrie-Norris', 'Other Info'].values[0]
    scotty_WO = df.loc[df['Name'] == 'Scotty Peotter', 'Other Info'].values[0]

    if survey_question("Which candidate has the least weird website component?", cottie_WO, scotty_WO):
        cottie += 1
        cottie_agree.append("Less weird website")
    else:
        scotty += 1
        scotty_agree.append("Less weird website")

    # Survey question: Hotness factor
    st.text("")
    st.text("")
    st.subheader("Candidate Hotness", divider="rainbow")
    image_cottie = Path(df.loc[df['Name'] == 'Cottie Petrie-Norris', 'Image'].values[0])
    image_scotty = Path(df.loc[df['Name'] == 'Scotty Peotter', 'Image'].values[0])

    colA, colB = st.columns(2)
    with colA:
        st.markdown("**Candidate A**")
        display_image(image_cottie)

    with colB:
        st.markdown("**Candidate B**")
        display_image(image_scotty)

    if survey_question("Who is hotter?", "Candidate A", "Candidate B"):
        cottie += 1
        cottie_agree.append("Hotness")
    else:
        scotty += 1
        scotty_agree.append("Hotness")

    return cottie, scotty, cottie_agree, scotty_agree



# Function to run the survey and calculate results for the School District race
def SchoolDistrict():

    # Get candidate info
    df = candidatetable()
    
    # Initial candidate scores
    amy = 0
    chris = 0
    krita = 0
    
    amy_agree = []
    chris_agree = []
    krita_agree = []

    # Survey question: Background
    st.text("")
    st.text("")
    st.subheader("Background", divider="rainbow")
    amy_bg = df.loc[df['Name'] == 'Amy Peters', 'Background'].values[0]
    chris_bg = df.loc[df['Name'] == 'Chris Kretzu', 'Background'].values[0]
    krita_bg = df.loc[df['Name'] == 'Krita Weigand', 'Background'].values[0]

    colA, colB, colC = st.columns(3)
    with colA:
        st.markdown("**Candidate A**")
        st.markdown(amy_bg)

    with colB:
        st.markdown("**Candidate B**")
        st.markdown(chris_bg)
    
    with colC:
        st.markdown("**Candidate C**")
        st.markdown(krita_bg)
            
    st.text("")
    st.text("")
    bg = st.radio("Which candidate's background do you think makes them a better fit for this role?", ["Candidate A", "Candidate B", "Candidate C"], horizontal=True)

    if bg == "Candidate A":
        amy += 1
        amy_agree.append("Background")
    elif bg == "Candidate B":
        chris += 1
        chris_agree.append("Background")
    else:
        krita += 1
        krita_agree.append("Background")

    # Survey question: Policy
    st.text("")
    st.text("")
    st.subheader("Policy", divider="rainbow")
    amy_pol = df.loc[df['Name'] == 'Amy Peters', 'Policy - All'].values[0]
    chris_pol = df.loc[df['Name'] == 'Chris Kretzu', 'Policy - All'].values[0]
    krita_pol = df.loc[df['Name'] == 'Krita Weigand', 'Policy - All'].values[0]

    colA, colB = st.columns([1,4])
    with colA:
        st.markdown("**Candidate A**")
    with colB:
        st.markdown(amy_pol)
    
    st.divider()
    
    colA, colB = st.columns([1,4])
    with colA:
        st.markdown("**Candidate B**")
    with colB:
        st.markdown(chris_pol)
    
    st.divider()

    colA, colB = st.columns([1,4])
    
    with colA:
        st.markdown("**Candidate C**")
    with colB:
        st.markdown(krita_pol)

    st.text("")
    st.text("")
    pol = st.radio("Which candidate's proposed policy do you think makes them a better fit for this role?", ["Candidate A", "Candidate B", "Candidate C"], horizontal=True)

    if pol == "Candidate A":
        amy += 1
        amy_agree.append("Policy")
    elif pol == "Candidate B":
        chris += 1
        chris_agree.append("Policy")
    else:
        krita += 1
        krita_agree.append("Policy")

    # Survey question: Hotness factor
    st.text("")
    st.text("")
    st.subheader("Candidate Hotness", divider="rainbow")
    image_amy = Path(df.loc[df['Name'] == 'Amy Peters', 'Image'].values[0])
    image_chris = Path(df.loc[df['Name'] == 'Chris Kretzu', 'Image'].values[0])
    image_krita = Path(df.loc[df['Name'] == 'Krita Weigand', 'Image'].values[0])

    colA, colB, colC = st.columns(3)

    with colA:
        st.markdown("**Candidate A**")
        display_image(image_amy, width=200)

    with colB:
        st.markdown("**Candidate B**")
        display_image(image_chris, width=200)

    with colC:
        st.markdown("**Candidate C**")
        display_image(image_krita, width=200)

    hotness = st.radio("Who is hotter?", ["Candidate A", "Candidate B", "Candidate C"], horizontal=True)

    if hotness == "Candidate A":
        amy += 1
        amy_agree.append("Hotness")
    elif hotness == "Candidate B":
        chris += 1
        chris_agree.append("Hotness")
    else:
        krita += 1
        krita_agree.append("Hotness")

    return amy, chris, krita, amy_agree, chris_agree, krita_agree



# Function to run the survey and calculate results for the Mayor race
def Mayor():

    # Get candidate info
    df = candidatetable()
    
    # Initial candidate scores
    james = 0
    john = 0
    
    james_agree = []
    john_agree = []
    
    # Survey question: Background
    st.text("")
    st.text("")
    st.subheader("Background", divider="rainbow")
    james_bg = df.loc[df['Name'] == 'James Peters', 'Background'].values[0]
    john_bg = df.loc[df['Name'] == 'John Stephens', 'Background'].values[0]

    colA, colB = st.columns(2)
    with colA:
        st.markdown("**Candidate A**")
        st.markdown(james_bg)

    with colB:
        st.markdown("**Candidate B**")
        st.markdown(john_bg)
            
    st.text("")
    st.text("")
    
    if survey_question("Which candidate's background do you think makes them a better fit for this role?", "Candidate A", "Candidate B"):
        james += 1
        james_agree.append("Background")
    else:
        john += 1
        john_agree.append("Background")

    # Survey question: Policy - Homelessness
    st.text("")
    st.text("")
    st.subheader("Policy - Homelessness", divider="rainbow")
    james_polH = df.loc[df['Name'] == 'James Peters', 'Policy - Homelessness'].values[0]
    john_polH = df.loc[df['Name'] == 'John Stephens', 'Policy - Homelessness'].values[0]

    colA, colB = st.columns(2)
    with colA:
        st.markdown("**Candidate A**")
        st.markdown(james_polH)

    with colB:
        st.markdown("**Candidate B**")
        st.markdown(john_polH)
            
    st.text("")
    st.text("")

    if survey_question("Which candidate's proposed policy on homelessness do you agree with most?", "Candidate A", "Candidate B"):
        james += 1
        james_agree.append("Homelessness Policy")
    else:
        john += 1
        john_agree.append("Homelessness Policy")
    
    # Survey question: Policy - Public Safety
    st.text("")
    st.text("")
    st.subheader("Policy - Public Safety", divider="rainbow")
    james_polS = df.loc[df['Name'] == 'James Peters', 'Policy - Public Safety'].values[0]
    john_polS = df.loc[df['Name'] == 'John Stephens', 'Policy - Public Safety'].values[0]

    colA, colB = st.columns(2)
    with colA:
        st.markdown("**Candidate A**")
        st.markdown(james_polS)

    with colB:
        st.markdown("**Candidate B**")
        st.markdown(john_polS)
            
    st.text("")
    st.text("")

    if survey_question("Which candidate's proposed policy on public safety do you agree with most?", "Candidate A", "Candidate B"):
        james += 1
        james_agree.append("Public Safety Policy")
    else:
        john += 1
        john_agree.append("Public Safety Policy")

    # Survey question: Policy - Other
    st.text("")
    st.text("")
    st.subheader("Policy - Other", divider="rainbow")
    james_polother = df.loc[df['Name'] == 'James Peters', 'Policy - Other'].values[0]
    john_polother = df.loc[df['Name'] == 'John Stephens', 'Policy - Other'].values[0]

    colA, colB = st.columns(2)
    with colA:
        st.markdown("**Candidate A**")
        st.markdown(james_polother)

    with colB:
        st.markdown("**Candidate B**")
        st.markdown(john_polother)
            
    st.text("")
    st.text("")

    if survey_question("Which candidate's proposed other policies do you agree with most?", "Candidate A", "Candidate B"):
        james += 1
        james_agree.append("Other Policies")
    else:
        john += 1
        john_agree.append("Other Policies") 

    # Survey question: Hobbies and other activities
    st.text("")
    st.text("")
    st.subheader("What Else The Candidates Are Up To", divider="rainbow")
    james_hobbies = df.loc[df['Name'] == 'James Peters', 'Other Info'].values[0]
    john_hobbies = df.loc[df['Name'] == 'John Stephens', 'Other Info'].values[0]
    
    colA, colB = st.columns(2)
    with colA:
        st.markdown("**Candidate A**")
        st.markdown(james_hobbies)

    with colB:
        st.markdown("**Candidate B**")
        st.markdown(john_hobbies)
            
    st.text("")
    st.text("")

    if survey_question("Which hobbies and fun facts do you think make for a better candidate?", "Candidate A", "Candidate B"):
        james += 1
        james_agree.append("Volunteering, hobbies, etc.")
    else:
        john += 1
        john_agree.append("Volunteering, hobbies, etc.")

    # Survey question: Hotness factor
    st.text("")
    st.text("")
    st.subheader("Candidate Hotness", divider="rainbow")
    image_james = Path(df.loc[df['Name'] == 'James Peters', 'Image'].values[0])
    image_john = Path(df.loc[df['Name'] == 'John Stephens', 'Image'].values[0])

    colA, colB = st.columns(2)
    with colA:
        st.markdown("**Candidate A**")
        display_image(image_james)

    with colB:
        st.markdown("**Candidate B**")
        display_image(image_john)

    if survey_question("Who is hotter?", "Candidate A", "Candidate B"):
        james += 1
        james_agree.append("Hotness")
    else:
        john += 1
        john_agree.append("Hotness")

    return james, john, james_agree, john_agree



# Function to run the survey and calculate results for the municipal water OC district director race
def CityCouncil():
    # Get candidate info
    df = candidatetable()
    
    # Initial candidate scores
    jeffH = 0
    jeffP = 0
    
    jeffH_agree = []
    jeffP_agree = []

    # Survey question: Background
    st.text("")
    st.text("")
    st.subheader("Background", divider="rainbow")
    jeffH_bg = df.loc[df['Name'] == 'Jeffrey Harlan', 'Background'].values[0]
    jeffP_bg= df.loc[df['Name'] == 'Jeff Pettis', 'Background'].values[0]

    colA, colB = st.columns(2)
    with colA:
        st.markdown("**Candidate A**")
        st.markdown(jeffH_bg)

    with colB:
        st.markdown("**Candidate B**")
        st.markdown(jeffP_bg)
            
    st.text("")
    st.text("")
    
    if survey_question("Which candidate's background do you think makes them a better fit for this role?", "Candidate A", "Candidate B"):
        jeffH += 1
        jeffH_agree.append("Background")
    else:
        jeffP += 1
        jeffP_agree.append("Background")

    # Survey question: Policy - Homelessness
    st.text("")
    st.text("")
    st.subheader("Policy - Homelessness", divider="rainbow")
    jeffH_polH = df.loc[df['Name'] == 'Jeffrey Harlan', 'Policy - Homelessness'].values[0]
    jeffP_polH = df.loc[df['Name'] == 'Jeff Pettis', 'Policy - Homelessness'].values[0]

    colA, colB = st.columns(2)
    with colA:
        st.markdown("**Candidate A**")
        st.markdown(jeffH_polH)

    with colB:
        st.markdown("**Candidate B**")
        st.markdown(jeffP_polH)

    st.text("")
    st.text("")

    if survey_question("Which candidate's proposed policy on homelessness do you agree with most?", "Candidate A", "Candidate B"):
        jeffH += 1
        jeffH_agree.append("Homelessness Policy")
    else:
        jeffP += 1
        jeffP_agree.append("Homelessness Policy")
    
    # Survey question: Policy - Public Safety
    st.text("")
    st.text("")
    st.subheader("Policy - Public Safety", divider="rainbow")
    jeffH_polS = df.loc[df['Name'] == 'Jeffrey Harlan', 'Policy - Public Safety'].values[0]
    jeffP_polS = df.loc[df['Name'] == 'Jeff Pettis', 'Policy - Public Safety'].values[0]

    colA, colB = st.columns(2)
    with colA:
        st.markdown("**Candidate A**")
        st.markdown(jeffH_polS)

    with colB:
        st.markdown("**Candidate B**")
        st.markdown(jeffP_polS)
            
    st.text("")
    st.text("")

    if survey_question("Which candidate's proposed policy on public safety do you agree with most?", "Candidate A", "Candidate B"):
        jeffH += 1
        jeffH_agree.append("Public Safety Policy")
    else:
        jeffP += 1
        jeffP_agree.append("Public Safety Policy")

    # Survey question: Policy - Development
    st.text("")
    st.text("")
    st.subheader("Policy - Development", divider="rainbow")
    jeffH_polD = df.loc[df['Name'] == 'Jeffrey Harlan', 'Policy - Development'].values[0]
    jeffP_polD = df.loc[df['Name'] == 'Jeff Pettis', 'Policy - Development'].values[0]

    colA, colB = st.columns(2)
    with colA:
        st.markdown("**Candidate A**")
        st.markdown(jeffH_polD)

    with colB:
        st.markdown("**Candidate B**")
        st.markdown(jeffP_polD)
            
    st.text("")
    st.text("")

    if survey_question("Which candidate's proposed policy on development do you agree with most?", "Candidate A", "Candidate B"):
        jeffH += 1
        jeffH_agree.append("Development Policy")
    else:
        jeffP += 1
        jeffP_agree.append("Development Policy")

    # Survey question: Policy - Other
    st.text("")
    st.text("")
    st.subheader("Policy - Other", divider="rainbow")
    jeffH_polother = df.loc[df['Name'] == 'Jeffrey Harlan', 'Policy - Other'].values[0]
    jeffP_polother = df.loc[df['Name'] == 'Jeff Pettis', 'Policy - Other'].values[0]

    colA, colB = st.columns(2)
    with colA:
        st.markdown("**Candidate A**")
        st.markdown(jeffH_polother)

    with colB:
        st.markdown("**Candidate B**")
        st.markdown(jeffP_polother)
            
    st.text("")
    st.text("")

    if survey_question("Which candidate's proposed other policies do you agree with most?", "Candidate A", "Candidate B"):
        jeffH += 1
        jeffH_agree.append("Other Policies")
    else:
        jeffP += 1
        jeffP_agree.append("Other Policies") 
    
    # Survey question: Endorsements
    st.text("")
    st.text("")
    st.subheader("Endorsements", divider="rainbow")
    jeffH_end = df.loc[df['Name'] == 'Jeffrey Harlan', 'Endorsements'].values[0]
    jeffP_end = df.loc[df['Name'] == 'Jeff Pettis', 'Endorsements'].values[0]
    
    if survey_question("Which endorsements do you think would indicate a better candidate??", jeffH_end, jeffP_end):
        jeffH += 1
        jeffH_agree.append("Endorsements")
    else:
        jeffP += 1
        jeffP_agree.append("Endorsements")

    # Survey question: Hobbies and other activities
    st.text("")
    st.text("")
    st.subheader("What Else The Candidates Are Up To", divider="rainbow")
    jeffH_hobbies = df.loc[df['Name'] == 'Jeffrey Harlan', 'Other Info'].values[0]
    jeffP_hobbies = df.loc[df['Name'] == 'Jeff Pettis', 'Other Info'].values[0]
    
    colA, colB = st.columns(2)
    with colA:
        st.markdown("**Candidate A**")
        st.markdown(jeffH_hobbies)

    with colB:
        st.markdown("**Candidate B**")
        st.markdown(jeffP_hobbies)
        
    st.text("")
    st.text("")

    if survey_question("Which hobbies and fun facts do you think make for a better candidate?", "Candidate A", "Candidate B"):
        jeffH += 1
        jeffH_agree.append("Volunteering, hobbies, etc.")
    else:
        jeffP += 1
        jeffP_agree.append("Volunteering, hobbies, etc.")

    # Survey question: Hotness factor
    st.text("")
    st.text("")
    st.subheader("Candidate Hotness", divider="rainbow")
    image_jeffH = Path(df.loc[df['Name'] == 'Jeffrey Harlan', 'Image'].values[0])
    image_jeffP = Path(df.loc[df['Name'] == 'Jeff Pettis', 'Image'].values[0])

    colA, colB = st.columns(2)
    with colA:
        st.markdown("**Candidate A**")
        display_image(image_jeffH)

    with colB:
        st.markdown("**Candidate B**")
        display_image(image_jeffP)

    if survey_question("Who is hotter?", "Candidate A", "Candidate B"):
        jeffH += 1
        jeffH_agree.append("Hotness")
    else:
        jeffP += 1
        jeffP_agree.append("Hotness")

    # Survey question: Dog Cutenesss
    st.text("")
    st.text("")
    st.subheader("Dog Cutenesss", divider="rainbow")
    image_jeffHdog = Path(df.loc[df['Name'] == 'Jeffrey Harlan', 'Dog'].values[0])
    image_jeffPdog = Path(df.loc[df['Name'] == 'Jeff Pettis', 'Dog'].values[0])

    colA, colB = st.columns(2)
    with colA:
        st.markdown("**Dog A**")
        display_image(image_jeffHdog)

    with colB:
        st.markdown("**Dog B**")
        display_image(image_jeffPdog)

    if survey_question("Which candidate's dog is cuter?", "Dog A", "Dog B"):
        jeffH += 1
        jeffH_agree.append("Dog Cuteness")
    else:
        jeffP += 1
        jeffP_agree.append("Dog Cuteness")

    return jeffH, jeffP, jeffH_agree, jeffP_agree



# Function to run the survey and calculate results for the municipal water OC district director race
def MunicipalWater():
    # Get candidate info
    df = candidatetable()

    # Initial candidate scores
    pano = 0
    karl = 0
    
    pano_agree = []
    karl_agree = []

    # Survey question: Background
    st.text("")
    st.text("")
    st.subheader("Work Experience", divider="rainbow")
    pano_work = df.loc[df['Name'] == 'Pano Frousakis', 'Background'].values[0]
    karl_work = df.loc[df['Name'] == 'Karl W. Seckel', 'Background'].values[0]

    colA, colB = st.columns(2)
    with colA:
        st.markdown("**Candidate A**")
        st.markdown(pano_work)

    with colB:
        st.markdown("**Candidate B**")
        st.markdown(karl_work)
            
    st.text("")
    st.text("")
    
    if survey_question("Which candidate's background do you think makes them a better fit for this role?", "Candidate A", "Candidate B"):
        pano += 1
        pano_agree.append("Work Experience")
    else:
        karl += 1
        karl_agree.append("Work Experience")


    # Survey question: Policy
    st.text("")
    st.text("")
    st.subheader("Policy", divider="rainbow")
    pano_pol = df.loc[df['Name'] == 'Pano Frousakis', 'Policy - All'].values[0]
    karl_pol = df.loc[df['Name'] == 'Karl W. Seckel', 'Policy - All'].values[0]

    colA, colB = st.columns(2)

    with colA:
        st.markdown("**Candidate A**")
        st.markdown(pano_pol)

    with colB:
        st.markdown("**Candidate B**")
        st.markdown(karl_pol)
            
    st.text("")
    st.text("")

    if survey_question("Which candidate's proposed policy do you think makes them a better fit for this role?", "Candidate A", "Candidate B"):
        pano += 1
        pano_agree.append("Policy")
    else:
        karl += 1
        karl_agree.append("Policy")

    # Survey question: Endorsements
    st.text("")
    st.text("")
    st.subheader("Endorsements", divider="rainbow")
    pano_end = df.loc[df['Name'] == 'Pano Frousakis', 'Endorsements'].values[0]
    karl_end = df.loc[df['Name'] == 'Karl W. Seckel', 'Endorsements'].values[0]
    
    if survey_question("Which endorsements do you think would indicate a better candidate??", pano_end, karl_end):
        pano += 1
        pano_agree.append("Endorsements")
    else:
        karl += 1
        karl_agree.append("Endorsements")

    # Survey question: Hotness factorß
    st.text("")
    st.text("")
    st.subheader("Candidate Hotness", divider="rainbow")
    image_pano = Path(df.loc[df['Name'] == 'Pano Frousakis', 'Image'].values[0])
    image_karl = Path(df.loc[df['Name'] == 'Karl W. Seckel', 'Image'].values[0])

    colA, colB = st.columns(2)
    with colA:
        st.markdown("**Candidate A**")
        display_image(image_pano)

    with colB:
        st.markdown("**Candidate B**")
        display_image(image_karl)

    if survey_question("Who is hotter?", "Candidate A", "Candidate B"):
        pano += 1
        pano_agree.append("Hotness")
    else:
        karl += 1
        karl_agree.append("Hotness")
    
    return pano, karl, pano_agree, karl_agree



# Function to run the survey and calculate results for the OC water district director race
def OCWater():
    # Get candidate info
    df = candidatetable()

    # Initial candidate scores
    bob = 0
    erik = 0
    
    bob_agree = []
    erik_agree = []

    # Survey question: Background
    st.text("")
    st.text("")
    st.subheader("Background", divider="rainbow")
    
    bob_bg = df.loc[df['Name'] == 'Bob Ooten', 'Background'].values[0]
    erik_bg = df.loc[df['Name'] == 'Erik Weigand', 'Background'].values[0]

    colA, colB = st.columns(2)

    with colA:
        st.markdown("**Candidate A**")
        st.markdown(bob_bg)

    with colB:
        st.markdown("**Candidate B**")
        st.markdown(erik_bg)
            
    st.text("")
    st.text("")
    
    if survey_question("Which candidate's background do you think makes them a better fit for this role?", "Candidate A", "Candidate B"):
        bob += 1
        bob_agree.append("Background")
    else:
        erik += 1
        erik_agree.append("Background")

    # Survey question: Hobbies and other activities
    st.text("")
    st.text("")
    st.subheader("What Else The Candidates Are Up To", divider="rainbow")
    bob_other = df.loc[df['Name'] == 'Bob Ooten', 'Other Info'].values[0]
    erik_other = df.loc[df['Name'] == 'Erik Weigand', 'Other Info'].values[0]

    if survey_question("What extra activities do you think make for a better candidate?", bob_other, erik_other):
        bob += 1
        bob_agree.append("Volunteering, Hobbies, etc.")
    else:
        erik += 1
        erik_agree.append("Volunteering, Hobbies, etc.")

    # Survey question: Hotness factor
    st.text("")
    st.text("")
    st.subheader("Candidate Hotness", divider="rainbow")
    image_bob = Path(df.loc[df['Name'] == 'Bob Ooten', 'Image'].values[0])
    image_erik = Path(df.loc[df['Name'] == 'Erik Weigand', 'Image'].values[0])

    colA, colB = st.columns(2)
    with colA:
        st.markdown("**Candidate A**")
        display_image(image_bob)

    with colB:
        st.markdown("**Candidate B**")
        display_image(image_erik)

    if survey_question("Who is hotter?", "Candidate A", "Candidate B"):
        bob += 1
        bob_agree.append("Hotness")
    else:
        erik += 1
        erik_agree.append("Hotness")

    return bob, erik, bob_agree, erik_agree



# Helper function to display candidate information
def display_candidate_info(col, name, colour, party, agree_list):
    # Get candidate info
    df = candidatetable()

    image = df.loc[df['Name'] == name, 'Image'].values[0]
    
    if Path(image).exists():
        col.image(image, width=100)
    
    if party:
        col.markdown(f":{colour}[**{name}**  \n <u>{df.loc[df['Name'] == name, 'Party'].values[0]}</u>  \n {df.loc[df['Name'] == name, 'Descriptor'].values[0]}]", unsafe_allow_html=True)
    else:     
        col.markdown(f":{colour}[**{name}**  \n {df.loc[df['Name'] == name, 'Descriptor'].values[0]}]")
    
    col.write("**You Prefer This Candidate On:**")
    if agree_list:
        for element in agree_list:
            col.write(f"- {element}")
    else:
        col.write("Nothing")



# Function to display results and the summary chart
def results(candidateA, candidateB, A_agree, B_agree, names, party):
    # Calculate percentages
    total = candidateA + candidateB
    if total == 0:
        st.error("Both candidates have 0 votes, cannot compute results.")
        return
    pct_A = candidateA / total
    pct_B = candidateB / total

    # Get candidate info
    df = candidatetable()

    # Create the DataFrame
    df_pct = pd.DataFrame({'Candidate A': [pct_A], 'Candidate B': [pct_B]})

    # Customize colors
    if party:
        colours = ['blue', 'red']
        colourA, colourB = 'blue', 'red'
    else:
        colours = ['tab:green', 'tab:orange']
        colourA, colourB = 'green', 'orange'

    # Create the bar chart
    fig, ax = plt.subplots(figsize=(10, 2))

    # Set the figure and axes face color to be transparent or match the background
    fig.patch.set_facecolor('none')  # Makes the figure background transparent
    ax.set_facecolor('none')  # Makes the axes background transparent

    df_pct.plot(kind='barh', stacked=True, ax=ax, color=colours, legend=False)

    # Hide axes and chart outline
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    for spine in ax.spines.values():
        spine.set_visible(False)

    # Add percentage labels inside the bars
    for i, (A_val, B_val) in enumerate(zip(df_pct['Candidate A'], df_pct['Candidate B'])):
        ax.text(A_val / 2, i, f'{A_val:.0%}', va='center', ha='center', color='white', fontweight='bold')
        ax.text(A_val + B_val / 2, i, f'{B_val:.0%}', va='center', ha='center', color='white', fontweight='bold')

    # Display the results summary
    if st.button("Submit"):
        if candidateA == candidateB:
            st.subheader("It's A Tie")
        elif candidateA > candidateB:
            st.subheader(f"Your Preferred Candidate Is: :{colourA}[{names[0]}]")
        else:
            st.subheader(f"Your Preferred Candidate Is: :{colourB}[{names[1]}]")

        # Display the chart and preferences in columns
        col1, col2, col3 = st.columns([1, 3, 1])

        with col1:
            display_candidate_info(col1, names[0], colourA, party, A_agree)

        with col2:
            st.pyplot(fig)

        with col3:
            display_candidate_info(col3, names[1], colourB, party, B_agree)



# Function to display results and the summary chart
def results3(candidateA, candidateB, candidateC, A_agree, B_agree, C_agree, names):
    # Calculate percentages
    total = candidateA + candidateB + candidateC
    if total == 0:
        st.error("All candidates have 0 votes, cannot compute results.")
        return
    pct_A = candidateA / total
    pct_B = candidateB / total
    pct_C = candidateC / total

    # Get candidate info
    df = candidatetable()

    # Create the DataFrame
    df_pct = pd.DataFrame({'Candidate A': [pct_A], 'Candidate B': [pct_B], 'Candidate C': [pct_C]})

    # Customize colors
    colours = ['tab:orange', 'tab:purple', 'tab:green']
    colourA, colourB, colourC = 'orange', 'violet', 'green'

    # Create the bar chart
    fig, ax = plt.subplots(figsize=(10, 2))
    df_pct.plot(kind='barh', stacked=True, ax=ax, color=colours, legend=False)

    # Hide axes and chart outline
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    for spine in ax.spines.values():
        spine.set_visible(False)

    # Add percentage labels inside the bars
    for i, (A_val, B_val, C_val) in enumerate(zip(df_pct['Candidate A'], df_pct['Candidate B'], df_pct['Candidate C'])):
        ax.text(A_val / 2, i, f'{A_val:.0%}', va='center', ha='center', color='white', fontweight='bold')
        ax.text(A_val + B_val / 2, i, f'{B_val:.0%}', va='center', ha='center', color='white', fontweight='bold')
        ax.text(A_val + B_val + C_val / 2, i, f'{C_val:.0%}', va='center', ha='center', color='white', fontweight='bold')

    # Display the results summary
    if st.button("Submit"):
        if candidateA > candidateB and candidateA > candidateC:
            st.subheader(f"Your Preferred Candidate Is: :{colourA}[{names[0]}]")
        elif candidateB > candidateA and candidateB > candidateC:
            st.subheader(f"Your Preferred Candidate Is: :{colourB}[{names[1]}]")
        elif candidateC > candidateA and candidateC > candidateB:
            st.subheader(f"Your Preferred Candidate Is: :{colourC}[{names[2]}]")
        else:
            st.subheader("It's A Tie")

        # Display the chart 
        st.pyplot(fig)

        # Display the preferences in columns
        col1, col2, col3 = st.columns(3)

        with col1:
            if Path(df.loc[df['Name'] == names[0], 'Image'].values[0]).exists():
                st.image(str(df.loc[df['Name'] == names[0], 'Image'].values[0]), width=100)
            st.markdown(f":{colourA}[**{names[0]}**  \n {df.loc[df['Name'] == names[0], 'Descriptor'].values[0]}]")
                    
            st.write("**You Prefer This Candidate On:**")
            if A_agree:
                for element in A_agree:
                    st.write(f"- {element}")
            else:
                st.write("Nothing")

        with col2:
            if Path(df.loc[df['Name'] == names[1], 'Image'].values[0]).exists():
                st.image(str(df.loc[df['Name'] == names[1], 'Image'].values[0]), width=100)
            st.markdown(f":{colourB}[**{names[1]}**  \n {df.loc[df['Name'] == names[1], 'Descriptor'].values[0]}]")
            
            st.write("**You Prefer This Candidate On:**")
            if B_agree:
                for element in B_agree:
                    st.write(f"- {element}")
            else:
                st.write("Nothing")
        
        with col3:
            if Path(df.loc[df['Name'] == names[2], 'Image'].values[0]).exists():
                st.image(str(df.loc[df['Name'] == names[2], 'Image'].values[0]), width=100)
            st.markdown(f":{colourC}[**{names[2]}**  \n {df.loc[df['Name'] == names[2], 'Descriptor'].values[0]}]")
            
            st.write("**You Prefer This Candidate On:**")
            if C_agree:
                for element in C_agree:
                    st.write(f"- {element}")
            else:
                st.write("Nothing")