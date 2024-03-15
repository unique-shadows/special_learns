from tkinter import *
import mysql.connector as sql
from datetime import date as dat



def logon():
    global aa,pos,us,pas,cursor;
    db_log=Tk();
    db_log.geometry('678x300');
    db_log.maxsize(678,300);
    db_log.minsize(678,300);

    db_log.title("SQL Database");
    us=str();
    pas=str();
    db_log.iconbitmap(True,'special.ico');
    name=StringVar();
    pw=StringVar();
    aa=IntVar(value=0);
    chkr=1;
    back='#6ac5fe';
    db_log.config(bg=back);

    def login():
        global chkr,us,pas,cursor,db;
        us=name.get();
        pas=pw.get();
        chk=1;

        try:
            db=sql.connect(host='localhost',user=us,password=pas);
            cursor=db.cursor();
        except:
            chk=0;

        if chk==1:
            db_log.destroy();
            open();
            
    def hide():
        global aa,pos;
        
        if aa.get()==1:
            pos.config(show='');
        elif aa.get()==0:
            pos.config(show='*')
        db_log.update();

    Label(
        db_log,
        text=" LOGIN TO YOUR SQL DATABASE ",
        font='courier 30 bold',
        fg='white',
        bg='red',
        ).place(
        x=0,
        y=0
    )
    Label(
        db_log,
        text="USER ID",
        font='courier 20 bold',
        fg='black',
        bg=back,
        ).place(
        x=90,
        y=80
    )
    Entry(
        db_log,
        textvar=name,
        font='calibri 25',
        width=20
        ).place(
        x=300,
        y=78
    )
    Label(
        db_log,
        text="PASSWORD",
        font='courier 20 bold',
        fg='black',
        bg=back,
        ).place(
        x=90,
        y=130
    )

    pos=Entry(
        db_log,
        textvar=pw,
        font='calibri 25',
        width=20,
        show='*'
    )

    pos.place(
        x=300,
        y=130
    )

    Checkbutton(
        db_log,
        text='Show password',
        font='calibri 10 bold',
        bg=back,
        onvalue=1,
        offvalue=0,
        variable=aa,
        command=hide
        ).place(
        x=300,
        y=183
    )

    Button(
        db_log,
        text='LOGIN',
        font='calibri 15 bold',
        command=login
        ).place(
        x=291,
        y=220
    )

    db_log.mainloop();
            
    return (us,pas);

