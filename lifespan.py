import bs4, urllib3, pandas, datetime, random, math, numpy
import matplotlib.pyplot as plt
from matplotlib.pyplot import *

# SOCIAL SECURITY ACTUARIAL LIFE TABLE
url = "https://www.ssa.gov/oact/STATS/table4c6.html"
page = urllib2.urlopen(url)
soup = bs4.BeautifulSoup(page.read(), 'html.parser')
table  = soup.find("table")#.get_text()
Life_List, j = ([], 0)
for tr in table.findAll("tr")[4:]:
    row = []
    td = tr.findAll("td")
    for columns in range(0 , 7):
        string = td[columns].text.replace(',', '')
        value = pandas.to_numeric(string)
        row.append(value)
    Life_List.append(row)
names = ["Age", "P(M)", "n(M)", "E(M)", "P(F)", "n(F)", "E(F)"]
Life_Table = pandas.DataFrame(Life_List, columns=names)
# For computational convenience, no one lives to more than 120 years
Life_Table.set_value(119, "P(M)", 1.0)
Life_Table.set_value(119, "P(F)", 1.0)
plt.figure(1)
for i in (1, 3, 4, 6):
    plt.subplot(211 + i % 3)
    if i == 1 or i == 3:
        p = plt.plot(Life_Table[names[0]], Life_Table[names[i]], 'b-', label="Male")
    else:
        p = plt.plot(Life_Table[names[0]], Life_Table[names[i]], 'r-', label="Female")
    if i == 1 or i == 4:
        plt.ylabel('Probability of Death')
        legend()
    else:
        plt.ylabel('Life Expectancy')
        legend()
plt.savefig(".\DATA_602_Project_1.png")
# plt.show()
plt.clf()

# GET DATE VARIABLES NEEDED FOR CALCULATIONS AND OUTPUT TEXT
def date_vars(DOB, L=0):
    birthdate = pandas.to_datetime(DOB, format='%m/%d/%Y')
    today = datetime.date.today()
    birthday = datetime.date(today.year, birthdate.month, birthdate.day)
    birthday_last = datetime.date(today.year - 1, birthdate.month, birthdate.day)
    year_int = (today.year if birthday <= today else today.year - 1) - birthdate.year
    date_diff = (today - birthday) if birthday <= today else (today - birthday_last)
    year_length = birthday - birthday_last
    year_dec = float(date_diff.days) / float(year_length.days)
    death_year = datetime.date(today.year + int(L), 1, 1)
    death_year_length = datetime.date(today.year + int(L) + 1, 1, 1) - death_year
    death_year_days = (L - int(L)) * death_year_length.days
    death_date = death_year + datetime.timedelta(days=death_year_days)
    return today, year_int, year_dec, death_date

# GENERATE CORRELATED STANDARD NORMALS USING THE POLAR METHOD, THEN CONVERT TO CORRELATED UNIFORMS
def CorrelatedUniforms(n, rho):
    if rho == 0:
        X = numpy.random.uniform(0.0, 1.0, n)
    else:
        rho = numpy.sign(rho) if (abs(rho) > 1) else rho
        accepted, U = (0, numpy.zeros(n))
        while not (accepted):
            U = numpy.random.uniform(0.0, 1.0, n)
            V = [-1.0 + 2.0 * u for u in U]
            S = sum([v * v for v in V])
            accepted = (S < 1)
        W = math.sqrt(-2 * math.log(S) / S)
        X = [v * W for v in V]
        for i in range(2, n):
            X[i] = rho * X[1] + math.sqrt(1.0 - rho**2) * X[i]
        A = (8 * (math.pi - 3)) / (3 * math.pi * (4 - math.pi))
        B = 4 / math.pi
        Y = [x * x * 0.5 for x in X]
        erf = [math.sqrt(1.0 - math.exp(-y * (B + A*y) / (1.0 + A*y))) for y in Y]
        X = [(0.5 + 0.5 * e) if (X >= 0) else (0.5 - 0.5 * e) for e in erf]
    return X

# CREATE CUMULATIVE PROBABILITY DISTRIBUTION 0<=F(120-a)<=1 WHERE a IS EXACT AGE
def InvertF(Gender, DOB):
    today, year_int, year_dec, not_used = date_vars(DOB)
    t, F = ([0], [0]) # Cumulative probability of death at time 0.
    t.append(1 - year_dec) # First period is for a partial year of length t[1]
    F.append(t[1] * Life_Table["P(" + Gender + ")"][year_int])
    # Now use that P[T <= t+1] = P[T <= t] + P[T <= t+1 | T > t] * P[T > t].
    for k in range(year_int + 1, 120):
        t.append(t[k - year_int] + 1.0)
        F.append(F[k - year_int] + Life_Table["P(F)"][k] * (1.0 - F[k - year_int]))
    du, H, k = (1.0 / 1000, [0], 0) # Invert the function starting with u = 0.
    for i in range(1, 1001):
        u = i * du
        while not (F[k] < u and u <= F[k + 1]):
            k += 1 # Locate the inversion interval.
        w = (u - F[k]) / (F[k + 1] - F[k]) # Invert "u" (interpolate between t[k] and t[k+1]).
        H.append((1.0 - w) * t[k] + w * t[k + 1])
    return H

