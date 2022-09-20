import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import smtplib
from email.message import EmailMessage


# Connecting MYSQL and Python
connector = mysql.connector.connect(host = "localhost" , user = "root" , password = "H@ri_005" , database = "sars")
mysql_cursor = connector.cursor()

# Creating a Mainwindow
Home_screen = Tk()
Home_screen.title("SARS - Student Assessment Recording System")
screen_width = Home_screen.winfo_screenwidth()
screen_height = Home_screen.winfo_screenheight()
app_width = 700
app_height = 300
x_coordinate = int((screen_width/2) - (app_width/2))
y_coordinate = int((screen_height/2) - (app_height/2))
Home_screen.geometry(f'{app_width}x{app_height}+{x_coordinate}+{y_coordinate}')
Home_screen.resizable(width = False  , height = False)
Home_screen["bg"] = "sky blue"


# Dropping marks into the MYSQL Table
def add_recs(adm_num , cls , section , exam):
   if cls_or_grp == "1 or 2":
      sql = "INSERT INTO 1st_2nd_std(Admn_num , Class , Sec , Exam , English , EVS , Maths , Tamil) VALUES(%s , %s , %s , %s , %s , %s , %s , %s);"
      value = (adm_num , cls , section , exam , int(eng_entry_1.get()) , int(mat_entry_1.get()) , int(evs_entry_1.get()) , int(tam_entry_1.get()))

      mysql_cursor.execute(sql , value)
      connector.commit()
      
      Exam.current(0)
      add_class.current(0)
      add_sec.current(0)
      admn_number.delete(0  ,END)
      eng_entry_1.delete(0 , END)
      mat_entry_1.delete(0 , END)
      evs_entry_1.delete(0 , END)
      tam_entry_1.delete(0 , END)

   elif cls_or_grp == "3 or 4":
      sql = "INSERT INTO 3rd_4th_std(Admn_num , Class , Sec , Exam , English , EVS , Maths , II_Lang , III_Lang , ICT) VALUES (%s , %s , %s , %s , %s , %s , %s , %s , %s , %s);"
      value = (adm_num , cls , section , exam , int(eng_entry_3.get()) , int(evs_entry_3.get()) , int(mat_entry_3.get()) , int(II_Lang_entry_3.get()) , int(III_Lang_entry_3.get()) , int(Computer_science_entry_3.get()))

      mysql_cursor.execute(sql , value)
      connector.commit()

      Exam.current(0)
      add_class.current(0)
      add_sec.current(0)
      admn_number.delete(0  ,END)
      eng_entry_3.delete(0  ,END)
      evs_entry_3.delete(0  ,END)
      mat_entry_3.delete(0  ,END)
      II_Lang_entry_3.delete(0  ,END)
      III_Lang_entry_3.delete(0  ,END)
      Computer_science_entry_3.delete(0  ,END)

   elif cls_or_grp == "5":
      sql = "INSERT INTO 5th_std(Admn_num , Class , Sec , Exam , English , Science , Maths , II_Lang , III_Lang , Social_science , Computer_science) VALUES (%s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s);"
      value = (adm_num , cls , section , exam , int(eng_entry_5.get()) , int(science_entry_5.get()) , int(mat_entry_5.get()) , int(II_Lang_entry_5.get()) , int(III_Lang_entry_5.get()) , int(Social_science_entry_5.get()) , int(Computer_science_entry_5.get()))

      mysql_cursor.execute(sql , value)
      connector.commit()

      Exam.current(0)
      add_class.current(0)
      add_sec.current(0)
      admn_number.delete(0  ,END)
      eng_entry_5.delete(0 , END)
      science_entry_5.delete(0 , END)
      mat_entry_5.delete(0 , END)
      II_Lang_entry_5.delete(0 , END)
      III_Lang_entry_5.delete(0 , END)
      Social_science_entry_5.delete(0 , END)
      Computer_science_entry_5.delete(0 , END)

   elif cls_or_grp == "6 to 8":
      sql = "INSERT INTO 6th_to_8th_std(Admn_num , Class , Sec , Exam , English , Science , Maths , II_Lang , III_Lang , Social_science , Computer_science , Sanskrit) VALUES (%s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s);"
      value = (adm_num , cls , section , exam , int(eng_entry_6.get()) , int(science_entry_6.get()) , int(mat_entry_6.get()) , int(II_Lang_entry_6.get()) , int(III_Lang_entry_6.get()) , int(Social_science_entry_6.get()) , int(Computer_science_entry_6.get()) , int(sanskrit_entry_6.get()))
      
      mysql_cursor.execute(sql , value)
      connector.commit()

      Exam.current(0)
      add_class.current(0)
      add_sec.current(0)
      admn_number.delete(0  ,END)
      eng_entry_6.delete(0 , END)
      science_entry_6.delete(0 , END)
      mat_entry_6.delete(0 , END)
      II_Lang_entry_6.delete(0 , END)
      III_Lang_entry_6.delete(0 , END)
      Social_science_entry_6.delete(0 , END)
      Computer_science_entry_6.delete(0 , END)
      sanskrit_entry_6.delete(0 , END)

   elif cls_or_grp == "9 or 10":
      sql = "INSERT INTO 9th_10th_std(Admn_num , Class , Sec , Exam , English , Science , Maths , II_Lang , Social_science , IT) VALUES (%s , %s , %s , %s , %s , %s , %s , %s , %s , %s);"
      value = (adm_num , cls , section , exam , int(eng_entry_9.get()) , int(science_entry_9.get()) , int(mat_entry_9.get()) , int(II_Lang_entry_9.get()) , int(Social_science_entry_9.get()) , int(IT_entry_9.get()))
      
      mysql_cursor.execute(sql , value)
      connector.commit()

      Exam.current(0)
      add_class.current(0)
      add_sec.current(0)
      admn_number.delete(0  ,END)
      eng_entry_9.delete(0 , END)
      science_entry_9.delete(0 , END)
      mat_entry_9.delete(0 , END)
      II_Lang_entry_9.delete(0 , END)
      Social_science_entry_9.delete(0 , END)
      IT_entry_9.delete(0 , END)

   elif cls_or_grp == "bio-cs":
      sql = "INSERT INTO bio_cs(Admn_num , Class , Sec , Exam , English , Computer_science , Biology , Physics , Chemistry) VALUES (%s , %s , %s , %s , %s , %s , %s , %s , %s);"
      value = (adm_num , cls , section , exam , int(eng_entry_biocs.get()) , int(computer_science_entry_biocs.get()) , int(biology_entry_biocs.get()) , int(physics_entry_biocs.get()) , int(chemistry_entry_biocs.get()))

      mysql_cursor.execute(sql , value)
      connector.commit()

      Exam.current(0)
      add_class.current(0)
      add_sec.current(0)
      admn_number.delete(0  ,END)
      eng_entry_biocs.delete(0 , END)
      computer_science_entry_biocs.delete(0 , END)
      biology_entry_biocs.delete(0 , END)
      physics_entry_biocs.delete(0 , END)
      chemistry_entry_biocs.delete(0 , END)

   elif cls_or_grp == "bio-mat":
      sql = "INSERT INTO bio_mat(Admn_num , Class , Sec , Exam , English , Maths , Biology , Physics , Chemistry) VALUES (%s , %s , %s , %s , %s , %s , %s , %s , %s);"
      value = (adm_num , cls , section , exam , int(english_entry_biomat.get()) , int(mat_entry_biomat.get()) , int(biology_entry_biomat.get()) , int(physics_entry_biomat.get()) , int(chemistry_entry_biomat.get()))

      mysql_cursor.execute(sql , value)
      connector.commit()

      Exam.current(0)
      add_class.current(0)
      add_sec.current(0)
      admn_number.delete(0  , END)
      english_entry_biomat.delete(0 , END)
      mat_entry_biomat.delete(0 , END)
      biology_entry_biomat.delete(0 , END)
      physics_entry_biomat.delete(0 , END)
      chemistry_entry_biomat.delete(0 , END)

   elif cls_or_grp == "cs-mat":
      sql = "INSERT INTO cs_mat(Admn_num , Class , Sec , Exam , English , Maths , Computer_science , Physics , Chemistry) VALUES (%s , %s , %s , %s , %s , %s , %s , %s , %s);"
      value = (adm_num , cls , section , exam , int(english_entry_csmat.get()) , int(mat_entry_csmat.get()) , int(computer_science_entry_csmat.get()) , int(physics_entry_csmat.get()) , int(chemistry_entry_csmat.get()))

      mysql_cursor.execute(sql , value)
      connector.commit()

      Exam.current(0)
      add_class.current(0)
      add_sec.current(0)
      admn_number.delete(0  ,END)
      english_entry_csmat.delete(0 , END)
      mat_entry_csmat.delete(0 , END)
      computer_science_entry_csmat.delete(0 , END)
      physics_entry_csmat.delete(0 , END)
      chemistry_entry_csmat.delete(0 , END)

   elif cls_or_grp == "com-eco":
      sql = "INSERT INTO com_eco(Admn_num , Class , Sec , Exam , English , Maths , Business_studies , Accounts , Economics) VALUES (%s , %s , %s , %s , %s , %s , %s , %s , %s);"
      value = (adm_num , cls , section , exam , int(english_entry_comeco.get()) , int(mat_entry_comeco.get()) , int(business_studies_entry_comeco.get()) , int(accounts_entry_comeco.get()) , int(economics_entry_comeco.get()))

      mysql_cursor.execute(sql , value)
      connector.commit()

      Exam.current(0)
      add_class.current(0)
      add_sec.current(0)
      admn_number.delete(0  ,END)
      english_entry_comeco.delete(0 , END)
      mat_entry_comeco.delete(0 , END)
      business_studies_entry_comeco.delete(0 , END)
      accounts_entry_comeco.delete(0 , END)
      economics_entry_comeco.delete(0 , END)
      
   elif cls_or_grp == "com-mar":
      sql = "INSERT INTO com_mar(Admn_num , Class , Sec , Exam , English , Maths , Business_studies , Accounts , Marketing) VALUES (%s , %s , %s , %s , %s , %s , %s , %s , %s);"
      value = (adm_num , cls , section , exam , int(english_entry_commar.get()) , int(mat_entry_commar.get()) , int(business_studies_entry_commar.get()) , int(accounts_entry_commar.get()) , int(marketing_entry_commar.get()))

      mysql_cursor.execute(sql , value)
      connector.commit()

      Exam.current(0)
      add_class.current(0)
      add_sec.current(0)
      admn_number.delete(0  ,END)
      english_entry_commar.delete(0 , END)
      mat_entry_commar.delete(0 , END)
      business_studies_entry_commar.delete(0 , END)
      accounts_entry_commar.delete(0 , END)
      marketing_entry_commar.delete(0 , END)

   elif cls_or_grp == "com-it":
      sql = "INSERT INTO com_it(Admn_num , Class , Sec , Exam , English , Maths , Business_studies , Accounts , IT) VALUES (%s , %s , %s , %s , %s , %s , %s , %s , %s);"
      value = (adm_num , cls , section , exam , int(english_entry_comit.get()) , int(mat_entry_comit.get()) , int(business_studies_entry_comit.get()) , int(accounts_entry_comit.get()) , int(It_entry_comit.get()))

      mysql_cursor.execute(sql , value)
      connector.commit()

      Exam.current(0)
      add_class.current(0)
      add_sec.current(0)
      admn_number.delete(0  ,END)
      english_entry_comit.delete(0 , END)
      mat_entry_comit.delete(0 , END)
      business_studies_entry_comit.delete(0 , END)
      accounts_entry_comit.delete(0 , END)
      It_entry_comit.delete(0 , END)


cls_or_grp = "Select Class"

