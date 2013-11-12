# Create your views here.
from django.shortcuts import render

gdp_strings = [
    ("GDP_SP", "Gross Domestic Product (GDP) (state annual product)"),
    ("RGDP_SP", "Real GDP (state annual product)"),
    ("PCRGDP_SP", "Per capita Real GDP (state annual product)"),
]
compensation_strings = [
    ("COMP_SP", "Compensation of Employees (state annual product)"),
    ("PJCOMP_SI", "Average compensation per job (state annual income)"),
    ("PJCOMP_CI", "Average compensation per job (state annual income)")
]
taxes_strings = [
    ("TOPILS_SP", "Taxes on Production and Imports less Subsidies (state annual product)"),
    ("TOPI_SP", "Taxes on Production and Imports (state annual product)")
]

data_strings = (("GDP", gdp_strings), ("Compensation", compensation_strings), ("Taxes", taxes_strings))


def index(request):
    global data_strings
    data = {'data': data_strings, "year": 2012, "query": None}
    return render(request, "index_page.html", data)


def graph(request, query, year):
    global data_strings
    data = {'data': data_strings, "year": year, "query": query}
    return render(request, "data_page.html", data)

    # < ParamValue
    # KeyCode = "GDP_SP"
    # Description = "Gross Domestic Product (GDP) (state annual product)" / >
    # < ParamValue
    # KeyCode = "RGDP_SP"
    # Description = "Real GDP (state annual product)" / >
    # < ParamValue
    # KeyCode = "PCRGDP_SP"
    # Description = "Per capita Real GDP (state annual product)" / >
    # < ParamValue
    # KeyCode = "COMP_SP"
    # Description = "Compensation of Employees (state annual product)" / >
    # < ParamValue
    # KeyCode = "TOPILS_SP"
    # Description = "Taxes on Production and Imports less Subsidies (state annual product)" / >
    # < ParamValue
    # KeyCode = "GOS_SP"
    # Description = "Gross Operating Surplus (state annual product)" / >
    # < ParamValue
    # KeyCode = "SUBS_SP"
    # Description = "Subsidies (state annual product)" / >
    # < ParamValue
    # KeyCode = "TOPI_SP"
    # Description = "Taxes on Production and Imports (state annual product)" / >
    # < ParamValue
    # KeyCode = "GDP_MP"
    # Description = "Gross Domestic Product (GDP) (MSA annual product)" / >
    # < ParamValue
    # KeyCode = "RGDP_MP"
    # Description = "Real GDP (MSA annual product)" / >
    # < ParamValue
    # KeyCode = "PCRGDP_MP"
    # Description = "Per capita Real GDP (MSA annual product)" / >
    # < ParamValue
    # KeyCode = "TPI_SI"
    # Description = "Total Personal Income (state annual income)" / >
    # < ParamValue
    # KeyCode = "POP_SI"
    # Description = "Population (state annual income)" / >
    # < ParamValue
    # KeyCode = "PCPI_SI"
    # Description = "Per Capita personal income (state annual income)" / >
    # < ParamValue
    # KeyCode = "NFPI_SI"
    # Description = "Nonfarm personal income (state annual income)" / >
    # < ParamValue
    # KeyCode = "FPI_SI"
    # Description = "Farm income (state annual income)" / >
    # < ParamValue
    # KeyCode = "EARN_SI"
    # Description = "Earnings by place of work (state annual income)" / >
    # < ParamValue
    # KeyCode = "CGSI_SI"
    # Description = "Contributions for government social insurance (state annual income)" / >
    # < ParamValue
    # KeyCode = "NE_SI"
    # Description = "Net Earnings by place of residence (state annual income)" / >
    # < ParamValue
    # KeyCode = "DIR_SI"
    # Description = "Dividends, interest, and rent (state annual income)" / >
    # 6 | Page
    # Wednesday, May
    # 0
    # 8, 2013
    # < ParamValue
    # KeyCode = "PCTR_SI"
    # Description = "Personal current transfer receipts (state annual income)" / >
    # < ParamValue
    # KeyCode = "WS_SI"
    # Description = "Wage and salary disbursements (state annual income)" / >
    # < ParamValue
    # KeyCode = "SUPP_SI"
    # Description = "Supplements to wages and salaries (state annual income)" / >
    # < ParamValue
    # KeyCode = "PROP_SI"
    # Description = "Proprietors Income (state annual income)" / >
    # < ParamValue
    # KeyCode = "EMP000_SI"
    # Description = "Total Employment (full and part time) (state annual income)" / >
    # < ParamValue
    # KeyCode = "EMP100_SI"
    # Description = "Wage and salary employment (state annual income)" / >
    # < ParamValue
    # KeyCode = "EMP200_SI"
    # Description = "Proprietors employment (state annual income)" / >
    # < ParamValue
    # KeyCode = "PJEARN_SI"
    # Description = "Average earnings per job (state annual income)" / >
    # < ParamValue
    # KeyCode = "PJWS_SI"
    # Description = "Average wage per job (state annual income)" / >
    # < ParamValue
    # KeyCode = "PJCOMP_SI"
    # Description = "Average compensation per job (state annual income)" / >
    # < ParamValue
    # KeyCode = "DPI_SI"
    # Description = "Disposable personal income (state annual income)" / >
    # < ParamValue
    # KeyCode = "PCDPI_SI"
    # Description = "Per capita disposable personal income (dollars) (state annual income)" / >
    # < ParamValue
    # KeyCode = "TPI_CI"
    # Description = "Total Personal Income (county annual income)" / >
    # < ParamValue
    # KeyCode = "POP_CI"
    # Description = "Population (county annual income)" / >
    # < ParamValue
    # KeyCode = "PCPI_CI"
    # Description = "Per Capita personal income (county annual income)" / >
    # < ParamValue
    # KeyCode = "NFPI_CI"
    # Description = "Nonfarm personal income (county annual income)" / >
    # < ParamValue
    # KeyCode = "FPI_CI"
    # Description = "Farm income (county annual income)" / >
    # < ParamValue
    # KeyCode = "EARN_CI"
    # Description = "Earnings by place of work (county annual income)" / >
    # < ParamValue
    # KeyCode = "CGSI_CI"
    # Description = "Contributions for government social insurance (county annual income)" / >
    # < ParamValue
    # KeyCode = "NE_CI"
    # Description = "Net Earnings by place of residence (county annual income)" / >
    # < ParamValue
    # KeyCode = "DIR_CI"
    # Description = "Dividends, interest, and rent (county annual income)" / >
    # < ParamValue
    # KeyCode = "PCTR_CI"
    # Description = "Personal current transfer receipts (county annual income)" / >
    # < ParamValue
    # KeyCode = "WS_CI"
    # Description = "Wage and salary disbursements (county annual income)" / >
    # < ParamValue
    # KeyCode = "SUPP_CI"
    # Description = "Supplements to wages and salaries (county annual income)" / >
    # < ParamValue
    # KeyCode = "PROP_CI"
    # Description = "Proprietors' Income (county annual income)" / >
    # < ParamValue
    # KeyCode = "EMP000_CI"
    # Description = "Total Employment (full and part time) (county annual income)" / >
    # < ParamValue
    # KeyCode = "EMP100_CI"
    # Description = "Wage and salary employment (county annual income)" / >
    # < ParamValue
    # KeyCode = "EMP200_CI"
    # Description = "Proprietors employment (county annual income)" / >
    # < ParamValue
    # KeyCode = "PJEARN_CI"
    # Description = "Average earnings per job (county annual income)" / >
    # < ParamValue
    # KeyCode = "PJWS_CI"
    # Description = "Average wage per job (county annual income)" / >
    # < ParamValue
    # KeyCode = "PJCOMP_CI"
    # Description = "Average compensation per job (county annual income)" / >
    # < ParamValue
    # KeyCode = "TPI_MI"
    # Description = "Total Personal Income (MSA annual income)" / >
    # < ParamValue
    # KeyCode = "POP_MI"
    # Description = "Population (MSA annual income)" / >
    # < ParamValue
    # KeyCode = "PCPI_MI"
    # Description = "Per Capita personal income (MSA annual income)" / >
    # < ParamValue
    # KeyCode = "NFPI_MI"
    # Description = "Nonfarm personal income (MSA annual income)" / >
    # < ParamValue
    # KeyCode = "FPI_MI"
    # Description = "Farm income (MSA annual income)" / >
    # < ParamValue
    # KeyCode = "EARN_MI"
    # Description = "Earnings by place of work (MSA annual income)" / >
    # < ParamValue
    # KeyCode = "CGSI_MI"
    # Description = "Contributions for government social insurance (MSA annual income)" / >
    # < ParamValue
    # KeyCode = "NE_MI"
    # Description = "Net Earnings by place of residence (MSA annual income)" / >
    # < ParamValue
    # KeyCode = "DIR_MI"
    # Description = "Dividends, interest, and rent (MSA annual income)" / >
    # < ParamValue
    # KeyCode = "PCTR_MI"
    # Description = "Personal current transfer receipts (MSA annual income)" / >
    # < ParamValue
    # KeyCode = "WS_MI"
    # Description = "Wage and salary disbursements (MSA annual income)" / >
    # < ParamValue
    # KeyCode = "SUPP_MI"
    # Description = "Supplements to wages and salaries (MSA annual income)" / >
    # < ParamValue
    # KeyCode = "PROP_MI"
    # Description = "Proprietors Income (MSA annual income)" / >
    # < ParamValue
    # KeyCode = "EMP000_MI"
    # Description = "Total Employment (full and part time) (MSA annual income)" / >
    # < ParamValue
    # KeyCode = "EMP100_MI"
    # Description = "Wage and salary employment (MSA annual income)" / >
    # < ParamValue
    # KeyCode = "EMP200_MI"
    # Description = "Proprietors employment (MSA annual income)" / >
    # < ParamValue
    # KeyCode = "PJEARN_MI"
    # Description = "Average earnings per job (MSA annual income)" / >
    # < ParamValue
    # KeyCode = "PJWS_MI"
    # Description = "Average wage per job (MSA annual income)" / >
    # < ParamValue
    # KeyCode = "PJCOMP_MI"
    # Description = "Average compensation per job (MSA annual income)" / >
    # < ParamValue
    # KeyCode = "TPI_QI"
    # Description = "Total Personal Income (state quarterly income)" / >
    # < ParamValue
    # KeyCode = "NFPI_QI"
    # Description = "Nonfarm personal income (state quarterly income)" / >
    # < ParamValue
    # KeyCode = "FPI_QI"
    # Description = "Farm income (state quarterly income)" / >
    # < ParamValue
    # KeyCode = "EARN_QI"
    # Description = "Earnings by place of work (state quarterly income)" / >
    # < ParamValue
    # KeyCode = "CGSI_QI"
    # Description = "Contributions for government social insurance (state quarterly income)" / >
    # < ParamValue
    # KeyCode = "AR_CI"
    # Description = "Adjustment for residence (county annual income)" / >
    # < ParamValue
    # KeyCode = "AR_QI"
    # Description = "Adjustment for residence (state quarterly income)" / >
    # < ParamValue
    # KeyCode = "AR_SI"
    # Description = "Adjustment for residence (state annual income)" / >
    # < ParamValue
    # KeyCode = "NE_QI"
    # Description = "Net Earnings by place of residence (state quarterly income)" / >
    # < ParamValue
    # KeyCode = "DIR_QI"
    # Description = "Dividends, interest, and rent (state quarterly income)" / >
    # < ParamValue
    # KeyCode = "PCTR_QI"
    # Description = "Personal current transfer receipts (state quarterly income)" / >
    # < ParamValue
    # KeyCode = "WS_QI"
    # Description = "Wage and salary disbursements (state quarterly income)" / >
    # < ParamValue
    # KeyCode = "SUPP_QI"
    # Description = "Supplements to wages and salaries (state quarterly income)" / >
    # < ParamValue
    # KeyCode = "PROP_QI"
    # Description = "Proprietors Income (state quarterly income)" / >
    # < / Results >
    # < / BEAAPI >