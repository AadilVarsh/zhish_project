#data handler
import arrow
import sys
import os

#CASE 1 EXACT 21 DAYS
#CASE  GREATER THAN 21 DAYS ALSO REMAINDER IS 0

sys.path.append(os.getcwd()[:os.getcwd().index('zhish_project')])
from zhish_project.excel_handler import pyxlhndlr

def return_user_list():
    sheet = pyxlhndlr.sheet("../workbooks/testXL2.xlsx")
    
    user_list = pyxlhndlr.get_msg_info(pyxlhndlr.get_sheet_format(sheet = sheet), sheet)

    return user_list


DATE_TODAY = arrow.now().format("MM-DD-YYYY")

def get_date_eligibility(days):
    if days < 21:
        return 0
    if days > 21 and days%7 == 0:
        return 1
    if days == 21:
        return 1

def sort_customer_list(user_list):
    sorted_users = list()

    for user in user_list:
        if user[2] is not None and user[2] != "last_service":
            name, phone_no, last_srvc = user[0], user[1], user[2]
            # last_srvc = str(last_srvc).strip().replace('/', '-')
            last_srvc = arrow.get(last_srvc,'YYYY-MM-DD' ).format("MM-DD-YYYY")
            intrvl_dif = arrow.get(DATE_TODAY, 'MM-DD-YYYY') - arrow.get(last_srvc, 'MM-DD-YYYY')

            if get_date_eligibility(intrvl_dif.days) == 1:
                sorted_users.append([name, phone_no])
            else:
                pass
    return sorted_users



if __name__ == "__main__":
    # print(DATE_TODAY)
    for i in sort_customer_list(return_user_list()):
        print(i[0] + ':' + i[1], end="\n")

        

