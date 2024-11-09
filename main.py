import sys
import pandas
from datetime import datetime, timedelta, date
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem, QHeaderView, QFileDialog
from PyQt6.QtCore import Qt, QDate
from Views.LoginWindow import Ui_LoginWindow
from Views.MainWindow import Ui_MainWindow
from Views.PopUpWidget import Ui_PopUp
from Views.ReservationsWindow import Ui_ReservationsWindow
from Views.NewReservationWindow import Ui_NewResWindow
from Views.RateWindow import Ui_RateWindow
from Views.GuestDetailsWindow import Ui_GuesDetailsWindow
from Views.GuestSelectWindow import Ui_SelectGuestWIndow
from Views.GuestAddWindow import Ui_AddGuestWindow
from Views.AdminWindow import Ui_AdminWindow
from Views.AddUserWindow import Ui_AddUserWindow
from Views.EdditUserWindow import Ui_EditUserWindow
from Views.DeleteUsrWIndow import Ui_DeleteUsrWindow
from Views.ReservationDetailsWindow import Ui_DetailsMAinWindow
from Views.EditReservationWindow import Ui_EditResWindow
from Views.ReservationEditRateWindow import Ui_ResEditRateWindow
from Views.ReportWindow import Ui_ReportWindow
from db_connections import cursor, conn

def validate_login(usr, pswd):
    cursor.execute("SELECT login, password FROM users")
    res = cursor.fetchall()
    for i in res:
        if usr in i and pswd in i:
            return True
        else:
            continue
    return False


def get_usr_id(usr, pswd):
    cursor.execute("""SELECT id FROM users WHERE login = %s AND password = %s""", [usr, pswd])
    res = str(cursor.fetchall()[0][0])
    return res


def update_last_login_date(usr_id):
    cursor.execute("""UPDATE users SET last_login = current_timestamp WHERE id = %s """, [usr_id])
    conn.commit()


def get_usr_role(usr):
    cursor.execute("""SELECT r.title
                    FROM users AS u
                    JOIN roles AS r
                    ON u.role_id = r.id
                    WHERE u.id = %s""", [usr])
    return cursor.fetchall()[0][0]


def login():
    usr = login_ui.usr_leddit.text()
    pswd = login_ui.pswd_leddit.text()
    if validate_login(usr, pswd):
        usr_id = get_usr_id(usr, pswd)
        update_last_login_date(usr_id)
        set_reservations_usr(usr, usr_id)
        show_reservation_window()
        login_window.close()
    else:
        pop_up_ui.popup_txt.setText("Incorrect login credentials")
        pop_up_widget.show()


def set_reservations_usr(usr, usr_id):
    reservations_ui.currentUsr_lbl.setText("Logged in as " + usr)
    reservations_ui.hiddenId_lbl.setText(usr_id)
    reservations_ui.hiddenId_lbl.hide()


def populate_rate_window(form, hide_primary_save_btn=False):
    if hide_primary_save_btn:
        rate_window_ui.save_btn.hide()
        rate_window_ui.saveEdit_btn.show()
    else:
        rate_window_ui.saveEdit_btn.hide()
        rate_window_ui.save_btn.show()
    arrival = datetime.strptime(form.doa_daddit.text(), '%d.%m.%Y').date()
    departure = datetime.strptime(form.dod_daddit.text(), '%d.%m.%Y').date()
    diff = (departure - arrival).days

    if diff <= 0:
        pop_up_ui.popup_txt.setText("Please specify the correct stay period")
        pop_up_widget.setFocus()
        pop_up_widget.show()

    else:
        headers = [arrival + timedelta(days=i) for i in range(diff)]

        for item in range(len(headers)):
            y, m, d = str(headers[item]).split('-')
            headers[item] = f"{d}.{m}.{y}"

        row_count = 1
        column_count = len(headers)

        table = rate_window_ui.rate_tWidget
        table.setRowCount(row_count)
        table.setColumnCount(column_count)
        table.setHorizontalHeaderLabels(headers)

        for row in range(row_count):
            for column in range(column_count):
                item = form.rate_leddit.text()
                table.setItem(row, column, QTableWidgetItem(item))
                table.item(row, column).setTextAlignment(Qt.AlignmentFlag.AlignCenter)

        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        rate_window.show()


def show_reservation_window():
    table = reservations_ui.data_twidget
    request = """SELECT DISTINCT on (rgm.reservation_id)
                rgm.reservation_id, g.first_name, g.last_name, rm.name,  r.date_arrival, r.date_departure, 
                r.is_cancelled, pm.name, r.total_cost, r.commentary
                FROM reservations AS r
                JOIN reservations_guests_rooms as rgm
                ON rgm.reservation_id = r.id
                JOIN guests AS g
                ON g.id = rgm.guest_id
                JOIN rooms as rm
                ON rm.id = rgm.room_id
                JOIN payment_methods AS pm
                ON pm.id = r.payment_method;"""
    keys = ["ID",
            "First name",
            "Last name",
            "Room type",
            "Arrival",
            "Departure",
            "Cancellation",
            "Payment type",
            "Total cost",
            "Commentary"]
    populate_table(request, table, keys)
    table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)

    usr_role = get_usr_role(reservations_ui.hiddenId_lbl.text())
    if usr_role == 'Reader':
        reservations_ui.edit_btn.setEnabled(False)
        reservations_ui.newRes_btn.setEnabled(False)
        reservations_ui.canc_btn.setEnabled(False)
        reservations_ui.rest_btn.setEnabled(False)
        reservations_ui.admin_btn.hide()
    elif usr_role == 'Manager':
        reservations_ui.admin_btn.hide()

    reservation_window.show()


