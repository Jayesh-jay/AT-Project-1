class Login:
    # Elements for login page
    username_text_box = "username"
    password_text_box = "password"
    login_btn = button = "[type='submit']"


class PimModule:
    # Elements for PIM module

    pim_menu = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]"
    add_btn = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button"
    first_name = ("//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div["
                  "1]/div[2]/input")
    mid_name = ("//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div["
                "2]/div[2]/input")
    last_name = ("//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div["
                 "3]/div[2]/input")
    employee_id = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input"
    save_btn = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]"
    employee_list = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]"
    save_button = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button"
    firstname = ("//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div/div/div[2]/div["
                 "1]/div[2]/input")
    search_btn = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]"
    edit_btn = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[2]"
    edited_name = ("//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div/div/div[2]/div["
                   "1]/div[2]/input")
    save_button1 = "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button"
    delete_btn = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[1]"
    confirm_btn = "//*[@id='app']/div[3]/div/div/div/div[3]/button[2]"
