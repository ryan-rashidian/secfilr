"""Containers of XBRL labels.

Used to parse labels into categorized metrics.
Tuples are ordered by most common/relevant labels first.
"""

# Shares Outstanding
labels_shares_outstanding = (
    'CommonStockSharesOutstanding',
    'WeightedAverageNumberOfSharesOutstandingBasic',
    'WeightedAverageNumberOfShareOutstandingBasicAndDiluted',
    'WeightedAverageNumberOfDilutedSharesOutstanding',
    'EntityCommonStockSharesOutstanding',
)

# Total Assets
labels_total_assets = (
    'Assets',
    'LiabilitiesAndStockholdersEquity',
)

# Cash and Cash Equivalents
labels_cash_equiv = (
    'CashAndCashEquivalentsAtCarryingValue',
    'CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents',
    'Cash',
    'CashCashEquivalentsAndShortTermInvestments',
)

# Accounts Payable
labels_acc_payable = (
    'AccountsPayableCurrent',
    'AccountsPayableAndAccruedLiabilitiesCurrent',
    'AccountsPayable',
    'TradeAccountsPayable',
    'PayablesAndAccrualsCurrent',
    'AccruedLiabilitiesCurrent',
    'OtherLiabilitiesCurrent',
)

# Accounts Receivable
labels_acc_receivable = (
    'AccountsReceivableNetCurrent',
    'AccountsReceivable',
    'TradeAccountsReceivable',
    'AccountsReceivableNet',
    'AccountsAndOtherReceivablesNetCurrent',
    'TradeAndOtherReceivablesNetCurrent',
    'ReceivablesNetCurrent',
)

# Marketable Securities
labels_market_securities = (
    'MarketableSecuritiesCurrent',
    'MarketableSecurities',
    'ShortTermInvestments',
    'AvailableForSaleSecuritiesCurrent',
    'TradingSecuritiesCurrent',
    'InvestmentsCurrent',
    'OtherCurrentInvestments'
)

# Property Plant and Equipment (PP&E)
labels_ppande = (
    'PropertyPlantAndEquipmentNet',
    'PropertyPlantAndEquipmentGross',
)

# Inventory
labels_inventory = (
    'InventoryNet',
)

# Goodwill
labels_goodwill = (
    'Goodwill',
)

# Total Debt
labels_debt = (
    'Debt',
    'DebtLongtermAndShorttermCombinedAmount',
    'LongTermDebtAndCapitalLeaseObligations',
    'DebtSecurities',
    'TotalDebt',
    # Legacy tags
    'NotesPayable',
    'NotesPayableRelatedPartiesCurrentAndNoncurrent',
    'ConvertibleDebtNoncurrent',
    'OperatingLeaseLiability',
    'DebtInstrumentCarryingAmount',
    'FinanceLeaseLiability',
    'FinanceLeaseObligation',
)

# Short Term Debt
labels_short_term_debt = (
    'ShortTermDebtAndCurrentPortionOfLongTermDebt',
    'ShortTermDebt',
    'DebtCurrent',
    'CurrentPortionOfLongTermDebt',
    'ShortTermBorrowings',
)

# Long Term Debt
labels_long_term_debt = (
    'LongTermDebt',
    'LongTermDebtAndLeaseObligation',
    'LongTermDebtNoncurrent',
    'LongTermDebtCurrent',
)

# Total Liabilities
labels_total_liabilities = (
    'Liabilities',
    'LiabilitiesCurrent',
)

# Stockholders' Equity
labels_stockholders_equity = (
    'StockholdersEquity',
    'CommonStockEquity',
    'TotalEquity',
    'TotalStockholdersEquity',
    'StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest',
    'PartnersCapital',
    'MemberEquity',
)

# Net Cash from Operating Activities (OCF)
labels_cash_operating = (
    'NetCashProvidedByUsedInOperatingActivities',
    'NetCashProvidedByUsedInOperatingActivitiesContinuingOperations',
    'NetCashProvidedByUsedInOperatingActivitiesNoncontrollingInterest',
    'CashProvidedByUsedInOperatingActivities',
    'NetCashProvidedByOperatingActivities',
    'NetCashFlowFromOperatingActivities',
)

# Net Cash from Financing Activities
labels_cash_financing = (
    'NetCashProvidedByUsedInFinancingActivities',
)

# Net Cash from Investing Activities
labels_cash_investing = (
    'NetCashProvidedByUsedInInvestingActivities',
)

# Capital Expenditure (CAPEX)
labels_capex = (
    'PaymentsToAcquirePropertyPlantAndEquipment',
    'CapitalExpenditures',
    'PaymentsToAcquireProductiveAssets',
    'PaymentsForProceedsFromProductiveAssets',
    'PaymentsToAcquireOtherPropertyPlantAndEquipment',
    'CapitalExpendituresIncurredButNotYetPaid',
)

# Revenue
labels_revenue = (
    'Revenues',
    'Revenue',
    'RevenueNet',
    'RevenueFromContractWithCustomerExcludingAssessedTax',
    'SalesRevenueNet',
    'TotalRevenues',
    'NetSales',
    'SalesRevenueGoodsNet',
)

# Cost of Goods and Services (COGS)
labels_cogs = (
    'CostOfRevenue',
    'CostOfRevenues',
    'CostOfGoodsAndServicesSold',
    'CostOfGoodsSold',
    'CostOfGoodsAndServiceExcludingDepreciationDepletionAndAmortization',
    'CostOfSales',
    'CostsOfSales',
    'CostOfGoodsSoldExcludingDepreciation',
    'CostsAndExpensesApplicableToRevenue',
    'CostsAndExpensesDirect',
    'ProgrammingCosts',
)