def show_guest_select_window(hide_primary_buttons=False):
    if hide_primary_buttons:
        guest_select_ui.select_btn.hide()
        guest_select_ui.selectRmate_btn.hide()
        guest_select_ui.addGuest_btn.hide()
        guest_select_ui.selectEdit_btn.show()
        guest_select_ui.selectEditRmate_btn.show()
        guest_select_ui.addEditGuest_btn.show()
    else:
        guest_select_ui.selectEdit_btn.hide()
        guest_select_ui.selectEditRmate_btn.hide()
        guest_select_ui.addEditGuest_btn.hide()
        guest_select_ui.select_btn.show()
        guest_select_ui.selectRmate_btn.show()
        guest_select_ui.addGuest_btn.show()

    table = guest_select_ui.select_twidget
    keys = [
        "ID",
        "First name",
        "Last name",
        "Date of birth",
        "Citizenship",
        "First visit",
        "E-mail",
        "Phone"]
    request = """SELECT id, first_name, last_name, date_of_birth, citizenship, is_first_visit, e_mail, phone
                FROM guests;"""
    populate_table(request, table, keys)
    table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
    guest_select_window.show()


def save_rate(form):
    table = rate_window_ui.rate_tWidget
    table2 = form.resRms_twidget
    data = []
    for row in range(table.rowCount()):
        for col in range(table.columnCount()):
            it = table.item(row, col)
            text = it.text()
            data.append(text)
    total = 0
    for i in data:
        if check_int(i):
            total += float(i)
        else:
            pop_up_ui.popup_txt.setText("Please use integers only for rate fields")
            pop_up_widget.show()
    avg_rate = round(total / table.columnCount())
    form.rate_leddit.setText(str(avg_rate))
    if table2.item(0, 8):
        item = QTableWidgetItem(str(total))
        if table2.currentRow() < 0:
            table2.setItem(0, 8, QTableWidgetItem(item))
            table2.item(0, 8).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        else:
            table2.setItem(table2.currentRow(), 8, QTableWidgetItem(item))
            table2.item(table2.currentRow(), 8).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
    show_total_rate(form)
    rate_window.close()


def get_stay_period(form):
    doa = form.doa_daddit.text()
    dod = form.dod_daddit.text()
    arrival = datetime.strptime(doa, '%d.%m.%Y').date()
    departure = datetime.strptime(dod, '%d.%m.%Y').date()
    return (departure - arrival).days


def show_stay_period(form):
    diff = get_stay_period(form)
    form.stay_lbl.setText(f"Stay period: {diff} days")


def show_total_rate(form):
    total = 0
    table = form.resRms_twidget
    if len(form.rate_leddit.text().strip()) == 0 or new_reservation_ui.rate_leddit.text().startswith('-'):
        total = 0
        form.total_lbl.setStyleSheet("color: red")
        form.create_btn.setEnabled(False)
    else:
        for i in range(table.rowCount()):
            if table.item(i, 8):
                item = table.item(i, 8).text()
                total += float(item)
            form.total_lbl.setStyleSheet("color: black")
            form.create_btn.setEnabled(True)

    form.total_lbl.setText(f"Total cost of stay: {total}")


def populate_cbox(request_string, cbox, request_arg=None):
    cursor.execute(request_string, request_arg)
    res = cursor.fetchall()
    data = []
    for i in range(len(res)):
        for y in res[i]:
            if type(y) is str:
                data.append(y)
            else:
                data.append(str(y))
    cbox.addItems(data)


def populate_table(request_string, table, keys_list, request_arg=None):
    cursor.execute(request_string, request_arg)
    data = cursor.fetchall()
    if len(data) == 0:
        table.setRowCount(1)
        table.setColumnCount(len(keys_list))
        table.setHorizontalHeaderLabels(keys_list)
    else:

        res = []
        for i in range(len(data)):
            res.append(dict(zip(keys_list, data[i])))

        for item in res:
            for key, value in item.items():
                item[key] = str(value)

        row_count = len(data)
        column_count = len(data[0])

        table.setRowCount(row_count)
        table.setColumnCount(column_count)
        table.setHorizontalHeaderLabels(keys_list)

        for row in range(row_count):
            for column in range(column_count):
                item = list(res[row].values())[column]
                table.setItem(row, column, QTableWidgetItem(item))
                table.item(row, column).setTextAlignment(Qt.AlignmentFlag.AlignCenter)


def add_guest(hide_primary_buttons=False):
    guest_select_window.close()
    form = guest_add_ui
    fname = form.fname_leddit.text()
    lname = form.lname_leddit.text()
    dob = format_dates(form.dob_deddit.text())
    citiz = form.citiz_leddit.text()
    visit = form.fVisit_cbx.isChecked()
    email = form.email_leddit.text()
    phone = form.phone_leddit.text()

    cursor.execute(f'INSERT INTO guests(first_name, last_name, date_of_birth, citizenship,'
                   f'is_first_visit, e_mail, phone)'
                   f'VALUES ('
                   f'%s,%s,%s,'
                   f'%s,'
                   f'%s,%s,%s);', [fname, lname, dob, citiz, visit, email, phone]
                   )
    conn.commit()
    guest_add_window.close()
    show_guest_select_window(hide_primary_buttons)


def format_dates(date_str):
    d, m, y = date_str.split('.')
    res = f"{y}-{m}-{d}"
    return res


def format_qdate(date_string):
    y, m, d = date_string.split('-')
    res = QDate(int(y), int(m), int(d))
    return res


def validate_stay(form):
    if get_stay_period(form) < 0:
        form.create_btn.setEnabled(False)
        form.total_lbl.hide()
        form.stay_lbl.setStyleSheet("color: red")
    else:
        form.create_btn.setEnabled(True)
        form.total_lbl.show()
        form.stay_lbl.setStyleSheet("color: black")


def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()