def enrollData_of_cs():
    global std,main,home_check,cursor;
    main.destroy();
    create_db();
    enroll=Tk();
    home_check='enroll';
    enroll.geometry('710x600');
    enroll.title('Welcome to SPECIAL LEARNS COMPUTER INSTITUTE');
    back='#6ac5fe';
    enroll.config(bg=back);

    tab_name='CS_data';
    gen=StringVar();
    name=StringVar();
    fname=StringVar();
    mname=StringVar();
    rol=StringVar();
    date=StringVar();
    mon=StringVar();
    year=StringVar();
    mob=StringVar();
    add=StringVar();
    course=StringVar();
    
    month=('January','Feburary','March','April','May','June','July','August','September','October','November','December');
    gender=('Male','Female');

    def home():
        global home_check;
        if home_check=='enroll':
            enroll.destroy();
        if home_check=='checkdata':
            checkdata.destroy();
        open();
        return home_check;
    def date_combine():
        d=str(date.get());
        m=str(mon.get());
        y=str(year.get());
        a="%s %s %s"%(d,m,y);
        return a;
    def date_check():
        chk='';
        mark=0;
        if year.get()=='':
            year.set('*%s'%(year.get()));
            chk='not';
        
        if mon.get()=='':
            mon.set('*%s'%(mon.get()));
            chk='not';
        if date.get()=='':
            date.set('*%s'%(date.get()));
            chk='not';
        if chk!='not':
            mark=0;
            yr=int(year.get());
            mn=mon.get();
            dt=int(date.get());
            tody=str(dat.today());
            tody=tody[0:4];
            tod=int(tody);

            if yr>1900 and yr<(tod-4):
                if mn=='January' or mn=='March' or mn=='May' or mn=='July' or mn=='August' or mn=='October' or mn=='December':
                    if dt<=31 and dt>0:
                        mark=1;
                    else:
                        date.set('*%s'%(date.get()));
                elif mn=='April' or mn=='June' or mn=='September' or mn=='November':
                    if dt<=30 and dt>0:
                        mark=1;
                    else:
                        date.set('*%s'%(date.get()));
                elif mn=='Feburary':
                    if yr//4==0:
                        if dt<=29 and dt>0:
                            mark=1;
                        else:
                            date.set('*%s'%(date.get()));
                    elif dt<=28 and dt>0:
                        mark=1;
                    else:
                        date.set('*%s'%(date.get()));
                else:
                    mon.set('*%s'%(mon.get()));
            else:
                year.set('*%s'%(year.get()));
        return mark;    
    def roll(tab_name,column):
        cursor.execute('select {} from {}'.format(column,tab_name));
        user_rec=cursor.fetchall();
        d=0;
        user_list=[];
        for name in user_rec:
            a=name[0];
            user_list.append(a);
        user_list=tuple(user_list);
        return user_list;
    def close():
        enroll.destroy();

    def course_():
                l1=[];
                cursor.execute("SELECT Name from course");
                course_q=cursor.fetchall();
                for k in course_q:
                     l1.append(k[0]);
                
                return l1;
    
    def course_dur():
            l1=[];
            cursor.execute("SELECT Name from course");
            course_q=cursor.fetchall();
            for k in course_q:
                 l1.append(k[1]);
            
            return l1;

    def course_check():
        mark=0;
        c_len=course_();
        for i in range(0,len(c_len)):
            if c_len[i]==course.get():
                mark=1;
                break;
        return mark;

    def gender_check():
        mark=1;
        if gen.get()!='Male' and gen.get()!='Female':
            temp_gen=gen.get();
            if len(temp_gen)==0:
                gen.set('*');
            elif temp_gen[0]!='*':
                gen.set('*%s'%(gen.get()));
                mark=0;
        return mark;
    
    def mob_check():
        mark=0;
        if mob.get()=='':
            mark-0;
        elif int(mob.get())>999999999 or int(mob.get())<600000000:
            mark=1;
        else:
            mark=0;
        return mark;
    
    def address_chk():
        mark=1;
        if add.get()=='':
            mark=0;
        return mark;
    
    def submit():
        mark=0;
        temp=roll(tab_name,'roll');
        g=1;
        if name.get()=='':
            name.set('*%s'%(name.get()));
            g=0;
        if mname.get()=='':
            mname.set('*%s'%(mname.get()));
            g=0;
        if fname.get()=='':
            fname.set('*%s'%(fname.get()));
            g=0;
        if gender_check()!=1:
            g=0;
        if date_check()!=1:
            g=0;
        if course_check()!=1:
            course.set('*%s'%(course.get()))
            g=0;
        
        if mob_check()!=1:
            mob.set('*%s'%(mob.get()));
            g=0;
        
        if address_chk()!=1:
            add.set('*%s'%(add.get()));
            g=0;

        if g==1:
            birth=date_combine();
            create_db();
            
            cursor.execute("insert into %s(roll,name,Father_name,Mother_name,Gender,dob,course,mob,address,adm) values('%d','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(tab_name,temp[-1]+1,name.get(),fname.get(),mname.get(),gen.get(),birth,course.get(),mob.get(),add.get(),today()));
            db.commit();

            cursor.execute('SELECT * FROM course');
            cur_name=cursor.fetchall();

            for k in cur_name:
                if course.get()==k[0]:
                    cur_dur=k[1];

            mont=('Month 1','Month 2','Month 3','Month 4','Month 5','Month 6','Month 7','Month 8','Month 9','Month 10','Month 11','Month 12',);

            for j in range(0,cur_dur):
                cursor.execute('USE feedata_cs');
                cursor.execute('CREATE TABLE IF NOT EXISTS %s(Month varchar(20),Amount varchar(20))'%(name.get()));
                cursor.execute('INSERT INTO %s(Month,Amount) values("%s","0")'%(name.get(),mont[j]));
                db.commit();

            rol.set(temp[-1]+1);
            enroll.geometry('710x650');
    
    Label(
        enroll,
        text="ENTER STUDENT DETAILS",
        font='courier 30 bold',
        fg='white',
        bg='red',
        ).place(
        x=100,
        y=0
        )
    Button(
        text='HOME',
        font='calibri 12 bold',
        bg='#32CD32',
        borderwidth=3,
        relief=SOLID,
        fg='black',
        command=home,
        ).place(
            x=20,
            y=7
        )

    Label(
        enroll,
        text="STUDENT'S NAME",
        font='courier 25 bold',
        bg=back,
        ).place(
        x=10,
        y=60,
        )

    Entry(
        enroll,
        textvar=name,
        font='courier 22',
        width='20'
        ).place(
        x=300,
        y=60
        )
    Label(
        enroll,
        text="MOTHER'S NAME",
        font='courier 25 bold',
        bg=back,
        ).place(
        x=10,
        y=120,
        )
    Entry(
        enroll,
        textvariable=mname,
        font='courier 22',
        width='20'
        ).place(
        x=300,
        y=120
        )
    Label(
        enroll,
        text="FATHER'S NAME",
        font='courier 25 bold',
        bg=back,
        ).place(
        x=10,
        y=180,
        )
    Entry(
        enroll,
        textvariable=fname,
        font='courier 22',
        width='20'
        ).place(
        x=300,
        y=180
        )
    Label(
        enroll,
        text="GENDER",
        font='courier 25 bold',
        bg=back,
        ).place(
        x=10,
        y=240,
        )
    Entry(
        enroll,
        textvar=gen,
        font='courier 22',
        width='20'
        ).place(
        x=300,
        y=240
        )
    OptionMenu(
        enroll,gen,*gender
        ).place(
        x=650,
        y=240,
        );
    Label(
        enroll,
        text="D.O.B",
        font='courier 25 bold',
        bg=back,
        ).place(
        x=10,
        y=300,
        )
    Entry(
        enroll,
        textvar=date,
        font='courier 22',
        width='3'
        ).place(
        x=300,
        y=300
        )
    Entry(
        enroll,
        textvar=mon,
        font='courier 22',
        width='8'
        ).place(
        x=400,
        y=300
        )
    Entry(
        enroll,
        textvar=year,
        font='courier 22',
        width='4'
        ).place(
        x=570,
        y=300
        )
    dob=OptionMenu(
        enroll,
        mon,
        *month,
        );
    dob.config(width='1');
    dob.place(x=650,y=300);
    course=StringVar();
    Label(
        enroll,
        text="COURSE",
        font='courier 25 bold',
        bg=back,
        ).place(
        x=10,
        y=360,
        )
    Entry(
        enroll,
        textvar=course,
        font='courier 22',
        width='20'
        ).place(
        x=300,
        y=360
        )

    std=course_();

    OptionMenu(enroll, course, *std).place(x=650,y=365);
    Label(
        enroll,
        text="MOBILE NO.",
        font='courier 25 bold',
        bg=back,
        ).place(
        x=10,
        y=420,
        )
    Entry(
        enroll,
        textvar=mob,
        font='courier 22',
        width='20'
        ).place(
        x=300,
        y=420
        )
    
    Label(
        enroll,
        text="ADDRESS",
        font='courier 25 bold',
        bg=back,
        ).place(
        x=10,
        y=480,
        )
    Entry(
        enroll,
        textvar=add,
        font='courier 22',
        width='20'
        ).place(
        x=300,
        y=480
        )
    Label(
        enroll,
        text="ROLL NO.",
        font='courier 25 bold',
        bg=back,
        ).place(
        x=10,
        y=600,
        )
    Entry(
        enroll,
        textvar=rol,
        font='courier 22',
        width='20'
        ).place(
        x=300,
        y=600
        )
    Button(
        enroll,
        text='SUBMIT',
        font='calibri 15 bold',
        bg='green',
        borderwidth=3,
        relief=SOLID,
        fg='white',
        command=submit,
        ).place(
            x=280,
            y=540
        );

    enroll.mainloop();

def checkData_of_cs():
        global main,home_check;
        home_check='checkdata';
        main.destroy();
        create_db();
        tab_name='cs_data';
        checkdata=Tk();
        checkdata.geometry('710x180');
        checkdata.title('CHECK ENROLLMENT DATA');
        back='#6ac5fe';
        checkdata.config(bg=back);

        name=StringVar();
        fname=StringVar();
        mname=StringVar();
        rol=StringVar();
        gen=StringVar();
        mob=StringVar();
        add=StringVar();
        gender=('Male','Female');
        month=('January','Feburary','March','April','May','June','July','August','September','October','November','December');
        
        def home():
            global home_check,enroll;
            if home_check=='enroll':
                enroll.destroy();
                
            if home_check=='checkdata':
                checkdata.destroy();

            open();
            return home_check;

        def roll_store(tab_name):
            new=[];
            roll=int (rol.get())
            cursor.execute("select roll from %s"%(tab_name));
            record=cursor.fetchall();
            for rec in record:
                new.append(rec[0]);
            new=tuple(new);

            return new;

        def select():
            roll=int (rol.get());
            cursor.execute("select * from %s"%(tab_name));
            record=cursor.fetchall();
            for rec in record:
                if rec[0]==roll:
                    user_rec=rec;
                    break;
            return rec;

        def submit():
            roll=rol.get();

            if roll!='':
                roll=int(roll);
                roll_list=roll_store('cs_data');

                if roll<=0:
                    rec=select();
                    name.set('Error');
                    fname.set('Error');
                    mname.set('Error');
                    gen.set('Error');
                    dob.set('Error');
                    mob.set('Error');
                    course.set('Error');
                    add.set('Error');
                    checkdata.geometry('710x660');

                elif roll_list.count(roll)!=0:
                    i=1;
                    rec=select();
                    name.set('%s'%(rec[i]));
                    i+=1;
                    fname.set('%s'%(rec[i]));
                    i+=1;
                    mname.set('%s'%(rec[i]));
                    i+=1;
                    gen.set('%s'%(rec[i]));
                    i+=1;
                    dob.set('%s'%(rec[i]));
                    i+=1;
                    course.set('%s'%(rec[i]));
                    i+=1;
                    mob.set('%s'%(rec[i]));
                    i+=1;
                    add.set('%s'%(rec[i]));
                    checkdata.geometry('710x660');

                else:
                    rec=select();
                    name.set('NA');
                    fname.set('NA');
                    mname.set('NA');
                    gen.set('NA');
                    dob.set('NA');
                    mob.set('NA');
                    course.set('NA');
                    add.set('NA');

                print("Done");
                checkdata.geometry('710x660');

            else:
                rol.set('*%s'%(rol.get()));
                checkdata.geometry('710x180');

        Button(
            text='HOME',
            font='calibri 12 bold',
            bg='#32CD32',
            borderwidth=3,
            relief=SOLID,
            fg='black',
            command=home,
            ).place(
                x=20,
                y=7
            )

        Label(
            checkdata,
            text="ENTER STUDENT DETAILS",
            font='courier 30 bold',
            fg='white',
            bg='red',
            ).place(
            x=100,
            y=0
            )

        Label(
            checkdata,
            text="ROLL NO.",
            font='courier 25 bold',
            bg=back,
            ).place(
            x=10,
            y=60,
            )

        Entry(
            checkdata,
            textvar=rol,
            font='courier 22',
            width='20'
            ).place(
            x=300,
            y=60
            )

        Button(
            checkdata,
            text='SUBMIT',
            font='calibri 15 bold',
            bg='green',
            borderwidth=3,
            relief=SOLID,
            fg='white',
            command=submit,
            ).place(
            x=280,
            y=120
            );

        Label(
            checkdata,
            text="STUDENT'S NAME",
            font='courier 25 bold',
            bg=back,
            ).place(
            x=10,
            y=180,
            )

        Entry(
            checkdata,
            textvar=name,
            font='courier 22',
            width='20'
            ).place(
            x=300,
            y=180
            )
        Label(
            checkdata,
            text="MOTHER'S NAME",
            font='courier 25 bold',
            bg=back,
            ).place(
            x=10,
            y=240,
            )

        Entry(
            checkdata,
            textvariable=mname,
            font='courier 22',
            width='20'
            ).place(
            x=300,
            y=240
            )

        Label(
            checkdata,
            text="FATHER'S NAME",
            font='courier 25 bold',
            bg=back,
            ).place(
            x=10,
            y=300,
            )
        Entry(
            checkdata,
            textvariable=fname,
            font='courier 22',
            width='20'
            ).place(
            x=300,
            y=300
            )
        Label(
            checkdata,
            text="GENDER",
            font='courier 25 bold',
            bg=back,
            ).place(
            x=10,
            y=360,
            )
        Entry(
            checkdata,
            textvar=gen,
            font='courier 22',
            width='20'
            ).place(
            x=300,
            y=360
            )

        Label(
            checkdata,
            text="D.O.B",
            font='courier 25 bold',
            bg=back,

            ).place(
            x=10,
            y=420,
            )

        dob=StringVar();

        Entry(
            checkdata,
            textvar=dob,
            font='courier 22',
            width='20'
            ).place(
            x=300,
            y=420
            )

        course=StringVar();

        Label(
            checkdata,
            text="COURSE",
            font='courier 25 bold',
            bg=back,
            ).place(
            x=10,
            y=480,
            )

        Entry(
            checkdata,
            textvar=course,
            font='courier 22',
            width='20'
            ).place(
            x=300,
            y=480
            )

        Label(
            checkdata,
            text="MOBILE NO.",
            font='courier 25 bold',
            bg=back,
            ).place(
            x=10,
            y=540,
            )
            
        Entry(
            checkdata,
            textvar=mob,
            font='courier 22',
            width='20'
            ).place(
            x=300,
            y=540
            )

        Label(
            checkdata,
            text="ADDRESS",
            font='courier 25 bold',
            bg=back,
            ).place(
            x=10,
            y=600,
            )
            
        Entry(
            checkdata,
            textvar=add,
            font='courier 22',
            width='20'
            ).place(
            x=300,
            y=600
            )

        checkdata.mainloop();

def feedata_cs():
    main.destroy();
    fee_cs=Tk();
    fee_cs.geometry('595x125');
    fee_cs.title('Fee data of computer institute');
    back='#6ac5fe';
    fee_cs.config(bg=back);
    create_db();

    def home():
            fee_cs.destroy();
            open(); 

    def collect(tab_name,column):
        cursor.execute('select {} from {}'.format(column,tab_name));
        user_rec=cursor.fetchall();
        d=0;
        user_list=[];
        for name in user_rec:
            a=name[0];
            user_list.append(a);
        user_list=tuple(user_list);
        return user_list;

    roll=StringVar();
    mon1_fee=StringVar();
    mon2_fee=StringVar();
    mon3_fee=StringVar();
    mon4_fee=StringVar();
    mon5_fee=StringVar();
    mon6_fee=StringVar();
    mon7_fee=StringVar();
    mon8_fee=StringVar();
    mon9_fee=StringVar();
    mon10_fee=StringVar();
    mon11_fee=StringVar();
    mon12_fee=StringVar();

    def ok():
        global duration,a_name;
        cursor.execute('USE student');
        rl=int(roll.get());
        c_list=collect('cs_data','course');
        crse_name=c_list[rl];
        
        name_list=collect('cs_data','name');
        act_name=name_list[rl];

        cursor.execute('select * from course');
        c_l=cursor.fetchall();

        for a in c_l:
            if crse_name==a[0]:
                cur_dur=a[1];
        
        cursor.execute('USE feedata_cs');
        cursor.execute('select amount from %s'%(act_name));
        fee=cursor.fetchall();

        fe_=[];
        for f in fee:
            fe_.append(f[0]);

        try:
            j=0;
            mon1_fee.set(fe_[j]);
            j+=1;
            mon2_fee.set(fe_[j]);
            j+=1;
            mon3_fee.set(fe_[j]);
            j+=1;
            mon4_fee.set(fe_[j]);
            j+=1;
            mon5_fee.set(fe_[j]);
            j+=1;
            mon6_fee.set(fe_[j]);
            j+=1;
            mon7_fee.set(fe_[j]);
            j+=1;
            mon8_fee.set(fe_[j]);
            j+=1;
            mon9_fee.set(fe_[j]);
            j+=1;
            mon10_fee.set(fe_[j]);
            j+=1;
            mon11_fee.set(fe_[j]);
            j+=1;
            mon12_fee.set(fe_[j]);
        except:
            moo=[mon1_fee,mon2_fee,mon3_fee,mon4_fee,mon5_fee,mon6_fee,mon7_fee,mon8_fee,mon9_fee,mon10_fee,mon11_fee,mon12_fee];
            for k in range(j,len(moo)):
                moo[k].set('NR');
        
        fee_cs.geometry('595x500');
    
    def update():
        cursor.execute('USE student');
        name_list=collect('cs_data','name');
        rl=int(roll.get());
        act_name=name_list[rl];

        x=0;
        fe_=[];
        fe_.append(mon1_fee.get());
        fe_.append(mon2_fee.get());
        fe_.append(mon3_fee.get());
        fe_.append(mon4_fee.get());
        fe_.append(mon5_fee.get());
        fe_.append(mon6_fee.get());
        fe_.append(mon7_fee.get());
        fe_.append(mon8_fee.get());
        fe_.append(mon9_fee.get());
        fe_.append(mon10_fee.get());
        fe_.append(mon11_fee.get());
        fe_.append(mon12_fee.get());

        cursor.execute('USE feedata_cs');
        for x in range(0,len(fe_)):
            cursor.execute("UPDATE %s SET Amount='%s' WHERE Month='Month %d'"%(act_name,fe_[x],int(x+1)));
            db.commit();

    Button(
        fee_cs,
        text='HOME',
        font='calibri 12 bold',
        bg='#32CD32',
        borderwidth=3,
        relief=SOLID,
        fg='black',
        command=home,
        ).place(
            x=20,
            y=7
        )

    Label(
        fee_cs,
        text="ENTER FEE DATA",
        font='courier 30 bold',
        fg='white',
        bg='red',
        ).place(
        x=125,
        y=0
    );

    Label(
        fee_cs,
        text="ROLL NO.",
        font='courier 25 bold',
        bg=back,
        ).place(
        x=10,
        y=70,
        );

    Entry(
        fee_cs,
        textvar=roll,
        width=5,
        font='calibri 20',
    ).place(
        x=200,
        y=70,
    )

    Button(
        fee_cs,
        text='OK',
        font='courier 15 bold',
        fg='white',
        bg='#1ec71e',
        border=1,
        relief=SOLID,
        command=ok,

        ).place(
        x=300,
        y=69
        );

    Label(
        fee_cs,
        text='MONTH 1',
        font='courier 20 bold',
        bg=back,

    ).place(
        x=10,
        y=140,
    );
    Entry(
        fee_cs,
        textvar=mon1_fee,
        font='courier 20 ',
        width=5,

    ).place(
        x=200,
        y=140
    );

    Label(
        fee_cs,
        text='MONTH 2',
        font='courier 20 bold',
        bg=back,

    ).place(
        x=10,
        y=190,
    )
    Entry(
        fee_cs,
        textvar=mon2_fee,
        font='courier 20 ',
        width=5,

    ).place(
        x=200,
        y=190
    );

    Label(
        fee_cs,
        text='MONTH 3',
        font='courier 20 bold',
        bg=back,

    ).place(
        x=10,
        y=240,
    );
    Entry(
        fee_cs,
        textvar=mon3_fee,
        font='courier 20 ',
        width=5,

    ).place(
        x=200,
        y=240
    );

    Label(
        fee_cs,
        text='MONTH 4',
        font='courier 20 bold',
        bg=back,

    ).place(
        x=10,
        y=290,
    );
    Entry(
        fee_cs,
        textvar=mon4_fee,
        font='courier 20 ',
        width=5,

    ).place(
        x=200,
        y=290
    );

    Label(
        fee_cs,
        text='MONTH 5',
        font='courier 20 bold',
        bg=back,

    ).place(
        x=10,
        y=340,
    );
    Entry(
        fee_cs,
        textvar=mon5_fee,
        font='courier 20 ',
        width=5,

    ).place(
        x=200,
        y=340
    );

    Label(
        fee_cs,
        text='MONTH 6',
        font='courier 20 bold',
        bg=back,

    ).place(
        x=10,
        y=390,
    );
    Entry(
        fee_cs,
        textvar=mon6_fee,
        font='courier 20 ',
        width=5,

    ).place(
        x=200,
        y=390
    );

    Label(
        fee_cs,
        text='MONTH 7',
        font='courier 20 bold',
        bg=back,

    ).place(
        x=350,
        y=140,
    );
    Entry(
        fee_cs,
        textvar=mon7_fee,
        font='courier 20 ',
        width=5,

    ).place(
        x=500,
        y=140
    );
    
    Label(
        fee_cs,
        text='MONTH 8',
        font='courier 20 bold',
        bg=back,

    ).place(
        x=350,
        y=190,
    );
    Entry(
        fee_cs,
        textvar=mon8_fee,
        font='courier 20 ',
        width=5,

    ).place(
        x=500,
        y=190
    );

    Label(
        fee_cs,
        text='MONTH 9',
        font='courier 20 bold',
        bg=back,

    ).place(
        x=350,
        y=240,
    );
    Entry(
        fee_cs,
        textvar=mon9_fee,
        font='courier 20 ',
        width=5,

    ).place(
        x=500,
        y=240
    );

    Label(
        fee_cs,
        text='MONTH 10',
        font='courier 20 bold',
        bg=back,

    ).place(
        x=350,
        y=290,
    );
    Entry(
        fee_cs,
        textvar=mon10_fee,
        font='courier 20 ',
        width=5,

    ).place(
        x=500,
        y=290
    );

    Label(
        fee_cs,
        text='MONTH 11',
        font='courier 20 bold',
        bg=back,

    ).place(
        x=350,
        y=340,
    );
    Entry(
        fee_cs,
        textvar=mon11_fee,
        font='courier 20 ',
        width=5,

    ).place(
        x=500,
        y=340
    );

    Label(
        fee_cs,
        text='MONTH 12',
        font='courier 20 bold',
        bg=back,

    ).place(
        x=350,
        y=390,
    );
    Entry(
        fee_cs,
        textvar=mon12_fee,
        font='courier 20 ',
        width=5,

    ).place(
        x=500,
        y=390
    );
    
    Button(
        fee_cs,
        text='UPDATE',
        font='courier 15 bold',
        bg='white',
        #bg='#1ec71e',
        border=1,
        relief=SOLID,
        command=update,

        ).place(
        x=240,
        y=450
        );

    fee_cs.mainloop();

def tuition_enroll():
        global std,main,home_check;
        main.destroy();
        tut=Tk();
        home_check='tut';
        tut.geometry('710x600');
        tut.title('Welcome to SPECIAL LEARNS COMPUTER INSTITUTE');
        back='#6ac5fe';
        tut.config(bg=back);
        create_db();

        gen=StringVar();
        name=StringVar();
        fname=StringVar();
        mname=StringVar();
        rol=StringVar();
        date=StringVar();
        mon=StringVar();
        year=StringVar();
        mob=StringVar();
        std=(1,2,3,4,5,6,7,8,9,10,11,12);
        month=('January','Feburary','March','April','May','June','July','August','September','October','November','December');
        gender=('Male','Female');
        standard=StringVar();
        subject=StringVar();
        add=StringVar();

        def home():
            global home_check;
            if home_check=='tut':
                tut.destroy();

            if home_check=='checkdata':
                checkdata.destroy();

            if home_check=='enrollData':
                checkdata.destroy();

            open();
            return home_check;

        def date_combine():
            d=str(date.get());
            m=str(mon.get());
            y=str(year.get());
            a="%s %s %s"%(d,m,y);

            return a;

        def date_check():
            chk='';
            mark=0;

            if year.get()=='':
                year.set('*%s'%(year.get()));
                chk='not';
            
            if mon.get()=='':
                mon.set('*%s'%(mon.get()));
                chk='not';

            if date.get()=='':
                date.set('*%s'%(date.get()));
                chk='not';

            if chk!='not':
                mark=0;
                yr=int(year.get());
                mn=mon.get();
                dt=int(date.get());
                dt=int(date.get());
                tody=str(dat.today());
                tody=tody[0:4];
                tod=int(tody);

                if yr>1900 and yr<tod-4:
                    if mn=='January' or mn=='March' or mn=='May' or mn=='July' or mn=='August' or mn=='October' or mn=='December':
                        if dt<=31 and dt>0:
                            mark=1;
                        else:
                            date.set('*%s'%(date.get()));

                    elif mn=='April' or mn=='June' or mn=='September' or mn=='November':
                        if dt<=30 and dt>0:
                            mark=1;
                        else:
                            date.set('*%s'%(date.get()));

                    elif mn=='Feburary':
                        if yr//4==0:
                            if dt<=29 and dt>0:
                                mark=1;
                            else:
                                date.set('*%s'%(date.get()));

                        elif dt<=28 and dt>0:
                            mark=1;
                        else:
                            date.set('*%s'%(date.get()));
                    else:
                        mon.set('*%s'%(mon.get()));
                else:
                    year.set('*%s'%(year.get()));

            return mark;   

        def roll(tab_name,column):
            cursor.execute('select {} from {}'.format(column,tab_name));
            user_rec=cursor.fetchall();
            d=0;
            user_list=[];
            for name in user_rec:
                a=name[0];
                user_list.append(a);

            user_list=tuple(user_list);
            return user_list;

            if gender.count(gen.get())!=0:
                mark=1;
            else:
                mark=0;
            return mark;

        def mob_check():
            mark=0;
            if mob.get()=='':
                mark-0;
            elif int(mob.get())>999999999 or int(mob.get())<600000000:
                mark=1;
            else:
                mark=0;
            return mark;

        def class_check():
            mark=1;
            if standard.get()=='':
                mark=0;
            else:
                st=int(standard.get());
                if st>=1 and st<=12:
                    if subject.get()!='':
                        def subject_check(value):
                            val=int (value);
                            sub_list=tuple();
                            mark=1;

                            if val>=1 and val<=10:
                                sub_list=('All','English','Hindi','Maths');
                            elif val==11 or val==12:
                                sub_list=('Physics','Chemistry','Maths','Biology','Economics','Accounts','Business');
                            else:
                                subject.set('*%s'%(subject.get()));
                                mark=0;

                            OptionMenu(tut, subject, *sub_list).place(x=650,y=363);
                    else:
                        subject.set('*%s'%(subject.get()));
            return mark;

        def subject_check(value):
            val=int (value);
            sub_list=tuple();
            mark=1;

            if val>=1 and val<=10:
                sub_list=('All','English','Hindi','Maths');
            elif val==11 or val==12:
                sub_list=('Physics','Chemistry','Maths','Biology','Economics','Accounts','Business');
            else:
                mark=0;

            OptionMenu(tut, subject, *sub_list).place(x=650,y=363);

            return mark;

        def gender_check():
            mark=1;
            if gen.get()!='Male' and gen.get()!='Female':
                temp_gen=gen.get();
                if len(temp_gen)==0:
                    gen.set('*');
                elif temp_gen[0]!='*':
                    gen.set('*%s'%(gen.get()));
                    mark=0;
            return mark;
        
        def add_chk():
            mark=1;
            if add.get()=='':
                mark=0;
            return mark;

        def submit():
            global val;
            temp=roll('tuition','roll');
            g=1;

            if name.get()=='':
                
                name.set('*%s'%(name.get()));
                g=0;

            if mname.get()=='':
               
                mname.set('*%s'%(mname.get()));
                g=0;

            if fname.get()=='':
                
                fname.set('*%s'%(fname.get()));
                g=0;

            if gender_check()!=1:
                
                g=0;

            if date_check()!=1:
                
                g=0;
            
            if class_check()!=1:
                
                standard.set('*%s'%(standard.get()));
                g=0;

            if mob_check()!=1:
                
                mob.set('*%s'%(mob.get()));
                g=0;
            
            if add_chk()==0:
                
                add.set('*%s'%(add.get()));
                g=0;
            
            if g==1:
                month=('Month 1','Month 2','Month 3','Month 4','Month 5','Month 6','Month 7','Month 8','Month 9','Month 10','Month 11','Month 12');
                birth=date_combine();
                cursor.execute("INSERT INTO tuition(roll,name,Father_name,Mother_name,Gender,dob,subject,mob,class,address,adm) values('%d','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(temp[-1]+1,name.get(),fname.get(),mname.get(),gen.get(),birth,mob.get(),subject.get(),standard.get(),add.get(),today()))
                db.commit();
                for j in month:
                    cursor.execute('USE feedata_tut');
                    cursor.execute('CREATE TABLE IF NOT EXISTS %s(Month varchar(20),Amount int)'%(name.get()));
                    cursor.execute('INSERT INTO %s(Month,Amount) values("%s",0)'%(name.get(),j));

                db.commit();
                print('DONE!');
                rol.set(temp[-1]+1);
                tut.geometry('710x650');

        Label(
            tut,
            text="ENTER STUDENT DETAILS",
            font='courier 30 bold',
            fg='white',
            bg='red',

            ).place(
            x=100,
            y=0
            )

        Button(
            text='HOME',
            font='calibri 12 bold',
            bg='#32CD32',
            borderwidth=3,
            relief=SOLID,
            fg='black',
            command=home,
            ).place(
                x=20,
                y=7
            )

        Label(
            tut,
            text="STUDENT'S NAME",
            font='courier 25 bold',
            bg=back,
            ).place(
            x=10,
            y=60,
            )

        Entry(
            tut,
            textvar=name,
            font='courier 22',
            width='20'
            ).place(
            x=300,
            y=60
            )

        Label(
            tut,
            text="MOTHER'S NAME",
            font='courier 25 bold',
            bg=back,

            ).place(
            x=10,
            y=120,
            )

        Entry(
            tut,
            textvariable=mname,
            font='courier 22',
            width='20'
            ).place(
            x=300,
            y=120
            )

        Label(
            tut,
            text="FATHER'S NAME",
            font='courier 25 bold',
            bg=back,
            ).place(
            x=10,
            y=180,

            )

        Entry(
            tut,
            textvariable=fname,
            font='courier 22',
            width='20'
            ).place(
            x=300,
            y=180
            )

        Label(
            tut,
            text="GENDER",
            font='courier 25 bold',
            bg=back,

            ).place(
            x=10,
            y=240,

            )

        Entry(
            tut,
            textvar=gen,
            font='courier 22',
            width='20'
            ).place(
            x=300,
            y=240
            )

        OptionMenu(
            tut,gen,*gender
            ).place(
            x=650,
            y=240,
            );

        Label(
            tut,
            text="D.O.B",
            font='courier 25 bold',
            bg=back,

            ).place(
            x=10,
            y=300,

            )

        Entry(
            tut,
            textvar=date,
            font='courier 22',
            width='3'
            ).place(
            x=300,
            y=300
            )

        Entry(
            tut,
            textvar=mon,
            font='courier 22',
            width='8'
            ).place(
            x=400,
            y=300
            )

        Entry(
            tut,
            textvar=year,
            font='courier 22',
            width='4'
            ).place(
            x=570,
            y=300
            )

        dob=OptionMenu(
            tut,
            mon,
            *month,
            );

        dob.config(width='1');
        dob.place(x=650,y=300);

        Label(
            tut,
            text="CLASS,SUBJECT",
            font='courier 25 bold',
            bg=back,

            ).place(
            x=10,
            y=360,

            )

        Entry(
            tut,
            textvar=standard,
            font='courier 22',
            width='3'
            ).place(
            x=300,
            y=360
            )

        Entry(
            tut,
            textvar=subject,
            font='courier 22',
            width='13'
            ).place(
            x=416,
            y=360
            )

        OptionMenu(
            tut,
            standard, 
            *std,
            command=subject_check
            ).place(
                x=360,
                y=364
            );

        Label(
            tut,
            text="MOBILE NO.",
            font='courier 25 bold',
            bg=back,
            ).place(
            x=10,
            y=420,
            );

        Entry(
            tut,
            textvar=mob,
            font='courier 22',
            width='20'
            ).place(
            x=300,
            y=420
            );

        Label(
            tut,
            text="ADDRESS",
            font='courier 25 bold',
            bg=back,
            ).place(
            x=10,
            y=480,
            );

        Entry(
            tut,
            textvar=add,
            font='courier 22',
            width='20'
            ).place(
            x=300,
            y=480
            );

        Button(
            tut,
            text='SUBMIT',
            font='calibri 15 bold',
            bg='green',
            borderwidth=3,
            relief=SOLID,
            fg='white',
            command=submit,

            ).place(
            x=280,
            y=540
            );

        Label(
            tut,
            text="ROLL NO.",
            font='courier 25 bold',
            bg=back,

            ).place(
            x=10,
            y=600,
            );
        Entry(
            tut,
            textvar=rol,
            font='courier 22',
            width='20'
            ).place(
            x=300,
            y=600
            )
            
        tut.mainloop();

def checkData_of_tut():
    global std,main,home_check;
    main.destroy();
    checkdata_tut=Tk();
    home_check='checkdata_tut';
    checkdata_tut.geometry('710x170');
    create_db();
    checkdata_tut.title('Welcome to SPECIAL LEARNS COMPUTER INSTITUTE');
    back='#6ac5fe';
    checkdata_tut.config(bg=back);
    gen=StringVar();
    name=StringVar();
    fname=StringVar();
    mname=StringVar();
    rol=StringVar();
    dob=StringVar();
    mob=StringVar();
    std=(1,2,3,4,5,6,7,8,9,10,11,12);
    month=('January','Feburary','March','April','May','June','July','August','September','October','November','December');
    gender=('Male','Female');
    standard=StringVar();
    subject=StringVar();
    def home():
        global home_check;
        if home_check=='checkdata_tut':
            checkdata_tut.destroy();
        if home_check=='checkdata':
            checkdata.destroy();
        if home_check=='enrollData':
            checkdata.destroy();
        
        open();
        return home_check;
    
    def roll_store(tab_n):
        new=[];
        roll=int (rol.get())
        cursor.execute("select roll from %s"%(tab_n));
        record=cursor.fetchall();
        for rec in record:
            new.append(rec[0]);
        new=tuple(new);
        return new;
    def select():
        roll=int (rol.get());
        tab_name='tuition';
        cursor.execute("select * from %s"%(tab_name));
        record=cursor.fetchall();
        for rec in record:
            if rec[0]==roll:
                user_rec=rec;
                break;
        return rec;
    def submit():
        roll=int(rol.get());
        tab_name='tuition';
        rec=select();
        #To check roll number in DB:
        roll_list=roll_store('tuition');
        if roll<=0:
            rec=select();
            name.set('Error');
            fname.set('Error');
            mname.set('Error');
            gen.set('Error');
            dob.set('Error');
            mob.set('Error');
            standard.set('Error');
            subject.set('Error');
            checkdata_tut.geometry('710x600');

        elif roll_list.count(roll)!=0:
            i=1;
            rec=select();
            name.set('%s'%(rec[i]));
            i+=1;
            fname.set('%s'%(rec[i]));
            i+=1;
            mname.set('%s'%(rec[i]));
            i+=1;
            gen.set('%s'%(rec[i]));
            i+=1;
            dob.set('%s'%(rec[i]));
            i+=1;
            mob.set('%s'%(rec[i]));
            i+=1;
            subject.set('%s'%(rec[i]));
            i+=1;
            standard.set('%s'%(rec[i]));
            
            checkdata_tut.geometry('710x600');
        else:
            rec=select();
            name.set('NA');
            fname.set('NA');
            mname.set('NA');
            gen.set('NA');
            dob.set('NA');
            mob.set('NA');
            standard.set('NA');
            subject.set('NA');
    Label(
        checkdata_tut,
        text="ENTER STUDENT DETAILS",
        font='courier 30 bold',
        fg='white',
        bg='red',
        ).place(
        x=100,
        y=0
        )
    Button(
        text='HOME',
        font='calibri 12 bold',
        bg='#32CD32',
        borderwidth=3,
        relief=SOLID,
        fg='black',
        command=home,
        ).place(
            x=20,
            y=7
        )
    Label(
        checkdata_tut,
        text="ROLL NO.",
        font='courier 25 bold',
        bg=back,
        ).place(
        x=10,
        y=60,
        )
    Entry(
        checkdata_tut,
        textvar=rol,
        font='courier 22',
        width='20'
        ).place(
        x=300,
        y=60
        )
    Button(
        checkdata_tut,
        text='SUBMIT',
        font='calibri 15 bold',
        bg='green',
        borderwidth=3,
        relief=SOLID,
        fg='white',
        command=submit,
        ).place(
        x=280,
        y=120
        );
    
    Label(
        checkdata_tut,
        text="STUDENT'S NAME",
        font='courier 25 bold',
        bg=back,
        ).place(
        x=10,
        y=180,
        )
    Entry(
        checkdata_tut,
        textvar=name,
        font='courier 22',
        width='20'
        ).place(
        x=300,
        y=180
        )
    Label(
        checkdata_tut,
        text="MOTHER'S NAME",
        font='courier 25 bold',
        bg=back,
        ).place(
        x=10,
        y=240,
        )
    Entry(
        checkdata_tut,
        textvariable=mname,
        font='courier 22',
        width='20'
        ).place(
        x=300,
        y=240
        )
    Label(
        checkdata_tut,
        text="FATHER'S NAME",
        font='courier 25 bold',
        bg=back,
        ).place(
        x=10,
        y=300,
        )
    Entry(
        checkdata_tut,
        textvariable=fname,
        font='courier 22',
        width='20'
        ).place(
        x=300,
        y=300
        )
    Label(
        checkdata_tut,
        text="GENDER",
        font='courier 25 bold',
        bg=back,
        ).place(
        x=10,
        y=360,
        )
    Entry(
        checkdata_tut,
        textvar=gen,
        font='courier 22',
        width='20'
        ).place(
        x=300,
        y=360
        )
    Label(
        checkdata_tut,
        text="D.O.B",
        font='courier 25 bold',
        bg=back,
        ).place(
        x=10,
        y=420,
        )
    Entry(
        checkdata_tut,
        textvar=dob,
        font='courier 22',
        width='20'
        ).place(
        x=300,
        y=420
        )
    Label(
        checkdata_tut,
        text="CLASS,SUBJECT",
        font='courier 25 bold',
        bg=back,
        ).place(
        x=10,
        y=480,
        )
    Entry(
        checkdata_tut,
        textvar=standard,
        font='courier 22',
        width='3'
        ).place(
        x=300,
        y=480
        )
    Entry(
        checkdata_tut,
        textvar=subject,
        font='courier 22',
        width='16'
        ).place(
        x=367,
        y=480
        );

    Label(
        checkdata_tut,
        text="MOBILE NO.",
        font='courier 25 bold',
        bg=back,
        ).place(
        x=10,
        y=540,
        );

    Entry(
        checkdata_tut,
        textvar=mob,
        font='courier 22',
        width='20'
        ).place(
        x=300,
        y=540
        );
    checkdata_tut.mainloop();

def feedata_tut():
    main.destroy();
    fee_tut=Tk();
    fee_tut.geometry('595x125');
    fee_tut.title('Fee data of computer institute');
    back='#6ac5fe';
    fee_tut.config(bg=back);
    create_db();

    def home():
            fee_tut.destroy();
            open(); 

    def collect(tab_name,column):
        cursor.execute('select {} from {}'.format(column,tab_name));
        user_rec=cursor.fetchall();
        d=0;
        user_list=[];
        for name in user_rec:
            a=name[0];
            user_list.append(a);
        user_list=tuple(user_list);
        return user_list;

    def ok():
        global duration,act_name;
        cursor.execute('USE student');
        rl=int(roll.get());
        
        name_list=collect('tuition','name');
        
        act_name=name_list[rl];
        
        cursor.execute('use feedata_tut');
        cursor.execute("SELECT table_name from information_schema.tables where table_schema='feedata_tut'");
        db_list=cursor.fetchall();
        
        for k in db_list:
            
            if k[0]==act_name:
                mark=1;
                break;
            else:
                mark=0;

        if mark==1:
            cursor.execute('SELECT * from %s'%(act_name));
            fee=cursor.fetchall();
            fee_list=[];
            for k in fee:
                fee_list.append(k[1]);
            
            i=0;
            jan_fee.set(fee_list[i]);
            i+=1;
            feb_fee.set(fee_list[i]);  
            i+=1;     
            mar_fee.set(fee_list[i]);
            i+=1;
            apr_fee.set(fee_list[i]);
            i+=1;
            may_fee.set(fee_list[i]);
            i+=1;
            june_fee.set(fee_list[i]);
            i+=1;
            july_fee.set(fee_list[i]);
            i+=1;
            aug_fee.set(fee_list[i]);
            i+=1;
            sep_fee.set(fee_list[i]);
            i+=1;
            oct_fee.set(fee_list[i]);
            i+=1;
            nov_fee.set(fee_list[i]);
            i+=1;
            dec_fee.set(fee_list[i]);
        
            fee_tut.geometry('595x500');

        else:
            print('NoT');

    def update():
        l1=[jan_fee.get(),feb_fee.get(),mar_fee.get(),apr_fee.get(),may_fee.get(),june_fee.get(),july_fee.get(),aug_fee.get(),sep_fee.get(),oct_fee.get(),nov_fee.get(),dec_fee.get()];
        
        month=('Month 1','Month 2','Month 3','Month 4','Month 5','Month 6','Month 7','Month 8','Month 9','Month 10','Month 11','Month 12');
        for i in range(0,11):
            cursor.execute("UPDATE %s SET amount=%d WHERE month='%s'"%(act_name,int(l1[i]),month[i]));
        
        db.commit();

    roll=StringVar();
    jan_fee=StringVar();
    feb_fee=StringVar();
    mar_fee=StringVar();
    apr_fee=StringVar();
    may_fee=StringVar();
    june_fee=StringVar();
    july_fee=StringVar();
    aug_fee=StringVar();
    sep_fee=StringVar();
    oct_fee=StringVar();
    nov_fee=StringVar();
    dec_fee=StringVar();

    Button(
        text='HOME',
        font='calibri 12 bold',
        bg='#32CD32',
        borderwidth=3,
        relief=SOLID,
        fg='black',
        command=home,
        ).place(
            x=20,
            y=7
        )

    Label(
        fee_tut,
        text="ENTER FEE DATA",
        font='courier 30 bold',
        fg='white',
        bg='red',
        ).place(
        x=125,
        y=0
    );

    Label(
        fee_tut,
        text="ROLL NO.",
        font='courier 25 bold',
        bg=back,
        ).place(
        x=10,
        y=70,
        );

    Entry(
        fee_tut,
        textvar=roll,
        width=5,
        font='calibri 20',
    ).place(
        x=200,
        y=70,
    )

    Button(
        fee_tut,
        text='OK',
        font='courier 15 bold',
        fg='white',
        bg='#1ec71e',
        border=1,
        relief=SOLID,
        command=ok,

        ).place(
        x=300,
        y=69
        );

    Label(
        text='MONTH 1',
        font='courier 20 bold',
        bg=back,

    ).place(
        x=10,
        y=140,
    );
    Entry(
        textvar=jan_fee,
        font='courier 20 ',
        width=5,

    ).place(
        x=200,
        y=140
    );

    Label(
        text='MONTH 2',
        font='courier 20 bold',
        bg=back,

    ).place(
        x=10,
        y=190,
    )
    Entry(
        textvar=feb_fee,
        font='courier 20 ',
        width=5,

    ).place(
        x=200,
        y=190
    );

    Label(
        text='MONTH 3',
        font='courier 20 bold',
        bg=back,

    ).place(
        x=10,
        y=240,
    );
    Entry(
        textvar=mar_fee,
        font='courier 20 ',
        width=5,

    ).place(
        x=200,
        y=240
    );

    Label(
        text='MONTH 4',
        font='courier 20 bold',
        bg=back,

    ).place(
        x=10,
        y=240,
    );
    Entry(
        textvar=mar_fee,
        font='courier 20 ',
        width=5,

    ).place(
        x=200,
        y=240
    );

    Label(
        text='MONTH 5',
        font='courier 20 bold',
        bg=back,

    ).place(
        x=10,
        y=290,
    );
    Entry(
        textvar=apr_fee,
        font='courier 20 ',
        width=5,

    ).place(
        x=200,
        y=290
    );

    Label(
        text='MONTH 6',
        font='courier 20 bold',
        bg=back,

    ).place(
        x=10,
        y=340,
    );
    Entry(
        textvar=may_fee,
        font='courier 20 ',
        width=5,

    ).place(
        x=200,
        y=340
    );

    Label(
        text='MONTH 6',
        font='courier 20 bold',
        bg=back,

    ).place(
        x=10,
        y=390,
    );
    Entry(
        textvar=june_fee,
        font='courier 20 ',
        width=5,

    ).place(
        x=200,
        y=390
    );
    
    Label(
        text='MONTH 7',
        font='courier 20 bold',
        bg=back,

    ).place(
        x=350,
        y=140,
    );
    Entry(
        textvar=july_fee,
        font='courier 20 ',
        width=5,

    ).place(
        x=500,
        y=140
    );
    
    Label(
        text='MONTH 8',
        font='courier 20 bold',
        bg=back,

    ).place(
        x=350,
        y=190,
    );
    Entry(
        textvar=aug_fee,
        font='courier 20 ',
        width=5,

    ).place(
        x=500,
        y=190
    );

    Label(
        text='MONTH 9',
        font='courier 20 bold',
        bg=back,

    ).place(
        x=350,
        y=240,
    );
    Entry(
        textvar=sep_fee,
        font='courier 20 ',
        width=5,

    ).place(
        x=500,
        y=240
    );

    Label(
        text='MONTH 10',
        font='courier 20 bold',
        bg=back,

    ).place(
        x=350,
        y=290,
    );
    Entry(
        textvar=oct_fee,
        font='courier 20 ',
        width=5,

    ).place(
        x=500,
        y=290
    );

    Label(
        text='MONTH 11',
        font='courier 20 bold',
        bg=back,

    ).place(
        x=350,
        y=340,
    );
    Entry(
        textvar=nov_fee,
        font='courier 20 ',
        width=5,

    ).place(
        x=500,
        y=340
    );

    Label(
        text='MONTH 12',
        font='courier 20 bold',
        bg=back,

    ).place(
        x=350,
        y=390,
    );
    Entry(
        textvar=dec_fee,
        font='courier 20 ',
        width=5,

    ).place(
        x=500,
        y=390
    );
    
    Button(
        fee_tut,
        text='UPDATE',
        font='courier 15 bold',
        bg='white',
        #bg='#1ec71e',
        border=1,
        relief=SOLID,
        command=update,

        ).place(
        x=240,
        y=450
        );

    fee_tut.mainloop();

def open():
    global main;
    main=Tk();
    main.geometry('800x350');
    main.maxsize(800,350);
    main.minsize(800,350);
    main.iconphoto(True,PhotoImage(file='special.png'));
    main.title('Special Learns Computer Institute');
    back='#6ac5fe';
    main.config(bg=back);
    
    Label(
        main,
        text="WELCOME TO SPECIAL LEARNS",
        font='courier 30 bold',
        fg='white',
        bg='red',
        ).place(
        x=100,
        y=0
    );

    f1=Frame(
        borderwidth=3,
        relief=SOLID,
        ).place(
            x=15,y=80
    );

    Label(
        f1,
        text='COMPUTER INSTITUTE',
        font='courier 20 bold',
        bg=back,
        background='#1ec71e',
        fg='white',
        ).place(
            x=15,
            y=80
        );

    Button(
        f1,
        text='ENROLL NEW!    ',
        font='courier 15 bold',
        fg='black',
        bg=back,
        border=1,
        relief=SOLID,
        command=enrollData_of_cs,
        ).place(
        x=15,
        y=130
        );
    
    Button(
        f1,
        text='CHECK OLD DATA!',
        font='courier 15 bold',
        fg='black',
        bg=back,
        border=1,
        relief=SOLID,
        command=checkData_of_cs

        ).place(
        x=15,
        y=180
        );
    
    Button(
        f1,
        text='FEE DATA!      ',
        font='courier 15 bold',
        fg='black',
        bg=back,
        border=1,
        relief=SOLID,
        command=feedata_cs,

        ).place(
        x=15,
        y=230
        );

    Button(
        f1,
        text='ADD NEW COURSE!',
        font='courier 15 bold',
        fg='black',
        bg=back,
        border=1,
        relief=SOLID,
        command=add_course,

        ).place(
        x=15,
        y=280
        );

    Label(
        f1,
        text='TUITION',
        font='courier 20 bold',
        bg=back,
        background='#1ec71e',
        fg='white',
        ).place(
            x=550,
            y=80
        );

    Button(
        f1,
        text='ENROLL NEW!    ',
        font='courier 15 bold',
        fg='black',
        bg=back,
        border=1,
        relief=SOLID,
        command=tuition_enroll,
        ).place(
        x=550,
        y=130
        );
    
    Button(
        f1,
        text='CHECK OLD DATA!',
        font='courier 15 bold',
        fg='black',
        bg=back,
        border=1,
        relief=SOLID,
        command=checkData_of_tut,

        ).place(
        x=550,
        y=180
        );
    
    Button(
        f1,
        text='FEE DATA!      ',
        font='courier 15 bold',
        fg='black',
        bg=back,
        border=1,
        relief=SOLID,
        command=feedata_tut,

        ).place(
        x=550,
        y=230
        );
    
    main.mainloop();

def create_db():
    cursor.execute('CREATE DATABASE IF NOT EXISTS student');
    cursor.execute('USE student');
    cursor.execute('CREATE TABLE IF NOT EXISTS CS_data(roll int,name varchar(20),Father_name varchar(20),Mother_name varchar(20),Gender varchar(10),dob varchar(20),course varchar(20),mob varchar(20),address varchar(50),adm varchar(15),PRIMARY KEY(roll))')
    cursor.execute('CREATE TABLE IF NOT EXISTS tuition(roll int,name varchar(20),Father_name varchar(20),Mother_name varchar(20),Gender varchar(10),dob varchar(20),subject varchar(20),mob varchar(20),class int,address varchar(50),adm varchar(15),PRIMARY KEY(roll))')
    cursor.execute("INSERT IGNORE cs_data(roll) values(0)");
    cursor.execute("INSERT IGNORE tuition(roll) values(0)");
    cursor.execute('CREATE TABLE IF NOT EXISTS course(Name varchar(50),Duration int,PRIMARY KEY(Name))');

    study=('D.C.A','Python','Web Designing','Editing','Excel','Graphics');
    study_dur=(12,6,12,12,6,12);
    i=0;

    for k in range(0,len(study)):
        cursor.execute("INSERT IGNORE INTO course(Name,duration) values('%s',%d)"%(study[k],study_dur[k]));
        

    cursor.execute('CREATE DATABASE IF NOT EXISTS feedata_cs');
    cursor.execute('CREATE DATABASE IF NOT EXISTS feedata_tut');

def today():
    dy=str(dat.today());
    return str(dy);

def add_course():
    global main;
    main.destroy();
    ad_c=Tk();
    ad_c.geometry('550x300');
    ad_c.maxsize(550,300);
    ad_c.minsize(550,300);

    back='#6ac5fe';
    ad_c.title('Add new course');
    ad_c.config(bg=back);

    cursor.execute('USE student');
    
    c_name=StringVar();
    c_dur=StringVar();

    def home():
            ad_c.destroy();
            open();

    def name_check():
        mark=1;
        if c_name.get()=='':
            mark=0;        
            c_name.set('*%s'%(c_name.get()));
        return mark;

    def dur_check():
        mark=1;
        if str(c_dur.get())=='' or int(c_dur.get())>12 or int(c_dur.get())==0:
            mark=0;
            c_dur.set('*%s'%(str(c_dur.get())));
        return mark;

    def upd():
        if name_check()==1 and dur_check()==1:
            cursor.execute('INSERT INTO course(Name,Duration) values("%s",%d)'%(c_name.get(),int(c_dur.get())));
            db.commit();
            print('done');
    
    
    Label(
        ad_c,
        text="ADD NEW COURSE",
        font='courier 30 bold',
        fg='white',
        bg='red',
        ).place(
        x=110,
        y=0
    );

    Button(
        text='HOME',
        font='calibri 12 bold',
        bg='#32CD32',
        borderwidth=1,
        relief=SOLID,
        fg='white',
        command=home,
        ).place(
            x=20,
            y=10
        )

    Label(
        ad_c,
        text="NAME",
        font='courier 20 bold',
        bg=back,

        ).place(
        x=20,
        y=85
    );

    Entry(
        ad_c,
        font='courier 20',
        textvar=c_name,
        
        ).place(
        x=190,
        y=85
    );

    Label(
        ad_c,
        text="DURATION",
        font='courier 20 bold',
        bg=back,

        ).place(
        x=20,
        y=150
    );

    
    duration_time=Entry(
                ad_c,
                font='courier 20',
                #fg='green',
                textvar=c_dur,

                )
        
    duration_time.place(
        x=190,
        y=150
    );

    Button(
        ad_c,
        text='UPDATE',
        font='courier 15 bold',
        border=1,
        relief=SOLID,
        command=upd,

        ).place(
        x=230,
        y=220
        );

    ad_c.mainloop();

    #return crse;


#Program starts here:-
logon();