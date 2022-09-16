import pandas as pd
from datetime import date


# import data csv and output csv. then get total rows with total = data.shape[0]
data = pd.DataFrame()
data_end = pd.DataFrame()
total = 0

# IF YOU'RE GETTING ERRORS, CHECK CAPITALISATION AND SPELLING OF CATEGORIES IN INSERT SHEET


def AnalyzeTopLevel():
    # create lists to allow search
    ob2data = ['OB2']
    ob3data = ['OB3']
    ob4data = ['OB4']
    mdata = ['Multi Program']
    ndata = ['Non Program']
    whole = ['OB2', 'OB3', 'OB4', 'Multi Program', 'Non Program']
    # subset data for each top level label type
    Ob2 = data[data["Label 1"].isin(ob2data) | data["Label 2"].isin(ob2data) | data["Label 3"].isin(ob2data)]
    Ob3 = data[data["Label 1"].isin(ob3data) | data["Label 2"].isin(ob3data) | data["Label 3"].isin(ob3data)]
    Ob4 = data[data["Label 1"].isin(ob4data) | data["Label 2"].isin(ob4data) | data["Label 3"].isin(ob4data)]
    m = data[data["Label 1"].isin(mdata) | data["Label 2"].isin(mdata) | data["Label 3"].isin(mdata)]
    n = data[data["Label 1"].isin(ndata) | data["Label 2"].isin(ndata) | data["Label 3"].isin(ndata)]
    K = data[data["Label 1"].isin(whole) | data["Label 2"].isin(whole) | data["Label 3"].isin(whole)]

    if Ob2.shape[0] != 0:
        calculate(Ob2, K, "OB2")

    if Ob3.shape[0] != 0:
        calculate(Ob3, K, "OB3")

    if Ob4.shape[0] != 0:
        calculate(Ob4, K, "OB4")

    if m.shape[0] != 0:
        calculate(m, K, "Multi Program")

    if n.shape[0] != 0:
        calculate(n, K, "Non Program")

    return


def LowerLevelAnalyze():
    # create lists to allow search
    Adata = ['Federal']
    Bdata = ['Nature']
    PRdata = ['Mine reclamation']
    Sdata = ['Solar']
    Cdata = ['Culture']
    whole = ['Federal', 'Nature', 'Mine Reclamation', 'Solar', 'Culture']

    # subset data for each top level label type
    A = data[data["Label 3"].isin(Adata)]
    B = data[data["Label 3"].isin(Bdata)]
    PR = data[data["Label 3"].isin(PRdata)]
    S = data[data["Label 3"].isin(Sdata)]
    C = data[data["Label 3"].isin(Cdata)]
    K = data[data["Label 3"].isin(whole)]

    if A.shape[0] != 0:
        calculate(A, K, "Federal")

    if B.shape[0] != 0:
        calculate(B, K, "Nature")

    if PR.shape[0] != 0:
        calculate(PR, K, "Mine Reclamation")

    if S.shape[0] != 0:
        calculate(S, K, "Solar")

    if C.shape[0] != 0:
        calculate(C, K, "Culture")
    return


# I reused the code from above and as such did not change a lot of the variable names for simplicity's sake
# they follow the exact same pattern and don't conflict with the variables above due to scoping
def LinkTypeAnalyze():
    # create lists to allow search
    Adata = ['Action']
    Bdata = ['Blog']
    PRdata = ['Press Release']
    whole = ['Action', 'Blog', 'Press Release']

    # subset data for each top level label type
    A = data[data["Type"].isin(Adata)]
    B = data[data["Type"].isin(Bdata)]
    PR = data[data["Type"].isin(PRdata)]
    K = data[data["Type"].isin(whole)]

    if A.shape[0] != 0:
        calculate(A, K, "Action")

    if B.shape[0] != 0:
        calculate(B, K, "Blog")

    if PR.shape[0] != 0:
        calculate(PR, K, "Press Release")

    return


