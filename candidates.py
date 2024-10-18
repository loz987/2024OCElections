import pandas as pd

# Function to generate the table of info on the different candidates
def candidatetable():
    # Candidate information stored in dictionaries

    # What election they are part of 
    race = {
        "Adam Schiff": "United States Senator",
        "Steve Garvey": "United States Senator",
        "Dave Min": "United States Senator",
        "Scott Baugh": "United States Senator",
        "Josh Newman": "State Senator for 37th District",
        "Steven 'Steve' Choi": "State Senator for 37th District",
        "Cottie Petrie-Norris": "Member of State Assembly for 73rd District",
        "Scotty Peotter": "Member of State Assembly for 73rd District",
        "Amy Peters": "Newport-Mesa Unified School District Governing Board Member, Trustee Area 6",
        "Chris Kretzu": "Newport-Mesa Unified School District Governing Board Member, Trustee Area 6",
        "Krita Weigand": "Newport-Mesa Unified School District Governing Board Member, Trustee Area 6",
        "James Peters": "City of Costa Mesa Mayor",
        "John Stephens": "City of Costa Mesa Mayor",
        "Jeffrey Harlan": "City of Costa Mesa Member, City Council, District 6",
        "Jeff Pettis": "City of Costa Mesa Member, City Council, District 6",
        "Pano Frousakis": "Municipal Water District of Orange County Director, Division 4",
        "Karl W. Seckel": "Municipal Water District of Orange County Director, Division 4",
        "Bob Ooten": "Orange County Water District Director, Division 7, Short Term", 
        "Erik Weigand": "Orange County Water District Director, Division 7, Short Term"
    }

    # Candidate parites
    party = {
        "Adam Schiff": "Democratic Party",
        "Steve Garvey": "Republican Party",
        "Dave Min": "Democratic Party",
        "Scott Baugh": "Republican Party",
        "Josh Newman": "Democratic Party",
        "Steven 'Steve' Choi": "Republican Party",
        "Cottie Petrie-Norris": "Democratic Party",
        "Scotty Peotter": "Republican Party"
    }

    # Candidate descriptions from ballots
    descriptor = {
        "Adam Schiff": "United States Representative",
        "Steve Garvey": "Professional Baseball Representative",
        "Dave Min": "State Senator / Dad",
        "Scott Baugh": "Orange County Business Owner",
        "Josh Newman": "California State Senator",
        "Steven 'Steve' Choi": "Small Businessman / Educator",
        "Cottie Petrie-Norris": "California State Assemblymember",
        "Scotty Peotter": "Architect / Small Businessman",
        "Amy Peters": "Businesswoman / Parent",
        "Chris Kretzu": "Parent / Design Consultant",
        "Krita Weigand": "Governing Board Member, Newport-Mesa Unified School District Trustee, Area 6",
        "James Peters": "Costa Mesa Business Owner",
        "John Stephens": "Mayor / Attorney",
        "Jeffrey Harlan": "City Councilmember / Attorney",
        "Jeff Pettis": "Veterans Health Administrator",
        "Pano Frousakis": "Nonprofit Executive",
        "Karl W. Seckel": "Incumbent",
        "Bob Ooten": "Environmental Engineer",
        "Erik Weigand": "Director, Orange County Water District, Division 7"
    }

    # Candidate education and work experience
    background = {
        "Adam Schiff": 
                "- Attended Stanford University and Harvard Law School.\n"
                "- Served as a federal prosecutor in Los Angeles where they successfully prosecuted a crooked FBI agent turned-Russian spy and started the first federal environmental crimes unit in Los Angeles. \n"
                "- Elected to Congress where they focused on protecting our national security and democracy, fighting for the planet, and creating an economy that works for everyone. \n"
                "- Led the first House impeachment inquiry and served as the lead Manager for the first impeachment trial of President Donald J. Trump, securing the first bipartisan vote ever to impeach a sitting president. \n"
                "- Chairman of the House Intelligence Committee and member of the January 6th Committee, lead author of a landmark package of reforms to prevent future abuses of executive power and reinforce our democratic institutions.",
        "Steve Garvey": 
                "- Earned a BS degree from Michigan State University, where they excelled in both baseball and football. \n"
                "- Played for Dodger and Padres and won World Series Champion and were a 10-time All-Star and National League Most Valuable Player. \n"
                "- Stated a marketing group after baseball. \n"
                "- National Campaign Chairman of the Multiple Sclerosis Society and assists in a variety of causes including the Special Olympics, Juvenile Diabetes, The Blind Children Center, The Sisters of Carondelet, United Way, Ronald McDonald House, Fans for the Cure Prostate Cancer Awareness, the Starlight Foundation, and ALS (Lou Gehrig’s Disease) and holds positions on numerous civic committees and corporate boards.",
        "Dave Min": 
                "- Elected in 2020 to represent OC State Senate District.\n"
                "- Serves as Chair of the Senate Natural Resources and Water Committee and member of many other committees and caucuses.\n"
                "- Was a law professor at UC Irvine and taught and researched business law.\n"
                "- One of the country’s leading experts on banking and housing policy and has testified six times before Congress on these issues.",
        "Scott Baugh": 
                "- Grew up in farming family raising organic alfalfa.\n"
                "- Played baseball and football, serving as Captain of both the JV and Varsity football teams.\n"
                "- While managing the farm, studied at community college, university, and law school.",
        "Josh Newman": 
                "- Majored in History with a focus on 20th Century politics and government at Yale.\n"
                "- Served as an artillery officer in the United States Army.\n"
                "- Work includes local government, public affairs and marketing, film and television production, and Internet media technology.\n"
                "- Founded ArmedForce2Workforce to assist young military veterans get jobs.\n"
                "- Ran for office because of frustration with the lack of progress and support for veterans.\n"
                "- Lives in Fullerton with  three weird but lovable rescue Chihuahuas.",
        "Steven 'Steve' Choi": 
                "- Has a B.A. from Kyung He University in Seoul, South Korea, M.A. in library science from Louisiana State University, and Ph.D. in library and information science from the University of Pittsburgh.\n"
                "- Professional experience includes working as a Peace Corps language instructor and college professor and operating Kumon Math and Reading Centers.\n"
                "- Assumed office as Member of the California State Assembly in 2016 and left office on December 5, 2022.",
        "Cottie Petrie-Norris": 
                "- Double majored in Economics and English from Yale University.\n"
                "- Had a successful career in finance and technology.\n"
                "- Helped build businesses and lead teams at Fortune 500 corporations, small companies and start-ups.\n"
                "- Ran for State Assembly in 2018 because Orange County residents were getting shortchanged by Sacramento.\n"
                "- Has secured millions of dollars in funding for projects in the district and introduced important legislation to combat sea level rise, improve services for veterans and help small businesses.\n"
                "- Passed legislation to make neighborhoods safer, improve schools, protect our environment, and help local veterans and small businesses.",
        "Scotty Peotter": 
                "- Background in architecture and construction.\n"
                "- Was on the Irvine and Newport Planning Commissions.\n"
                "- Got elected to the Newport Beach City Council in 2014.\n"
                "- Survived a recall attempt after criticizing the Supreme Court for getting it wrong when they 'found' a right to same sex marriage in the Constitution.\n"
                "- Got involved in politics when the Irvine city council decided to give special rights to a class of people based on who they sleep with.\n"
                "- Is running because 'When a legislator doesn’t know the difference between a man and a woman, how can you trust them to make any wise decisions on anything?'",
        "Amy Peters": 
                "- Mother of three, businesswoman, former educator, and community advocate.\n"
                "- Graduated from Newport Harbor High School, attended Orange Coast College and earned a BA from the UC Irvine.\n"
                "- Part of a bunch of councils, academic and sports initiatives and programs at a local high school and elementary school.",
        "Chris Kretzu": 
                "- Has two boys and has been volunteers, at school events, on the PTA, etc.\n"
                "- Used to do full-time church work before moving to design and consulting, but still officiate the occasional wedding.",
        "Krita Weigand": 
                "- Current Trustee with the Newport-Mesa Unified School District.\n"
                "- Has an MBA from the USC and currently serves as a National Account Manager for a Fortune 500 company.\n"
                "- Mother to twins who are attending local elementary school.",
        "James Peters": 
                "- 30 years of tax and wealth management experience.",
        "John Stephens": 
                "- Mayor of Costa Mesa since 2021.\n"
                "- Elected to City Council and served on many committees and foundations.\n"
                "- Has a bachelor’s degree in Business Administration and Marketing from Cal Poly Pomona, received his law degree from the UC Davis Law School.\n"
                "- Recognized as a Super Lawyer, Best Lawyers of America, and Top Attorneys in Orange County.",
        "Jeffrey Harlan": 
                "- Degree in environmental design from the University of Pennsylvania and Juris Doctor from Vermont Law School with a focus on environmental and land use law.\n"
                "- Incumbent 6th District Council Member and current City Council Mayor Pro Tem (Leader of the Council).\n"
                "- Served on the Costa Mesa Planning Commission and as a Board Member of the Costa Mesa Community Foundation.\n"
                "- Wrote a weekly column for the La Times Daily Pilot covering civil affairs, urban planning, and local business.\n"
                "- Worked for LA City Attorney's Office in the Environmental Protection Division.",
        "Jeff Pettis": 
                "- Poli Sci degree from University Long Beach, learned nursing at California Baptist University and got a Masters in Science in Nursing Administration.\n"
                "- 'The business world came calling' for him to work as a district sales leader for Frito-Lay followed by working in sales for a major auto group.\n"
                "- Found sales unfulfilling and chose to become a nurse focusing on working in mental health and substance use disorders.\n"
                "- Deputy Chief Mental Health RN at VA hospital.\n"
                "- Ran for City Council in 2020 because of their perceived attach on medical freedom during the pandemic (They did not win that election).",
        "Pano Frousakis": 
                "- Public Works Commissioner in Huntington Beach.\n"
                "- Vice President of Olympiacos CA steering the nonprofit towards becoming a professional soccer franchise.",
        "Karl W. Seckel": 
                "- Incumbent Municipal Water District Director.\n"
                "- 40+ years of professional water experience and expertise.\n"
                "- Appointed to the Metropolitan Water District of Southern California in 2023.\n"
                "- Has worked with the Water Emergency Response Organization for OC.",
        "Bob Ooten": 
                "- Degree in Civil Engineering.\n"
                "- 25 years experience as a civil engineer in water/wastewater collections.\n"
                "- 40 years experience in planning, design, and construction of sewers and wastewater systems.\n"
                "- Collaborated on OC Sanitation feasibility study of developing a dependable water supply from wastewater.",
        "Erik Weigand": 
                    "- Degree in Criminal Justice.\n"
                    "- Over two decades of legislative, political, and public policy experience.\n"
                    "- Worked on Presidential, Gubernatorial, and Congressional campaigns throughout the country."
    }

    # All candidate policies
    policy_all = {
        "Josh Newman": 
                "- Supports election reforms for less confusing ballots, more candidate transparency, extending the signature verification period, mandating that candidates follow electoral guidelines, and removing antiquated instructions that appear on the ballot.\n"
                "- Wants to ensure all K-8 pupils in California have access to a minimum standard of recess, and encourages Mathematics, Engineering, and Science Achievement (MESA) Programs, wants to require schools to offer halal and kosher meals in diverse communities.\n"
                "- Wants to make recycling more efficient, supports rebates for hydrogen fuel cell vehicles and restoration and climate resiliency along the California Coast.\n"
                "- Wants to improve public transport.\n",
        "Steven 'Steve' Choi": 
                "- (Does not appear have website or easy way to figure out any proposed policy, only has a couple low quality photos online. Man of mystery.)",
        "Amy Peters": 
                "- Improve academic outcomes while advocating for the removal of controversial programming and materials in schools.\n"
                "- Manage budget prioritizing classroom-based student achievement.\n"
                "- Ensure that transparent and responsive governance and leadership with respect to parent rights is prioritized.\n"
                "- Create a safe learning environment by auditing security, policy and practice.\n"
                "- Retain talent by respecting educators and strengthening trust.",
        "Chris Kretzu": 
                "- Better communication of phone-free policy with parents and enforcement on campus.\n"
                "- Increase bicycle safety by clarifying laws around e-bikes, doubling down on bicycle lanes, and educating students and parents.\n"
                "- Provide better support and programming for students moving from 6th to 7th grade.\n"
                "- Continue to expand on math proficiency as well as readiness for creative careers.\n"
                "- Fight for healthier education systems without disparaging and discouraging teachers and administrators.",
        "Krita Weigand": 
                "- Keep students safe.\n"
                "- Promote a well-balanced education including quality curriculum, access to the latest technology and limited class size.\n"
                "- Provide students with a world-class education to advance them to college, a vocational profession, or the military.\n"
                "- Increase opportunities for art, music, and vocational education.\n"
                "- Ensure financial accountability that protects all taxpayers.\n"
                "- Put a stop to new bonds and parcel taxes.\n"
                "- Hire the best and brightest teachers to guide our students to success.\n"
                "- Guarantee that decisions are not made behind closed doors and that the public is included every step of the way.",
        "Pano Frousakis": 
                "- Boost water quality and safety by implementing rigorous water quality monitoring and reporting as well as upgrading filtration and treatment facilities to ensure top-tier water safety.\n"
                "- Improve water supply reliability.\n"
                "- Strengthen emergency preparedness.\n"
                "- Enhance regulatory efficiency.\n"
                "- Optimize fiscal management.\n"
                "- Advocate for sustainable and responsible water management.\n"
                "- Prioritize the needs of water ratepayers, ensuring affordable water bills.",
        "Karl W. Seckel":
                "- Using water efficiently should be our way of life!\n"
                "- Dealing with climate change and planning for our future needs to be adaptive and cognizant of possible precipitation changes.\n"
                "- On-going investments are needed in water supply and water system reliability because many facilities are aging and need to be repaired.\n"
                "- More flexibility is needed to export stormflows during wet periods and cutback export of water during dry periods to help endangered fish, food production, and fisheries.\n"
                "- Balance needs to be brought among the states that share the Colorado River because water supplies have been over-allocated beyond what Mother Nature provides.\n"
                "- Water managers must be good stewards of the public resources and of the ratepayer's funds."
    }

    # Candidate reporductive rights policies
    policy_healthcare = {
        "Adam Schiff": 
                "-	Authored a patient bill of rights to provide patients recourse when health insurance companies deny them the medical care they need.\n"
                "-	Secured federal funding to improve and expand health care including boosting access to mental health care including telehealth services, upgrades to health care facilities, and investments for first responder services.\n"
                "-	Helped pass act which lowered the cost of certain prescription drugs for seniors on Medicare.\n"
                "-	Advocated for the expansion of Medi-Cal to ensure low-income children and families, expectant mothers, and people with disabilities have free or low-cost quality health care.\n"
                "-	Voted to codify Roe v. Wade into law, protect abortion access nationwide, and ensure access to contraception and other reproductive health care.\n"
                "-	Fighting for the passage of the Medicare for All Act and full implementation of the landmark Affordable Care Act.",
        "Steve Garvey": 
                "-	Work to reduce the cost of health care by increasing competition, cutting bureaucracy, and promoting transparency in pricing.\n"
                "-	Ensure that all Americans have access to affordable, quality health care, including rural and underserved communities.\n"
                "-	Protect the right of individuals and families to choose the health care plan and providers that work best for them, including private insurance options.\n"
                "-	Encourage the development of new treatments and technologies by reducing regulatory barriers and incentivizing research.\n"
                "-	Prioritize mental health services and addiction treatment as key components of a comprehensive health care system.\n"
                "-	Reform Medicare and Medicaid to ensure long-term sustainability while protecting benefits for seniors and low-income Americans.\n"
                "-	Stand against proposals like Medicare for All that eliminate choice and put the government in control of health care decisions.\n",
        "Cottie Petrie-Norris": 
                "- Fight for reproductive rights and ensuring access to abortion care and birth control for California women.\n"
                "- Support abortion rights and medical privacy, protect access to birth control and contraceptives, improve access to contraception by expanding telehealth, and expand childcare and family leave from working parents.",
        "Scotty Peotter": 
                "- No taxpayer funding of abortions.\n"
                "- No late term abortions.\n"
                "- No abortions based on sex selection.\n"
                "- Allow abortion if the mother’s life is in danger because of the pregnancy or a pregnancy from rape or incest.\n"
    }

    # Candidate education policies
    policy_education = {
        "Adam Schiff": 
                "-	Advocate of early investments in childhood education and universal expansion of pre-K.\n"
                "-	Helped deliver federal funding for Early Head Start programs ensuring that children were healthy and ready for school.\n"
                "-	Secured federal funds for youth development including education technology and workforce development in his district.\n"
                "-	Authored legislation guaranteeing funding for up-to-date textbooks and reduced class sizes.\n"
                "-	Secured critical cost-of-living increases for teacher pensions.\n"
                "-	Supports canceling at least $50,000 in student loan debt for every borrower.\n"
                "-	Fights to expand Pell Grant funding to boost college access for low-income students.\n"
                "-	Make public college free for Californians.",
        "Steve Garvey": 
                "-	Ensure schools are teaching the math, reading, science, and critical thinking.\n"
                "-	Ensure state and federal education dollars are directed to classrooms, not lost in bureaucratic overhead.\n"
                "-	Support parents choosing the schooling options that best suits their child’s needs including federal funding for for-profit private charter schools.\n"
                "-	Reduce costs of higher education, ensuring affordability for students and their families without compromising quality.\n"
                "-	Encourage universities and community colleges to prioritize degrees and programs that lead directly to good-paying jobs in growing industries.\n"
                "-	Expand access to trades and apprenticeships and expand Pell Grants to pay for short-term skills-based training providing access to more low-skilled workers.\n"
                "-	Ensure that colleges and universities are transparent about outcomes, including graduation rates and job placement, so students and families can make informed decisions.\n"
                "-	Advocate for practical solutions to alleviate the student debt burden, including exploring income-based repayment options and financial literacy education.",
        "Cottie Petrie-Norris": 
                "- Prioritized improving education outcomes for OC students.\n"
                "- Expanded free preschool enrollment, boosted UC & CSU enrollment, and provided millions in additional funding for local schools.\n"
                "- Focused on making smart investments in STEM education and workforce development programs to prepare workers for the job of tomorrow.",
        "Scotty Peotter": 
                "- Kids are having their innocence stolen and being indoctrinating.\n"
                "- Reading, writing or arithmetic is not being taught but instead some kids have 2 mommies and Drag Queen Story Hour is being taught.\n"
                "- Kids to transition to the opposite sex without parental consent or knowledge.\n"
                "- Will fight for schools to educate children and teach critical thinking skills, not indoctrinate or sexualize children.\n"
                "- The answer is school choice where parents choose between Public, Charter, Private or home school and state tax money for education should follow the student.\n"
                "- Will fight for all colleges to grant admittance based on merit not your skin color and is against DEI and affirmative action."

    }

    # Candidate economic policies
    policy_economy = {
        "Adam Schiff": 
                "- Expanded unemployment insurance for contractors and freelancers. \n"
                "-	Led efforts to raise minimum wage to $15 an hour. \n"
                "-	Voted against efforts to undercut overtime pay. \n"
                "-	Fought to protect pregnant workers and LGBTQ workers from discrimination. \n"
                "-	Pushed for act to ensure women earn equal pay. \n"
                "-	Backed legislation to help small businesses stay open during the pandemic. \n"
                "-	Protect and strengthen the right to organize and supports union workers and picket lines. \n"
                "-	Beef up antitrust enforcement and implementing a set of price-gouging regulations to bring down prices. \n"
                "-	Rein in or prohibit corporate use of stock buybacks to inflate share values.\n"
                "-	Ban non-compete, non-solicit, no-poaching agreements, and eliminate rules preventing workers from suing employers for violations.",
        "Steve Garvey": 
                "-	Streamline federal regulations to make it easier to start and grow businesses.\n"
                "-	Get the federal budget under control to maintain low inflation.\n"
                "-	Address high costs of food, energy, interest rates.\n"
                "-	Cut federal regulations to emphasize free market control, spending, and reduce unnecessary mandates that drive up costs.\n"
                "-	Confirm judges that will not allow bureaucrats do expand their regulatory authority.\n"
                "-	The Federal Reserve must make clear to markets that it will maintain its two percent inflation target and commit itself to reducing its balance sheet (congress does not control the Fed so not sure how they plan to make them do this).\n"
                "-	Ensure federal spending is controlled and targeted, by returning government spending to the January 2020 baseline.\n"
                "-	Cut unnecessary government programs and eliminate inefficiencies that lead to overspending.\n"
                "-	Push for balanced budgets submitted on time that prioritize key investments while reducing the national debt for future generations.\n"
                "-	Focus spending on critical areas like infrastructure, national security, and education—while eliminating reckless expenditures.\n"
                "-	Ensure that government growth is kept in check, supporting a leaner, more effective federal system.",
        "Dave Min": 
                "- Authored bill provided billions in grant relief funding statewide, with millions more distributed to more than 5,000 local small businesses, helping them to survive during the pandemic.\n"
                "- Coauthored a bill allowing businesses who received Paycheck Protection Program (PPP) assistance not to have the income taxed by the state.",
        "Scott Baugh": 
                "- Supports a Balanced Budget Amendment requiring Congress to respect taxpayers, prioritize spending, and balance a budget each year.\n"
                "- Will oppose any new tax because it is time for government to begin respecting those who pay taxes by requiring government to live within its means rather than continually tapping into its people for new revenue.\n"
                "- Believes it is time to roll back gas taxes and finally provide some relief from the increasing inflation and cost of goods and services.",
        "Cottie Petrie-Norris": 
                "- Strong advocate for protecting taxpayers, helping businesses grow and responsibly manage tax dollars.\n"
                "- Received OC Taxpayers Association Award for fiscally responsible leadership.",
        "Scotty Peotter": 
                "- Believes government is the problem for high costs and is killing the economy through regulation and overspending."
    }

    # Candidate gun policies
    policy_guns = {
        "Cottie Petrie-Norris": 
                "- Fighting for a solution to gun violence and keep communities safe by securing additional funding for the Disarming Prohibited Persons Taskforce program and co-authored legislation to improve systems for seizing illegal weapons and to keep guns out of hands of dangerous criminals.",
        "Scotty Peotter": 
                "- Will fight to protect the constitutional right to own firearms."
    }

    policy_taxes = {
        "Adam Schiff": 
                "-	Opposed tax giveaway to the wealthy and large corporations.\n"
                "-	Increase taxes on corporate profits by returning the corporate tax rate to 35% and make sure corporations cannot evade taxes through tactics like offshoring profits and onshoring debt to eliminate their taxable income.\n"
                "-	Fully fund the IRS to go after tax cheats. Increasing the IRS’s budget would allow them to hire more auditors and train their workforce better to ensure that wealthy individuals pay their fair share and cannot evade taxes.\n"
                "-	Middle class tax cut and restore the State and Local Tax Deduction for families making less than $400,000.",
        "Steve Garvey": 
                "-	Support tax cuts for middle-class families to help alleviate the financial burden and boost the economy.\n"
                "-	Streamline and simplify the tax code to make it easier for families and businesses to understand and comply, reducing costly loopholes.\n"
                "-	Provide tax incentives for small businesses to invest, expand, and create jobs in local communities.\n"
                "-	Ensure that taxes are fair, with everyone paying their fair share while protecting middle- and working-class families from undue burden.\n"
                "-	Oppose tax hikes that fund unnecessary government growth, and focus instead on creating a more efficient, responsible federal budget.",
    }

    policy_housing = {
        "Adam Schiff": 
                "- Need to build more housing that’s affordable – and fast.\n"
                "-	High costs of development for affordable housing, drawn out timelines, complex local zoning laws, and resistant attitudes towards high-density housing have all contributed to the housing crisis.\n"
                "-	Create federal low-interest loans for multifamily housing construction and convert unused federal and state government buildings and land into housing.\n"
                "-	Make homebuilding faster, cheaper and safer.\n"
                "-	Expand the Low-Income Housing Tax Credit (LIHTC) program, make low-income housing entitlement, and create incentives for landlords who accept tenants in housing voucher programs.\n"
                "-	Create a federal renter’s tax credit, create a federal fund for tenant’s rights organizing and legal action, and create a federal office of eviction protection.\n"
                "-	Building positive credit scores through renting.\n"
                "-	Create a nationwide down payment assistance program for low-income homebuyers.\n"
                "-	Place restrictions on corporate and private equity landlords.\n"
                "-	Fund pilot programs for nonprofits that lease land and sell homes at a low price for moderate income community members.\n"
                "-	Protect homeowners from environmental financial catastrophes.\n",
        "Steve Garvey": 
                "-	The cost of building a home has increased due to inflation and costly regulations.\n"
                "-	Mortgage rates have soared, doubling the cost of monthly payments for families.\n"
                "-	Federal, state, and local regulations make up nearly 20% of the cost of a home. A moratorium on new regulations—other than for safety—is needed to streamline the building process.\n"
                "-	New energy standards and regulations are increasing the cost of a new home and should be repealed. \n"
                "-	Advocate for more disciplined government spending to reduce inflation and bring down interest rates.\n"
                "-	Provide tax benefits to builders who focus on producing entry-level homes for first-time buyers.\n"
                "-	Offer incentives to communities (without mandates) to adjust zoning restrictions that make it difficult to build affordable housing.",
    }

    # Candidate honelessness policies
    policy_homelessness = {
        "Adam Schiff": 
                "-	Adopt a wraparound approach to address homelessness including housing subsidies that make housing affordable, adopt of the evidence-based practice of housing first, healthcare, research to improve operations/implementation efforts, address social needs, increase access to transportation and employment opportunities, develop a peer support model for homeless programs, integrate legal aid with medical care, and  focus on community integration.\n"
                "-	Creating a national housing strategy and increase federal funding for people experiencing homelessness and the affordable housing shortage.\n"
                "-	Address the root causes of homelessness and housing availability.\n"
                "-	Invest in housing choice vouchers, project-based rental assistance, and continuums of care to address the homelessness crisis.\n"
                '-	Federal investment in the eviction protection program, mobile crisis intervention teams, and hotel conversions to permanent supportive housing.\n'
                "-	Provide direct housing guidance to people experiencing homelessness.\n"
                "-	Expand access to occupational licensing for long-term career opportunities.",
        "Steve Garvey": 
                "-	Audit where the money allocated for dealing with homelessness is going.\n"
                "-	Partner with private organizations, including faith-based organizations, to develop effective solutions.\n"
                "-	Judges handcuffed local government’s ability to ensure public safety by ruling that it was unconstitutional to enforce the bans on camping or sleeping in public.\n"
                "-	Enforce laws because the criminal justice reforms intending to reduce the state’s incarcerated population have likely exacerbated the homelessness problem.",
        "Cottie Petrie-Norris":
                "- Reduce homelessness, ensure adequate supply of affordable housing, and fix the state's broken mental healthcare and support services.\n"
                "- Supported providing millions in new funding for local cities to address the homelessness crisis , and to end veterans homelessness.",
        "Scotty Peotter":
                "- Does not agree that you must provide a roof before you can successfully help the homeless.\n"
                "- The underlying problem of drug and alcohol addiction and mental illness must be addressed before you can help them out of homelessness.\n"
                "- Non-profits, like the Rescue Mission have had the best and highest success rates. (This seems like a very Jesus-y org)",
        "James Peters": 
                "- Develop comprehensive support programs.\n"
                "- Collaborate with local organizations to provide housing solutions.",
        "John Stephens": 
                "- Opened a temporary and permanent shelter facilities, found permanent housing for individuals, and obtained millions in funding to convert a motel into units of permanent supportive housing for those at risk of homelessness, veterans, and seniors.\n"
                "- Reestablished anti-encampment ordinances through a Federal Court order, to keep our parks and public spaces free of encampments.",
        "Jeffrey Harlan": 
                "- Tackle homelessness by opening shelters and championing housing initiatives.",
        "Jeff Pettis": 
                "- Approach the homelessness crisis with a plan of going after the issues that lead to homelessness (economic instability, substance abuse and mental illness) along with an effort to support housing because the current city plan directing millions of taxpayer dollars toward new construction of housing for the homeless is shortsighted.."
    }

    # Candidate public safety policies
    policy_safety = {
        "Adam Schiff": 
                "-	Worked to root out corruption, improve public safety, and reform our criminal justice system.\n"
                "-	Ushered in law providing funding to curb crime among at-risk youth and young offenders and passed legislation to protect children from online predators and to assist law enforcement in solving difficult murder cases.\n"
                "-	Secured federal funding to create a DNA lab to improve the processing of DNA evidence and take violent offenders off the eliminate the rape-kit backlog in Los Angeles, give more tools to county welfare departments to protect foster children, and strengthened protections for domestic violence victims.\n"
                "-	Increase the number of justices on the Supreme Court from 9 to 13, so that new Justices can be appointed who would restore balance to the Court.\n"
                "-	Set reasonable term limits for Supreme Court justices (18 years) while establishing a better process for Supreme Court appointments.\n"
                "-	Restore the court’s integrity by strengthening the ethics requirements for Justices and establishing an enforceable code of ethics for all Justices.\n"
                "-	Stop the active trading of individual stocks by all judges and help ensure that federal judges and justices are making decisions based on the law and not because of any financial interest.",
        "Steve Garvey": 
                "-	Protect our southern border by providing more resources and support for border patrol agents, ensure asylum seekers remain in Mexico while their claims are processed and prevent illegal immigrants from being released into U.S. communities without proper legal proceedings.\n"
                "-	Fix immigration law to allow DHS to ban asylum claims for those entering unlawfully.\n"
                "-	Immigration reform must include an overhaul in the nation’s legal immigration system and address the legal status of those here unlawfully.\n"
                "-	Reducing penalties for serious offenses has led to a surge in crime and tougher sentences should be enforced.\n"
                "-	Ensure law enforcement has the training, equipment, and education needed to protect our communities.\n"
                "-	Hold prosecutors accountable and ensure existing laws are enforced and thinks justice reforms may be necessary to ensure fairness.",
        "Dave Min": 
                "- Passed bills protecting domestic violence survivors and foster youth from debts coerced by their abusers, codifying that Domestic Violence Restraining Orders may be renewed as many times as necessary, expanding the scope of Domestic Violence Review Teams, protections for victims of reproductive coercion, and defending the rights of children in custody battles.\n"
                "- Partnered with Stop AAPI Hate and LA Metro to introduce data-driven safety solutions to increase transport ridership and put a stop to street harassment.\n"
                "- Founded the Senate Select Committee on Cybersecurity.\n"
                "- Has worked hard to explore solutions and best practices for how the state can aggressively address cybersecurity, identity theft, digital privacy, and other emerging threats to data security.\n"
                "- Helped secure the passage of the historic AAPI Equity Budget addressing racial inequities, providing services to victims of hate crimes, and funds prevention efforts designed to keep all Californians safe.",
        "Scott Baugh": 
                "- Wants to secure border to keep human traffickers, drug dealers, and violent criminals out of the country.\n"
                "- Wants to overhaul our legal immigration system to simplify and expedite our legal immigration system.\n"
                "- Supports federal legislation to guarantee victims of crime rights equal to those accused and convicted of crimes because they believes far-left legislators are tilting the scales of justice in favor of criminals.\n"
                "- Believes in funding law enforcement agencies effectively, effective and consistent training of officers, and standing with the men and women of law enforcement whenever they are under attack – by criminals, rioters, or politicians.\n" 
                "- Believes that those in Congress should be required to follow the laws they pass (pretty sure they are already supposed to be following the law).",
        "Cottie Petrie-Norris": 
                "- Supported by firefighters and police because they fight for safe neighbourhoods and have fast emergency response times.",
        "Scotty Peotter": 
                "- Believes 'illegal aliens are being given free healthcare while citizens are fined and punished if they do not have healthcare coverage.\n"
                "- Believes the democrats are allowing Human Trafficking and modern-day Slavery to continue and prosper.\n"
                "- 'Enemies have been crossing, unchecked. Thousands of military age men from China have crossed. Who knows how many terrorists are crossing.'",
        "James Peters": 
                "- Implement stronger community policing strategies.\n"
                "- Increase resources for law enforcement.",
        "John Stephens": 
                "- Enacted, implemented, and defended reasonable regulations on Sober Living Homes.\n"
                "- Sued the Federal and State governments to prevent early Covid-19 patients from being relocated to Costa Mesa.\n"
                "- Hired a Police Chief who has served as the President of the California Police Chiefs Association.\n"
                "- Funded millions to remodel Police and Fire training facilities and upgrade two Fire Stations to state-of-the-art.\n"
                "- Increased sworn police officers, including adding a sergeant to protect retail stores, and restored and reinforced special units such as the gang, narcotics, canine, and community policing.",
        "Jeffrey Harlan": 
                "- Ensure public safety & reduce crime by increasing staff levels for fire and police departments..\n"
                "- Create safer streets for cyclists & pedestrians by reducing speeding in neighbourhoods, improving pedestrian crossings, and bike lanes.",
        "Jeff Pettis": 
                "- Stands with police and is anti 'defund the police' but thinks individual officers should have consequences for wrongdoing."
    }

    # Candidate climate policies
    policy_climate = {
        "Adam Schiff": 
                "-	Co-sponsor of the Green New Deal pushing for renewable energy policies that keep energy prices low, make America energy independent, and dramatically develop and expand clean energy technologies and jobs. \n"
                "-	Sped up testing for chromium-6 in local drinking water and want to provide robust funding for lead pipe replacement. \n"
                "-	Worked on expanding Metro light rail across Southern California.\n"
                "-	Ushered into law an act to expand the Santa Monica Mountains National Recreation Area. \n"
                "-	Opposes oil and gas drilling off the coast of California and votes against efforts that weaken environmental protections and harm progress on climate action. \n"
                "-	End federal subsidies for fossil fuel production and lower gas prices by suspending the gas tax and making oil companies pay for it instead. \n"
                "-	Increase federal support for clean energy innovation and tech innovator hubs.\n"
                "-	Increase grid resiliency through community-level microgrids. \n"
                "-	Address price gouging in the energy market. \n"
                "-	Set an ambitious decarbonization date for the aviation sector and make shipping greener. \n"
                "-	Pass bills which will prioritize community forestry assistance in areas that lack green spaces and create a pilot grant program to create urban gardens at schools.  \n"
                "-	Address aging water infrastructure and increase water capture. \n"
                "-	Increase investments in co-stewardship of National Forests for prescribed burns. \n"
                "-	Invest in firefighter protection & address long term health risks. \n"
                "-	Create incentives for U.S. Forest Service jobs and wildland federal firefighters. \n"
                "-	Adjust the permitting process for oil rigs to hold polluters accountable and hold companies accountable for PFAS contamination. \n"
                "-	Increase federal funding for oil and gas site reclamation. \n"
                "-	Prohibit oil and gas leasing off the coast of California. \n"
                "-	Preserve our natural lands, expand national monuments, and protect more of California. \n"
                "-	Protect and preserve our kelp forests.",
        "Steve Garvey":
                "-	Ensure a transparent, gradual transition to renewable energy sources that protects jobs and the economy.\n"
                "-	Streamline federal permitting process for energy projects to ensure regulators cannot stymie new energy projects and codify rules that prevent bureaucrats from abusing environmental regulations to stop vital energy and infrastructure projects.\n"
                "-	The National Environmental Policy Act, the Clean Air Act, the Clean Water Act, and the Endangered Species Act have resulted in higher energy prices and that that is the goal of Washington.\n"
                "-	Energy tax credits were a giveaway to corporations and interest groups and that the tax credits need to be reformed to cap the expense for new projects.\n"
                "-	Increase leases for drilling on federal lands to lower fuel prices.\n"
                "-	Prioritize infrastructure projects to improve water storage, delivery, and recycling, ensuring California has a reliable water supply even during droughts.\n"
                "-	Invest in technologies and policies that support water efficiency and availability for farmers and ranchers.\n"
                "-	Balance conservation and growth by encouraging responsible water use while supporting policies that allow communities and industries to grow sustainably.\n"
                "-	Work to eliminate excessive regulations that restrict water access and innovation.\n"
                "-	Promote research and development in desalination, groundwater replenishment, and other advanced water technologies to address long-term water security.",
        "Dave Min":
                "- Wants to work to address the climate crisis with urgency and bold action.\n"
                "- Introducing legislation to ban offshore oil drilling in state waters.\n"
                "- Helped secure funding for the protection of Banning Ranch, California’s largest, unprotected wetlands habitat.\n"
                "- Has held over a dozen beach cleanups and community service events aimed at protecting our local environment.", 
        "Scott Baugh":
                "- Opposes any new offshore drilling initiatives, recognizing the potential environmental risks such activities pose to marine ecosystems, coastal tourism, and local economies."
    }

    # Candidate development policies
    policy_develop = {
        "Jeffrey Harlan":
                "- Preserve the charm & enhance the Eastside Neighbourhoods by directing future growth to the north and along existing commercial corridors.\n"
                "- Plans for smart growth citywide by locating housing near existing jobs, investing in affordable housing, expanding transportation, and reducing environmental impacts.",
        "Jeff Pettis":
                "- Encourage smart development that prioritizes the consensus of the constituency because the current city leadership sides too often with developers on high-density housing and rezoning."
    }

    # Candidate other policies that didnt fit in a category with their opponent 
    policy_other = {
        "Adam Schiff": 
                "-	Support abolishing the Electoral College and expanding the multi-state compact in which states agree that whoever wins the national popular vote will earn all of their state’s electoral votes.\n"
                "-	Led efforts to reform campaign finance laws by cracked down on corporations and foreign organizations spending to influence elections.\n"
                "-	Author of a constitutional amendment to overturn Citizens United which would limit the influence of corporate special interest groups.\n"
                "-	Advocates for abolishing the filibuster, ending partisan gerrymandering, removing barriers to voting by making Election Day a federal holiday, expanding automatic voter registration and early voting, and preventing future abuses of executive power with stronger checks and balances.\n"
                "-	Support families though paid family and parental leave, funds care for elderly and sick, universal childcare, expanding the child tax credit and make it permanent.\n"
                "-	Support low income people through, pilot guaranteed income programs grant, expanding and strengthen social security, expanding eligibility and funding for snap benefits, and expanding Medicaid eligibility.",
        "Steve Garvey": 
                "-	Ensure our military remains the most powerful in the world by focusing on readiness, training, and advanced equipment.\n"
                "-	Ensure that funds are defence spent efficiently and effectively, maximizing value and eliminating waste.\n"
                "-	Prioritize investment in cutting-edge technologies to maintain our military advantage in the face of emerging threats, such as the use of low-cost drones against high-value assets.\n"
                "-	Advocate for a strong foreign policy that projects firmness, not weakness, and protects America’s interests abroad.\n"
                "-	Ensure our defense strategy evolves to meet modern threats, focusing on cybersecurity, space defense, and new forms of warfare.\n"
                "-	Will consider additional funding if it is justified and properly allocated by the Department of Defense.\n"
                "-	The U.S. needs to reinvest its naval fleet, modernize its nuclear force, and expand domestic manufacturing of munitions and other arms and reforms are needed to the Pentagon’s procurement process.\n"
                "-	Reform an overly bureaucratic and cumbersome hiring process that makes it difficult for the government to hire and retain cybersecurity experts.",
        "Dave Min": 
                "- Introduced bill to ban gun shows at the Orange County Fairgrounds.\n"
                "- Wrote a bill that ultimately ended the sale of firearms and ammunition on all state property.\n"
                "- Worked to pass a bill which requiring licensed firearms dealers to reform antiquated policies by carrying liability insurance and having onsite surveillance."
                "- Defended language access at the Department of Motor Vehicles and the state’s Responsible Beverage Service (RBS) Training Program.\n"
                "- Piloted historic state investments in our public schools, community colleges and universities.\n"
                "- Worked to safely and quickly reopen schools during the pandemic, expand early childhood education, tackled food insecurity among school children, address Covid-related learning loss, and increase enrollment to University of California.\n"
                "- Stepped up to enshrine abortion rights in our state’s constitution and is fighting to end discriminatory practices against LGBTQ+ patients and reproductive services on the basis of religious beliefs.",
        "Scott Baugh": 
                "- Supports legislation that would ban everyone in Congress from individual stock trading.\n"
                "- Will sponsor legislation to increase penalties for those who peddle fentanyl and other hard drugs.\n"
                "- Will support efforts to help make sure those battling addiction have resources available, so they are not fighting alone.\n"
                "- (Notably absent any mention of education, abortion or gun policy)",
        "Cottie Petrie-Norris": 
                "- Wrote and passes a law protecting coastlines from the rise of sea levels.\n"
                "- Fighting to protect clean air standards and carbon emissions regulations.\n"
                "- Led efforts to prevent, combat, and recover from wildfires.\n"
                "- Fought for additional investment in technology to detect fires, supported funding for firefighting equipment, co-authored legislation to compensate firefighters injured on-duty, secured funding to improve infrastructure to prevent fires.",
        "Scotty Peotter": 
                "- Wants to pass a 'LET THE GIRLS BE GIRLS AND THE BOYS BE BOYS Act' requiring students to use bathrooms and play sports based on their God-given sex.\n"
                "- The schools will not participate nor teach that gender can be changed or that it is separate from your biological sex.\n"
                "- No more tampon machines in the boy’s bathrooms.",
        "James Peters": 
                "- Promote sustainable development practices, protect green spaces, and maintaining the city's character.\n"
                "- Help ensure that if another 2020 event occurs, all families will retain their freedom to go to the park, groceries store, church and work.\n"
                "- Reevaluate zoning by laws and regulations to deal with high concentration of pot shops to considers community concerns.",
        "John Stephens": 
                "- Secured funding for small business grants to keep businesses open in partnership with the Small Business Administration and the Chamber of Commerce.\n"
                "- Passed ordinances allowing outside use at restaurants and retail shops.\n"
                "- Established a Recovery Team with local business owners, non-profits, and other agencies to accelerate recovery from the pandemic.\n"
                "- Worked with the State to develop affordable housing and developing a first-time home buyer's program using cannabis tax revenue.\n"
                "- Invested millions in Active Transportation projects, including protected bike lanes, and Electric Vehicle charging stations.",
        "Jeffrey Harlan": 
                "- Invest in Costa Mesa by exploring ways to keep existing businesses growing, recruiting new ventures, additional revenue streams for the city, and invest in neighbourhoods. \n" 
                "- Protect the environment by installing EV charging stations, providing an electric shuttle bus for the senior center, voting to upgrade to energy efficient streetlights..\n" 
                "- Reimagine public spaces by improving local parks, streetscapes and support sustainability, walkability and bikeability.",
        "Jeff Pettis": 
                "- Costa Mesa City Hall is 'drunk on Federal Covid relief money' and needs long-term financial planning and sustainability, avoiding short-term fixes. \n" 
                "- Address unfunded liabilities such as pension reform and making wise infrastructure investments to maximize taxpayer returns. \n"
                "- Promote fiscal discipline, accountability, and transparency in spending while fostering an environment conductive to economic prosperity for residents.\n"

    }

    # Candidate endorsements
    endorsements = {
        "Cottie Petrie-Norris": 
                "An assortment of police, firefighters, women's associations, teaches association, etc.",
        "Scotty Peotter": 
                "California Republican Assembly, California Riffle and Pistol Association, various politicians, etc.",
        "Jeffrey Harlan": 
                "An assortment of Costa Mesa firefighters and police, teachers, truckers, carpenters, and various politicians (50% of them are women).",
        "Jeff Pettis": 
                "An assortment of republican organizationa, OC Gun Owners, California Rifle & Pistol Association, and various politicians (all old white men).",
        "Pano Frousakis": 
                "An assortment of republican politicians and organizations, radio hosts, Huntington Beach Council Members, and soccer organizations.",
        "Karl W. Seckel": 
                "An assortment of other water district directors (like a lot of them), and  Council Members"
    }

    # Other candidate info
    other_info = {
        "Cottie Petrie-Norris": 
                "Has a weirdly extensive photo galley of pics of themself.",
        "Scotty Peotter":
                 "Website is called Taxfighter.com and has a page about choosing them over the other candidate (it is full of lies and insanity).",
        "Amy Peters": 
                "No other info provided",
        "Chris Kretzu": 
                "Enjoys riding bikes with the family and locally-owned restaurants and coffee shops.",
        "Krita Weigand": 
                "Endorsements include OC Sheriff, the republican US congress candidate, Newport Beach Police Association, Newport Beach Mayor, other politicians and parents.",
        "James Peters": 
                "- Coaches baseball.",
        "John Stephens": 
                "- Initiated the City’s Independence Day Celebration and has been Santa Claus at Snoopy House for the past six years.\n"
                "- Coached baseball, softball, and basketball.\n"
                "- Is an avid golfer and karaoke enthusiast.",
        "Jeffrey Harlan": 
                "- Tennis player, golfer, yoga enthusiast, and hiker.\n"
                "- Mentor in Newport Harbour High School's program for juniors interested in various career paths.",
        "Jeff Pettis": 
                "- Quotes Marcus Aurelius in his webpage (I guess the roman empire is his roman empire).",
        "Pano Frousakis": 
                "- Committed to fostering community engagement and promoting organizational excellence\n"
                "- Dedicates time to youth sports programs for children with special needs and autism",
        "Karl W. Seckel": 
                "No mention of what they do other than water-related work",
        "Bob Ooten": 
                "Volunteers in the Senior Center, Friends of the Library Book Store, Friends of Fairview Park, and the Lions Club",
        "Erik Weigand": 
                "Participated in OC fair demolition derby for charity, former Newport Beach Junior Lifeguard."
    }

    # Candidate photos
    images = {
        "Adam Schiff": "CandidatePics/adam.png",
        "Steve Garvey": "CandidatePics/steve.png",
        "Dave Min": "CandidatePics/dave.png",
        "Scott Baugh": "CandidatePics/scott.png",
        "Josh Newman": "CandidatePics/josh.png",
        "Steven 'Steve' Choi": "CandidatePics/steven.png",
        "Cottie Petrie-Norris": "CandidatePics/cottie.png",
        "Scotty Peotter": "CandidatePics/scotty.png",
        "Amy Peters": "CandidatePics/amy.png",
        "Chris Kretzu": "CandidatePics/chris.png",
        "Krita Weigand": "CandidatePics/krita.png",
        "James Peters": "CandidatePics/james.png",
        "John Stephens": "CandidatePics/john.png",
        "Jeffrey Harlan": "CandidatePics/jeffH.png",
        "Jeff Pettis": "CandidatePics/jeffP.png",
        "Pano Frousakis": "CandidatePics/pano.png",
        "Karl W. Seckel": "CandidatePics/karl.png",
        "Bob Ooten": "CandidatePics/bob.png",
        "Erik Weigand": "CandidatePics/erik.png"
    }

    # Candidate dog photos
    dog= {
        "Jeffrey Harlan": "CandidatePics/jeffHdog.png",
        "Jeff Pettis": "CandidatePics/jeffPdog.png"
    }

    # Create a DataFrame from each dictionary
    df_race = pd.DataFrame.from_dict(race, orient='index', columns=['Race'])
    df_party = pd.DataFrame.from_dict(party, orient='index', columns=['Party'])
    df_descriptor = pd.DataFrame.from_dict(descriptor, orient='index', columns=['Descriptor'])
    df_bg = pd.DataFrame.from_dict(background, orient='index', columns=['Background'])
    df_policyAll = pd.DataFrame.from_dict(policy_all, orient='index', columns=['Policy - All'])
    df_policyHealth = pd.DataFrame.from_dict(policy_healthcare, orient='index', columns=['Policy - Healthcare'])
    df_policyHousing = pd.DataFrame.from_dict(policy_housing, orient='index', columns=['Policy - Housing'])
    df_policyHomeless = pd.DataFrame.from_dict(policy_homelessness, orient='index', columns=['Policy - Homelessness'])
    df_policyEdu = pd.DataFrame.from_dict(policy_education, orient='index', columns=['Policy - Education'])
    df_policyEcon = pd.DataFrame.from_dict(policy_economy, orient='index', columns=['Policy - Economy'])
    df_policyTaxes = pd.DataFrame.from_dict(policy_taxes, orient='index', columns=['Policy - Taxes'])
    df_policyGun = pd.DataFrame.from_dict(policy_guns, orient='index', columns=['Policy - Guns'])
    df_policySafety = pd.DataFrame.from_dict(policy_safety, orient='index', columns=['Policy - Public Safety'])
    df_policyClimate = pd.DataFrame.from_dict(policy_climate, orient='index', columns=['Policy - Climate'])
    df_policyDevelop = pd.DataFrame.from_dict(policy_develop, orient='index', columns=['Policy - Development'])
    df_policyOther = pd.DataFrame.from_dict(policy_other, orient='index', columns=['Policy - Other'])
    df_endorsements = pd.DataFrame.from_dict(endorsements, orient='index', columns=['Endorsements'])
    df_oi = pd.DataFrame.from_dict(other_info, orient='index', columns=['Other Info'])
    df_images = pd.DataFrame.from_dict(images, orient='index', columns=['Image'])
    df_dog = pd.DataFrame.from_dict(dog, orient='index', columns=['Dog'])

    # Combine all the DataFrames into one
    df = pd.concat([df_race, df_party, df_descriptor, df_bg,
                    df_policyAll, df_policyHealth, df_policyHousing, df_policyHomeless, df_policyEdu, df_policyEcon, 
                    df_policyTaxes, df_policyGun, df_policySafety, df_policyClimate, df_policyDevelop, df_policyOther, 
                    df_endorsements, df_oi, df_images, df_dog], axis=1)

    # Reset the index to have a "Name" column
    df = df.reset_index().rename(columns={'index': 'Name'})

    return df