def search():
    request = """SELECT DISTINCT on (rgm.reservation_id)
                    rgm.reservation_id, g.first_name, g.last_name, rm.name, r.date_arrival, r.date_departure, 
                    r.is_cancelled, pm.name, r.total_cost, r.commentary
                    FROM reservations AS r
                    JOIN reservations_guests_rooms as rgm
                    ON rgm.reservation_id = r.id
                    JOIN guests AS g
                    ON g.id = rgm.guest_id
                    JOIN rooms as rm
                    ON rm.id = rgm.room_id
                    JOIN payment_methods AS pm
                    ON pm.id = r.payment_method;"""

    table = reservations_ui.data_twidget
    keys = ["ID",
            "First name",
            "Last name",
            "Room type",
            "Arrival",
            "Departure",
            "Cancellation",
            "Payment type",
            "Total cost",
            "Commentary"]
    if len(reservations_ui.id_leddit.text().strip()) > 0:
        arg = reservations_ui.id_leddit.text()
        if check_int(arg):
            request = """SELECT DISTINCT on (rgm.reservation_id)
                            rgm.reservation_id, g.first_name, g.last_name, rm.name,  r.date_arrival, r.date_departure, 
                            r.is_cancelled, pm.name, r.total_cost, r.commentary
                            FROM reservations AS r
                            JOIN reservations_guests_rooms as rgm
                            ON rgm.reservation_id = r.id
                            JOIN guests AS g
                            ON g.id = rgm.guest_id
                            JOIN rooms as rm
                            ON rm.id = rgm.room_id
                            JOIN payment_methods AS pm
                            ON pm.id = r.payment_method
                            WHERE r.id = %s;
                            """
            reservations_ui.id_leddit.clear()
            populate_table(request, table, keys, [arg])
        else:
            pop_up_ui.popup_txt.setText("Please use integer values only")
            pop_up_widget.show()
            reservations_ui.id_leddit.clear()
    elif len(reservations_ui.lname_leddit.text().strip()) > 0:
        arg = reservations_ui.lname_leddit.text()
        if check_int(arg):
            pop_up_ui.popup_txt.setText("Please use letters only")
            pop_up_widget.show()
            reservations_ui.lname_leddit.clear()
        else:
            request = """SELECT DISTINCT on (rgm.reservation_id)
                            rgm.reservation_id, g.first_name, g.last_name, rm.name,  r.date_arrival, r.date_departure, 
                            r.is_cancelled, pm.name, r.total_cost, r.commentary
                            FROM reservations AS r
                            JOIN reservations_guests_rooms as rgm
                            ON rgm.reservation_id = r.id
                            JOIN guests AS g
                            ON g.id = rgm.guest_id
                            JOIN rooms as rm
                            ON rm.id = rgm.room_id
                            JOIN payment_methods AS pm
                            ON pm.id = r.payment_method
                            WHERE g.last_name = %s;
                            """
            populate_table(request, table, keys, [arg])
            reservations_ui.lname_leddit.clear()
    elif len(reservations_ui.doa_deddit.text().strip()) > 0:
        arg = reservations_ui.doa_deddit.text()
        request = """SELECT DISTINCT on (rgm.reservation_id)
                        rgm.reservation_id, g.first_name, g.last_name, rm.name,  r.date_arrival, r.date_departure, 
                        r.is_cancelled, pm.name, r.total_cost, r.commentary
                        FROM reservations AS r
                        JOIN reservations_guests_rooms as rgm
                        ON rgm.reservation_id = r.id
                        JOIN guests AS g
                        ON g.id = rgm.guest_id
                        JOIN rooms as rm
                        ON rm.id = rgm.room_id
                        JOIN payment_methods AS pm
                        ON pm.id = r.payment_method
                        WHERE r.date_arrival = %s;
                        """
        populate_table(request, table, keys, [arg])
    else:
        show_reservation_window()
    table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)


def refresh_reservation_window():
    show_reservation_window()


def add_user():
    form = add_usr_ui
    login = form.login_leddit.text().lower()
    pswd = form.pswd_leddit.text()
    fname = form.fname_leddit.text()
    lname = form.lname_leddit.text()
    email = form.email_leddit.text()
    phone = form.phone_leddit.text()
    date_added = datetime.now()
    if login != '' and pswd !='' and fname != '' and lname != '' and email != '' and phone != '':
        cursor.execute("""INSERT INTO users(login, password, first_name, last_name, e_mail, phone, date_added, role_id)
                          VALUES(%s, %s, %s, %s, %s, %s, %s, %s)""",
                       [login, pswd, fname, lname, email, phone, date_added, 3])

        conn.commit()
        add_usr_window.close()
    else:
        pop_up_ui.popup_txt.setText("Please fill out all fields")
        pop_up_widget.show()


def populate_lbl(request, lbl, request_arg=None, beginning_string="", ending_string=""):
    cursor.execute(request, [request_arg])
    res = cursor.fetchall()
    if len(res) == 0:
        lbl.setText(beginning_string + "None" + ending_string)
    else:
        lbl.setText(beginning_string + str(res[0][0]) + ending_string)


def show_edit_usr_window():
    populate_edit_cbox()
    populate_edit_lbl()
    edit_usr_window.show()


def populate_edit_lbl():
    request = """SELECT r.title
                FROM users AS u
                JOIN roles AS r
                ON r.id = u.role_id
                WHERE u.login = %s"""
    populate_lbl(request,
                 edit_usr_ui.setRole_lbl, edit_usr_ui.usr_cbx.currentText(), "Current role: ")


def populate_edit_cbox():
    usr_cbox = edit_usr_ui.usr_cbx
    usr_cbox.clear()
    request = "SELECT login FROM users;"
    populate_cbox(request, usr_cbox)
    role_cbox = edit_usr_ui.role_cbx
    role_cbox.clear()
    request = "SELECT title FROM roles;"
    populate_cbox(request, role_cbox)


def populate_edit_leddit():
    form = edit_usr_ui
    arg = form.usr_cbx.currentText().lower()
    if len(arg) > 0:
        cursor.execute("""
        SELECT login, password, first_name, last_name, e_mail, phone from users where login = %s;""", [arg])
        data = cursor.fetchall()[0]
        form.login_leddit.setText(data[0])
        form.pswd_leddit.setText(data[1])
        form.fname_leddit.setText(data[2])
        form.lname_leddit.setText(data[3])
        form.email_leddit.setText(data[4])
        form.phone_leddit.setText(data[5])