# INVERSE TRANSFORM MAPS 0<=U<=1 TO 0<=H(U)<=(120-a) WHERE a IS EXACT AGE
def HofU(H, U):
    du = 1.0 / 1000
    i = int(1000 * U) # Determine the appropriate interpolation interval so that (i*du)<=U <=((i+1)*du)
    w = (U - i * du) / du # Determine the appropriate interpolation weights
    L = (1.0 - w) * H[i]  +  w * H[i + 1] # Interpolate between H[i] and H[i+1].
    return L

# MONTE CARLO SIMULATION OF REMAINING LIFESPAN
def Simulate(Insured, Policy, rho):
    persons = len(Insured)
    # Gender = [sublist[0:1][0] for sublist in Insured]
    # DOB = [sublist[1:2][0] for sublist in Insured]
    H = [InvertF(sublist[0:1][0], sublist[1:2][0])for sublist in Insured]
    limit, r = (Policy[0], Policy[2])
    Term = 120 if (Policy[1] == None) else Policy[1]
    Lifespan_Data, Lbar, L2bar, epsilon_1, done, n = ([], 0, 0, 0.01, 0, 0)
    Premium_Data, pihat, Pbar, P2bar, Bbar, B2bar, BPbar, benefit = ([], 0, 0, 0, 0, 0, 0, 0)
    start = datetime.datetime.now()
    while not done:
        U = CorrelatedUniforms(persons, rho)
        LS_Estimates, LS_Antithetic, L, P, B = ([], [], 0, 0, 0)
        Lifespans, Premiums, Benefits = ([], [], [])
        for i in range(0, persons):
            LS_Estimates.append(HofU(H[i], U[i]))
            LS_Antithetic.append(HofU(H[i], 1.0 - U[i]))
            P1, P2 = (0, 0)
            for t in range(0, int(LS_Estimates[i]) if LS_Estimates[i] < Term else Term - 1):
                P1 += math.exp(-r * t) # PV of premium payments (at $1/year) received
            for t in range(0, int(LS_Antithetic[i]) if LS_Antithetic[i] < Term else Term - 1):
                P2 += math.exp(-r * t) # PV of premium payments (at $1/year) received
            benefit = limit if (Policy[3] == "Lump") else (limit * int(LS_Estimates[i]))
            B1 = benefit * math.exp(-r * LS_Estimates[i]) # PV of benefit payments
            benefit = limit if (Policy[3] == "Lump") else (limit * int(LS_Antithetic[i]))
            B2 = benefit * math.exp(-r * LS_Antithetic[i]) # PV of benefit payments
            Lifespans.append((LS_Estimates[i] + LS_Antithetic[i]) / 2.0) # Average the two realizations
            Premiums.append((P1 + P2) / 2.0) # Average the two realizations
            Benefits.append((B1 + B2) / 2.0) # Average the two realizations
        if Policy[3] == "Lump":
            L = sorted(Lifespans)[-2] # penultimate life for end of premium payments and lump benefit payment
            P = sum([sorted(Premiums)[-2] if p == max(Premiums) else p for p in Premiums])
            B = sorted(Benefits)[-2]
        if Policy[3] == "Annuity":
            L = max(Lifespans) # penultimate life for end of premium payments, max life for annuity begin/end
            P = sum([sorted(Premiums)[-2] if p == max(Premiums) else p for p in Premiums])
            B = Benefits[numpy.argmax(numpy.max(Lifespans, axis=0))]
        if Policy[3] == "Pension":
            L = max(Lifespans) # max life for end of both all premium payments and benefit payments
            P = Premiums[numpy.argmax(numpy.max(Lifespans, axis=0))]
            B = sum(Benefits)
        n += 1 # Update sample moments
        Lbar = ((n - 1) * Lbar + L) / n
        L2bar = ((n - 1) * L2bar + L * L) / n
        Pbar  = ((n-1) * Pbar + P) / n
        P2bar = ((n-1) * P2bar + P*P) / n
        Bbar  = ((n-1) * Bbar + B) / n
        B2bar = ((n-1) * B2bar + B*B) / n
        BPbar = ((n-1) * BPbar + B*P) / n
        Lifespan_Data.append(Lbar)
        Premium_Data.append(Bbar / Pbar)
        if (n % 100000 == 0): # Test if error is acceptable, and report results to this point
            pihat = Bbar / Pbar # estimator of the "fair" premium
            epsilon_2 = pihat * 0.001
            varB = B2bar - Bbar*Bbar
            varP = P2bar - Pbar*Pbar
            covBP = BPbar - Bbar*Pbar
            s_pihat = pihat * math.sqrt((varB/(Bbar*Bbar) - 2 * covBP/(Bbar*Pbar) + varP/(Pbar*Pbar))/n)
            s_Lbar = math.sqrt((L2bar - Lbar ** 2) / n)
            t = datetime.datetime.now() - start # Computing elapsed time and estimated time of completion
            t_star_1 = t.total_seconds() * (1.96 * s_Lbar / epsilon_1)**2
            t_star_2 = t.total_seconds() * (1.96 * s_pihat / epsilon_2)**2
            if n == 100000:
                print "\nFAIR ANNUAL PREMIUM FOR YEARS REMAINING BASED ON  ACTUARIAL LIFE EXPECTANCIES\n" \
                    '%-12s%-11s%-10s%-12s%-10s%-13s%-15s' % ("SIMULATIONS", "YEARS", \
                    "+/-", "PREMIUM", "+/-", "ELAPSED TIME", "ESTIMATED TIME")
            print '%-12i%-11f%-10f%-12.2f%-10.2f%-13f%-15f' % \
                  (n, Lbar, 1.96 * s_Lbar, pihat, 1.96 * s_pihat, t.total_seconds(), max(t_star_1, t_star_2))
            if (1.96 * s_Lbar <= epsilon_1 and 1.96 * s_pihat <= epsilon_2):
                done = 1  # When error tolerances are met
    return Lbar, Lifespan_Data, pihat, Premium_Data

