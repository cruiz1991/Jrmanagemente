
from datetime import datetime
import sqlite3

#Ensure the user is valid

def is_valid_employee(employee_id):
    conn = sqlite3.connect('rrtables.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM employees WHERE id = ?", (employee_id,))
    result = cursor.fetchone()
    conn.close()
    return result is not None



# Punch-in:


def punch_in(employee_id):
    conn=sqlite3.connect('rrtables.db')
    cursor=conn.cursor()

    # Get the current time as a string (this will be the punch-in time)
        
    punch_in_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Insert the punch-in time into the database
    cursor.execute('INSERT INTO rrtables (employee_id, punch_in_time) VALUES (?, ?)',( employee_id, punch_in_time))
    conn.commit()
    conn.close()
    print(f'Employee {employee_id} came in at {punch_in_time} and punched in successfully.')



# Punch-out :


def punch_out(employee_id):
    conn=sqlite3.connect('rrtables.db')
    cursor=conn.cursor()

    # Get the current time as a string (this will be the punch-out time)
        
    punch_out_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Update the punch-out time in the database
    cursor.execute("UPDATE rrtables SET punch_out_time = ? WHERE employee_id = ? AND punch_out_time IS NULL", ( punch_out_time, employee_id))
    conn.commit()
    conn.close()

    print(f'Employee {employee_id} went out at {punch_out_time} and punched out successfully.')

def main():
    print('Welcome to the RIOR rrtables system')
    employee_id = input('Enter your employee ID: ')
    action= input('Press (1) To Punch in or (2) To Punch out: ')
    if action == '1':
        punch_in(employee_id)
    elif action == '2':
        punch_out(employee_id)
    else:
        print('Invalid input. Please try again.')
                        
if __name__ == '__main__':
    main()
    
    # Query to verify the employees in the database

    conn=sqlite3.connect('rrtables.db')
    cursor =conn.cursor()
    cursor.execute("SELECT * FROM rrtables")
    rrtables =cursor.fetchall()
    print(rrtables)