def save_usr_edit():
    form = edit_usr_ui
    usr_login = form.usr_cbx.currentText()
    cursor.execute("""SELECT id FROM users WHERE login = %s""", [usr_login])
    usr_id = cursor.fetchall()[0][0]
    role_title = form.role_cbx.currentText()
    cursor.execute("""SELECT id
    FROM roles
    WHERE title = %s""", [role_title])
    role_id = cursor.fetchall()[0][0]

    cursor.execute("""UPDATE users 
    SET login = %s, password = %s, first_name = %s, last_name = %s, e_mail = %s, phone = %s, role_id = %s
    WHERE id = %s""",
                   [form.login_leddit.text(), form.pswd_leddit.text(), form.fname_leddit.text(),
                    form.lname_leddit.text(), form.email_leddit.text(), form.phone_leddit.text(),
                    role_id, usr_id])  #refactor to use login instead of usr_id?
    conn.commit()
    populate_edit_leddit()
    populate_edit_lbl()
    pop_up_ui.popup_txt.setText("Changes saved")
    pop_up_widget.show()


def populate_delete_window():
    table = delete_usr_ui.usr_twidget
    request = """SELECT u.id, u.login, u.first_name, u.last_name, r.title, r.description, u.date_added
                FROM users AS u
                JOIN roles AS r
                ON u.role_id = r.id"""
    keys = ["ID", "Login", "First name", "Last name", "Role", "Role description", "Date added"]
    populate_table(request, table, keys)
    table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)


def show_delete_usr_window():
    populate_delete_window()
    delete_usr_window.show()


def delete_usr():
    usr_id = delete_usr_ui.usr_twidget.item(delete_usr_ui.usr_twidget.currentRow(), 0).text()
    cursor.execute("""DELETE FROM users WHERE id = %s;
    """, [usr_id])
    conn.commit()
    populate_delete_window()


def populate_room_id_cbx(form):
    form.rmNum_cbx.clear()
    room_type = form.roomtype_cbox.currentText()
    arrival = format_dates(form.doa_daddit.text())
    departure = format_dates(form.dod_daddit.text())
    reserved_id = []
    for row in range(form.resRms_twidget.rowCount()):
        reserved_id.append(form.resRms_twidget.item(row, 6).text())
    request = """
    SELECT id FROM rooms WHERE name = %s
    AND id NOT IN 
    (SELECT rooms.id
    FROM rooms
    JOIN reservations_guests_rooms AS rgm
    ON rooms.id = rgm.room_id
    JOIN reservations AS r
    ON r.id = rgm.reservation_id
    WHERE r.is_cancelled != true 
    AND (r.date_arrival, r.date_departure) 
    OVERLAPS (%s, %s))
    AND id != ALL(%s::int[]);"""
    populate_cbox(request, form.rmNum_cbx, [room_type, arrival, departure, reserved_id])


def delete_selected_row(table):
    row = table.currentRow()
    table.removeRow(row)


def del_rm(form):
    table = form.resRms_twidget
    reserved_id = []
    for row in range(table.rowCount()):
        reserved_id.append(table.item(row, 0).text())
    row = table.currentRow()
    if table.item(row, 0):
        reserved_id.pop(reserved_id.index(table.item(row, 0).text()))
        delete_selected_row(form.resRms_twidget)
    else:
        delete_selected_row(form.resRms_twidget)
    if table.rowCount() <= 0:
        form.doa_daddit.setEnabled(True)
        form.dod_daddit.setEnabled(True)

    show_total_rate(form)
    populate_room_id_cbx(form)
    validate_room_capacity(form)


def add_roommate(form):
    table = guest_select_ui.select_twidget
    table2 = form.resRms_twidget
    if (table.item(table.currentRow(), 0) and table2.item(table2.currentRow(), 5)
            and table2.item(table2.currentRow(), 6).text()):
        guest_id = table.item(table.currentRow(), 0).text()
        arrival = table2.item(table2.currentRow(), 1).text()
        departure = table2.item(table2.currentRow(), 2).text()
        first_name = table.item(table.currentRow(), 1).text()
        last_name = table.item(table.currentRow(), 2).text()
        room_type = table2.item(table2.currentRow(), 5).text()
        room_id = table2.item(table2.currentRow(), 6).text()
        payment_method = table2.item(table2.currentRow(), 7).text()
        total_cost = '0'
        col_values = [
            guest_id, arrival, departure, first_name, last_name, room_type, room_id, payment_method, total_cost]
        row = table2.rowCount()
        table2.insertRow(row)
        for column in range(table2.columnCount()):
            item = col_values[column]
            table2.setItem(row, column, QTableWidgetItem(item))
            table2.item(row, column).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        guest_select_window.close()
        show_total_rate(form)
        populate_room_id_cbx(form)
        validate_room_capacity(form)


def get_selected_data(form):
    table = guest_select_ui.select_twidget
    table2 = form.resRms_twidget
    guest_id = table.item(table.currentRow(), 0)
    arrival = format_dates(form.doa_daddit.text())
    departure = format_dates(form.dod_daddit.text())
    first_name = table.item(table.currentRow(), 1)
    last_name = table.item(table.currentRow(), 2)
    room_type = form.roomtype_cbox.currentText()
    room_id = form.rmNum_cbx.currentText()
    payment_method = form.payment_cbx.currentText()
    if check_int(form.rate_leddit.text()):
        total_cost = str((float(get_stay_period(form))) * (float(form.rate_leddit.text())))
        col_values = [guest_id, arrival, departure, first_name, last_name, room_type, room_id, payment_method, total_cost]
        row = table2.rowCount()
        table2.insertRow(row)
        for column in range(table2.columnCount()):
            item = col_values[column]
            table2.setItem(row, column, QTableWidgetItem(item))
            table2.item(row, column).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        guest_select_window.close()
        form.doa_daddit.setEnabled(False)
        form.dod_daddit.setEnabled(False)
        show_total_rate(form)
        populate_room_id_cbx(form)
        validate_room_capacity(form)
    else:
        pop_up_ui.popup_txt.setText("Please use integers only for rate field")
        pop_up_widget.show()


