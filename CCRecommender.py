import pandas as pd

# put provided credit card usage data into 'ccData'
cc_cols = ['ID', 'Date', 'Des1', 'Des2', 'Des3', 'Payment']
ccData = pd.read_csv('CreditCardData.csv', sep=',', names=cc_cols).drop(['Date', 'Des2', 'Des3'], axis=1)

# splits data set into groups by ID
DF2 = ccData.groupby(["ID"])

# iterates through the list of users in the grouped DataFrame
for ID, ID_ccData in DF2:

    # find the sums of the purchases in each category in which cards give points or cash back
    netPurchaseSum = ID_ccData[(ID_ccData.Des1 != "GROCERIES") & (ID_ccData.Des1 != "GAS") & (ID_ccData.Des1 != "RESTAURANTS") & (ID_ccData.Des1 != "PHARMACY")]["Payment"].sum()
    grocerySum = ID_ccData[(ID_ccData.Des1 == "GROCERIES")]["Payment"].sum()
    gasSum = ID_ccData[(ID_ccData.Des1 == "GAS")]["Payment"].sum()
    restaurantSum = ID_ccData[(ID_ccData.Des1 == "RESTAURANTS")]["Payment"].sum()
    pharmacySum = ID_ccData[(ID_ccData.Des1 == "PHARMACY")]["Payment"].sum()

    # add new columns to DataFrame to show points and cash back for each card
    CashWiseVisa_Points = (gasSum * 0) + (grocerySum * 0) + (pharmacySum * 0) + (restaurantSum * 0) + (netPurchaseSum * 0)
    CashWiseVisa_CashBack = (gasSum * 0.015) + (grocerySum * 0.015) + (pharmacySum * 0.015) + (restaurantSum * 0.015) + (netPurchaseSum * 0.015)

    PropelAmericanExpress_Points = (gasSum * 3) + (grocerySum * 1) + (pharmacySum * 1) + (restaurantSum * 2) + (netPurchaseSum * 1)
    PropelAmericanExpress_CashBack = (gasSum * 0) + (grocerySum * 0) + (pharmacySum * 0) + (restaurantSum * 0) + (netPurchaseSum * 0)

    VisaSignature_Points = (gasSum * 5) + (grocerySum * 5) + (pharmacySum * 5) + (restaurantSum * 1) + (netPurchaseSum * 1)
    VisaSignature_CashBack = (gasSum * 0) + (grocerySum * 0) + (pharmacySum * 0) + (restaurantSum * 0) + (netPurchaseSum * 0)

    Propel365AmericanExpress_Points = (gasSum * 3) + (grocerySum * 1) + (pharmacySum * 1) + (restaurantSum * 2) + (netPurchaseSum * 1)
    Propel365AmericanExpress_CashBack = (gasSum * 0) + (grocerySum * 0) + (pharmacySum * 0) + (restaurantSum * 0) + (netPurchaseSum * 0)

    Rewards_Points = (gasSum * 5) + (grocerySum * 5) + (pharmacySum * 5) + (restaurantSum * 1) + (netPurchaseSum * 1)
    Rewards_CashBack = (gasSum * 0) + (grocerySum * 0) + (pharmacySum * 0) + (restaurantSum * 0) + (netPurchaseSum * 0)

    Platinum_Points = (gasSum * 0) + (grocerySum * 0) + (pharmacySum * 0) + (restaurantSum * 0) + (netPurchaseSum * 0)
    Platinum_CashBack = (gasSum * 0) + (grocerySum * 0) + (pharmacySum * 0) + (restaurantSum * 0) + (netPurchaseSum * 0)

    CashBackCollege_Points = (gasSum * 0) + (grocerySum * 0) + (pharmacySum * 0) + (restaurantSum * 0) + (netPurchaseSum * 0)
    CashBackCollege_CashBack = (gasSum * 0.03) + (grocerySum * 0.03) + (pharmacySum * 0.03) + (restaurantSum * 0.01) + (netPurchaseSum * 0.01)

    Secured_Points = (gasSum * 0) + (grocerySum * 0) + (pharmacySum * 0) + (restaurantSum * 0) + (netPurchaseSum * 0)
    Secured_CashBack = (gasSum * 0) + (grocerySum * 0) + (pharmacySum * 0) + (restaurantSum * 0) + (netPurchaseSum * 0)

    # creates list of each user and the types of cards and their corresponding points and cash back
    bestCard = [{'ID': ID, 'Points': CashWiseVisa_Points, 'CashBack': CashWiseVisa_CashBack},
                {'ID': ID, 'Points': PropelAmericanExpress_Points, 'CashBack': PropelAmericanExpress_CashBack},
                {'ID': ID, 'Points': VisaSignature_Points, 'CashBack': VisaSignature_CashBack},
                {'ID': ID, 'Points': Propel365AmericanExpress_Points, 'CashBack': Propel365AmericanExpress_CashBack},
                {'ID': ID, 'Points': Rewards_Points, 'CashBack': Rewards_CashBack},
                {'ID': ID, 'Points': Platinum_Points, 'CashBack': Platinum_CashBack},
                {'ID': ID, 'Points': CashBackCollege_Points, 'CashBack': CashBackCollege_CashBack},
                {'ID': ID, 'Points': Secured_Points, 'CashBack': Secured_CashBack}]

    # creates new DataFrame for each user and the types of cards and their corresponding points and cash back
    df = pd.DataFrame(bestCard, index=['CashWiseVisa', 'PropelAmericanExpress', 'VisaSignature', 'Propel365AmericanExpress', 'Rewards', 'Platinum', 'CashBackCollege', 'Secured'])

    # assigns the index of the maximum number of points to the variable 'maxPoints'
    maxPoints = df['Points'].idxmax()

    # assigns the index of the maximum number of cash back to the variable 'maxCashBack'
    maxCashBack = df['CashBack'].idxmax()

    # here I just print the data for each user but, you can output it in any other way that works with your stack
    # most likely you would marshall it to JSON and have your webserver push it to the app
    # in the real world, there would be more checks to ensure that the user is qualified for the recommended credit card
    print(ID)
    print(df)
    print("The best card for points is:", maxPoints)
    print("The best card for cash back is:", maxCashBack)











