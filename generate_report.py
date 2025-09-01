import sqlite3

def generate_report():
    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT employees.id, employees.name, employees.position, 
               attendance.punch_in_time, attendance.punch_out_time
        FROM attendance
        INNER JOIN employees ON attendance.employee_id = employees.id
        ORDER BY attendance.punch_in_time DESC
    """)

    records =cursor.fetchall()
    conn.close()

    if not records:
        print("No records found.")
        return
    
    print("\n ---Attendance Report ---\n")
    print(f"{'ID':<5}{'Name':<15}{'Position':<15}{'Punch in':<20}{'Punch Out':<20}")
    print("-"*75)

    for record in records:
        employee_id, name, position, punch_in, punch_out = record
        print(f"{employee_id:<5}{name:<15}{position:<15}{punch_in:<20}{punch_out or 'Still working' }")

def main():
    print("Generating attendance report...")
    generate_report()

if __name__ == '__main__':
    main()