def set_current_date(form):
    today = str(date.today())
    y, m, d = today.split('-')
    today = QDate(int(y), int(m), int(d))
    form.doa_daddit.setDate(today)
    form.dod_daddit.setDate(today)
    form.doa_daddit.setMinimumDate(today)


def show_new_res_window():
    form = new_reservation_ui
    set_current_date(form)
    form.rmNum_cbx.clear()
    form.payment_cbx.clear()
    form.roomtype_cbox.clear()
    populate_cbox("SELECT name FROM payment_methods;", new_reservation_ui.payment_cbx)
    populate_cbox("SELECT DISTINCT name FROM rooms;", new_reservation_ui.roomtype_cbox)
    res_keys = [
        "Guest ID",
        "Arrival",
        "Departure",
        "First name",
        "Last name",
        "Room type",
        "Room ID",
        "Payment Method",
        "Total cost"
    ]
    res_table = new_reservation_ui.resRms_twidget
    res_table.setColumnCount(len(res_keys))
    res_table.setHorizontalHeaderLabels(res_keys)
    res_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    res_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
    clear_table(res_table)
    populate_room_id_cbx(form)
    new_res_window.show()


def validate_room_capacity(form):
    table = form.resRms_twidget
    column = 6
    room_id = set()
    room_occupancy = {}
    for row in range(table.rowCount()):
        _item = table.item(row, column)
        if _item:
            item = table.item(row, column).text()
            room_id.add(item)
            cursor.execute("""SELECT maximum_capacity FROM rooms WHERE id = %s""", [item])
            if item in room_occupancy:
                _i = room_occupancy[item][1]
                _i += 1
                room_occupancy[item] = [cursor.fetchall()[0][0], _i]
            else:
                room_occupancy[item] = [cursor.fetchall()[0][0], 1]

    for i in room_occupancy:
        if room_occupancy[i][0] < room_occupancy[i][1]:
            form.create_btn.setEnabled(False)
            pop_up_ui.popup_txt.setText(
                f"Room capacity exceeded! Room ID:{i} Capacity: {room_occupancy[i][1]}/{room_occupancy[i][0]}")
            break
        else:
            form.create_btn.setEnabled(True)


def show_res_details():
    details_table = details_ui.details_twidget
    for row in range(details_table.rowCount()):
        details_table.removeRow(row)
    reservations_table = reservations_ui.data_twidget
    res_id = reservations_table.item(reservations_table.currentRow(), 0)
    if res_id:
        res_id = str(res_id.text())
        keys = [
            "ID",
            "Arrival",
            "Departure",
            "First name",
            "Last name",
            "Room category",
            "Room id"
        ]
        request = """
        SELECT DISTINCT r.id, r.date_arrival, r.date_departure, g.first_name, g.last_name, rm.name, rm.id
        FROM reservations_guests_rooms AS rgm
        JOIN reservations AS r
        ON rgm.reservation_id = r.id
        JOIN guests AS g
        ON rgm.guest_id = g.id
        JOIN rooms AS rm
        ON rgm.room_id = rm.id
        WHERE r.id = %s;"""
        populate_table(request, details_table, keys, [res_id])
        details_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        details_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        details_window.show()


def show_add_guest_window():
    guest_add_ui.fname_leddit.clear()
    guest_add_ui.lname_leddit.clear()
    guest_add_ui.dob_deddit.clear()
    guest_add_ui.citiz_leddit.clear()
    guest_add_ui.email_leddit.clear()
    guest_add_ui.phone_leddit.clear()
    guest_add_ui.fVisit_cbx.setChecked(False)
    guest_add_window.show()


def show_edit_res_window():
    edit_form = edit_reservation_ui
    res_form = reservations_ui
    res_table = res_form.data_twidget
    if res_table.item(res_table.currentRow(), 0):
        res_id = res_table.item(res_table.currentRow(), 0).text()
        edit_table = edit_form.resRms_twidget
        doa = res_table.item(res_table.currentRow(), 4).text()
        dod = res_table.item(res_table.currentRow(), 5).text()
        qdate = format_qdate(doa)
        edit_form.doa_daddit.setDate(qdate)
        qdate = format_qdate(dod)
        edit_form.dod_daddit.setDate(qdate)
        arrival = datetime.strptime(doa, '%Y-%m-%d').date()
        departure = datetime.strptime(dod, '%Y-%m-%d').date()
        total_cost = float(res_table.item(res_table.currentRow(), 8).text())
        diff = (departure - arrival).days
        edit_form.rate_leddit.setText(str(total_cost / diff))
        edit_form.resId_lbl.setText(res_id)
        edit_form.resId_lbl.hide()
        edit_form.doa_daddit.setEnabled(False)
        edit_form.dod_daddit.setEnabled(False)
        edit_form.rmNum_cbx.clear()
        edit_form.payment_cbx.clear()
        edit_form.roomtype_cbox.clear()

        populate_cbox("SELECT name FROM payment_methods;", edit_form.payment_cbx)
        populate_cbox("SELECT DISTINCT name FROM rooms;", edit_form.roomtype_cbox)

        res_keys = [
            "Guest ID",
            "Arrival",
            "Departure",
            "First name",
            "Last name",
            "Room type",
            "Room ID",
            "Payment Method",
            "Total cost"
        ]

        request = """SELECT g.id, r.date_arrival, r.date_departure, g.first_name, g.last_name, rm.name, rm.id,
                    pm.name, r.total_cost
                    FROM reservations_guests_rooms AS rgm
                    JOIN reservations AS r
                    ON rgm.reservation_id = r.id
                    JOIN guests AS g
                    ON rgm.guest_id = g.id
                    JOIN rooms AS rm
                    ON rgm.room_id = rm.id
                    JOIN payment_methods AS pm
                    ON pm.id = r.payment_method
                    WHERE r.id = %s;"""
        populate_table(request, edit_table, res_keys, [res_id])
        edit_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        edit_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        for row in range(1, edit_table.rowCount()):
            edit_table.setItem(row, 8, QTableWidgetItem('0'))
            edit_table.item(row, 8).setTextAlignment(Qt.AlignmentFlag.AlignCenter)

        edit_form.comment_leddit.setText(res_table.item(res_table.currentRow(), 9).text())
        show_total_rate(edit_form)
        populate_room_id_cbx(edit_form)
        edit_reservation_window.show()
    else:
        pop_up_ui.popup_txt.setText("PLease select a reservation")
        pop_up_widget.show()