# VISUALIZATIONS
def Plot_Simulation(Lbar, Lifespan_Data, pihat, Premium_Data, save):
    plt.title('Monte Carlo Simulation Results')
    plt.xlabel('Years of Life Remaining')
    plt.ylabel('Fair Annual Premium')
    plt.plot(Lifespan_Data, Premium_Data, 'b.')
    plt.axhline(y=pihat, xmin=0, xmax=Lbar, color='k', linestyle='-')
    plt.axvline(x=Lbar, ymin=0, ymax=pihat, color='k', linestyle='-')
    plt.plot(Lbar, pihat, 'ro')
    plt.savefig(".\DATA_602_Project_" + str(save) + ".png")
    # plt.show()
    plt.clf()

# SCENARIO 1 (n premium payment sources, 1 benefit payment)
Person1 = ["M", "01/01/1987"] # Bill
Person2 = ["M", "04/02/1982"] # Jim
Person3 = ["M", "07/02/1977"] # Mike
Person4 = ["F", "10/01/1980"] # Jill
Person5 = ["F", "12/31/1975"] # Martha
Insured = [Person1, Person2, Person3, Person4, Person5]
Policy = [1000000, None, 0.05, "Lump"]
Correlation = [0.00]

print "\n", "=" * 40, "SCENARIO 1", "=" * 40
for rho in Correlation:
    w, x, y, z = Simulate(Insured, Policy, rho)
    Plot_Simulation(w, x, y, z, Correlation.index(rho) + 2)

# SCENARIO 2 (1 premium payment source, n benefit payments)
Person1 = ["M", "01/01/1987"]
Person2 = ["F", "06/01/1987"]
Insured = [Person1, Person2]
Policy = [50000, None, 0.05, "Annuity"]
Correlation = [0.00, 0.25, 0.5, 0.75]

print "\n", "=" * 40, "SCENARIO 2", "=" * 40
for rho in Correlation:
    w, x, y, z = Simulate(Insured, Policy, rho)
    Plot_Simulation(w, x, y, z, Correlation.index(rho) + 3)

# SCENARIO 3 (n premium payment sources, n benefit payments)
Person1 = ["M", "01/01/1952"]
Person2 = ["M", "03/14/1952"]
Person3 = ["M", "05/26/1952"]
Person4 = ["M", "08/07/1952"]
Person5 = ["M", "10/19/1952"]
Person6 = ["M", "12/31/1952"]
Person7 = ["F", "01/01/1952"]
Person8 = ["F", "05/02/1952"]
Person9 = ["F", "08/31/1952"]
Person10 = ["F", "12/31/1952"]
Insured = [Person1, Person2, Person3, Person4, Person5, Person6, Person7, Person8, Person9, Person10]
Policy = [30000, None, 0.05, "Pension"]
Correlation = [0.00, 0.25]

print "\n", "=" * 40, "SCENARIO 3", "=" * 40
for rho in Correlation:
    w, x, y, z = Simulate(Insured, Policy, rho)
    Plot_Simulation(w, x, y, z, Correlation.index(rho) + 7)
