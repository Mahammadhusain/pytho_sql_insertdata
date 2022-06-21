import mysql.connector

# -------- Api Call -------------
# importing the requests library
import requests

# --------- Database Connection --------------
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="demo"  # Running database name
)


URL = "https://lspcdata.com/api/v1/app_coverage?limit=100"

# sending get request and saving the response as response object
r = requests.get(url=URL)

# extracting data in json format
response = r.json()['data']['app_coverage']
for i in response:

    mycursor = mydb.cursor()

    sql = """
    INSERT INTO userdata 
    (id, collection_id, patid, fname, mname, 
    lname, suffix, gender, dob, living_california, 
    county, homeless, address,apt, city, state, zip_code, 
    mailing_address, apt2, city2, state2, zip2, contact_no, 
    other_phone, email, speak_language, read_language, ssn, 
    us_citizen, naturalized, alien_no, naturalization_no, eligible_immi, 
    immi_doc_type, immi_status, immi_name, immi_alienno, immi_i94_no, immi_passportno, 
    immi_country, immi_sevisid, immi_other, medicare, health_ins, sign, 
    signdt, appc_pdf, client_id, created_at, updated_at, deleted_at, 
    created_by, updated_by, deleted_by)

    VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,
    %s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,
    %s, %s,%s, %s,%s, %s,%s, %s,%s,%s,%s, %s,%s,%s)
    """
    val = (
    i['id'],
    i['collection_id'],
    i['patid'],
    i['fname'],
    i['mname'],
    i['lname'],
    i['suffix'],
    i['gender'],
    i['dob'],
    i['living_california'],
    i['county'],
    i['homeless'],
    i['address'],
    i['apt'],
    i['city'],
    i['state'],
    i['zip'],
    i['mailing_address'],
    i['apt2'],
    i['city2'],
    i['state2'],
    i['zip2'],
    i['contact_no'],
    i['other_phone'],
    i['email'],
    i['speak_language'],
    i['read_language'],
    i['ssn'],
    i['us_citizen'],
    i['naturalized'],
    i['alien_no'],
    i['naturalization_no'],
    i['eligible_immi'],
    i['immi_doc_type'],
    i['immi_status'],
    i['immi_name'],
    i['immi_alienno'],
    i['immi_i94_no'],
    i['immi_passportno'],
    i['immi_country'],
    i['immi_sevisid'],
    i['immi_other'],
    i['medicare'],
    i['health_ins'],
    i['sign'],
    i['signdt'],
    i['appc_pdf'],
    i['client_id'],
    i['created_at'],
    i['updated_at'],
    i['deleted_at'],
    i['created_by'],
    i['updated_by'],
    i['deleted_by'],

    )
    mycursor.execute(sql, val)

    mydb.commit()  # Save data in table

    print(mycursor.rowcount, "record inserted.")