def clear_table(table):
    table.setRowCount(0)


def create_reservation():
    reservation_window.close()
    form = new_reservation_ui
    table = form.resRms_twidget
    reservation_comment = str(form.comment_leddit.text()).lower()
    cursor.execute(f"SELECT id FROM payment_methods WHERE name = '{str(form.payment_cbx.currentText()).lower()}';")
    payment_id = str(cursor.fetchall()[0][0])
    cost = form.total_lbl.text()[20:]
    cancelled = False
    created_by = reservations_ui.hiddenId_lbl.text()
    arrival = format_dates(form.doa_daddit.text())
    departure = format_dates(form.dod_daddit.text())

    guests_rooms_id = []
    for row in range(table.rowCount()):
        guest_id = table.item(row, 0)
        room_id = table.item(row, 6)
        if guest_id and room_id:
            guests_rooms_id.append([str(guest_id.text()), str(room_id.text())])

    if len(guests_rooms_id) <= 0:
        pop_up_ui.popup_txt.setText("Please add at least one guest")
        pop_up_widget.show()
    else:
        cursor.execute("""INSERT INTO reservations(date_arrival, date_departure, total_cost, payment_method, commentary,
                       is_cancelled, created_by, last_update_by)
                       VALUES (
                       %s, %s,
                       %s, %s,
                       %s, %s,
                       %s, %s);""",
                       [arrival, departure,
                        cost, payment_id,
                        reservation_comment, cancelled,
                        created_by, created_by]
                       )
        conn.commit()

        cursor.execute("""SELECT id FROM reservations
                        ORDER BY id DESC
                        LIMIT 1;""")

        new_res_id = cursor.fetchall()[0][0]

        for item in range(len(guests_rooms_id)):
            cursor.execute("""
                            INSERT INTO reservations_guests_rooms (reservation_id, guest_id, room_id)
                            VALUES( %s, %s, %s);""", [new_res_id, guests_rooms_id[item][0], guests_rooms_id[item][1]]
                           )
            conn.commit()
        show_reservation_window()
        new_res_window.close()


def update_reservation():
    form = edit_reservation_ui
    table = form.resRms_twidget
    res_id = form.resId_lbl.text()
    reservation_comment = str(form.comment_leddit.text()).lower()
    cursor.execute(f"SELECT id FROM payment_methods WHERE name = '{str(form.payment_cbx.currentText()).lower()}';")
    payment_id = str(cursor.fetchall()[0][0])
    cost = form.total_lbl.text()[20:]
    created_by = reservations_ui.hiddenId_lbl.text()
    arrival = format_dates(form.doa_daddit.text())
    departure = format_dates(form.dod_daddit.text())

    guests_rooms_id = []
    for row in range(table.rowCount()):
        guest_id = table.item(row, 0)
        room_id = table.item(row, 6)
        if guest_id and room_id:
            guests_rooms_id.append([str(guest_id.text()), str(room_id.text())])
    cursor.execute("""UPDATE reservations SET
                    date_arrival = %s,
                    date_departure = %s,
                    total_cost = %s,
                    payment_method = %s,
                    commentary = %s,
                    last_update_by = %s
                    WHERE id = %s;""",
                   [arrival, departure,
                    cost, payment_id,
                    reservation_comment,
                    created_by, res_id]
                   )
    conn.commit()

    cursor.execute("""DELETE FROM reservations_guests_rooms WHERE reservation_id = %s;"""
                   , [res_id])
    conn.commit()

    for item in range(len(guests_rooms_id)):
        cursor.execute("""
                        INSERT INTO reservations_guests_rooms (reservation_id, guest_id, room_id)
                        VALUES( %s, %s, %s);""", [res_id, guests_rooms_id[item][0], guests_rooms_id[item][1]]
                       )
        conn.commit()
    show_reservation_window()
    edit_reservation_window.close()


def cancel_res():
    table = reservations_ui.data_twidget
    res_id = table.item(table.currentRow(), 0).text()
    usr_id = reservations_ui.hiddenId_lbl.text()
    cursor.execute("""UPDATE reservations SET 
                    is_cancelled = true,
                    last_update_by = %s 
                    WHERE id = %s;""", [usr_id, res_id])
    conn.commit()
    refresh_reservation_window()


def reinstate_res():
    table = reservations_ui.data_twidget
    res_id = table.item(table.currentRow(), 0).text()
    usr_id = reservations_ui.hiddenId_lbl.text()
    cursor.execute("""UPDATE reservations SET 
                    is_cancelled = false,
                    last_update_by = %s 
                    WHERE id = %s;""", [usr_id, res_id])
    conn.commit()
    refresh_reservation_window()


def show_report_window():
    table = report_ui.reports_twidget
    keys = [
        "ID",
        "First name",
        "Last name",
        "Room type",
        "Room ID",
        "Arrival",
        "Departure",
        "Cancellation",
        "Payment type",
        "Total cost",
        "Commentary"
    ]
    table.setColumnCount(len(keys))
    table.setHorizontalHeaderLabels(keys)
    table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
    clear_table(table)
    report_window.show()