# Removing already present Labels and Entry boxes
def remove_labels_and_entry():
   if cls_or_grp == "1 or 2":
      eng_1.place_forget()
      mat_1.place_forget()
      evs_1.place_forget()
      tam_1.place_forget()

      eng_entry_1.place_forget()
      mat_entry_1.place_forget()
      evs_entry_1.place_forget()
      tam_entry_1.place_forget()

      add_recs_button.place_forget()
      
   elif cls_or_grp == "3 or 4":
      eng_3.place_forget()
      mat_3.place_forget()
      evs_3.place_forget()
      IIlang_3.place_forget()
      IIIlang_3.place_forget()
      cs_3.place_forget()

      eng_entry_3.place_forget()
      mat_entry_3.place_forget()
      evs_entry_3.place_forget()
      II_Lang_entry_3.place_forget()
      III_Lang_entry_3.place_forget()
      Computer_science_entry_3.place_forget()

      add_recs_button.place_forget()
      
   elif cls_or_grp == "5":
      eng_5.place_forget()
      mat_5.place_forget()
      sci_5.place_forget()
      IIlang_5.place_forget()
      IIIlang_5.place_forget()
      soc_5.place_forget()
      cs_5.place_forget()

      eng_entry_5.place_forget()
      mat_entry_5.place_forget()
      science_entry_5.place_forget()
      II_Lang_entry_5.place_forget()
      III_Lang_entry_5.place_forget()
      Social_science_entry_5.place_forget()
      Computer_science_entry_5.place_forget()

      add_recs_button.place_forget()
      
   elif cls_or_grp == "6 to 8":
      eng_6.place_forget()
      mat_6.place_forget()
      sci_6.place_forget()
      IIlang_6.place_forget()
      IIIlang_6.place_forget()
      soc_6.place_forget()
      cs_6.place_forget()
      sans_6.place_forget()

      eng_entry_6.place_forget()
      mat_entry_6.place_forget()
      science_entry_6.place_forget()
      II_Lang_entry_6.place_forget()
      III_Lang_entry_6.place_forget()
      Social_science_entry_6.place_forget()
      Computer_science_entry_6.place_forget()
      sanskrit_entry_6.place_forget()

      add_recs_button.place_forget()
      
   elif cls_or_grp == "9 or 10":
      eng_9.place_forget()
      mat_9.place_forget()
      sci_9.place_forget()
      IIlang_9.place_forget()
      it_9.place_forget()
      soc_9.place_forget()

      eng_entry_9.place_forget()
      mat_entry_9.place_forget()
      science_entry_9.place_forget()
      II_Lang_entry_9.place_forget()
      IT_entry_9.place_forget()
      Social_science_entry_9.place_forget()

      add_recs_button.place_forget()
      
   elif cls_or_grp == "bio-cs":
      cs_biocs.place_forget()
      eng_biocs.place_forget()
      bio_biocs.place_forget()
      phy_biocs.place_forget()
      chem_biocs.place_forget()

      computer_science_entry_biocs.place_forget()
      eng_entry_biocs.place_forget()
      biology_entry_biocs.place_forget()
      physics_entry_biocs.place_forget()
      chemistry_entry_biocs.place_forget()
      
      add_recs_button.place_forget()
      
   elif cls_or_grp == "bio-mat":
      mat_biomat.place_forget()
      bio_biomat.place_forget()
      eng_biomat.place_forget()
      phy_biomat.place_forget()
      chem_biomat.place_forget()

      mat_entry_biomat.place_forget()
      biology_entry_biomat.place_forget()
      english_entry_biomat.place_forget()
      physics_entry_biomat.place_forget()
      chemistry_entry_biomat.place_forget()

      add_recs_button.place_forget()
      
   elif cls_or_grp == "cs-mat":
      cs_csmat.place_forget()
      mat_csmat.place_forget()
      eng_csmat.place_forget()
      phy_csmat.place_forget()
      chem_csmat.place_forget()

      computer_science_entry_csmat.place_forget()
      mat_entry_csmat.place_forget()
      english_entry_csmat.place_forget()
      physics_entry_csmat.place_forget()
      chemistry_entry_csmat.place_forget()

      add_recs_button.place_forget()
      
   elif cls_or_grp == "com-eco":
      acc_comeco.place_forget()
      mat_comeco.place_forget()
      eng_comeco.place_forget()
      bs_comeco.place_forget()
      eco_comeco.place_forget()

      accounts_entry_comeco.place_forget()
      mat_entry_comeco.place_forget()
      english_entry_comeco.place_forget()
      business_studies_entry_comeco.place_forget()
      economics_entry_comeco.place_forget()

      add_recs_button.place_forget()
      
   elif cls_or_grp == "com-mar":
      acc_commar.place_forget()
      mat_commar.place_forget()
      eng_commar.place_forget()
      bs_commar.place_forget()
      mar_commar.place_forget()

      accounts_entry_commar.place_forget()
      mat_entry_commar.place_forget()
      english_entry_commar.place_forget()
      business_studies_entry_commar.place_forget()
      marketing_entry_commar.place_forget()

      add_recs_button.place_forget()
      
   elif cls_or_grp == "com-it":
      acc_comit.place_forget()
      mat_comit.place_forget()
      eng_comit.place_forget()
      bs_comit.place_forget()
      it_comit.place_forget()

      accounts_entry_comit.place_forget()
      mat_entry_comit.place_forget()
      english_entry_comit.place_forget()
      business_studies_entry_comit.place_forget()
      It_entry_comit.place_forget()

      add_recs_button.place_forget()
   