def StateAnalyze():
    # create lists to allow search
    KYdata = ['KY']
    NCdata = ['NC']
    VAdata = ['VA']
    TNdata = ['TN']
    WVdata = ['WV']
    whole = ['KY', 'NC', 'VA', 'TN', 'WV']
    # subset data for each top level label type
    KY = data[data["State"].isin(KYdata) | data["State 2"].isin(KYdata) | data["State 3"].isin(KYdata) |
              data["State 4"].isin(KYdata)]
    NC = data[data["State"].isin(NCdata) | data["State 2"].isin(NCdata) | data["State 3"].isin(NCdata) |
              data["State 4"].isin(NCdata)]
    VA = data[data["State"].isin(VAdata) | data["State 2"].isin(VAdata) | data["State 3"].isin(VAdata) |
              data["State 4"].isin(VAdata)]
    TN = data[data["State"].isin(TNdata) | data["State 2"].isin(TNdata) | data["State 3"].isin(TNdata) |
              data["State 4"].isin(TNdata)]
    WV = data[data["State"].isin(WVdata) | data["State 2"].isin(WVdata) | data["State 3"].isin(WVdata) |
              data["State 4"].isin(WVdata)]
    K = data[data["State"].isin(whole) | data["State 2"].isin(whole) | data["State 3"].isin(whole) |
             data["State 4"].isin(whole)]

    if KY.shape[0] != 0:
        calculate(KY, K, "KY")

    if NC.shape[0] != 0:
        calculate(NC, K, "NC")

    if VA.shape[0] != 0:
        calculate(VA, K, "VA")

    if TN.shape[0] != 0:
        calculate(TN, K, "TN")

    if WV.shape[0] != 0:
        calculate(WV, K, "WV")

    return


def calculate(Ob2, K, e):
    EngageTotal = sum(K["ENGAGED USERS"])
    ShareTotal = sum(K["SHARES"])
    ClickTotal = sum(K["CLICKS"])
    ReachTotal = sum(K["REACH"])
    totalOb2 = Ob2.shape[0]
    data_end.at[e, "# of Posts"] = totalOb2
    data_end.at[e, "% of posts"] = "%" + str((totalOb2 / total) * 100)
    Ob2Engage = sum(Ob2["ENGAGED USERS"])
    data_end.at[e, "# of engagements"] = Ob2Engage
    data_end.at[e, "% of engagements"] = "%" + str((Ob2Engage / EngageTotal) * 100)
    enPer2 = Ob2Engage / totalOb2
    data_end.at[e, "AVG engagements/post"] = enPer2
    Ob2Share = sum(Ob2["SHARES"])
    data_end.at[e, "# of shares"] = Ob2Share
    data_end.at[e, "% of shares"] = "%" + str((Ob2Share / ShareTotal) * 100)
    Ob2Click = sum(Ob2["CLICKS"])
    data_end.at[e, "# of clicks"] = Ob2Click
    data_end.at[e, "% of clicks"] = "%" + str((Ob2Click / ClickTotal) * 100)
    Ob2Reach = sum(Ob2["REACH"])
    data_end.at[e, "Reach"] = Ob2Reach
    data_end.at[e, "% of Reach"] = "%" + str((Ob2Reach / ReachTotal) * 100)
    data_end.at[e, "Reach/Engagement Rate"] = "%" + str((Ob2Engage / Ob2Reach) * 100)
    return


def initialize(name, othername):
    global data
    data = pd.read_csv(r"" + name)
    global data_end
    data_end = pd.read_csv(r"" + othername, index_col = "Campaign")
    global total
    total = data.shape[0]
    calculate(data, data, "OVERALL")


def Special():
    ReclaimData = ['Yes']
    R = data[data["Reclaim"].isin(ReclaimData)]
    if R.shape[0] != 0:
        calculate(R, R, "Reclamation Act")
    return


def main():
    # prompt for csv names
    name = input("Enter the file path for your data file, WITHOUT quotes\n")
    othername = input("Enter the path for your output file WITHOUT quotes\n")
    # pass csv names to initialize function, making sure we keep the pandas dataframes global
    initialize(name, othername)
    # call top level analyze
    AnalyzeTopLevel()
    # call lower level analyze
    LowerLevelAnalyze()
    # call link type analyze
    LinkTypeAnalyze()
    # call state analyze
    StateAnalyze()
    Special()
    # get today's date
    t = date.today()
    t = str(t)
    t = t + " App Voices Analytics.csv"
    t = 'C:\\Users\\mraus\\Downloads\\' + t
    # export to csv containing date in the file path to differentiate
    data_end.to_csv(r"" + t)


if __name__ == "__main__":
    main()