def generate_report(report_type):
    table = report_ui.reports_twidget
    clear_table(table)
    date_data = report_ui.report_daddit.text()
    include_cancelled = report_ui.incCanc_chbx.isChecked()
    request = """SELECT
                 rgm.reservation_id, g.first_name, g.last_name, rm.name, rm.id,  r.date_arrival, r.date_departure, 
                 r.is_cancelled, pm.name, r.total_cost, r.commentary
                 FROM reservations AS r
                 JOIN reservations_guests_rooms as rgm
                 ON rgm.reservation_id = r.id
                 JOIN guests AS g
                 ON g.id = rgm.guest_id
                 JOIN rooms as rm
                 ON rm.id = rgm.room_id
                 JOIN payment_methods AS pm
                 ON pm.id = r.payment_method                 
                 ;"""
    keys = [
        "ID",
        "First name",
        "Last name",
        "Room type",
        "Room ID",
        "Arrival",
        "Departure",
        "Cancellation",
        "Payment type",
        "Total cost",
        "Commentary"
    ]
    if include_cancelled:
        if report_type == "arrivals":
            request = request[:-1] + " WHERE date_arrival = %s ORDER BY rgm.reservation_id;"
            populate_table(request, table, keys, [date_data])
        elif report_type == "departures":
            request = request[:-1] + " WHERE date_departure = %s ORDER BY rgm.reservation_id;"
            populate_table(request, table, keys, [date_data])
    else:
        if report_type == "arrivals":
            request = request[:-1] + " WHERE date_arrival = %s AND is_cancelled = false ORDER BY rgm.reservation_id;"
            populate_table(request, table, keys, [date_data])
        elif report_type == "departures":
            request = request[:-1] + " WHERE date_departure = %s AND is_cancelled = false ORDER BY rgm.reservation_id;"
            populate_table(request, table, keys, [date_data])
    dup_rooms_id = []
    for row in range(table.rowCount()):
        if table.item(row, 0):
            if table.item(row, 0).text() in dup_rooms_id:
                table.setItem(row, 9, QTableWidgetItem(''))
                table.item(row, 9).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                table.setItem(row, 10, QTableWidgetItem(''))
            else:
                dup_rooms_id.append(table.item(row, 0).text())

    total = 0.0
    for row in range(table.rowCount()):
        if table.item(row, 9):
            if table.item(row, 9).text() != '' and table.item(row, 7).text() != 'True':
                item = table.item(row, 9).text()
                total += float(item)

    table.insertRow(table.rowCount())
    final_row = table.rowCount()
    table.insertRow(final_row)
    table.setItem(final_row, 10, QTableWidgetItem("Final cost: " + str(total)))