# Gross Profit
labels_gross_profit = (
    'GrossProfit',
    'GrossProfitLoss',
    'GrossProfitLossAvailableToCommonStockholders',
)

# Research and Development (R&D)
labels_randd = (
    'ResearchAndDevelopmentExpense',
    'EngineeringAndProductDevelopmentExpense',
)

# General and Administrative (G&A)
labels_ganda = (
    'GeneralAndAdministrativeExpense',
    'SellingGeneralAndAdministrativeExpense',
)

# Operating Income / Loss
labels_operating_income = (
    'OperatingIncomeLoss',
    'OperatingIncomeLossBeforeOtherIncomeExpense',
    'OperatingIncomeLossBeforeInterestAndIncomeTaxes',
    'IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest',
    'IncomeLossFromOperations',
    'IncomeLossFromContinuingOperations',
    'OperatingIncomeLossFromContinuingOperations',
)

# Net Income / Loss
labels_net_income = (
    'NetIncomeLoss',
    'NetIncomeLossAvailableToCommonStockholdersBasic',
    'NetIncomeLossFromContinuingOperationsAvailableToCommonShareholdersBasic',
    'ProfitLoss',
    'NetIncomeLossIncludingPortionAttributableToNoncontrollingInterest',
)

# Operating Expenditure (OPEX)
labels_opex = (
    'OperatingExpenses',
    'OperatingCostsAndExpenses',
    'CostsAndExpenses',
    'NoninterestExpense',
    'GeneralAndAdministrativeExpense',
    'EngineeringAndProductDevelopmentExpense',
    'ResearchAndDevelopmentExpense',
    'SellingGeneralAndAdministrativeExpense',
)

# Earnings per Share Basic
labels_eps_basic = (
    'EarningsPerShareBasic',
    'EarningsPerShareBasicIncludingExtraordinaryItems',
)

# Earnings per Share Diluted
labels_eps_diluted = (
    'EarningsPerShareDiluted',
    'EarningsPerShareDilutedIncludingExtraordinaryItems',
)

# Parent Containers
balance_sheet = {
    'Shares Outstanding': labels_shares_outstanding,
    'Assets': labels_total_assets,
    'Cash & Equivalents': labels_cash_equiv,
    'Accounts Payable': labels_acc_payable,
    'Accounts Receivable': labels_acc_receivable,
    'Marketable Securities': labels_market_securities,
    'PP&E': labels_ppande,
    'Inventory': labels_inventory,
    'Goodwill': labels_goodwill,
    'Debt': labels_debt,
    'Shortterm Debt': labels_short_term_debt,
    'Longterm Debt': labels_long_term_debt,
    'Total Liabilities': labels_total_liabilities,
    'Stockholders Equity': labels_stockholders_equity
}

cash_flow_statement = {
    'Operating Cash Flow': labels_cash_operating,
    'Net Cash: Financing': labels_cash_financing,
    'Net Cash: Investing': labels_cash_investing,
    'CAPEX': labels_capex
}

income_statement = {
    'Revenue': labels_revenue,
    'COGS': labels_cogs,
    'Gross Profit': labels_gross_profit,
    'R&D': labels_randd,
    'G&A': labels_ganda,
    'Operating Income': labels_operating_income,
    'Net Income': labels_net_income,
    'OPEX': labels_opex,
    'EPS Basic': labels_eps_basic,
    'EPS Diluted': labels_eps_diluted
}

# Nested dictionary of all tags
statements = {
    'Balance Sheet': balance_sheet,
    'Cash Flow Statement': cash_flow_statement,
    'Income Statement': income_statement
}

# Argument mapping
map_arg = {
    'shares':   ('Balance Sheet', 'Shares Outstanding'),
    'assets':   ('Balance Sheet', 'Assets'),
    'cash':     ('Balance Sheet', 'Cash & Equivalents'),
    'apay':     ('Balance Sheet', 'Accounts Payable'),
    'arec':     ('Balance Sheet', 'Accounts Receivable'),
    'marsec':   ('Balance Sheet', 'Marketable Securities'),
    'ppe':      ('Balance Sheet', 'PP&E'),
    'inven':    ('Balance Sheet', 'Inventory'),
    'goodw':    ('Balance Sheet', 'Goodwill'),
    'debt':     ('Balance Sheet', 'Debt'),
    'sdebt':    ('Balance Sheet', 'Shortterm Debt'),
    'ldebt':    ('Balance Sheet', 'Longterm Debt'),
    'liab':     ('Balance Sheet', 'Total Liabilities'),
    'equity':   ('Balance Sheet', 'Stockholders Equity'),
    'ocf':      ('Cash Flow Statement', 'Operating Cash Flow'),
    'netcashf': ('Cash Flow Statement', 'Net Cash: Financing'),
    'netcashi': ('Cash Flow Statement', 'Net Cash: Investing'),
    'capex':    ('Cash Flow Statement', 'CAPEX'),
    'revenue':  ('Income Statement', 'Revenue'),
    'cogs':     ('Income Statement', 'COGS'),
    'gprofit':  ('Income Statement', 'Gross Profit'),
    'randd':    ('Income Statement', 'R&D'),
    'ganda':    ('Income Statement', 'G&A'),
    'opinc':    ('Income Statement', 'Operating Income'),
    'netinc':   ('Income Statement', 'Net Income'),
    'opex':     ('Income Statement', 'OPEX'),
    'epsb':     ('Income Statement', 'EPS Basic'),
    'epsd':     ('Income Statement', 'EPS Diluted'),
}