# Creating Entry boxes and Labels for classes 1 and 2
def _1st_2nd_std():
   remove_labels_and_entry()
   Home_screen.geometry("400x400")

   global cls_or_grp
   cls_or_grp = "1 or 2"

   global eng_1
   global mat_1
   global evs_1
   global tam_1
   
   eng_1 = Label(Home_screen , text = "English:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   mat_1 = Label(Home_screen , text = "Maths:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   evs_1 = Label(Home_screen , text = "EVS:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   tam_1 = Label(Home_screen , text = "Tamil:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")

   eng_1.place(x = 15 , y = 195)
   mat_1.place(x = 15 , y = 235)
   evs_1.place(x = 15 , y = 275)
   tam_1.place(x = 15 , y = 315)

   global eng_entry_1
   global mat_entry_1
   global evs_entry_1
   global tam_entry_1

   eng_entry_1 = Entry(Home_screen , width = 30)
   mat_entry_1 = Entry(Home_screen , width = 30)
   evs_entry_1 = Entry(Home_screen , width = 30)
   tam_entry_1 = Entry(Home_screen , width = 30)

   eng_entry_1.place(x = 100 , y = 201)
   mat_entry_1.place(x = 100 , y = 241)
   evs_entry_1.place(x = 100 , y = 281)
   tam_entry_1.place(x = 100 , y = 321)
   add_recs_button.place(x = 125 , y = 361)


# Creating Entry boxes and Labels for classes 3 and 4
def _3rd_4th_std():
   remove_labels_and_entry()
   Home_screen.geometry("400x481")

   global cls_or_grp
   cls_or_grp = "3 or 4"

   global eng_3
   global mat_3
   global evs_3
   global IIlang_3
   global IIIlang_3
   global cs_3
   
   eng_3 = Label(Home_screen , text = "English:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   mat_3 = Label(Home_screen , text = "Maths:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   evs_3 = Label(Home_screen , text = "EVS:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   IIlang_3 = Label(Home_screen , text = "II - Lang:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   IIIlang_3 = Label(Home_screen , text = "III - Lang:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   cs_3 = Label(Home_screen , text = "Computer Science:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")

   eng_3.place(x = 15 , y = 195)
   mat_3.place(x = 15 , y = 235)
   evs_3.place(x = 15 , y = 275)
   IIlang_3.place(x = 15 , y = 315)
   IIIlang_3.place(x = 15 , y = 355)
   cs_3.place(x = 15 , y = 395)

   global eng_entry_3
   global mat_entry_3 
   global evs_entry_3
   global II_Lang_entry_3
   global III_Lang_entry_3
   global Computer_science_entry_3

   eng_entry_3 = Entry(Home_screen , width = 30)
   mat_entry_3 = Entry(Home_screen , width = 30)
   evs_entry_3 = Entry(Home_screen , width = 30)
   II_Lang_entry_3 = Entry(Home_screen , width = 30)
   III_Lang_entry_3 = Entry(Home_screen , width = 30)
   Computer_science_entry_3 = Entry(Home_screen , width = 30)

   eng_entry_3.place(x = 200 , y = 201)
   mat_entry_3.place(x = 200 , y = 241)
   evs_entry_3.place(x = 200 , y = 281)
   II_Lang_entry_3.place(x = 200, y = 321)
   III_Lang_entry_3.place(x = 200 , y = 361)
   Computer_science_entry_3.place(x = 200, y = 401)
   add_recs_button.place(x = 145 , y = 441)


# Creating Entry boxes and Labels for class 5
def _5th_std():
   remove_labels_and_entry()
   Home_screen.geometry("400x521")

   global cls_or_grp
   cls_or_grp = "5"

   global eng_5
   global mat_5
   global sci_5
   global IIlang_5
   global IIIlang_5
   global soc_5
   global cs_5
   
   eng_5 = Label(Home_screen , text = "English:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   mat_5 = Label(Home_screen , text = "Maths:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   sci_5 = Label(Home_screen , text = "Science:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   IIlang_5 = Label(Home_screen , text = "II_Lang:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   IIIlang_5 = Label(Home_screen , text = "III_Lang:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   soc_5 = Label(Home_screen , text = "Social_science:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   cs_5 = Label(Home_screen , text = "Computer_science:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")

   eng_5.place(x = 15 , y = 195)
   mat_5.place(x = 15 , y = 235)
   sci_5.place(x = 15 , y = 275)
   IIlang_5.place(x = 15 , y = 315)
   IIIlang_5.place(x = 15 , y = 355)
   soc_5.place(x = 15 , y = 395)
   cs_5.place(x = 15 , y = 435)

   global eng_entry_5
   global mat_entry_5
   global science_entry_5
   global II_Lang_entry_5
   global III_Lang_entry_5
   global Social_science_entry_5
   global Computer_science_entry_5
    
   eng_entry_5 = Entry(Home_screen , width = 30)
   mat_entry_5 = Entry(Home_screen , width = 30)
   science_entry_5 = Entry(Home_screen , width = 30)
   II_Lang_entry_5 = Entry(Home_screen , width = 30)
   III_Lang_entry_5 = Entry(Home_screen , width = 30)
   Social_science_entry_5 = Entry(Home_screen , width = 30)
   Computer_science_entry_5 = Entry(Home_screen , width = 30)
   
   eng_entry_5.place(x = 200 , y = 201)
   mat_entry_5.place(x = 200 , y = 241)
   science_entry_5.place(x = 200 , y = 281)
   II_Lang_entry_5.place(x = 200, y = 321)
   III_Lang_entry_5.place(x = 200 , y = 361)
   Social_science_entry_5.place(x = 200, y = 401)
   Computer_science_entry_5.place(x = 200 , y = 441)
   add_recs_button.place(x = 145 , y = 481)


# Creating Entry boxes and Labels for classes 6 to 8
def _6th_to_8th_std():
   remove_labels_and_entry()
   Home_screen.geometry("400x561")

   global cls_or_grp
   cls_or_grp = "6 to 8"

   global eng_6
   global mat_6
   global sci_6
   global IIlang_6
   global IIIlang_6
   global soc_6
   global cs_6
   global sans_6
   
   eng_6 = Label(Home_screen , text = "English:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   mat_6 = Label(Home_screen , text = "Maths:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   sci_6 = Label(Home_screen , text = "Science:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   IIlang_6 = Label(Home_screen , text = "II - Lang:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   IIIlang_6 = Label(Home_screen , text = "III - Lang:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   soc_6 = Label(Home_screen , text = "Social Science:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   cs_6 = Label(Home_screen , text = "Computer Science:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   sans_6 = Label(Home_screen , text = "Sanskrit:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")

   eng_6.place(x = 15 , y = 195)
   mat_6.place(x = 15 , y = 235)
   sci_6.place(x = 15 , y = 275)
   IIlang_6.place(x = 15 , y = 315)
   IIIlang_6.place(x = 15 , y = 355)
   soc_6.place(x = 15 , y = 395)
   cs_6.place(x = 15 , y = 435)
   sans_6.place(x = 15 , y = 475)

   global eng_entry_6
   global mat_entry_6
   global science_entry_6
   global II_Lang_entry_6
   global III_Lang_entry_6
   global Social_science_entry_6
   global Computer_science_entry_6
   global sanskrit_entry_6
   
   eng_entry_6 = Entry(Home_screen , width = 30)
   mat_entry_6 = Entry(Home_screen , width = 30)
   science_entry_6 = Entry(Home_screen , width = 30)
   II_Lang_entry_6 = Entry(Home_screen , width = 30)
   III_Lang_entry_6 = Entry(Home_screen , width = 30)
   Social_science_entry_6 = Entry(Home_screen , width = 30)
   Computer_science_entry_6 = Entry(Home_screen , width = 30)
   sanskrit_entry_6 = Entry(Home_screen , width = 30)

   eng_entry_6.place(x = 200 , y = 201)
   mat_entry_6.place(x = 200 , y = 241)
   science_entry_6.place(x = 200 , y = 281)
   II_Lang_entry_6.place(x = 200 , y = 321)
   III_Lang_entry_6.place(x = 200 , y = 361)
   Social_science_entry_6.place(x = 200 , y = 401)
   Computer_science_entry_6.place(x = 200, y = 441)
   sanskrit_entry_6.place(x = 200 , y = 481)
   add_recs_button.place(x = 145 , y = 521)


# Creating Entry boxes and Labels for classes 9 and 10
def _9th_10th_std():
   remove_labels_and_entry()
   Home_screen.geometry("400x481")

   global cls_or_grp
   cls_or_grp = "9 or 10"

   global eng_9
   global mat_9
   global sci_9
   global IIlang_9
   global it_9
   global soc_9
   
   eng_9 = Label(Home_screen , text = "English:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   mat_9= Label(Home_screen , text = "Maths:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   sci_9 = Label(Home_screen , text = "Science:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   IIlang_9 = Label(Home_screen , text = "II - Lang:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   it_9 = Label(Home_screen , text = "IT:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   soc_9 = Label(Home_screen , text = "Social Science:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")

   eng_9.place(x = 15 , y = 195)
   mat_9.place(x = 15 , y = 235)
   sci_9.place(x = 15 , y = 275)
   IIlang_9.place(x = 15 , y = 315)
   it_9.place(x = 15 , y = 355)
   soc_9.place(x = 15 , y = 395)

   global eng_entry_9
   global mat_entry_9
   global science_entry_9
   global II_Lang_entry_9
   global IT_entry_9
   global Social_science_entry_9

   eng_entry_9 = Entry(Home_screen , width = 30)
   mat_entry_9 = Entry(Home_screen , width = 30)
   science_entry_9 = Entry(Home_screen , width = 30)
   II_Lang_entry_9 = Entry(Home_screen , width = 30)
   IT_entry_9 = Entry(Home_screen , width = 30)
   Social_science_entry_9 = Entry(Home_screen , width = 30)

   eng_entry_9.place(x = 165 , y = 201)
   mat_entry_9.place(x = 165 , y = 241)
   science_entry_9.place(x = 165 , y = 281)
   II_Lang_entry_9.place(x = 165, y = 321)
   IT_entry_9.place(x = 165, y = 361)
   Social_science_entry_9.place(x = 165, y = 401)
   add_recs_button.place(x = 145 , y = 441)

# Creating Entry boxes and Labels for bio-cs group
def Bio_cs():
   remove_labels_and_entry()
   Home_screen.geometry("400x441")

   global cls_or_grp
   cls_or_grp = "bio-cs"

   global cs_biocs
   global eng_biocs
   global bio_biocs
   global phy_biocs
   global chem_biocs
   
   cs_biocs = Label(Home_screen , text = "Computer science:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   eng_biocs = Label(Home_screen , text = "English:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   bio_biocs = Label(Home_screen , text = "Biology:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   phy_biocs = Label(Home_screen , text = "Physics:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   chem_biocs = Label(Home_screen , text = "Chemistry:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")

   cs_biocs.place(x = 15 , y = 195)
   eng_biocs.place(x = 15 , y = 235)
   bio_biocs.place(x = 15 , y = 275)
   phy_biocs.place(x = 15 , y = 315)
   chem_biocs.place(x = 15 , y = 355)

   global computer_science_entry_biocs
   global eng_entry_biocs
   global biology_entry_biocs
   global physics_entry_biocs
   global chemistry_entry_biocs
   
   computer_science_entry_biocs = Entry(Home_screen , width = 30)
   eng_entry_biocs = Entry(Home_screen , width = 30)
   biology_entry_biocs = Entry(Home_screen , width = 30)
   physics_entry_biocs = Entry(Home_screen , width = 30)
   chemistry_entry_biocs = Entry(Home_screen , width = 30)
 
   computer_science_entry_biocs.place(x = 195 , y = 201)
   eng_entry_biocs.place(x = 195, y = 241)
   biology_entry_biocs.place(x = 195, y = 281)
   physics_entry_biocs.place(x = 195 ,y = 321)
   chemistry_entry_biocs.place(x =195, y = 361)
   add_recs_button.place(x = 145 , y = 401)


# Creating Entry boxes and Labels for bio-mathsgroup
def Bio_mat():
   remove_labels_and_entry()
   Home_screen.geometry("400x441")

   global cls_or_grp
   cls_or_grp = "bio-mat"

   global mat_biomat
   global bio_biomat
   global eng_biomat
   global phy_biomat
   global chem_biomat
   
   mat_biomat = Label(Home_screen , text = "Maths:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   bio_biomat = Label(Home_screen , text = "Biology:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   eng_biomat = Label(Home_screen , text = "English:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   phy_biomat = Label(Home_screen , text = "Physics:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   chem_biomat = Label(Home_screen , text = "Chemistry:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")

   mat_biomat.place(x = 15 , y = 195)
   bio_biomat.place(x = 15 , y = 235)
   eng_biomat.place(x = 15 , y = 275)
   phy_biomat.place(x = 15 , y = 315)
   chem_biomat.place(x = 15 , y = 355)

   global mat_entry_biomat
   global biology_entry_biomat
   global english_entry_biomat
   global physics_entry_biomat
   global chemistry_entry_biomat
   
   mat_entry_biomat = Entry(Home_screen , width = 30)
   biology_entry_biomat = Entry(Home_screen , width = 30)
   english_entry_biomat = Entry(Home_screen , width = 30)
   physics_entry_biomat = Entry(Home_screen , width = 30)
   chemistry_entry_biomat = Entry(Home_screen , width = 30)
 
   mat_entry_biomat.place(x = 125 , y = 201)
   biology_entry_biomat.place(x = 125, y = 241)
   english_entry_biomat.place(x = 125, y = 281)
   physics_entry_biomat.place(x = 125 ,y = 321)
   chemistry_entry_biomat.place(x =125, y = 361)
   add_recs_button.place(x = 145 , y = 401)
   

# Creating Entry boxes and Labels for cs-maths group
def Cs_mat():
   remove_labels_and_entry()
   Home_screen.geometry("400x441")

   global cls_or_grp
   cls_or_grp = "cs-mat"

   global cs_csmat
   global mat_csmat
   global eng_csmat
   global phy_csmat
   global chem_csmat
   
   cs_csmat = Label(Home_screen , text = "Computer science:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   mat_csmat = Label(Home_screen , text = "Maths:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   eng_csmat = Label(Home_screen , text = "English:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   phy_csmat = Label(Home_screen , text = "Physics:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   chem_csmat = Label(Home_screen , text = "Chemistry:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")

   cs_csmat.place(x = 15 , y = 195)
   mat_csmat.place(x = 15 , y = 235)
   eng_csmat.place(x = 15 , y = 275)
   phy_csmat.place(x = 15 , y = 315)
   chem_csmat.place(x = 15 , y = 355)

   global computer_science_entry_csmat
   global mat_entry_csmat
   global english_entry_csmat
   global physics_entry_csmat
   global chemistry_entry_csmat
   
   computer_science_entry_csmat = Entry(Home_screen , width = 30)
   mat_entry_csmat = Entry(Home_screen , width = 30)
   english_entry_csmat = Entry(Home_screen , width = 30)
   physics_entry_csmat = Entry(Home_screen , width = 30)
   chemistry_entry_csmat = Entry(Home_screen , width = 30)
 
   
   computer_science_entry_csmat.place(x = 195 , y = 201)
   mat_entry_csmat.place(x = 195, y = 241)
   english_entry_csmat.place(x = 195, y = 281)
   physics_entry_csmat.place(x = 195 ,y = 321)
   chemistry_entry_csmat.place(x =195, y = 361)
   add_recs_button.place(x = 145 , y = 401)
   

# Creating Entry boxes and Labels for comerce-economics group
def Com_eco():
   remove_labels_and_entry()
   Home_screen.geometry("400x441")

   global cls_or_grp
   cls_or_grp = "com-eco"

   global acc_comeco
   global mat_comeco
   global eng_comeco
   global bs_comeco
   global eco_comeco
   
   acc_comeco = Label(Home_screen , text = "Accounts:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   mat_comeco = Label(Home_screen , text = "Maths:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   eng_comeco = Label(Home_screen , text = "English:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   bs_comeco = Label(Home_screen , text = "Business Studies:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   eco_comeco = Label(Home_screen , text = "Economics:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")

   acc_comeco.place(x = 15 , y = 195)
   mat_comeco.place(x = 15 , y = 235)
   eng_comeco.place(x = 15 , y = 275)
   bs_comeco.place(x = 15 , y = 315)
   eco_comeco.place(x = 15 , y = 355)

   global accounts_entry_comeco
   global mat_entry_comeco
   global english_entry_comeco
   global business_studies_entry_comeco
   global economics_entry_comeco
   
   accounts_entry_comeco = Entry(Home_screen , width = 30)
   mat_entry_comeco = Entry(Home_screen , width = 30)
   english_entry_comeco = Entry(Home_screen , width = 30)
   business_studies_entry_comeco = Entry(Home_screen , width = 30)
   economics_entry_comeco = Entry(Home_screen , width = 30)
 
   accounts_entry_comeco.place(x = 188 , y = 201)
   mat_entry_comeco.place(x = 188, y = 241)
   english_entry_comeco.place(x = 188, y = 281)
   business_studies_entry_comeco.place(x = 188,y = 321)
   economics_entry_comeco.place(x =188, y = 361)
   add_recs_button.place(x = 145 , y = 401)
   

# Creating Entry boxes and Labels for comerce-marketing group
def Com_mar():
   remove_labels_and_entry()
   Home_screen.geometry("400x441")

   global cls_or_grp
   cls_or_grp = "com-mar"

   global acc_commar
   global mat_commar
   global eng_commar
   global bs_commar
   global mar_commar
   
   acc_commar = Label(Home_screen , text = "Accounts:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   mat_commar = Label(Home_screen , text = "Maths:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   eng_commar = Label(Home_screen , text = "English:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   bs_commar = Label(Home_screen , text = "Business Studies:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   mar_commar = Label(Home_screen , text = "Marketing:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")

   acc_commar.place(x = 15 , y = 195)
   mat_commar.place(x = 15 , y = 235)
   eng_commar.place(x = 15 , y = 275)
   bs_commar.place(x = 15 , y = 315)
   mar_commar.place(x = 15 , y = 355)

   global accounts_entry_commar
   global mat_entry_commar
   global english_entry_commar
   global business_studies_entry_commar
   global marketing_entry_commar
   
   accounts_entry_commar = Entry(Home_screen , width = 30)
   mat_entry_commar = Entry(Home_screen , width = 30)
   english_entry_commar = Entry(Home_screen , width = 30)
   business_studies_entry_commar = Entry(Home_screen , width = 30)
   marketing_entry_commar = Entry(Home_screen , width = 30)
 
   accounts_entry_commar.place(x = 188 , y = 201)
   mat_entry_commar.place(x = 188, y = 241)
   english_entry_commar.place(x = 188, y = 281)
   business_studies_entry_commar.place(x = 188,y = 321)
   marketing_entry_commar.place(x =188, y = 361)
   add_recs_button.place(x = 145 , y = 401)


# Creating Entry boxes and Labels for comerce-it group
def Com_it():
   remove_labels_and_entry()
   Home_screen.geometry("400x441")

   global cls_or_grp
   cls_or_grp = "com-it"

   global acc_comit
   global mat_comit
   global eng_comit
   global bs_comit
   global it_comit
   
   acc_comit = Label(Home_screen , text = "Accounts:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   mat_comit = Label(Home_screen , text = "Maths:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   eng_comit = Label(Home_screen , text = "English:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   bs_comit = Label(Home_screen , text = "Business Studies:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   it_comit = Label(Home_screen , text = "IT:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")

   acc_comit.place(x = 15 , y = 195)
   mat_comit.place(x = 15 , y = 235)
   eng_comit.place(x = 15 , y = 275)
   bs_comit.place(x = 15 , y = 315)
   it_comit.place(x = 15 , y = 355)

   global accounts_entry_comit
   global mat_entry_comit
   global english_entry_comit
   global business_studies_entry_comit
   global It_entry_comit
   
   accounts_entry_comit = Entry(Home_screen , width = 30)
   mat_entry_comit = Entry(Home_screen , width = 30)
   english_entry_comit = Entry(Home_screen , width = 30)
   business_studies_entry_comit = Entry(Home_screen , width = 30)
   It_entry_comit = Entry(Home_screen , width = 30)
 
   accounts_entry_comit.place(x = 188 , y = 201)
   mat_entry_comit.place(x = 188, y = 241)
   english_entry_comit.place(x = 188, y = 281)
   business_studies_entry_comit.place(x = 188,y = 321)
   It_entry_comit.place(x =188, y = 361)
   add_recs_button.place(x = 145 , y = 401)


# grp Dropdown box command function
def group(event):
   if grp.get() == "CS-Maths":
      Cs_mat()
   elif grp.get() == "Bio-Maths":
      Bio_mat()
   elif grp.get() == "Bio-Cs":
      Bio_cs()
   elif grp.get() == "Comerce-It":
      Com_it()
   elif grp.get() == "Comerce-Economics":
      Com_eco()
   elif grp.get() == "Comerce-Marketing":
      Com_mar()


# grp Dropdown Binding function
def dropdown_bind(event):
   if add_class.get() == "I" or add_class.get() == "II":
      grp.current(0)
      grp.config(state = DISABLED)
      _1st_2nd_std()
   elif add_class.get() == "III" or add_class.get() == "IV":
      grp.current(0)
      grp.config(state = DISABLED)
      _3rd_4th_std()
   elif add_class.get() == "V":
      grp.current(0)
      grp.config(state = DISABLED)
      _5th_std()
   elif add_class.get() == "VI" or add_class.get() == "VII" or add_class.get() == "VIII":
      grp.current(0)
      grp.config(state = DISABLED)
      _6th_to_8th_std()
   elif add_class.get() == "IX" or add_class.get() == "X":
      grp.current(0)
      grp.config(state = DISABLED)
      _9th_10th_std()
   elif add_class.get() == "XII" or add_class.get() == "XI":
      grp.config(state = NORMAL)
      grp.bind("<<ComboboxSelected>>" , group)


# Showing Marks according to the respective group selected
def groupwise_view(event):
   Home_screen.geometry("2000x600")
   if select_grp.get() == "CS-Maths":
      sql = "SELECT Exam , English , Maths , Computer_science , Physics , Chemistry FROM cs_mat WHERE Admn_num = %s and Class = %s and Sec = %s;"
      value = (admn_num , cls , sec)
      col_1 = "Exam"
      col_2 = "English"
      col_3 = "Computer science"
      col_4 = "Physics"
      col_5 = "Chemistry"
      col_6 = "Maths"
         
   elif select_grp.get() == "Bio-Maths":
      sql = "SELECT Exam , English , Maths , Biology , Physics , Chemistry FROM bio_mat WHERE Admn_num = %s and Class = %s and Sec = %s;"
      value = (admn_num , cls , sec)
      col_1 = "Exam"
      col_2 = "English"
      col_3 = "Biology"
      col_4 = "Physics"
      col_5 = "Chemistry"
      col_6 = "Maths"
      
   elif select_grp.get() == "Bio-Cs":
      sql = "SELECT Exam , English , Computer_science , Biology , Physics , Chemistry FROM bio_cs WHERE Admn_num = %s and Class = %s and Sec = %s;"
      value = (admn_num , cls , sec)
      col_1 = "Exam"
      col_2 = "English"
      col_3 = "Computer science"
      col_4 = "Physics"
      col_5 = "Chemistry"
      col_6 = "Biology"

   elif select_grp.get() == "Comerce-it":
      sql = "SELECT Exam , English , Maths , Accounts , Business_studies , IT FROM com_it WHERE Admn_num = %s and Class = %s and Sec = %s;"
      value = (admn_num , cls , sec)
      col_1 = "Exam"
      col_2 = "English"
      col_3 = "Business Studies"
      col_4 = "Accounts"
      col_5 = "IT"
      col_6 = "Maths"

   elif select_grp.get() == "Comerce-Economics":
      sql = "SELECT Exam , English , Maths , Accounts , Business_studies , Economics FROM com_eco WHERE Admn_num = %s and Class = %s and Sec = %s;"
      value = (admn_num , cls , sec)
      col_1 = "Exam"
      col_2 = "English"
      col_3 = "Business Studies"
      col_4 = "Accounts"
      col_5 = "Economics"
      col_6 = "Maths"
          
   elif select_grp.get() == "Comerce-Marketing":
      sql = "SELECT Exam , English , Maths , Accounts , Business_studies , Marketing FROM com_mar WHERE Admn_num = %s and Class = %s and Sec = %s;"
      value = (admn_num , cls , sec)
      col_1 = "Exam"
      col_2 = "English"
      col_3 = "Business Studies"
      col_4 = "Accounts"
      col_5 = "Marketing"
      col_6 = "Maths"

   mysql_cursor.execute(sql , value)
   marks = mysql_cursor.fetchall()

   Mark_reg["columns"] = (col_1 , col_2 , col_3 , col_4 , col_5 , col_6)
   Mark_reg.column("#0" , width = 0 , stretch = NO)
   Mark_reg.column(col_1 ,  anchor = W , width = 150)
   Mark_reg.column(col_2 ,  anchor = CENTER , width = 100)
   Mark_reg.column(col_3 ,  anchor = CENTER , width = 100)
   Mark_reg.column(col_4 ,  anchor = CENTER , width = 100)
   Mark_reg.column(col_5 ,  anchor = CENTER , width = 100)
   Mark_reg.column(col_6 ,  anchor = CENTER , width = 100)

   Mark_reg.heading("#0" , text = "" , anchor = CENTER)
   Mark_reg.heading(col_1 , text = col_1 , anchor = CENTER)
   Mark_reg.heading(col_2 , text = col_2 , anchor = CENTER)
   Mark_reg.heading(col_3 , text = col_3 , anchor = CENTER)
   Mark_reg.heading(col_4 , text = col_4 , anchor = CENTER)
   Mark_reg.heading(col_5 , text = col_5 , anchor = CENTER)
   Mark_reg.heading(col_6 , text = col_6 , anchor = CENTER)

   cnt = 0
   for something in marks:
       Mark_reg.insert(parent = '' , index = 'end' , iid = cnt , text = '' , values = (something[0] , something[1] , something[2] , something[3] , something[4] , something[5]))
       cnt += 1


# Showing Marks of the student logged in
def table_stud():
   global admn_num
   global cls
   global sec
   admn_num = recs[0][0]
   cls = recs[0][6]
   sec = recs[0][7]

   if cls == "XII" or cls == "XI":
      select_grp.config(state = NORMAL)

      Mark_reg["columns"] = ("exam" , "subject1" , "subject2" , "subject3" , "subject4" , "subject5")
      Mark_reg.column("#0" , width = 0 , stretch = NO)
      Mark_reg.column("exam" ,  anchor = W , width = 150)
      Mark_reg.column("subject1" ,  anchor = CENTER , width = 100)
      Mark_reg.column("subject2" ,  anchor = CENTER , width = 100)
      Mark_reg.column("subject3" ,  anchor = CENTER , width = 100)
      Mark_reg.column("subject4" ,  anchor = CENTER , width = 100)
      Mark_reg.column("subject5" ,  anchor = CENTER , width = 100)

      Mark_reg.heading("#0" , text = "" , anchor = CENTER)
      Mark_reg.heading("exam" , text = "exam" , anchor = CENTER)
      Mark_reg.heading("subject1" , text = "subject1" , anchor = CENTER)
      Mark_reg.heading("subject2" , text = "subject2" , anchor = CENTER)
      Mark_reg.heading("subject3" , text = "subject3" , anchor = CENTER)
      Mark_reg.heading("subject4" , text = "subject4" , anchor = CENTER)
      Mark_reg.heading("subject5" , text = "subject5" , anchor = CENTER)
      
   elif cls == "IX" or cls == "X":
      sql = "SELECT Exam , English , Science , Maths , II_Lang , Social_Science , IT FROM 9th_10th_std WHERE Admn_num = %s and Class = %s and Sec = %s;"
      value = (admn_num , cls , sec)

      mysql_cursor.execute(sql , value)
      marks = mysql_cursor.fetchall()

      Mark_reg["columns"] = ("exam" , "english" , "science" , "maths" , "IIlang" , "soc" , "it")
      Mark_reg.column("#0" , width = 0 , stretch = NO)
      Mark_reg.column("exam" ,  anchor = W , width = 150)
      Mark_reg.column("english" ,  anchor = CENTER , width = 100)
      Mark_reg.column("science" ,  anchor = CENTER , width = 100)
      Mark_reg.column("maths" ,  anchor = CENTER , width = 100)
      Mark_reg.column("IIlang" ,  anchor = CENTER , width = 100)
      Mark_reg.column("soc" ,  anchor = CENTER , width = 100)
      Mark_reg.column("it" ,  anchor = CENTER , width = 100)

      Mark_reg.heading("#0" , text = "" , anchor = CENTER)
      Mark_reg.heading("exam" , text = "Exam" , anchor = CENTER)
      Mark_reg.heading("english" , text = "English" , anchor = CENTER)
      Mark_reg.heading("science" , text = "Science" , anchor = CENTER)
      Mark_reg.heading("maths" , text = "Maths" , anchor = CENTER)
      Mark_reg.heading("IIlang" , text = "II Language" , anchor = CENTER)
      Mark_reg.heading("soc" , text = "Social Science" , anchor = CENTER)
      Mark_reg.heading("it" , text = "IT" , anchor = CENTER)

      cnt = 0
      for something in marks:
          Mark_reg.insert(parent = '' , index = 'end' , iid = cnt , text = '' , values = (something[0] , something[1] , something[2] , something[3] , something[4] , something[5] , something[6]))
          cnt += 1
   
   elif cls == "VI" or cls == "VII" or cls == "VIII":
      sql = "SELECT Exam , English , Science , Maths , II_Lang , III_Lang , Social_Science , Computer_Science , Sanskrit FROM 6th_to_8th_std WHERE Admn_num = %s and Class = %s and Sec = %s;"
      value = (admn_num , cls , sec)

      mysql_cursor.execute(sql , value)
      marks = mysql_cursor.fetchall()

      Mark_reg["columns"] = ("exam" , "english" , "science" , "maths" , "IIlang" , "IIIlang", "soc" , "cs" , "sans")
      Mark_reg.column("#0" , width = 0 , stretch = NO)
      Mark_reg.column("exam" ,  anchor = W , width = 150)
      Mark_reg.column("english" ,  anchor = CENTER , width = 100)
      Mark_reg.column("science" ,  anchor = CENTER , width = 100)
      Mark_reg.column("maths" ,  anchor = CENTER , width = 100)
      Mark_reg.column("IIlang" ,  anchor = CENTER , width = 100)
      Mark_reg.column("IIIlang" ,  anchor = CENTER , width = 100)
      Mark_reg.column("soc" ,  anchor = CENTER , width = 100)
      Mark_reg.column("cs" ,  anchor = CENTER , width = 100)
      Mark_reg.column("sans" ,  anchor = CENTER , width = 100)

      Mark_reg.heading("#0" , text = "" , anchor = CENTER)
      Mark_reg.heading("exam" , text = "Exam" , anchor = CENTER)
      Mark_reg.heading("english" , text = "English" , anchor = CENTER)
      Mark_reg.heading("science" , text = "Science" , anchor = CENTER)
      Mark_reg.heading("maths" , text = "Maths" , anchor = CENTER)
      Mark_reg.heading("IIlang" , text = "II Language" , anchor = CENTER)
      Mark_reg.heading("IIIlang" , text = "III Language" , anchor = CENTER)
      Mark_reg.heading("soc" , text = "Social Science" , anchor = CENTER)
      Mark_reg.heading("cs" , text = "Computer Science" , anchor = CENTER)
      Mark_reg.heading("sans" , text = "Sanskrit" , anchor = CENTER)

      cnt = 0
      for something in marks:
          Mark_reg.insert(parent = '' , index = 'end' , iid = cnt , text = '' , values = (something[0] , something[1] , something[2] , something[3] , something[4] , something[5] , something[6] , something[7] , something[8]))
          cnt += 1
   
   elif cls == "V":
      sql = "SELECT Exam , English , Science , Maths , II_Lang , III_Lang , Social_Science , Computer_Science FROM 5th_std WHERE Admn_num = %s and Class = %s and Sec = %s;"
      value = (admn_num , cls , sec)

      mysql_cursor.execute(sql , value)
      marks = mysql_cursor.fetchall()

      Mark_reg["columns"] = ("exam" , "english" , "science" , "maths" , "IIlang" , "IIIlang", "soc" , "cs")
      Mark_reg.column("#0" , width = 0 , stretch = NO)
      Mark_reg.column("exam" ,  anchor = W , width = 150)
      Mark_reg.column("english" ,  anchor = CENTER , width = 100)
      Mark_reg.column("science" ,  anchor = CENTER , width = 100)
      Mark_reg.column("maths" ,  anchor = CENTER , width = 100)
      Mark_reg.column("IIlang" ,  anchor = CENTER , width = 100)
      Mark_reg.column("IIIlang" ,  anchor = CENTER , width = 100)
      Mark_reg.column("soc" ,  anchor = CENTER , width = 100)
      Mark_reg.column("cs" ,  anchor = CENTER , width = 100)

      Mark_reg.heading("#0" , text = "" , anchor = CENTER)
      Mark_reg.heading("exam" , text = "Exam" , anchor = CENTER)
      Mark_reg.heading("english" , text = "English" , anchor = CENTER)
      Mark_reg.heading("science" , text = "Science" , anchor = CENTER)
      Mark_reg.heading("maths" , text = "Maths" , anchor = CENTER)
      Mark_reg.heading("IIlang" , text = "II Language" , anchor = CENTER)
      Mark_reg.heading("IIIlang" , text = "III Language" , anchor = CENTER)
      Mark_reg.heading("soc" , text = "Social Science" , anchor = CENTER)
      Mark_reg.heading("cs" , text = "Computer Science" , anchor = CENTER)

      cnt = 0
      for something in marks:
          Mark_reg.insert(parent = '' , index = 'end' , iid = cnt , text = '' , values = (something[0] , something[1] , something[2] , something[3] , something[4] , something[5] , something[6] , something[7]))
          cnt += 1
   
   elif cls == "III" or cls == "IV":
      sql = "SELECT Exam , English , EVS , Maths , II_Lang , III_Lang , ICT FROM 3rd_4th_std WHERE Admn_num = %s and Class = %s and Sec = %s;"
      value = (admn_num , cls , sec)

      mysql_cursor.execute(sql , value)
      marks = mysql_cursor.fetchall()

      Mark_reg["columns"] = ("exam" , "english" , "evs" , "maths" , "IIlang" , "IIIlang", "cs")
      Mark_reg.column("#0" , width = 0 , stretch = NO)
      Mark_reg.column("exam" ,  anchor = W , width = 150)
      Mark_reg.column("english" ,  anchor = CENTER , width = 100)
      Mark_reg.column("evs" ,  anchor = CENTER , width = 100)
      Mark_reg.column("maths" ,  anchor = CENTER , width = 100)
      Mark_reg.column("IIlang" ,  anchor = CENTER , width = 100)
      Mark_reg.column("IIIlang" ,  anchor = CENTER , width = 100)
      Mark_reg.column("cs" ,  anchor = CENTER , width = 100)

      Mark_reg.heading("#0" , text = "" , anchor = CENTER)
      Mark_reg.heading("exam" , text = "Exam" , anchor = CENTER)
      Mark_reg.heading("english" , text = "English" , anchor = CENTER)
      Mark_reg.heading("evs" , text = "EVS" , anchor = CENTER)
      Mark_reg.heading("maths" , text = "Maths" , anchor = CENTER)
      Mark_reg.heading("IIlang" , text = "II Language" , anchor = CENTER)
      Mark_reg.heading("IIIlang" , text = "III Language" , anchor = CENTER)
      Mark_reg.heading("cs" , text = "Computer Science" , anchor = CENTER)

      cnt = 0
      for something in marks:
          Mark_reg.insert(parent = '' , index = 'end' , iid = cnt , text = '' , values = (something[0] , something[1] , something[2] , something[3] , something[4] , something[5] , something[6]))
          cnt += 1
   
   elif cls == "I" or cls == "II":
      sql = "SELECT Exam , English , EVS , Maths , Tamil FROM 1st_2nd_std WHERE Admn_num = %s and Class = %s and Sec = %s;"
      value = (admn_num , cls , sec)

      mysql_cursor.execute(sql , value)
      marks = mysql_cursor.fetchall()

      Mark_reg["columns"] = ("exam" , "english" , "evs" , "maths" , "tamil")
      Mark_reg.column("#0" , width = 0 , stretch = NO)
      Mark_reg.column("exam" ,  anchor = W , width = 150)
      Mark_reg.column("english" ,  anchor = CENTER , width = 100)
      Mark_reg.column("evs" ,  anchor = CENTER , width = 100)
      Mark_reg.column("maths" ,  anchor = CENTER , width = 100)
      Mark_reg.column("tamil" ,  anchor = CENTER , width = 100)

      Mark_reg.heading("#0" , text = "" , anchor = CENTER)
      Mark_reg.heading("exam" , text = "Exam" , anchor = CENTER)
      Mark_reg.heading("english" , text = "English" , anchor = CENTER)
      Mark_reg.heading("evs" , text = "EVS" , anchor = CENTER)
      Mark_reg.heading("maths" , text = "Maths" , anchor = CENTER)
      Mark_reg.heading("tamil" , text = "Tamil" , anchor = CENTER)

      cnt = 0
      for something in marks:
          Mark_reg.insert(parent = '' , index = 'end' , iid = cnt , text = '' , values = (something[0] , something[1] , something[2] , something[3] , something[4]))
          cnt += 1

   Mark_reg.place(x = 40 , y = 240)

# Command for student's view button in  the menu      
def stud_view():
   Home_screen.geometry("1000x600")

   global select_grp
   select_grps = ["Select Group" , "CS-Maths" , "Bio-Maths" , "Bio-Cs" , "Comerce-It" , "Comerce-Economics" , "Comerce-Marketing"]
   select_grp = ttk.Combobox(Home_screen , value = select_grps , state = DISABLED)
   select_grp.current(0)
   select_grp.bind("<<ComboboxSelected>>" , groupwise_view)

   global Mark_reg
   Mark_reg = ttk.Treeview(Home_screen)

   select_grp.place(x = 40 , y = 200)
   
   table_stud()

# Marks table when logged in as teacher
def table_teach():
   global admn_num
   global cls
   global sec
   admn_num = admn_no.get()
   cls = class_.get()
   sec = sec_.get()

   if cls == "XII" or cls == "XI":
      if select_grp_.get() == "CS-Maths":
         sql = "SELECT Exam , English , Maths , Computer_science , Physics , Chemistry FROM cs_mat WHERE Admn_num = %s and Class = %s and Sec = %s;"
         value = (admn_num , cls , sec)
         col_1 = "Exam"
         col_2 = "English"
         col_3 = "Computer science"
         col_4 = "Physics"
         col_5 = "Chemistry"
         col_6 = "Maths"
         
      elif select_grp_.get() == "Bio-Maths":
         sql = "SELECT Exam , English , Maths , Biology , Physics , Chemistry FROM cs_mat WHERE Admn_num = %s and Class = %s and Sec = %s;"
         value = (admn_num , cls , sec)
         col_1 = "Exam"
         col_2 = "English"
         col_3 = "Biology"
         col_4 = "Physics"
         col_5 = "Chemistry"
         col_6 = "Maths"
         
      elif select_grp_.get() == "Bio-Cs":
         sql = "SELECT Exam , English , Computer_science , Biology , Physics , Chemistry FROM cs_mat WHERE Admn_num = %s and Class = %s and Sec = %s;"
         value = (admn_num , cls , sec)
         col_1 = "Exam"
         col_2 = "English"
         col_3 = "Computer science"
         col_4 = "Physics"
         col_5 = "Chemistry"
         col_6 = "Biology"

      elif select_grp_.get() == "Comerce-it":
         sql = "SELECT Exam , English , Maths , Accounts , Business_studies , IT FROM cs_mat WHERE Admn_num = %s and Class = %s and Sec = %s;"
         value = (admn_num , cls , sec)
         col_1 = "Exam"
         col_2 = "English"
         col_3 = "Business Studies"
         col_4 = "Accounts"
         col_5 = "IT"
         col_6 = "Maths"

      elif select_grp_.get() == "Comerce-Economics":
         sql = "SELECT Exam , English , Maths , Accounts , Business_studies , Economics FROM cs_mat WHERE Admn_num = %s and Class = %s and Sec = %s;"
         value = (admn_num , cls , sec)
         col_1 = "Exam"
         col_2 = "English"
         col_3 = "Business Studies"
         col_4 = "Accounts"
         col_5 = "Economics"
         col_6 = "Maths"
             
      elif select_grp_.get() == "Comerce-Marketing":
         sql = "SELECT Exam , English , Maths , Accounts , Business_studies , Marketing FROM cs_mat WHERE Admn_num = %s and Class = %s and Sec = %s;"
         value = (admn_num , cls , sec)
         col_1 = "Exam"
         col_2 = "English"
         col_3 = "Business Studies"
         col_4 = "Accounts"
         col_5 = "Marketing"
         col_6 = "Maths"

      mysql_cursor.execute(sql , value)
      marks = mysql_cursor.fetchall()

      Mark_reg["columns"] = (col_1 , col_2 , col_3 , col_4 , col_5 , col_6)
      Mark_reg.column("#0" , width = 0 , stretch = NO)
      Mark_reg.column(col_1 ,  anchor = W , width = 150)
      Mark_reg.column(col_2 ,  anchor = CENTER , width = 105)
      Mark_reg.column(col_3 ,  anchor = CENTER , width = 105)
      Mark_reg.column(col_4 ,  anchor = CENTER , width = 105)
      Mark_reg.column(col_5 ,  anchor = CENTER , width = 105)
      Mark_reg.column(col_6 ,  anchor = CENTER , width = 105)

      Mark_reg.heading("#0" , text = "" , anchor = CENTER)
      Mark_reg.heading(col_1 , text = col_1 , anchor = CENTER)
      Mark_reg.heading(col_2 , text = col_2 , anchor = CENTER)
      Mark_reg.heading(col_3 , text = col_3 , anchor = CENTER)
      Mark_reg.heading(col_4 , text = col_4 , anchor = CENTER)
      Mark_reg.heading(col_5 , text = col_5 , anchor = CENTER)
      Mark_reg.heading(col_6 , text = col_6 , anchor = CENTER)

      cnt = 0
      for something in marks:
          Mark_reg.insert(parent = '' , index = 'end' , iid = cnt , text = '' , values = (something[0] , something[1] , something[2] , something[3] , something[4] , something[5]))
          cnt += 1

   elif cls == "IX" or cls == "X":
      sql = "SELECT Exam , English , Science , Maths , II_Lang , Social_Science , IT FROM 9th_10th_std WHERE Admn_num = %s and Class = %s and Sec = %s;"
      value = (admn_num , cls , sec)

      mysql_cursor.execute(sql , value)
      marks = mysql_cursor.fetchall()

      Mark_reg["columns"] = ("exam" , "english" , "evs" , "maths" , "IIlang" , "soc" , "it")
      Mark_reg.column("#0" , width = 0 , stretch = NO)
      Mark_reg.column("exam" ,  anchor = W , width = 150)
      Mark_reg.column("english" ,  anchor = CENTER , width = 105)
      Mark_reg.column("evs" ,  anchor = CENTER , width = 105)
      Mark_reg.column("maths" ,  anchor = CENTER , width = 105)
      Mark_reg.column("IIlang" ,  anchor = CENTER , width = 105)
      Mark_reg.column("soc" ,  anchor = CENTER , width = 105)
      Mark_reg.column("it" ,  anchor = CENTER , width = 105)

      Mark_reg.heading("#0" , text = "" , anchor = CENTER)
      Mark_reg.heading("exam" , text = "Exam" , anchor = CENTER)
      Mark_reg.heading("english" , text = "English" , anchor = CENTER)
      Mark_reg.heading("evs" , text = "EVS" , anchor = CENTER)
      Mark_reg.heading("maths" , text = "Maths" , anchor = CENTER)
      Mark_reg.heading("IIlang" , text = "II Language" , anchor = CENTER)
      Mark_reg.heading("soc" , text = "Social Science" , anchor = CENTER)
      Mark_reg.heading("it" , text = "IT" , anchor = CENTER)

      cnt = 0
      for something in marks:
          Mark_reg.insert(parent = '' , index = 'end' , iid = cnt , text = '' , values = (something[0] , something[1] , something[2] , something[3] , something[4] , something[5] , something[6]))
          cnt += 1
   
   elif cls == "VI" or cls == "VII" or cls == "VIII":
      sql = "SELECT Exam , English , Science , Maths , II_Lang , III_Lang , Social_Science , Computer_Science , Sanskrit FROM 6th_to_8th_std WHERE Admn_num = %s and Class = %s and Sec = %s;"
      value = (admn_num , cls , sec)

      mysql_cursor.execute(sql , value)
      marks = mysql_cursor.fetchall()

      Mark_reg["columns"] = ("exam" , "english" , "evs" , "maths" , "IIlang" , "IIIlang", "soc" , "cs" , "sans")
      Mark_reg.column("#0" , width = 0 , stretch = NO)
      Mark_reg.column("exam" ,  anchor = W , width = 150)
      Mark_reg.column("english" ,  anchor = CENTER , width = 105)
      Mark_reg.column("evs" ,  anchor = CENTER , width = 105)
      Mark_reg.column("maths" ,  anchor = CENTER , width = 105)
      Mark_reg.column("IIlang" ,  anchor = CENTER , width = 105)
      Mark_reg.column("IIIlang" ,  anchor = CENTER , width = 105)
      Mark_reg.column("soc" ,  anchor = CENTER , width = 105)
      Mark_reg.column("cs" ,  anchor = CENTER , width = 105)
      Mark_reg.column("sans" ,  anchor = CENTER , width = 105)

      Mark_reg.heading("#0" , text = "" , anchor = CENTER)
      Mark_reg.heading("exam" , text = "Exam" , anchor = CENTER)
      Mark_reg.heading("english" , text = "English" , anchor = CENTER)
      Mark_reg.heading("evs" , text = "EVS" , anchor = CENTER)
      Mark_reg.heading("maths" , text = "Maths" , anchor = CENTER)
      Mark_reg.heading("IIlang" , text = "II Language" , anchor = CENTER)
      Mark_reg.heading("IIIlang" , text = "III Language" , anchor = CENTER)
      Mark_reg.heading("soc" , text = "Social Science" , anchor = CENTER)
      Mark_reg.heading("cs" , text = "Computer Science" , anchor = CENTER)
      Mark_reg.heading("sans" , text = "Sanskrit" , anchor = CENTER)

      cnt = 0
      for something in marks:
          Mark_reg.insert(parent = '' , index = 'end' , iid = cnt , text = '' , values = (something[0] , something[1] , something[2] , something[3] , something[4] , something[5] , something[6] , something[7] , something[8]))
          cnt += 1
   
   elif cls == "V":
      sql = "SELECT Exam , English , Science , Maths , II_Lang , III_Lang , Social_Science , Computer_Science FROM 5th_std WHERE Admn_num = %s and Class = %s and Sec = %s;"
      value = (admn_num , cls , sec)

      mysql_cursor.execute(sql , value)
      marks = mysql_cursor.fetchall()

      Mark_reg["columns"] = ("exam" , "english" , "evs" , "maths" , "IIlang" , "IIIlang", "soc" , "cs")
      Mark_reg.column("#0" , width = 0 , stretch = NO)
      Mark_reg.column("exam" ,  anchor = W , width = 150)
      Mark_reg.column("english" ,  anchor = CENTER , width = 105)
      Mark_reg.column("evs" ,  anchor = CENTER , width = 105)
      Mark_reg.column("maths" ,  anchor = CENTER , width = 105)
      Mark_reg.column("IIlang" ,  anchor = CENTER , width = 105)
      Mark_reg.column("IIIlang" ,  anchor = CENTER , width = 105)
      Mark_reg.column("soc" ,  anchor = CENTER , width = 105)
      Mark_reg.column("cs" ,  anchor = CENTER , width = 105)

      Mark_reg.heading("#0" , text = "" , anchor = CENTER)
      Mark_reg.heading("exam" , text = "Exam" , anchor = CENTER)
      Mark_reg.heading("english" , text = "English" , anchor = CENTER)
      Mark_reg.heading("evs" , text = "EVS" , anchor = CENTER)
      Mark_reg.heading("maths" , text = "Maths" , anchor = CENTER)
      Mark_reg.heading("IIlang" , text = "II Language" , anchor = CENTER)
      Mark_reg.heading("IIIlang" , text = "III Language" , anchor = CENTER)
      Mark_reg.heading("soc" , text = "Social Science" , anchor = CENTER)
      Mark_reg.heading("cs" , text = "Computer Science" , anchor = CENTER)

      cnt = 0
      for something in marks:
          Mark_reg.insert(parent = '' , index = 'end' , iid = cnt , text = '' , values = (something[0] , something[1] , something[2] , something[3] , something[4] , something[5] , something[6] , something[7]))
          cnt += 1
   
   elif cls == "III" or cls == "IV":
      sql = "SELECT Exam , English , EVS , Maths , II_Lang , III_Lang , ICT FROM 3rd_4th_std WHERE Admn_num = %s and Class = %s and Sec = %s;"
      value = (admn_num , cls , sec)

      mysql_cursor.execute(sql , value)
      marks = mysql_cursor.fetchall()

      Mark_reg["columns"] = ("exam" , "english" , "evs" , "maths" , "IIlang" , "IIIlang", "cs")
      Mark_reg.column("#0" , width = 0 , stretch = NO)
      Mark_reg.column("exam" ,  anchor = W , width = 150)
      Mark_reg.column("english" ,  anchor = CENTER , width = 105)
      Mark_reg.column("evs" ,  anchor = CENTER , width = 105)
      Mark_reg.column("maths" ,  anchor = CENTER , width = 105)
      Mark_reg.column("IIlang" ,  anchor = CENTER , width = 105)
      Mark_reg.column("IIIlang" ,  anchor = CENTER , width = 105)
      Mark_reg.column("cs" ,  anchor = CENTER , width = 105)

      Mark_reg.heading("#0" , text = "" , anchor = CENTER)
      Mark_reg.heading("exam" , text = "Exam" , anchor = CENTER)
      Mark_reg.heading("english" , text = "English" , anchor = CENTER)
      Mark_reg.heading("evs" , text = "EVS" , anchor = CENTER)
      Mark_reg.heading("maths" , text = "Maths" , anchor = CENTER)
      Mark_reg.heading("IIlang" , text = "II Language" , anchor = CENTER)
      Mark_reg.heading("IIIlang" , text = "III Language" , anchor = CENTER)
      Mark_reg.heading("cs" , text = "Computer Science" , anchor = CENTER)

      cnt = 0
      for something in marks:
          Mark_reg.insert(parent = '' , index = 'end' , iid = cnt , text = '' , values = (something[0] , something[1] , something[2] , something[3] , something[4] , something[5] , something[6]))
          cnt += 1
   
   elif cls == "I" or cls == "II":
      sql = "SELECT Exam , English , EVS , Maths , Tamil FROM 1st_2nd_std WHERE Admn_num = %s and Class = %s and Sec = %s;"
      value = (admn_num , cls , sec)

      mysql_cursor.execute(sql , value)
      marks = mysql_cursor.fetchall()

      Mark_reg["columns"] = ("exam" , "english" , "evs" , "maths" , "tamil")
      Mark_reg.column("#0" , width = 0 , stretch = NO)
      Mark_reg.column("exam" ,  anchor = W , width = 150)
      Mark_reg.column("english" ,  anchor = CENTER , width = 105)
      Mark_reg.column("evs" ,  anchor = CENTER , width = 105)
      Mark_reg.column("maths" ,  anchor = CENTER , width = 105)
      Mark_reg.column("tamil" ,  anchor = CENTER , width = 105)

      Mark_reg.heading("#0" , text = "" , anchor = CENTER)
      Mark_reg.heading("exam" , text = "Exam" , anchor = CENTER)
      Mark_reg.heading("english" , text = "English" , anchor = CENTER)
      Mark_reg.heading("evs" , text = "EVS" , anchor = CENTER)
      Mark_reg.heading("maths" , text = "Maths" , anchor = CENTER)
      Mark_reg.heading("tamil" , text = "Tamil" , anchor = CENTER)

      cnt = 0
      for something in marks:
          Mark_reg.insert(parent = '' , index = 'end' , iid = cnt , text = '' , values = (something[0] , something[1] , something[2] , something[3] , something[4]))
          cnt += 1

   Mark_reg.place(x = 40 , y = 180)


# Enable group Dropdown box
def enable_grp(event):
   if class_.get() == "XII" or class_.get() == "XI":
      select_grp_.config(state = NORMAL)
   elif class_.get() == "I" or class_.get() == "II":
      select_grp_.current(0)
      select_grp_.config(state = DISABLED)
   elif class_.get() == "III" or class_.get() == "IV":
      select_grp_.current(0)
      select_grp_.config(state = DISABLED)
   elif class_.get() == "V":
      select_grp_.current(0)
      select_grp_.config(state = DISABLED)
   elif class_.get() == "VI" or class_.get() == "VII" or class_.get() == "VIII":
      select_grp_.current(0)
      select_grp_.config(state = DISABLED)
   elif class_.get() == "IX" or class_.get() == "X":
      select_grp_.current(0)
      select_grp_.config(state = DISABLED)


# Command for view button in menu
def teach_view():
   global view_or_add
   global adm_num_label
   global admn_no
   global class_
   global sec_
   global select_grp_
   global Mark_reg
   global view_recs
   
   if view_or_add == "add":
      stud_dets_label.place_forget()
      admn_num_label.place_forget()
      admn_number.place_forget()
      add_class.place_forget()
      add_sec.place_forget()
      grp.place_forget()
      Exam.place_forget()
      add_recs_button.place_forget()

      if cls_or_grp == "com-it":
         acc_comit.place_forget()
         mat_comit.place_forget()
         eng_comit.place_forget()
         bs_comit.place_forget()
         it_comit.place_forget()

         accounts_entry_comit.place_forget()
         mat_entry_comit.place_forget()
         english_entry_comit.place_forget()
         business_studies_entry_comit.place_forget()
         It_entry_comit.place_forget()

      elif cls_or_grp == "com-mar":
         acc_commar.place_forget()
         mat_commar.place_forget()
         eng_commar.place_forget()
         bs_commar.place_forget()
         mar_commar.place_forget()

         accounts_entry_commar.place_forget()
         mat_entry_commar.place_forget()
         english_entry_commar.place_forget()
         business_studies_entry_commar.place_forget()
         marketing_entry_commar.place_forget()

      elif cls_or_grp == "com-eco":
         acc_comeco.place_forget()
         mat_comeco.place_forget()
         eng_comeco.place_forget()
         bs_comeco.place_forget()
         eco_comeco.place_forget()

         accounts_entry_comeco.place_forget()
         mat_entry_comeco.place_forget()
         english_entry_comeco.place_forget()
         business_studies_entry_comeco.place_forget()
         economics_entry_comeco.place_forget()

      elif cls_or_grp == "cs-mat":
         cs_csmat.place_forget()
         mat_csmat.place_forget()
         eng_csmat.place_forget()
         phy_csmat.place_forget()
         chem_csmat.place_forget()

         computer_science_entry_csmat.place_forget()
         mat_entry_csmat.place_forget()
         english_entry_csmat.place_forget()
         physics_entry_csmat.place_forget()
         chemistry_entry_csmat.place_forget()

      elif cls_or_grp == "bio-cs":
         cs_biocs.place_forget()
         eng_biocs.place_forget()
         bio_biocs.place_forget()
         phy_biocs.place_forget()
         chem_biocs.place_forget()

         computer_science_entry_biocs.place_forget()
         eng_entry_biocs.place_forget()
         biology_entry_biocs.place_forget()
         physics_entry_biocs.place_forget()
         chemistry_entry_biocs.place_forget()

      elif cls_or_grp == "bio-mat":
         mat_biomat.place_forget()
         bio_biomat.place_forget()
         eng_biomat.place_forget()
         phy_biomat.place_forget()
         chem_biomat.place_forget()

         mat_entry_biomat.place_forget()
         biology_entry_biomat.place_forget()
         english_entry_biomat.place_forget()
         physics_entry_biomat.place_forget()
         chemistry_entry_biomat.place_forget()

      elif cls_or_grp == "9 or 10":
         eng_9.place_forget()
         mat_9.place_forget()
         sci_9.place_forget()
         IIlang_9.place_forget()
         it_9.place_forget()
         soc_9.place_forget()

         eng_entry_9.place_forget()
         mat_entry_9.place_forget()
         science_entry_9.place_forget()
         II_Lang_entry_9.place_forget()
         IT_entry_9.place_forget()
         Social_science_entry_9.place_forget()

      elif cls_or_grp == "6 to 8":
         eng_6.place_forget()
         mat_6.place_forget()
         sci_6.place_forget()
         IIlang_6.place_forget()
         IIIlang_6.place_forget()
         soc_6.place_forget()
         cs_6.place_forget()
         sans_6.place_forget()
         
         eng_entry_6.place_forget()
         mat_entry_6.place_forget()
         science_entry_6.place_forget()
         II_Lang_entry_6.place_forget()
         III_Lang_entry_6.place_forget()
         Social_science_entry_6.place_forget()
         Computer_science_entry_6.place_forget()
         sanskrit_entry_6.place_forget()

      elif cls_or_grp == "5":
         eng_5.place_forget()
         mat_5.place_forget()
         sci_5.place_forget()
         IIlang_5.place_forget()
         IIIlang_5.place_forget()
         soc_5.place_forget()
         cs_5.place_forget()
         
         eng_entry_5.place_forget()
         mat_entry_5.place_forget()
         science_entry_5.place_forget()
         II_Lang_entry_5.place_forget()
         III_Lang_entry_5.place_forget()
         Social_science_entry_5.place_forget()
         Computer_science_entry_5.place_forget()

      elif cls_or_grp == "3 or 4":
         eng_3.place_forget()
         mat_3.place_forget()
         evs_3.place_forget()
         IIlang_3.place_forget()
         IIIlang_3.place_forget()
         cs_3.place_forget()
         
         eng_entry_3.place_forget()
         mat_entry_3.place_forget()
         evs_entry_3.place_forget()
         II_Lang_entry_3.place_forget()
         III_Lang_entry_3.place_forget()
         Computer_science_entry_3.place_forget()

      elif cls_or_grp == "1 or 2":
         eng_1.place_forget()
         mat_1.place_forget()
         evs_1.place_forget()
         tam_1.place_forget()
         
         eng_entry_1.place_forget()
         mat_entry_1.place_forget()
         evs_entry_1.place_forget()
         tam_entry_1.place_forget()
         
   elif view_or_add == "view":
      adm_num_label.place_forget()
      admn_no.place_forget()
      class_.place_forget()
      sec_.place_forget()
      select_grp_.place_forget()
      Mark_reg.place_forget()
      view_recs.place_forget()

   view_or_add = "view"
   
   Home_screen.geometry("800x500")
   quote3.place_forget()

   adm_num_label = Label(Home_screen , text = "Admission Number:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")   
   admn_no = Entry(Home_screen , width = 30)
 
   classes_ = ['Select Class' , 'XII' , 'XI' , 'X' , 'IX' , 'VIII' , 'VII' , 'VI' , 'V' , 'IV' , 'III' , 'II' , 'I']
   class_ = ttk.Combobox(Home_screen , value = classes_)
   class_.current(0)
   class_.bind("<<ComboboxSelected>>" , enable_grp)

   sections_ = ['Select Section' , 'A' , 'B' , 'C' , 'D']
   sec_ = ttk.Combobox(Home_screen , value = sections_)
   sec_.current(0)
   
   select_grps_ = ["Select Group" , "CS-Maths" , "Bio-Maths" , "Bio-Cs" , "Comerce-It" , "Comerce-Economics" , "Comerce-Marketing"]
   select_grp_ = ttk.Combobox(Home_screen , value = select_grps_ , state = DISABLED)
   select_grp_.current(0)
   
   Mark_reg = ttk.Treeview(Home_screen)
   view_recs = Button(Home_screen , text = "View Records" , command = table_teach)

   adm_num_label.place(x = 40 , y = 60)
   admn_no.place(x = 250 , y = 66)
   class_.place(x = 40 , y = 100)
   sec_.place(x = 200 , y = 100)
   select_grp_.place(x = 40 , y = 140)
   view_recs.place(x = 200 , y = 140)
   
   
def add():
   global view_or_add
   global stud_dets_label
   global admn_num_label
   global admn_number
   global add_class
   global add_sec
   global grp
   global Exam
   global add_recs_button

   if view_or_add == "view":
      adm_num_label.place_forget()
      admn_no.place_forget()
      class_.place_forget()
      sec_.place_forget()
      select_grp_.place_forget()
      Mark_reg.place_forget()
      view_recs.place_forget()

   elif view_or_add == "add":
      stud_dets_label.place_forget()
      admn_num_label.place_forget()
      admn_number.place_forget()
      add_class.place_forget()
      add_sec.place_forget()
      grp.place_forget()
      Exam.place_forget()
      add_recs_button.place_forget()

      if cls_or_grp == "com-it":
         acc_comit.place_forget()
         mat_comit.place_forget()
         eng_comit.place_forget()
         bs_comit.place_forget()
         it_comit.place_forget()

         accounts_entry_comit.place_forget()
         mat_entry_comit.place_forget()
         english_entry_comit.place_forget()
         business_studies_entry_comit.place_forget()
         It_entry_comit.place_forget()

      elif cls_or_grp == "com-mar":
         acc_commar.place_forget()
         mat_commar.place_forget()
         eng_commar.place_forget()
         bs_commar.place_forget()
         mar_commar.place_forget()

         accounts_entry_commar.place_forget()
         mat_entry_commar.place_forget()
         english_entry_commar.place_forget()
         business_studies_entry_commar.place_forget()
         marketing_entry_commar.place_forget()

      elif cls_or_grp == "com-eco":
         acc_comeco.place_forget()
         mat_comeco.place_forget()
         eng_comeco.place_forget()
         bs_comeco.place_forget()
         eco_comeco.place_forget()

         accounts_entry_comeco.place_forget()
         mat_entry_comeco.place_forget()
         english_entry_comeco.place_forget()
         business_studies_entry_comeco.place_forget()
         economics_entry_comeco.place_forget()

      elif cls_or_grp == "cs-mat":
         cs_csmat.place_forget()
         mat_csmat.place_forget()
         eng_csmat.place_forget()
         phy_csmat.place_forget()
         chem_csmat.place_forget()

         computer_science_entry_csmat.place_forget()
         mat_entry_csmat.place_forget()
         english_entry_csmat.place_forget()
         physics_entry_csmat.place_forget()
         chemistry_entry_csmat.place_forget()

      elif cls_or_grp == "bio-cs":
         cs_biocs.place_forget()
         eng_biocs.place_forget()
         bio_biocs.place_forget()
         phy_biocs.place_forget()
         chem_biocs.place_forget()

         computer_science_entry_biocs.place_forget()
         eng_entry_biocs.place_forget()
         biology_entry_biocs.place_forget()
         physics_entry_biocs.place_forget()
         chemistry_entry_biocs.place_forget()

      elif cls_or_grp == "bio-mat":
         mat_biomat.place_forget()
         bio_biomat.place_forget()
         eng_biomat.place_forget()
         phy_biomat.place_forget()
         chem_biomat.place_forget()

         mat_entry_biomat.place_forget()
         biology_entry_biomat.place_forget()
         english_entry_biomat.place_forget()
         physics_entry_biomat.place_forget()
         chemistry_entry_biomat.place_forget()

      elif cls_or_grp == "9 or 10":
         eng_9.place_forget()
         mat_9.place_forget()
         sci_9.place_forget()
         IIlang_9.place_forget()
         it_9.place_forget()
         soc_9.place_forget()

         eng_entry_9.place_forget()
         mat_entry_9.place_forget()
         science_entry_9.place_forget()
         II_Lang_entry_9.place_forget()
         IT_entry_9.place_forget()
         Social_science_entry_9.place_forget()

      elif cls_or_grp == "6 to 8":
         eng_6.place_forget()
         mat_6.place_forget()
         sci_6.place_forget()
         IIlang_6.place_forget()
         IIIlang_6.place_forget()
         soc_6.place_forget()
         cs_6.place_forget()
         sans_6.place_forget()
         
         eng_entry_6.place_forget()
         mat_entry_6.place_forget()
         science_entry_6.place_forget()
         II_Lang_entry_6.place_forget()
         III_Lang_entry_6.place_forget()
         Social_science_entry_6.place_forget()
         Computer_science_entry_6.place_forget()
         sanskrit_entry_6.place_forget()

      elif cls_or_grp == "5":
         eng_5.place_forget()
         mat_5.place_forget()
         sci_5.place_forget()
         IIlang_5.place_forget()
         IIIlang_5.place_forget()
         soc_5.place_forget()
         cs_5.place_forget()
         
         eng_entry_5.place_forget()
         mat_entry_5.place_forget()
         science_entry_5.place_forget()
         II_Lang_entry_5.place_forget()
         III_Lang_entry_5.place_forget()
         Social_science_entry_5.place_forget()
         Computer_science_entry_5.place_forget()

      elif cls_or_grp == "3 or 4":
         eng_3.place_forget()
         mat_3.place_forget()
         evs_3.place_forget()
         IIlang_3.place_forget()
         IIIlang_3.place_forget()
         cs_3.place_forget()
         
         eng_entry_3.place_forget()
         mat_entry_3.place_forget()
         evs_entry_3.place_forget()
         II_Lang_entry_3.place_forget()
         III_Lang_entry_3.place_forget()
         Computer_science_entry_3.place_forget()

      elif cls_or_grp == "1 or 2":
         eng_1.place_forget()
         mat_1.place_forget()
         evs_1.place_forget()
         tam_1.place_forget()
         
         eng_entry_1.place_forget()
         mat_entry_1.place_forget()
         evs_entry_1.place_forget()
         tam_entry_1.place_forget()

   view_or_add = "add"
   
   Home_screen.geometry("400x250")
   quote3.place_forget()
   
   stud_dets_label = Label(Home_screen , text = "Student Details:" , font = ("Consolas Bold" , 17) , bg = "sky blue")
   admn_num_label = Label(Home_screen , text = "Admission Number:" , font = ("Colonna MT Bold" , 15) , bg = "sky blue")
   admn_number = Entry(Home_screen , width = 30)

   classes = ['Select Class' , 'XII' , 'XI' , 'X' , 'IX' , 'VIII' , 'VII' , 'VI' , 'V' , 'IV' , 'III' , 'II' , 'I']
   add_class = ttk.Combobox(Home_screen , value = classes)
   add_class.current(0)
   add_class.bind("<<ComboboxSelected>>" , dropdown_bind)
   
   sections = ['Select Section' , 'A' , 'B' , 'C' , 'D']
   add_sec = ttk.Combobox(Home_screen , value = sections)
   add_sec.current(0)
   
   grps = ["Select Group" , "CS-Maths" , "Bio-Maths" , "Bio-Cs" , "Comerce-It" , "Comerce-Economics" , "Comerce-Marketing"]
   grp = ttk.Combobox(Home_screen , value = grps , state = DISABLED)
   grp.current(0)
   
   Exams = ["Select Examination" , "April Monthly Test" , "June Monthly Test" , "July Monthly Test" , "August Monthly Test" , "Half-yearly Examination" , "November Monthly Test" , "December Monthly Test" , "January Monthly Test" , "February Monthly Test" , "Annual Examination"]
   Exam = ttk.Combobox(Home_screen , value = Exams)
   Exam.current(0)

   add_recs_button = Button(Home_screen , text = "Add Records" , command = lambda: add_recs(admn_number.get() , add_class.get() , add_sec.get() , Exam.get()))

   stud_dets_label.place(x = 110 , y = 55)
   admn_num_label.place(x = 15 , y = 90)
   admn_number.place(x = 200 , y = 96)
   add_class.place(x = 15 , y = 130)
   add_sec.place(x =175 , y = 130)
   grp.place(x = 15 , y = 170)
   Exam.place(x = 175 , y = 170)
   

def logged_in_as_stud(username):
    mysql_cursor.execute("SELECT * FROM stud_dets , login_credentials WHERE login_credentials.Username = %s AND stud_dets.Username = login_credentials.Username;" , (username ,))
    global recs
    recs = mysql_cursor.fetchall()
    Label(Home_screen , text = "Name : " + recs[0][1] , font = ("Comic sans" , 15) , bg = "sky blue" , fg = "#ac7d0c").place(x = 25 , y = 40)
    Label(Home_screen , text = "Class and Section : " + recs[0][6] + "-" + recs[0][7], font = ("Comic sans" , 15) , bg = "sky blue" , fg = "#ac7d0c").place(x = 25 , y = 67)
    Label(Home_screen , text = "Admission Number : " + str(recs[0][0]) , font = ("Comic sans" , 15) , bg = "sky blue" , fg = "#ac7d0c").place(x = 25 , y = 94)
    Label(Home_screen , text = "Father Name : " + recs[0][3] , font = ("Comic sans" , 15) , bg = "sky blue" , fg = "#ac7d0c").place(x = 25 , y = 121)
    Label(Home_screen , text = "Mother Name : " + recs[0][4] , font = ("Comic sans" , 15) , bg = "sky blue" , fg = "#ac7d0c").place(x = 25 , y = 148)
    Home_screen.geometry("310x200")

    menu_bar.delete("Signup")
    Home_menu.entryconfig("View" , state = NORMAL , command = stud_view)
    

def logged_in_as_teach(username):
    global quote3
    global view_or_add

    view_or_add = ""
    
    mysql_cursor.execute("SELECT Name FROM teach_dets , login_credentials WHERE login_credentials.Username = %s AND teach_dets.Username = login_credentials.Username;" , (username ,))
    name = mysql_cursor.fetchall()
    Label(Home_screen , text = "Name : " + name[0][0] , font = ("Comic sans" , 15) , bg = "sky blue" , fg = "#ac7d0c").place(x = 25 , y = 30)
    Home_screen.geometry("310x200")

    quote3 = Label(Home_screen , text = "The best teachers teach\nfrom the heart\nnot from the book." , font = ("Consolas" , 16 , "bold") , bg = "sky blue" , fg = "dark violet")
    quote3.place(x = 15 , y = 100)

    menu_bar.delete("Signup")
    Home_menu.entryconfig("View" , state = NORMAL , command = teach_view)
    Home_menu.entryconfig("Add" , state = NORMAL , command = add)

def query(Name , Username , Password):
    if state == "teach signup":
        sql = "INSERT INTO login_credentials(Username , Password , Teacher) VALUES(%s , %s , %s);"
        value = (Username , Password , "Yes")
        mysql_cursor.execute(sql , value)

        sql = "INSERT INTO teach_dets(Name , Username) VALUES(%s , %s);"
        value = (Name , Username)
        mysql_cursor.execute(sql , value)
        
        connector.commit()

        login()
    elif state == "stud signup":
        sql = "INSERT INTO login_credentials(Username , Password , Teacher) VALUES(%s , %s , %s);"
        value = (Username , Password , "No")
        mysql_cursor.execute(sql , value)

        sql = "INSERT INTO stud_dets(Admission_num , Name , Username , Father_name , Mother_name , DOB , Class , Section) VALUES(%s , %s , %s , %s , %s , %s , %s , %s);"
        value = (stud_admn_num_entry.get() , Name , Username , stud_fathername_entry.get() , stud_mothername_entry.get() , stud_DOB_entry.get() , stud_class.get() , stud_sec.get())
        mysql_cursor.execute(sql , value)
        
        connector.commit()

        login()
    else:
        sql = "SELECT * FROM login_credentials WHERE Username = %s AND Password = %s AND Teacher = %s;"
        value = (Username , Password , selection)
        mysql_cursor.execute(sql , value)

        tab_cred = mysql_cursor.fetchall()

        if selection == "Yes":
            tab_selection = "teach_dets"
        else:
            tab_selection = "stud_dets"
        sql = "SELECT Name FROM {} WHERE Name = %s;".format(tab_selection)
        value = (Name ,)
        mysql_cursor.execute(sql , value)

        tab_name = mysql_cursor.fetchall()
        if len(tab_cred) > 0 and len(tab_name) > 0:
            login_window.destroy()
            
            quote1.place_forget()
            quote2.place_forget()
            byline1.place_forget()
            byline2.place_forget()

            if selection == "Yes":
                logged_in_as_teach(Username)
            else:
                logged_in_as_stud(Username)
        else:
            Label(login_window , text = "Incorrect Username or Password" , font = ("Consolas" , 8) , bg = "white" , fg = "red").place(x = 5 , y = 149)


# Show or hide password funvtion
def Show_password_command():
    if show_or_hide_password.get() == "Show":
        if are_you_a_teacher == "yes":
            teach_password_entry.config(show = "")
        elif are_you_a_teacher == "no":
            stud_password_entry.config(show = "")
    elif show_or_hide_password.get() == "hide":
        if are_you_a_teacher == "yes":
            teach_password_entry.config(show = "*")
        elif are_you_a_teacher == "no":
            stud_password_entry.config(show = "*")


def Show_password_cmd():
    if show_or_hide_pass.get() == "hide":
        password_entry.config(show = "*")
    elif show_or_hide_pass.get() == "Show":
        password_entry.config(show = "")


def reset_pass(new_password , username):
   sql = "UPDATE login_credentials SET Password = %s WHERE Username = %s;"
   value = (new_password , username)

   mysql_cursor.execute(sql , value)
   connector.commit()

   reset_pass_window.destroy()
   login()


def verification():
      label_2.pack_forget()
      otp_verification.pack_forget()
      verify_1.pack_forget()

      uname = Entry(reset_pass_window , width = 30)
      new_pass = Entry(reset_pass_window , width = 30)
      reset = Button(reset_pass_window , text = "Reset Password" , command = lambda: reset_pass(new_pass.get() , uname.get()))

      Label(reset_pass_window , text = "Username").pack(pady = 5)
      uname.pack(pady = 10)
      Label(reset_pass_window , text = "New Password").pack(pady = 5)
      new_pass.pack(pady = 10)
      reset.pack(pady = 10)
      

def send_otp(to_email):
    global OTP
    global label_2
    global otp_verification
    global verify_1
    otp = ""
    for iteration in range(4):
        digit = random.randrange(10)
        otp += str(digit)
    OTP = otp
    
    
    msg = EmailMessage()
    msg['Subject'] = "Reset Password"
    msg['From'] = "sarsofficial.ad@gmail.com"
    msg['To'] = to_email
    msg.set_content("""
<html>
    <body>                            
        <h1>OTP Requested<h1>
        <h3>Hello \nYour One Time Password is: {}
        <br>Don't share it with anybody.


        <br><br>Thank you,
        <br>SARS Team<h3>
    <body>
<html>""".format(otp) , subtype = "html")


    server = smtplib.SMTP("smtp.gmail.com" , 587)
    server.starttls()
    server.login("sarsofficial.ad@gmail.com" , "Sarsofficial123")
    server.send_message(msg)
    server.quit()

    label_1.pack_forget()
    email.pack_forget()
    otp_button.pack_forget()

    label_2 = Label(reset_pass_window , text = "Enter OTP" , font = ("Comic Sans" , 12))
    label_2.pack(pady = 5)
    otp_verification = Entry(reset_pass_window , width = 20)
    otp_verification.pack(pady = 5)
    verify_1 = Button(reset_pass_window , text = "Verify" , command = verification)
    verify_1.pack(pady = 10)


def forgot_password():
    global label_1
    global email
    global otp_button
    global reset_pass_window

    login_window.destroy()
    reset_pass_window = Toplevel()
    reset_pass_window.title("Reset Password")
    reset_pass_window.geometry("250x190")
    reset_pass_window.resizable(width = False , height = False)

    label_1 = Label(reset_pass_window , text = "Enter email id to send otp\nfor resetting password " , font = ("Comic Sans" , 12))
    label_1.pack(padx = 25 , pady = 10)
    email = Entry(reset_pass_window , width = 40 , borderwidth = 2)
    email.pack(padx = 25)
    otp_button = Button(reset_pass_window , text = "Send OTP" , command = lambda: send_otp(email.get()))
    otp_button.pack(pady = 15)


def login():
    global password_entry
    global state
    global show_or_hide_pass
    global selection
    global login_window
    global forgot_pass

    if state == "teach signup":
        teach_signup_window.destroy()
    elif state == "stud signup":
        stud_signup_window.destroy()

    state = "login"

    teach_or_stud = messagebox.askquestion("Select and login" , "Are you a teacher?")
    if teach_or_stud == "yes":
        selection = "Yes"
    else:
        selection = "No"
    
    login_window = Toplevel()
    login_window.title("Login")
    login_window["bg"] = "white"
    login_window.geometry("255x235")
    login_window.resizable(width = False , height = False)

    name = Label(login_window , text = "Name" , font = ("MS UI GOTHIC" , 10 , "bold") , bg = "white")
    username = Label(login_window , text = "Username" , font = ("MS UI GOTHIC" , 10 , "bold") , bg = "white")
    password = Label(login_window , text = "Password" , font = ("MS UI GOTHIC" , 10 , "bold") , bg = "white")

    name_entry = Entry(login_window , width = 40 , borderwidth = 2)
    username_entry = Entry(login_window , width = 40 , borderwidth = 2)
    password_entry = Entry(login_window , width = 40 , borderwidth = 2)

    show_or_hide_pass = StringVar()
    show_or_hide_pass.set("hide")
    show_pass = Checkbutton(login_window , text = "Show Password" , onvalue = "Show" , offvalue = "hide" , variable = show_or_hide_pass , bg = "white" , activebackground = "white" , command = Show_password_cmd)

    Show_password_cmd()

    forgot_pass = Button(login_window , text = "forgot password?" , font = ("Segoe print" , 10 , "underline") , bg = "white" , fg = "blue" , border = 0 , activebackground = "white" , command = forgot_password)
                         
    login = Button(login_window , text = "Login" , font = ("Times new roman bold" , 12) , bg = "white" , command = lambda: query(name_entry.get() , username_entry.get() , password_entry.get()))

    name.place(x= 5 , y = 5)
    name_entry.place(x = 5 , y = 25)
    username.place(x = 5 , y = 47)
    username_entry.place(x = 5 , y = 67)
    password.place(x = 5 , y = 89)
    password_entry.place(x = 5 , y = 109)
    show_pass.place(x = 5 , y = 131)
    forgot_pass.place(x = 5 , y = 150)
    login.place(x = 100 , y = 190)


# Signup page for a teacher
def teacher_signup():
    global teach_signup_window
    global show_or_hide_password
    global teach_password_entry
    global state

    state = "teach signup"
    
    teach_signup_window = Toplevel()
    teach_signup_window.title("Signup")
    teach_signup_window["bg"] = "white"
    app_width = 255
    app_height = 235
    x_coordinate = int((screen_width/2) - (app_width/2))
    y_coordinate = int((screen_height/2) - (app_height/2))
    teach_signup_window.geometry(f'{app_width}x{app_height}+{x_coordinate}+{y_coordinate}')
    teach_signup_window.resizable(width = False , height = False)
    
    teach_name = Label(teach_signup_window , text = "Name" , font = ("MS UI GOTHIC" , 10 , "bold") , bg = "white")
    teach_username = Label(teach_signup_window , text = "Username" , font = ("MS UI GOTHIC" , 10 , "bold") , bg = "white")
    teach_password = Label(teach_signup_window , text = "Password" , font = ("MS UI GOTHIC" , 10 , "bold") , bg = "white")

    teach_name_entry = Entry(teach_signup_window , width = 40 , borderwidth = 2)
    teach_username_entry = Entry(teach_signup_window , width = 40 , borderwidth = 2)
    teach_password_entry = Entry(teach_signup_window , width = 40 , borderwidth = 2)

    show_or_hide_password = StringVar()
    show_or_hide_password.set("hide")
    show_password = Checkbutton(teach_signup_window , text = "Show Password" , variable = show_or_hide_password , onvalue = "Show" , offvalue = "hide" , command  = Show_password_command , bg = "white" , activebackground = "white")
    show_password.deselect()

    Show_password_command()
    
    teach_Signup = Button(teach_signup_window , text = "Signup" , font = ("Times new roman bold" , 12) , bg = "white" , command = lambda: query(teach_name_entry.get() , teach_username_entry.get() , teach_password_entry.get()))

    already_have_an_acc = Button(teach_signup_window , text = "Already have an account?" , font = ("Segoe print" , 10 , "underline") , bg = "white" , fg = "blue" , border = 0 , activebackground = "white" , command = login)
    
    teach_name.place(x = 5 , y = 5)
    teach_name_entry.place(x = 5 , y = 25)
    teach_username.place(x = 5 , y = 47)
    teach_username_entry.place(x = 5 , y = 67)
    teach_password.place(x = 5 , y = 89)
    teach_password_entry.place(x = 5 , y = 109)
    show_password.place(x= 5 , y = 131)
    teach_Signup.place(x = 100 , y = 160)
    already_have_an_acc.place(x = 5 , y = 195)
    

def student_signup():
    global stud_signup_window
    global show_or_hide_password
    global stud_password_entry
    global stud_fathername_entry
    global stud_mothername_entry
    global stud_admn_num_entry
    global stud_DOB_entry
    global stud_class
    global stud_sec
    global state

    state = "stud signup"
    
    stud_signup_window = Toplevel()
    stud_signup_window.title("Signup")
    stud_signup_window["bg"] = "white"
    app_width = 305
    app_height = 415
    x_coordinate = int((screen_width/2) - (app_width/2))
    y_coordinate = int((screen_height/2) - (app_height/2))
    stud_signup_window.geometry(f'{app_width}x{app_height}+{x_coordinate}+{y_coordinate}')
    stud_signup_window.resizable(width = False , height = False)

    stud_name = Label(stud_signup_window , text = "Name" , font = ("MS UI GOTHIC" , 10 , "bold") , bg = "white")
    stud_fathername = Label(stud_signup_window , text = "Father Name" , font = ("MS UI GOTHIC" , 10 , "bold") , bg = "white")
    stud_mothername = Label(stud_signup_window , text = "Mother Name" , font = ("MS UI GOTHIC" , 10 , "bold") , bg = "white")
    stud_admn_num = Label(stud_signup_window , text = "Admission Number" , font = ("MS UI GOTHIC" , 10 , "bold") , bg = "white")
    stud_DOB = Label(stud_signup_window , text = "Date of Birth" , font = ("MS UI GOTHIC" , 10 , "bold") , bg = "white")
    stud_username = Label(stud_signup_window , text = "Username" , font = ("MS UI GOTHIC" , 10 , "bold") , bg = "white")
    stud_password = Label(stud_signup_window , text = "Password" , font = ("MS UI GOTHIC" , 10 , "bold") , bg = "white")

    stud_class_values = ['Select Class' , 'XII' , 'XI' , 'X' , 'IX' , 'VIII' , 'VII' , 'VI' , 'V' , 'IV' , 'III' , 'II' , 'I'] 
    stud_class = ttk.Combobox(stud_signup_window , value = stud_class_values)
    stud_class.current(0)

    stud_sec_values = ['Select Section' , 'A' , 'B' , 'C' , 'D']
    stud_sec = ttk.Combobox(stud_signup_window , value = stud_sec_values)
    stud_sec.current(0)

    stud_name_entry = Entry(stud_signup_window , width = 40 , borderwidth = 2)
    stud_fathername_entry = Entry(stud_signup_window , width = 40 , borderwidth = 2)
    stud_mothername_entry = Entry(stud_signup_window , width = 40 , borderwidth = 2)
    stud_admn_num_entry = Entry(stud_signup_window , width = 40 , borderwidth = 2)
    stud_DOB_entry = Entry(stud_signup_window , width = 40 , borderwidth = 2)
    stud_DOB_entry.insert(0 , "YYYY-MM-DD")
    stud_username_entry = Entry(stud_signup_window , width = 40 , borderwidth = 2)
    stud_password_entry = Entry(stud_signup_window , width = 40 , borderwidth = 2)

    show_or_hide_password = StringVar()
    show_or_hide_password.set("hide")
    show_password = Checkbutton(stud_signup_window , text = "Show Password" , variable = show_or_hide_password , onvalue = "Show" , offvalue = "hide" , command  = Show_password_command , bg = "white" , activebackground = "white")
    show_password.deselect()

    Show_password_command()

    already_have_an_acc = Button(stud_signup_window , text = "Already have an account?" , font = ("Segoe print" , 10 , "underline") , bg = "white" , fg = "blue" , border = 0 , activebackground = "white" , command = login)

    stud_Signup = Button(stud_signup_window , text = "Signup" , font = ("Times new roman bold" , 12) , bg = "white" , command = lambda: query(stud_name_entry.get() , stud_username_entry.get() , stud_password_entry.get()))

    stud_name.place(x = 5 , y = 5)
    stud_name_entry.place(x = 5 , y = 25)
    stud_fathername.place(x = 5 , y = 47)
    stud_fathername_entry.place(x = 5 , y = 67)
    stud_mothername.place(x = 5 , y = 89)
    stud_mothername_entry.place(x = 5  , y = 109)
    stud_admn_num.place(x = 5 , y = 131)
    stud_admn_num_entry.place(x = 5 , y = 151)
    stud_DOB.place(x = 5 , y = 173)
    stud_DOB_entry.place(x = 5 , y = 193)
    stud_class.place(x = 5 , y = 220)
    stud_sec.place(x = 155 , y = 220)
    stud_username.place(x = 5 , y = 242)
    stud_username_entry.place(x = 5 , y = 262)
    stud_password.place(x = 5 , y = 284)
    stud_password_entry.place(x = 5 , y = 304)
    show_password.place(x = 5 , y = 326)
    stud_Signup.place(x = 120 , y = 350)
    already_have_an_acc.place(x = 5 , y = 379)

    
def Signup_button_command():
    global are_you_a_teacher

    are_you_a_teacher = messagebox.askquestion("Select and signup" , "Are you a teacher?")
    if are_you_a_teacher == "yes":
        teacher_signup()
    else:
        student_signup()


#Creating menu bar
menu_bar = Menu(Home_screen)
Home_screen.config(menu = menu_bar)

Home_menu = Menu(menu_bar , tearoff = False)
menu_bar.add_cascade(label = "☰" , menu = Home_menu)
Home_menu.add_command(label = "Home")
Home_menu.add_command(label = "View" , state = DISABLED)
Home_menu.add_command(label = "Add" , state = DISABLED)
menu_bar.add_cascade(label = "Signup" , command = Signup_button_command)

quote1 = Label(Home_screen , text = "I failed my exam in some subjects but my friend passed.\nNow he's an engineer in Microsoft and I am the owner." , font = ("Consolas" , 16 , "bold") , bg = "sky blue" , fg = "dark violet")
quote1.place(x = 5 , y = 60)
byline1 = Label(Home_screen , text = "- Bill Gates" , font = ("Consolas" , 16 , "bold") , bg = "sky blue" , fg = "black")
byline1.place(x = 500 , y = 110)
quote2 = Label(Home_screen , text = "Scoring good marks is important but it should not be the \nsole criterion of education. Work for marks in such a way \nthat it may work for you the other way." , font = ("Consolas" , 16 , "bold") , bg = "sky blue" , fg = "dark violet")
quote2.place(x = 5 , y = 170)
byline2 = Label(Home_screen , text = "- Mukesh Parasar" , font = ("Consolas" , 16 , "bold") , bg = "sky blue" , fg = "black")
byline2.place(x = 500 , y = 250)



Home_screen.mainloop()