def save_report():
    data = []
    table = report_ui.reports_twidget
    table_headers = [table.horizontalHeaderItem(col).text() for col in range(table.columnCount())]

    for row in range(table.rowCount()):
        entry = [table.item(row, col).text()
                 if table.item(row, col) is not None else "" for col in range(table.columnCount())]
        data.append(entry)

    data_frame = pandas.DataFrame(data, columns=table_headers)

    file_dialog = QFileDialog()
    path, _ = file_dialog.getSaveFileName(None, "Save file", "", "Excel Files (*.xlsx);;All Files (*)")

    if path:
        data_frame.to_excel(path, index=False)

    pop_up_ui.popup_txt.setText("Saved successfully")
    pop_up_widget.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    login_window = QMainWindow()
    main_window = QMainWindow()
    reservation_window = QMainWindow()
    new_res_window = QMainWindow()
    rate_window = QMainWindow()
    guest_details_window = QMainWindow()
    guest_select_window = QMainWindow()
    guest_add_window = QMainWindow()
    admin_window = QMainWindow()
    add_usr_window = QMainWindow()
    edit_usr_window = QMainWindow()
    delete_usr_window = QMainWindow()
    details_window = QMainWindow()
    edit_reservation_window = QMainWindow()
    edit_res_rate_edit_window = QMainWindow()
    report_window = QMainWindow()

    pop_up_widget = QWidget()

    login_ui = Ui_LoginWindow()
    main_ui = Ui_MainWindow()
    reservations_ui = Ui_ReservationsWindow()
    new_reservation_ui = Ui_NewResWindow()
    rate_window_ui = Ui_RateWindow()
    guest_details_ui = Ui_GuesDetailsWindow()
    guest_select_ui = Ui_SelectGuestWIndow()
    guest_add_ui = Ui_AddGuestWindow()
    admin_ui = Ui_AdminWindow()
    add_usr_ui = Ui_AddUserWindow()
    edit_usr_ui = Ui_EditUserWindow()
    delete_usr_ui = Ui_DeleteUsrWindow()
    details_ui = Ui_DetailsMAinWindow()
    edit_reservation_ui = Ui_EditResWindow()
    edit_res_rate_edit_ui = Ui_ResEditRateWindow()
    report_ui = Ui_ReportWindow()

    pop_up_ui = Ui_PopUp()

    login_ui.setupUi(login_window)
    main_ui.setupUi(main_window)
    reservations_ui.setupUi(reservation_window)
    new_reservation_ui.setupUi(new_res_window)
    rate_window_ui.setupUi(rate_window)
    guest_details_ui.setupUi(guest_details_window)
    guest_select_ui.setupUi(guest_select_window)
    guest_add_ui.setupUi(guest_add_window)
    admin_ui.setupUi(admin_window)
    add_usr_ui.setupUi(add_usr_window)
    edit_usr_ui.setupUi(edit_usr_window)
    delete_usr_ui.setupUi(delete_usr_window)
    details_ui.setupUi(details_window)
    edit_reservation_ui.setupUi(edit_reservation_window)
    edit_res_rate_edit_ui.setupUi(edit_res_rate_edit_window)
    report_ui.setupUi(report_window)

    pop_up_ui.setupUi(pop_up_widget)

    login_window.show()

    login_ui.submit_btn.clicked.connect(login)
    reservations_ui.newRes_btn.clicked.connect(show_new_res_window)
    reservations_ui.search_btn.clicked.connect(search)
    reservations_ui.refresh_btn.clicked.connect(refresh_reservation_window)
    reservations_ui.admin_btn.clicked.connect(admin_window.show)
    reservations_ui.details_btn.clicked.connect(show_res_details)
    reservations_ui.report_btn.clicked.connect(show_report_window)
    reservations_ui.edit_btn.clicked.connect(show_edit_res_window)
    reservations_ui.canc_btn.clicked.connect(cancel_res)
    reservations_ui.rest_btn.clicked.connect(reinstate_res)

    details_ui.close_btn.clicked.connect(details_window.close)

    report_ui.arrReport_btn.clicked.connect(lambda: generate_report("arrivals"))
    report_ui.depReport_btn.clicked.connect(lambda: generate_report("departures"))
    report_ui.canc_btn.clicked.connect(report_window.close)
    report_ui.save_btn.clicked.connect(save_report)

    edit_reservation_ui.doa_daddit.dateChanged.connect(lambda: show_stay_period(edit_reservation_ui))
    edit_reservation_ui.dod_daddit.dateChanged.connect(lambda: show_stay_period(edit_reservation_ui))
    edit_reservation_ui.doa_daddit.dateChanged.connect(lambda: show_total_rate(edit_reservation_ui))
    edit_reservation_ui.dod_daddit.dateChanged.connect(lambda: show_total_rate(edit_reservation_ui))
    edit_reservation_ui.doa_daddit.dateChanged.connect(lambda: validate_stay(edit_reservation_ui))
    edit_reservation_ui.dod_daddit.dateChanged.connect(lambda: validate_stay(edit_reservation_ui))
    edit_reservation_ui.dod_daddit.dateChanged.connect(lambda: populate_room_id_cbx(edit_reservation_ui))
    edit_reservation_ui.doa_daddit.dateChanged.connect(lambda: populate_room_id_cbx(edit_reservation_ui))
    edit_reservation_ui.rate_leddit.textChanged.connect(lambda: show_total_rate(edit_reservation_ui))
    edit_reservation_ui.roomtype_cbox.currentTextChanged.connect(lambda: populate_room_id_cbx(edit_reservation_ui))
    edit_reservation_ui.rateEdit_btn.clicked.connect(lambda:
                                                     populate_rate_window(edit_reservation_ui, True))
    edit_reservation_ui.selectGuest_btn.clicked.connect(lambda: show_guest_select_window(True))
    edit_reservation_ui.drm_btn.clicked.connect(lambda: del_rm(edit_reservation_ui))
    edit_reservation_ui.drm_btn.clicked.connect(lambda: populate_room_id_cbx(edit_reservation_ui))
    edit_reservation_ui.create_btn.clicked.connect(update_reservation)
    edit_reservation_ui.exit_Btn.clicked.connect(edit_reservation_window.close)

    new_reservation_ui.doa_daddit.dateChanged.connect(lambda: show_stay_period(new_reservation_ui))
    new_reservation_ui.dod_daddit.dateChanged.connect(lambda: show_stay_period(new_reservation_ui))
    new_reservation_ui.doa_daddit.dateChanged.connect(lambda: show_total_rate(new_reservation_ui))
    new_reservation_ui.dod_daddit.dateChanged.connect(lambda: show_total_rate(new_reservation_ui))
    new_reservation_ui.doa_daddit.dateChanged.connect(lambda: validate_stay(new_reservation_ui))
    new_reservation_ui.dod_daddit.dateChanged.connect(lambda: validate_stay(new_reservation_ui))
    new_reservation_ui.dod_daddit.dateChanged.connect(lambda: populate_room_id_cbx(new_reservation_ui))
    new_reservation_ui.doa_daddit.dateChanged.connect(lambda: populate_room_id_cbx(new_reservation_ui))
    new_reservation_ui.rate_leddit.textChanged.connect(lambda: show_total_rate(new_reservation_ui))
    new_reservation_ui.roomtype_cbox.currentTextChanged.connect(lambda: populate_room_id_cbx(new_reservation_ui))
    new_reservation_ui.rateEdit_btn.clicked.connect(lambda: populate_rate_window(new_reservation_ui))
    new_reservation_ui.selectGuest_btn.clicked.connect(show_guest_select_window)
    new_reservation_ui.create_btn.clicked.connect(create_reservation)
    new_reservation_ui.exit_Btn.clicked.connect(new_res_window.close)
    new_reservation_ui.drm_btn.clicked.connect(lambda: del_rm(new_reservation_ui))
    new_reservation_ui.drm_btn.clicked.connect(lambda: populate_room_id_cbx(new_reservation_ui))

    rate_window_ui.save_btn.clicked.connect(lambda: save_rate(new_reservation_ui))
    rate_window_ui.saveEdit_btn.clicked.connect(lambda: save_rate(edit_reservation_ui))

    guest_select_ui.select_btn.clicked.connect(lambda: get_selected_data(new_reservation_ui))
    guest_select_ui.selectRmate_btn.clicked.connect(lambda: add_roommate(new_reservation_ui))
    guest_select_ui.selectEdit_btn.clicked.connect(lambda: get_selected_data(edit_reservation_ui))
    guest_select_ui.selectEditRmate_btn.clicked.connect(lambda: add_roommate(edit_reservation_ui))
    guest_select_ui.addGuest_btn.clicked.connect(show_add_guest_window)
    guest_select_ui.close_btn.clicked.connect(guest_select_window.close)

    guest_add_ui.add_btn.clicked.connect(add_guest)
    guest_add_ui.canc_btn.clicked.connect(guest_add_window.close)

    admin_ui.addUsr_btn.clicked.connect(add_usr_window.show)
    admin_ui.editUsr_btn.clicked.connect(show_edit_usr_window)
    admin_ui.deleteUsr_btn.clicked.connect(show_delete_usr_window)

    add_usr_ui.add_btn.clicked.connect(add_user)
    add_usr_ui.canc_btn.clicked.connect(add_usr_window.close)

    edit_usr_ui.canc_btn.clicked.connect(edit_usr_window.close)
    edit_usr_ui.usr_cbx.currentTextChanged.connect(populate_edit_leddit)
    edit_usr_ui.usr_cbx.currentTextChanged.connect(populate_edit_lbl)
    edit_usr_ui.save_btn.clicked.connect(save_usr_edit)

    delete_usr_ui.delete_btn.clicked.connect(delete_usr)
    delete_usr_ui.close_btn.clicked.connect(delete_usr_window.close)

    sys.exit(app.exec())
