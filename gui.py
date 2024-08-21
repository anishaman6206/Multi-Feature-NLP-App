from tkinter import *
from database import Database
from tkinter import messagebox
from api import API
from tkinter import Canvas

'''canvas = Canvas(self.root, width=400, height=400)
canvas.pack(fill="both", expand=True)

gradient = canvas.create_rectangle(0, 0, 400, 400, fill="")
canvas.itemconfig(gradient, fill="linear-gradient(#283747, #F7F9F9)")'''


class NLPApp:

    def __init__(self):
        self.dbo = Database()
        self.apio = API()

        # Initialize main window
        self.root = Tk()
        self.root.title('NLP App')
        self.root.iconbitmap('C:/Users/anish/Desktop/NLPApp/logo.ico')
        self.root.geometry('800x600')

        self.root.configure(bg='#F2D7D5')

        self.login_gui()

        self.root.mainloop()

    def login_gui(self):
        self.clear()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        frame_width = int(screen_width * 0.8)  # 80% of screen width
        frame_height = int(screen_height * 0.8)  # 80% of screen height

    # Create and configure the outer frame
        frame = Frame(self.root, bg='#2F2F2F', width=frame_width, height=frame_height, padx=20, pady=20)
        frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        heading = Label(frame, text='Welcome to NLP App', bg='#2F2F2F', fg='white', font=('Helvetica', 28, 'bold'))
        heading.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        label1 = Label(frame, text='Enter Email', bg='#2F2F2F', fg='white', font=('Helvetica', 14))
        label1.grid(row=1, column=0, sticky=E, pady=10, padx=10)

        self.email_input = Entry(frame, width=30, font=('Helvetica', 12))
        self.email_input.grid(row=1, column=1, pady=10, padx=10)

        label2 = Label(frame, text='Enter Password', bg='#2F2F2F', fg='white', font=('Helvetica', 14))
        label2.grid(row=2, column=0, sticky=E, pady=10, padx=10)

        self.password_input = Entry(frame, width=30, show='*', font=('Helvetica', 12))
        self.password_input.grid(row=2, column=1, pady=10, padx=10)

        login_btn = Button(frame, text='Login', width=20, height=2, bg='#1ABC9C', fg='white', 
                           font=('Helvetica', 12, 'bold'), command=self.perform_login)
        login_btn.grid(row=3, column=0, columnspan=2, pady=(20, 10))

        label3 = Label(frame, text='Not a member?', bg='#2F2F2F', fg='white', font=('Helvetica', 12))
        label3.grid(row=4, column=0, columnspan=2, pady=(30, 10))

        redirect_btn = Button(frame, text='Register Now', bg='#E74C3C', fg='white', 
                              font=('Helvetica', 12, 'bold'), command=self.register_gui)
        redirect_btn.grid(row=5, column=0, columnspan=2, pady=10)

    def register_gui(self):
        self.clear()

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        frame_width = int(screen_width * 0.8)  # 80% of screen width
        frame_height = int(screen_height * 0.8)  # 80% of screen height

        frame = Frame(self.root, bg='#2F2F2F', width=frame_width, height=frame_height, padx=20, pady=20)
        frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        heading = Label(frame, text='NLP App', bg='#2F2F2F', fg='white', font=('Helvetica', 28, 'bold'))
        heading.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        label0 = Label(frame, text='Enter Name', bg='#2F2F2F', fg='white', font=('Helvetica', 14))
        label0.grid(row=1, column=0, sticky=E, pady=10, padx=10)

        self.name_input = Entry(frame, width=30, font=('Helvetica', 12))
        self.name_input.grid(row=1, column=1, pady=10, padx=10)

        label1 = Label(frame, text='Enter Email', bg='#2F2F2F', fg='white', font=('Helvetica', 14))
        label1.grid(row=2, column=0, sticky=E, pady=10, padx=10)

        self.email_input = Entry(frame, width=30, font=('Helvetica', 12))
        self.email_input.grid(row=2, column=1, pady=10, padx=10)

        label2 = Label(frame, text='Enter Password', bg='#2F2F2F', fg='white', font=('Helvetica', 14))
        label2.grid(row=3, column=0, sticky=E, pady=10, padx=10)

        self.password_input = Entry(frame, width=30, show='*', font=('Helvetica', 12))
        self.password_input.grid(row=3, column=1, pady=10, padx=10)

        register_btn = Button(frame, text='Register', width=20, height=2, bg='#1ABC9C', fg='white', 
                              font=('Helvetica', 12, 'bold'), command=self.perform_registration)
        register_btn.grid(row=4, column=0, columnspan=2, pady=(20, 10))

        label3 = Label(frame, text='Already a member?', bg='#2F2F2F', fg='white', font=('Helvetica', 12))
        label3.grid(row=5, column=0, columnspan=2, pady=(30, 10))

        redirect_btn = Button(frame, text='Login Now', bg='#E74C3C', fg='white', 
                              font=('Helvetica', 12, 'bold'), command=self.login_gui)
        redirect_btn.grid(row=6, column=0, columnspan=2, pady=10)

    def clear(self):
    # Clear widgets managed by 'pack'
        for widget in self.root.pack_slaves():
            widget.destroy()
    
    # Clear widgets managed by 'place'
        for widget in self.root.place_slaves():
            widget.destroy()
    
    # Clear widgets managed by 'grid'
        for widget in self.root.grid_slaves():
            widget.destroy()


    def perform_registration(self):
        # fetch data from the gui
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        if(name!='' and email!='' and password!=''):

         response = self.dbo.add_data(name, email, password)

         if response:
            messagebox.showinfo('Success','Registration successful. You can login now')
         else:
            messagebox.showerror('Error','Email already exists')
        else:
            messagebox.showerror('Error','Fill all the details')    

    def perform_login(self):

        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.search(email, password)

        if response:
            messagebox.showinfo('success','Login successful')
            self.home_gui()
        else:
            messagebox.showerror('error','Incorrect email/password')

    def home_gui(self):
        self.clear()

    # Create and configure the outer frame
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        frame_width = int(screen_width * 0.8)  # 60% of screen width
        frame_height = int(screen_height * 0.8)  # 60% of screen height

        frame = Frame(self.root, bg='#2F2F2F', width=frame_width, height=frame_height, padx=20, pady=20)
        frame.place(relx=0.5, rely=0.5, anchor=CENTER)
    # Heading
        heading = Label(frame, text='NLP App', bg='#2F2F2F', fg='white', font=('Helvetica', 28, 'bold'))
        heading.grid(row=0, column=0, columnspan=2, pady=(0, 20))

    # Sentiment Analysis Button
        sentiment_btn = Button(frame, text='Sentiment Analysis', width=20, height=2, bg='#1ABC9C', fg='white', 
                           font=('Helvetica', 12, 'bold'), command=self.sentiment_gui)
        sentiment_btn.grid(row=1, column=0, columnspan=2, pady=(10, 10))

    # Language Detection Button
        langdet_btn = Button(frame, text='Language Detection', width=20, height=2, bg='#3498DB', fg='white', 
                         font=('Helvetica', 12, 'bold'), command=self.langdet_gui)
        langdet_btn.grid(row=2, column=0, columnspan=2, pady=(10, 10))

    # Emotion Prediction Button
        emotion_btn = Button(frame, text='Emotion Prediction', width=20, height=2, bg='#9B59B6', fg='white', 
                         font=('Helvetica', 12, 'bold'), command=self.emotion_prediction_gui)
        emotion_btn.grid(row=3, column=0, columnspan=2, pady=(10, 10))
    #lang translate buttonS
        langtra_btn = Button(frame, text='Translate English to Hindi', width=20, height=2, bg='#FF5733', fg='white', 
                         font=('Helvetica', 12, 'bold'), command=self.language_translate_gui)
        langtra_btn.grid(row=4, column=0, columnspan=2, pady=(10, 10))

    # Logout Button
        logout_btn = Button(frame, text='Logout', bg='#E74C3C', fg='white', 
                        font=('Helvetica', 12, 'bold'), command=self.login_gui)
        logout_btn.grid(row=5, column=0, columnspan=2, pady=(30, 10))
        
        frame.update_idletasks()

    def sentiment_gui(self):

        self.clear()

    # Create the main frame to hold the content
        main_frame = Frame(self.root, bg='#2F2F2F')
        main_frame.pack(expand=True, fill=BOTH, padx=20, pady=20)

    # App heading
        heading = Label(main_frame, text='NLP App', bg='#2F2F2F', fg='white', font=('verdana', 24, 'bold'))
        heading.pack(pady=(10, 20))

    # Section heading
        heading2 = Label(main_frame, text='Sentiment Analysis', bg='#2F2F2F', fg='white', font=('verdana', 20))
        heading2.pack(pady=(5, 20))

    # Input label and text widget
        label1 = Label(main_frame, text='Enter the text:', bg='#2F2F2F', fg='white', font=('verdana', 12))
        label1.pack(anchor=W)

        self.sentiment_input = Text(main_frame, width=45, height=8, wrap=WORD, font=('verdana', 12))
        self.sentiment_input.pack(pady=(5, 15), padx=5)

    # Analyze Sentiment button
        sentiment_btn = Button(main_frame, text='Analyze Sentiment', width=20, height=2,
                           bg='#5DADE2', fg='white', font=('verdana', 12, 'bold'),
                           command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady=(10, 15))

    # Result display area
        result_frame = LabelFrame(main_frame, text="Sentiment Result", bg='#2F2F2F', fg='white',
                              font=('verdana', 12, 'bold'), labelanchor=N)
        result_frame.pack(fill=BOTH, pady=(5, 15), padx=5)

        self.sentiment_result = Label(result_frame, text='', bg='#2F2F2F', fg='white',
                                  font=('verdana', 13), anchor=W, justify=LEFT)
        self.sentiment_result.pack(pady=10, padx=10)

    # Go Back button
        goback_btn = Button(main_frame, text='Go Back', width=15, height=2,
                        bg='#E74C3C', fg='white', font=('verdana', 12, 'bold'),
                        command=self.home_gui)
        goback_btn.pack(pady=10)

    def language_translate_gui(self):

        self.clear()

    # Create the main frame to hold the content
        main_frame = Frame(self.root, bg='#2F2F2F')
        main_frame.pack(expand=True, fill=BOTH, padx=20, pady=20)

    # App heading
        heading = Label(main_frame, text='NLP App', bg='#2F2F2F', fg='white', font=('verdana', 24, 'bold'))
        heading.pack(pady=(10, 20))

    # Section heading
        heading2 = Label(main_frame, text='Translate English to Hindi', bg='#2F2F2F', fg='white', font=('verdana', 20))
        heading2.pack(pady=(5, 20))

    # Input label and text widget
        label1 = Label(main_frame, text='Enter the text to translate:', bg='#2F2F2F', fg='white', font=('verdana', 12))
        label1.pack(anchor=W)

        self.translate_input = Text(main_frame, width=45, height=8, wrap=WORD, font=('verdana', 12))
        self.translate_input.pack(pady=(5, 15), padx=5)

    # Analyze Sentiment button
        translate_btn = Button(main_frame, text='Translate', width=20, height=2,
                           bg='#5DADE2', fg='white', font=('verdana', 12, 'bold'),
                           command=self.do_language_translation)
        translate_btn.pack(pady=(10, 15))

    # Result display area
        result_frame = LabelFrame(main_frame, text="Translated Text", bg='#2F2F2F', fg='white',
                              font=('verdana', 12, 'bold'), labelanchor=N)
        result_frame.pack(fill=BOTH, pady=(5, 15), padx=5)

        self.translate_result = Label(result_frame, text='', bg='#2F2F2F', fg='white',
                                  font=('verdana', 13), anchor=W, justify=LEFT)
        self.translate_result.pack(pady=10, padx=10)

    # Go Back button
        goback_btn = Button(main_frame, text='Go Back', width=15, height=2,
                        bg='#E74C3C', fg='white', font=('verdana', 12, 'bold'),
                        command=self.home_gui)
        goback_btn.pack(pady=10)

    def do_language_translation(self):
        self.translate_result['text'] = "Model is loading, please wait for a few seconds..."
        self.root.update() 

        text = self.translate_input.get("1.0", END).strip()
        
        result = self.apio.translate_en_to_hi(text)
        print(result)
        self.translate_result['text'] = result    
    def emotion_prediction_gui(self):
        self.clear()
        

    # Create the main frame to hold the content
        main_frame = Frame(self.root, bg='#2F2F2F')
        main_frame.pack(expand=True, fill=BOTH, padx=20, pady=20)

    # App heading
        heading = Label(main_frame, text='NLP App', bg='#2F2F2F', fg='white', font=('verdana', 24, 'bold'))
        heading.pack(pady=(10, 20))

    # Section heading
        heading2 = Label(main_frame, text='Emotion Prediction', bg='#2F2F2F', fg='white', font=('verdana', 20))
        heading2.pack(pady=(5, 20))

    # Input label and text widget
        label1 = Label(main_frame, text='Enter the text:', bg='#2F2F2F', fg='white', font=('verdana', 12))
        label1.pack(anchor=W)

        self.emotion_input = Text(main_frame, width=45, height=8, wrap=WORD, font=('verdana', 12))
        self.emotion_input.pack(pady=(5, 15), padx=5)

    # Analyze Sentiment button
        emotion_btn = Button(main_frame, text='Analyze Emotion', width=20, height=2,
                           bg='#5DADE2', fg='white', font=('verdana', 12, 'bold'),
                           command=self.do_emotion_prediction)
        emotion_btn.pack(pady=(10, 15))

    # Result display area
        result_frame = LabelFrame(main_frame, text="Emotion Result", bg='#2F2F2F', fg='white',
                              font=('verdana', 12, 'bold'), labelanchor=N)
        result_frame.pack(fill=BOTH, pady=(5, 15), padx=5)

        self.emotion_result = Label(result_frame, text='', bg='#2F2F2F', fg='white',
                                  font=('verdana', 13), anchor=W, justify=LEFT)
        self.emotion_result.pack(pady=10, padx=10)

    # Go Back button
        goback_btn = Button(main_frame, text='Go Back', width=15, height=2,
                        bg='#E74C3C', fg='white', font=('verdana', 12, 'bold'),
                        command=self.home_gui)
        goback_btn.pack(pady=10)


   

    
    def do_emotion_prediction(self):
        self.emotion_result['text'] = "Model is loading, please wait for a few seconds..."
        self.root.update() 

        text = self.emotion_input.get("1.0", END).strip()
        
        result = self.apio.emotion_prediction(text)

      
            

        txt=''
        for item in result:
           print(f"{item['label']} => {item['score']:.4f}")
           txt = txt + 'Emotion:' + ' ' + item['label'] + '\t'+ 'Score:' + ' ' + str(item['score'])[0:8] + '\n'

       
        print(result)
        self.emotion_result['text'] = txt
    
    def do_sentiment_analysis(self):
        self.sentiment_result['text'] = "Model is loading, please wait for a few seconds..."
        self.root.update() 

        text = self.sentiment_input.get("1.0", END).strip()
        result = self.apio.sentiment_analysis(text)

        while "error" in result and "loading" in result["error"].lower():
            import time
            print(result["error"])
            print("Retrying in 5 seconds...")
            time.sleep(5)  # Wait for 5 seconds before retrying
            

        txt=''
        for item in result:
          for i in range(3):
            print(f"Label: {item[i]['label']}, Score: {item[i]['score']:.8f}")
            txt = txt + 'Sentiment:' + ' ' + item[i]['label'] + '\t'+ 'Score:' + ' ' + str(item[i]['score'])[0:8] + '\n'

        
        print(result)
        self.sentiment_result['text'] = txt
    '''def ner_gui(self):

        self.clear()

        heading = Label(self.root, text='NLP App', bg='#2F2F2F', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Named Entity Recognition', bg='#2F2F2F', fg='white')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 20))

        label1 = Label(self.root, text='Enter the text')
        label1.pack(pady=(10, 10))

        self.ner_input = Entry(self.root, width=50)
        self.ner_input.pack(pady=(5, 10), ipady=4)
        
        label2 = Label(self.root, text='Enter the entity you want to extract from the text, separated by commas (e.g., person, location, etc.):')
        label2.pack(pady=(10, 10))

        self.entity_input = Entry(self.root, width=50)
        self.entity_input.pack(pady=(5, 10), ipady=4)

        ner_btn = Button(self.root, text='Analyze NER', command=self.do_ner)
        ner_btn.pack(pady=(10, 10))

        self.ner_result = Label(self.root, text='',bg='#2F2F2F',fg='white')
        self.ner_result.pack(pady=(10, 10))
        self.ner_result.configure(font=('verdana', 13))


        goback_btn = Button(self.root, text='Go Back', command=self.home_gui)
        goback_btn.pack(pady=(10, 10))'''

    '''def do_ner(self):
        self.sentiment_result['text'] = "Model is loading, please wait for a few seconds..."
        self.root.update() 

        text = self.sentiment_input.get("1.0", END).strip()
        

        
        labels= self.entity_input.get()
        labels_list = [label.strip() for label in labels.split(',')]
        result = self.apio.ner(text,labels_list)
        txt=""
        for entity in result:
          print(entity["text"], "=>", entity["label"])
          txt=txt+ entity["text"]+' '+ "=>" + entity["label"] + '/n'


        self.ner_result['text'] = txt  '''

    def langdet_gui(self):
        self.clear()
       
        

    # Create the main frame to hold the content
        main_frame = Frame(self.root, bg='#2F2F2F')
        main_frame.pack(expand=True, fill=BOTH, padx=20, pady=20)

    # App heading
        heading = Label(main_frame, text='NLP App', bg='#2F2F2F', fg='white', font=('verdana', 24, 'bold'))
        heading.pack(pady=(10, 20))

    # Section heading
        heading2 = Label(main_frame, text='Language Detection', bg='#2F2F2F', fg='white', font=('verdana', 20))
        heading2.pack(pady=(5, 20))

    # Input label and text widget
        label1 = Label(main_frame, text='Enter the text:', bg='#2F2F2F', fg='white', font=('verdana', 12))
        label1.pack(anchor=W)

        self.language_input = Text(main_frame, width=45, height=8, wrap=WORD, font=('verdana', 12))
        self.language_input.pack(pady=(5, 15), padx=5)

    # Analyze Sentiment button
        language_btn = Button(main_frame, text='Detect Language', width=20, height=2,
                           bg ='#5DADE2', fg='white', font=('verdana', 12, 'bold'),
                           command=self.do_language_detection)
        language_btn.pack(pady=(10, 15))

    # Result display area
        result_frame = LabelFrame(main_frame, text="Detected Language", bg='#2F2F2F', fg='white',
                              font=('verdana', 12, 'bold'), labelanchor=N)
        result_frame.pack(fill=BOTH, pady=(5, 15), padx=5)

        self.language_result = Label(result_frame, text='', bg='#2F2F2F', fg='white',
                                  font=('verdana', 13), anchor=W, justify=LEFT)
        self.language_result.pack(pady=10, padx=10)

    # Go Back button
        goback_btn = Button(main_frame, text='Go Back', width=15, height=2,
                        bg='#E74C3C', fg='white', font=('verdana', 12, 'bold'),
                        command=self.home_gui)
        goback_btn.pack(pady=10)


    

    def do_language_detection(self):
        self.language_result['text'] = "Model is loading, please wait for a few seconds..."
        self.root.update() 

        text = self.language_input.get("1.0", END).strip()
        
        result = self.apio.language_detection(text)

        

        txt=''
        for item in result:
           print(f"Language: {item['label']} - Confidence: {item['score']:.4f}")
           txt = txt + 'Language:' + ' ' + item['label'] + '\t'+ 'Confidence:' + ' ' + str(item['score'])[0:8] + '\n'

        '''txt = ''
        for i in result['sentiment']:
            txt = txt + i + ' -> ' + str(result['sentiment'][i]) + '\n'

        print(txt)'''
        print(result)
        self.language_result['text'] = txt



nlp = NLPApp()


